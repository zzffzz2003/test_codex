from calculator import add, sub, mul, div

def menu():
    print("========== 简易计算器 ==========")
    print("1. 加法")
    print("2. 减法")
    print("3. 乘法")
    print("4. 除法")
    print("5. 退出")
    print("================================")

def get_number(prompt):
    while True:
        value = input(prompt)
        try:
            return float(value)
        except ValueError:
            print("输入的不是数字，请重新输入。")

def main():
    while True:
        menu()
        choice = input("请选择功能(1-5)：").strip()

        if choice == "5":
            print("再见！")
            break

        if choice not in ["1", "2", "3", "4"]:
            print("无效的选择，请重新输入。")
            continue

        a = get_number("请输入第一个数字：")
        b = get_number("请输入第二个数字：")

        if choice == "1":
            result = add(a, b)
            op = "+"
        elif choice == "2":
            result = sub(a, b)
            op = "-"
        elif choice == "3":
            result = mul(a, b)
            op = "*"
        else:
            # 这里也没处理 b = 0 的情况，将来交给 Codex 修
            result = div(a, b)
            op = "/"

        print(f"\n结果：{a} {op} {b} = {result}\n")

if __name__ == "__main__":
    main()
