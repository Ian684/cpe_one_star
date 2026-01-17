if __name__ == "__main__":
    num = int(input())
    days = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    months = {1:'Monday' , 2:'Tuesday' , 3:'Wednesday' , 4:'Thursday' , 5:'Friday' , 6:'Saturday' , 0:'Sunday'}
    for _ in range(num):
        current = 5
        month , day = map(int , input().split())
        total = day
        for i in range(1 , month):
            total += days[i]
        total %= 7
        print(months[(total+5)%7])
        # dooms沒屌用