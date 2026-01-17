if __name__ == "__main__":
    while True:
        try:
            text = input()
            arr = []
            for n in range(len(text)):
                a = ord(text[n])
                if 48 <= a <= 57:
                    arr.append(a-48)
                elif 65 <= a <= 90:
                    arr.append(a-55)
                elif 97 <= a <= 122:
                    arr.append(a-61)
            result = max(arr) + 1
            # for i in range(result , 63):
            #     count = 0
            #     now = 0
            #     for t in reversed(arr):
            #         count += t * (i**now)
            #         now += 1
            #     if count % (i-1) == 0:
            #         ans = i
            #         break
            for i in range(result , 63):
                count = 0
                now = 0
                for t in reversed(arr):
                    count += t % (i - 1)
                    now += 1
                if count % (i - 1) == 0:
                    ans = i
                    break
            else:
                ans = "such number is impossible!"
            print(ans)
        except EOFError:
            break
        # ABC 10 11 12 只需要檢查每個數 % (n - 1)的餘數和再 % (n - 1) == 0 