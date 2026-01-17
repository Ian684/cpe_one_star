if __name__ =="__main__":
    now = 1
    while True:
        try:
            text = int(input())
            if text == 0:
                print(f"{now}. 0")
                now += 1
                continue
            arr = [
                "shata" , "hajar" , "lakh" , "kuti"
            ]
            result = []
            end = text % 100 
            text //= 100
            i = 0
            while True:
                if text == 0:
                    break
                if arr[i] == "shata":

                    result.append(text % 10)
                    text //= 10
                else:
                    result.append(text % 100)
                    text //= 100
                if i == 3:
                    i = 0
                    continue
                i += 1 
            n = len(result)%4 - 1
            result = reversed(result)
            print(f"{   now}." , end=" ")
            for r in result:
                if n == -1:
                    n = 3
                if r != 0:
                    print(r , arr[n] , end=" ")
                elif r == 0 and arr[n] == "kuti":
                    print("kuti" , end=" ")
                n -= 1
            if end != 0:
                print(end)
            else:
                print()
            now += 1
        except EOFError:
            break
        # text == 0
        # 0 跳過
        # 數字要記得空格
        # kuti 要在下一個循環補上
