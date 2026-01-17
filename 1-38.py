if __name__ == "__main__":
    while True:
        text = input()
        if text == "0":
            break
        count = 0
        for i in range(len(text)):
            count += int(text[i])
        if count % 9 != 0:
            print(f"{text} is not a multiple of 9.")
            continue
        print(f"{text} is a multiple of 9 and has 9-degree" ,end=" ")
        degree = 1
        while True:
            text = str(count)
            count = 0
            if int(text) // 10 == 0:
                break
            for i in range(len(text)):
                count += int(text[i])
            degree += 1
        print(f"{degree}.")