if __name__ == "__main__":
    while True:
        num = int(input())
        if num == 0:
            break
        num = bin(num)[2:]
        print(f"The parity of {num} is {num.count('1')} (mod 2).")
        # 轉bin會有0b前綴
        # 用''不要""