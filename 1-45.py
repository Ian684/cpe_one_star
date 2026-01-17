def cal(current):
    count = 0
    while current > 0:
        count += current%10
        current //= 10
    return count
if __name__ =="__main__":
    while True:
        n = int(input())
        if n == 0:
            break
        while True:
            if n // 10 == 0:
                print(n)
                break
            n = cal(n)