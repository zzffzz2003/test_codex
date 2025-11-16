import sys
from pathlib import Path

from openai import OpenAI
from dotenv import load_dotenv

# 读取 .env 里的 OPENAI_API_KEY
load_dotenv()
client = OpenAI()

INSTRUCTIONS = """
你是一个资深 Python 程序员，正在帮我重构项目中的一个文件。

要求：
1. 保持原有功能不变。
2. 修复明显的 bug（例如除以 0 等错误）。
3. 提高代码可读性，适当拆分长函数。
4. 为重要函数添加清晰的注释或 docstring（可以用中文或者英文）。
5. 统一代码风格（适当空行、缩进、命名更规范）。
6. **只输出修改后的完整代码，不要额外解释文字。**
"""

def fix_file(path_str: str) -> None:
    path = Path(path_str)

    if not path.exists():
        print(f"❌ 找不到文件：{path}")
        return

    # 读取原始代码
    original_code = path.read_text(encoding="utf-8")

    print(f"🔧 正在用 Codex 重构文件：{path.name} ...")

    prompt = f"""{INSTRUCTIONS}

下面是需要修改的文件 {path.name} 当前的内容：

```python
{original_code}
```"""

    # 调用 Codex 模型
    response = client.responses.create(
        model="gpt-5.1-codex",
        input=prompt,
    )

    new_code = response.output_text

    # 先备份原文件
    backup_path = path.with_suffix(path.suffix + ".bak")
    backup_path.write_text(original_code, encoding="utf-8")

    # 写入新代码
    path.write_text(new_code, encoding="utf-8")

    print(f"✅ 已备份原文件到：{backup_path.name}")
    print(f"✅ 已用 Codex 修改：{path.name}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法：python codex_fix_file.py <要修改的文件路径>")
        print("例如：python codex_fix_file.py calculator.py")
        sys.exit(1)

    fix_file(sys.argv[1])
