def main():
    fac = [0 , 1 , 2]
    now = 3
    while True:
        fac.append(fac[now-1]*now)
        if fac[-1] > 6227020800:
            fac.pop()
            break
        now += 1

    while True:
        try:
            n = int(input())
        except EOFError:break
        if n < 0:
            if abs(n) & 1:
                print("Overflow!")
            else:
                print("Underflow!")
            continue
        if n >= len(fac):
            print("Overflow!")
        elif fac[n] < 10000:
            print("Underflow!")
        else:
            print(fac[n])

if __name__ == "__main__":
    main()
