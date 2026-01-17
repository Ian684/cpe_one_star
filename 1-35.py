if __name__ == "__main__":
    n = int(input())
    for i in range(1 , n+1):
        a = int(input())
        b = int(input())
        count = 0
        if a % 2 == 0:
            a += 1
        if b % 2 == 0:
            b -= 1
        for c in range(a , b+1 , 2):
            count += c
        print(f"Case {i}: {count}")