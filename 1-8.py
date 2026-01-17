def decimal(a):
    count = 0
    while a != 0 and a != 1:
        if a % 2 == 1:
            count += 1
            a //= 2
        else:
            a //= 2
    if a == 1:
        count += 1
    return count
    # return bin(a).count('1')
def hexadecimal(a):
    i = 0
    num = 0
    while a != 0:
        num += (a % 10) * (16 ** i)
        a //= 10
        i += 1
    return decimal(num)
    # return bin(int(str(a), 16)).count('1')
if __name__ == "__main__":
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(int(input()))
    for a in arr:
        print(decimal(a) , hexadecimal(a))
