def calculate(l , x , y , center):
    while True:
        l += 2
        x -= 1
        y -= 1
        if x < 0 or y < 0 or x+l-1 >= m or y+l-1 >= n:
            return l - 2
        for _ in range(l-1):
            y += 1
            if arr[x][y] != center:
                return l - 2
        for _ in range(l-1):
            x += 1
            if arr[x][y] != center:
                return l - 2
        for _ in range(l-1):
            y -= 1
            if arr[x][y] != center:
                return l - 2
        for _ in range(l-1):
            x -= 1
            if arr[x][y] != center:
                return l - 2
if __name__ == "__main__":
    num = int(input())
    for _ in range(num):
        arr = []
        check = []
        m , n , q = map(int , input().split())
        for i in range(m):
            arr.append(input())
        for qq in range(q):
            check.append(list(map(int , input().split())))
        print(m , n , q)
        for c in check:
            x , y = c
            l = 1
            print(calculate(l , x , y , arr[x][y]))
    # 直接上右下左邊去遍歷看是否相同