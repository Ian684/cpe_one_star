if __name__ == "__main__":
    arr = []
    while True:
        try:
            sentense = str(input())
            arr.append(sentense)
        except EOFError:
            break
    longer = 0
    for long in arr:
        if len(long) > longer:
            longer = len(long)
    for i in range(longer):
        for j in range(len(arr)-1 , -1 , -1):
            try:
                print(arr[j][i] , end="")
            except IndexError:
                print(" " , end="")
        print()