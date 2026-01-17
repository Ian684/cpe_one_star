if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        s , d = map(int , input().split())
        if (s + d) % 2 != 0:
            print("impossible")
            continue
        a = (s + d) // 2
        if s - a == a - d:
            b = s - a
        else:
            print("impossible")
            continue
        if a >= 0 and b >= 0:
            print(a , b)
        else:
            print("impossible")