if __name__ == "__main__":
    from collections import deque
    find = ((-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1))
    num = int(input())
    for i in range(num):
        arr = []
        check = []
        m , n , q = map(int , input().split())
        for a in range(m):
            arr.append(input())
        for b in range(q):
            check.append(list(map(int , input().split())))
        for x , y in check:
            valid = True
            history = [[0]*n for _ in range(m)]
            history[x][y] = -1
            queue = deque()
            queue.append((x , y))
            while True:
                nowx , nowy = queue.popleft()
                for dx , dy in find:
                    nx , ny = nowx + dx , nowy + dy
                    if m-1 < nx or nx < 0 or n-1 < ny or ny < 0:
                        valid = False
                        break
                    if history[nx][ny] == 0:
                        if arr[nx][ny] == arr[x][y]:
                            history[nx][ny] = -1
                            queue.append((nx , ny))
                        else:
                            valid = False
                            break
                if not valid:
                    break