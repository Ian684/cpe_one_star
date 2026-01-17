if __name__ == "__main__":
    now = 0
    while True:
        now += 1
        try:
            num = int(input())
            arr = list(map(int , input().split()))
            if arr[0] < 1:
                print(f"Case #{now}: It is not a B2-Sequence." , end="\n\n")
                continue
            valid = True
            for i in range(len(arr)-1):
                if arr[i]<arr[i+1]:
                    continue
                else:
                    print(f"Case #{now}: It is not a B2-Sequence." , end="\n\n")
                    valid = False
                    break
            if not valid:
                continue
            check = set()
            valid = True
            for start in range(len(arr)):
                for after in range(start,len(arr)):
                    if (arr[start]+arr[after]) in check:
                        valid = False
                        print(f"Case #{now}: It is not a B2-Sequence." , end="\n\n")
                        break
                    else:
                        check.add(arr[start]+arr[after])
                if not valid:
                    break
            if valid:
                print(f"Case #{now}: It is a B2-Sequence." , end="\n\n")
        except EOFError:
            break
        # b1 >= 1
        # b1 < b2 < b3 ....