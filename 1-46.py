if __name__ == "__main__":
    num = int(input())
    for _ in range(1 , num+1):
        valid = True
        n = int(input().split()[-1])
        arr = []
        for i in range(n):
            j = list(map(int , input().split()))
            arr.append(j)
            for jj in j:
                if jj < 0:
                    valid = False
        if not valid:
            print(f"Test #{_}: Non-symmetric.")
            continue
        check = [[0]*n for i in range(n)]
        double_centerx , double_centery = n - 1, n - 1 
        if n % 2 == 1:
            check[double_centerx][double_centery] = -1
        valid = True
        for x in range(n):
            for y in range(n):
                if check[x][y] == -1:
                    continue
                check[x][y] = -1
                if arr[x][y] == arr[double_centerx-x][double_centery-y]:
                    continue
                else:
                    valid = False
                    break
            if not valid:
                break
        if not valid:
            print(f"Test #{_}: Non-symmetric.")
        else:
            print(f"Test #{_}: Symmetric.")
        # 有回文解法，對稱必回文