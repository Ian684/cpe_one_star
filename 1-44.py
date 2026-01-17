if __name__ == "__main__":
    while True:
        n , m = map(int , input().split())
        print(n , m)
        if n == 0 and m == 0:
            break
        arr = []
        for _ in range(n):
            a = int(input())
            if a > 0:
                arr.append([a, a % m])
            else:
                arr.append([a , -(-a%m)])
        arr = sorted(arr , key=lambda x:(x[1] , x[0] % 2 == 0 , -x[0] if x[0]%2==1 else x[0]))
        for i , j in arr:
            print(i)
        # 不要用字典，會被覆蓋
        # python!!!!要特別處理a為負數，以c風格