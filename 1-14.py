if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        people , win , find = input().split()
        if win == "1":
            print("1.0000")
            continue
        people = int(people)
        win = float(win)
        find = int(find)
        current = win * ((1 - win) ** (find - 1))
        every_time = (1 - win) ** people
        total = current / (1 - every_time)
        print(f"{total:.4f}")
        # 等比極限和
