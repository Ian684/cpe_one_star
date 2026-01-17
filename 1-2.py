n , m = map(int , input().split())
lost = []
while True:
    try:
        x , y , side = input().split()
        x , y = int(x) , int(y)
        process = input()
        for p in range(len(process)):
            valid = True
            if process[p] == 'F':
                if side == 'N':
                    if y+1 <= m :
                        y += 1
                    else:
                        if [x , y] in lost:
                            continue
                        lost.append([x , y])
                        print(f"{x} {y} {side} LOST")
                        valid = False
                        break
                elif side == 'E':
                    if x+1 <= n :
                        x += 1
                    else:
                        if [x , y] in lost:
                            continue
                        lost.append([x , y])
                        print(f"{x} {y} {side} LOST")
                        valid = False
                        break
                elif side == 'S':
                    if y-1 >= 0 :
                        y -= 1
                    else:
                        if [x , y] in lost:
                            continue
                        lost.append([x , y])
                        print(f"{x} {y} {side} LOST")
                        valid = False
                        break
                elif side == 'W':
                    if x-1 >= 0 :
                        x -= 1
                    else:
                        if [x , y] in lost:
                            continue
                        lost.append([x , y])
                        print(f"{x} {y} {side} LOST")
                        valid = False
                        break
            elif process[p] == 'R':
                if side == 'N':
                    side = 'E'
                elif side == 'E':
                    side = 'S'
                elif side == 'S':
                    side = 'W'
                elif side == 'W':
                    side = 'N'
            elif process[p] == 'L':
                if side == 'N':
                    side = 'W'
                elif side == 'W':
                    side = 'S'
                elif side == 'S':
                    side = 'E'
                elif side == 'E':
                    side = 'N'
        if valid:print(f"{x} {y} {side}")
    except EOFError:
        break