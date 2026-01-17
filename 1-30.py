if __name__ == "__main__":
    while True:
        try:
            x = int(input())
            arr = list(map(int, input().split()))
            n = len(arr) - 1
            result = 0
            j = n
            for i in range(n):
                result += arr[i] * j *(x ** (j - 1))
                j -= 1
            print(int(result))
        except EOFError:
            break