if __name__ == "__main__":
    while True:
        n = int(input())
        if n == 0:
            break
        dice = [
            [0 , 4 , 0 , 0],
            [2 , 1 , 5 , 6],
            [0 , 3 , 0 , 0],
        ]
        # north 
        # [0 , 4 , 0 , 0]
        # [1 , 5 , 6 , 2]
        # [0 , 3 , 0 , 0]
        # west
        # [0 , 6 , 0 , 0]
        # [2 , 4 , 5 , 3]
        # [0 , 1 , 0 , 0]
        # east
        # [0 , 1 , 0 , 0]
        # [2 , 3 , 5 , 4]
        # [0 , 6 , 0 , 0]
        # south
        # [0 , 4 , 0 , 0]
        # [6 , 2 , 1 , 5]
        # [0 , 3 , 0 , 0]
        for _ in range(n):
            dir = input()
            if dir == "north":
                dice[1][0] , dice[1][1] , dice[1][2] , dice[1][3] = dice[1][1] , dice[1][2] , dice[1][3] , dice[1][0]
            elif dir == "west":
                dice[0][1] , dice[1][1] , dice[1][3] , dice[2][1] = dice[1][3] , dice[0][1] , dice[2][1] ,dice[1][1]
            elif dir == "east":
                dice[0][1] , dice[1][1] , dice[1][3] , dice[2][1] = dice[1][1] , dice[2][1] , dice[0][1] , dice[1][3]
            else:
                dice[1][0] , dice[1][1] , dice[1][2] , dice[1][3] = dice[1][3] , dice[1][0] , dice[1][1] , dice[1][2]
        print(dice[1][1])