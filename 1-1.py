def calculate(current):
    count = 0
    num = current
    while True:
        if num in history:
            count += history[num]
            break
        count += 1
        if num == 1:
            break
        if num % 2 == 0:
            num //= 2
        else:
            num = 3 * num + 1
    history[current] = count
    return count
    # 多了紀錄歷史跑過的路徑可以直接用
if __name__ == "__main__":
    history = {}
    while (True):
        try:
            n = input()
            i , j = n.split()
            arr = [0]
            for x in range(min(int(i), int(j)) , max(int(i), int(j)) + 1):
                current = x
                arr.append(calculate(current))
            print(i , j , max(arr))
        except EOFError:
            break