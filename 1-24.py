if __name__ == "__main__":
    import math
    while True:
        try:
            s , a , ch = input().split()
            s = int(s) + 6440
            if ch == 'min':
                a = int(a) / 60
            else:
                a = int(a)
            result = math.sqrt((2 * (s ** 2)) * (1 - math.cos(a * math.pi / 180)))
            print(f"{s * a * math.pi / 180:.6f}")
            print(f"{result:.6f}")
        except EOFError:
            break
        # 弧長 = 半徑 * 弧度
        # 弧度 = 角度 * π / 180