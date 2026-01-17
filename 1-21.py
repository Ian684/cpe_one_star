if __name__ == "__main__":
    now = 0
    while True:
        n , m = map(int , input().split())
        if n == 0 and m == 0:
            break
        arr = []
        find = ((-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1))
        now += 1
        for y in range(n):
            arr.append(input())
        for y in range(n):
            for x in range(m):
                if arr[y][x] == "*":
                    continue
                elif arr[y][x] == ".":
                    count = 0
                    for dx , dy in find:
                        nx = x + dx
                        ny = y + dy
                        if 0 <= nx < m and 0 <= ny < n:
                            if arr[ny][nx] == "*":
                                count += 1
                    arr[y] = arr[y][:x] + str(count) + arr[y][x+1:]
        print(f"Field #{now}:")
        for i in arr:
            print(i)
