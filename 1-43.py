if __name__ == "__main__":
    while True:
        try:
            n = int(input())
            d = n
            while n >= 3:
                d += n//3
                n = n//3 + n%3
            if n == 2:
                d += 1
            print(d)
        except EOFError:
            break