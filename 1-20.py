if __name__ == "__main__":
    while True:
        try:
            import math
            start , day = map(int , input().split())
            n = (-1 + math.sqrt(-1 + 4 * start**2 + 8*day -4 * start))/2
            print(math.ceil(n))
        except EOFError:
            break
            # 暴力會tle