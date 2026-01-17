if __name__ == "__main__":
    while True:
        num = int(input())
        if num == 0:
            break
        if num % 11 == 0:
            print(f"{num} is a multiple of 11.")
        else:
            print(f"{num} is not a multiple of 11.")
