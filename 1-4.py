if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        l = int(input())
        arr = list(map(int, input().split()))
        count = 0
        for j in range(l):
            for k in range(j+1 , l):
                if arr[j] > arr[k]:
                    count += 1
        print(f"Optimal train swapping takes {count} swaps.")