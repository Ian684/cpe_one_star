if __name__ == "__main__":
    while True:
        import math
        try:
            n , m =map(int , input().split())
            if n == 0 or m == 0:
                print("Boring!")
                continue
            if m == 1 and n != 1:
                print("Boring!")
                continue
            if pow(m , round(math.log(n , m))) != n:
                print("Boring!")
            else:
                while True:
                    if n == 1:
                        print(1)
                        break
                    print(n , end = " ")
                    n //= m
        except EOFError:
            break
        # n == 0 or m == 0
        # m == 1會無限迴圈 但n == 1會結束