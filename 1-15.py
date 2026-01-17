if __name__ == "__main__":
    while True:
        try:
            n = int(input())
            arr = []
            for i in range(n):
                arr.append(int(input()))
            arr.sort()
            if n % 2 == 1:
                print(arr[(n//2)] , end=" ")
            else:
                print(arr[(n//2) - 1] , end=" ")
            c = 0
            for a in arr:
                if n % 2 == 0 and (a == arr[(n//2) - 1] or a == arr[n//2]):
                    c += 1
                elif n % 2 == 1 and a == arr[n//2]:
                    c += 1
            print(c, end=" ")
            if n % 2 == 1:
                print(1)
            else:
                print(arr[n//2] - arr[n//2 - 1] + 1)
        except EOFError:
            break