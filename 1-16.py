if __name__ == "__main__":
    while True:
        try:
            text = input()
            count = {}
            for i in range(len(text)):
                if text[i] in count:
                    count[text[i]] += 1
                else:
                    count[text[i]] = 1
            count = sorted(count.items() , key=lambda x: (x[1] , -ord(x[0])))
            for a in count:
                print(ord(a[0]) , a[1])
        except EOFError:
            break