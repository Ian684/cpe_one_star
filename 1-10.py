if __name__ == "__main__":
    while True:
        try:
            arr = list(map(int , input().split()))
            n = arr[0]
            del arr[0]
            check = set(range(1,n))
            if n == 1:
                print("Jolly")
                continue
            for i in range(n-1):
                difference = abs(arr[i+1] - arr[i])
                if 1 <= difference <= n:
                    if difference in check:
                        check.remove(difference) 
                else:
                    print("Not jolly")
                    break
            else:
                if len(check) == 0:print("Jolly")
                else:print("Not jolly")
        except EOFError:
            break