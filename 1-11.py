if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        result = 0
        arr = list(map(int , input().split()))
        r = arr[0]
        del arr[0]
        arr = sorted(arr)
        middle = arr[len(arr)//2]
        for a in arr:
            result += abs(a-middle)
        print(result)

