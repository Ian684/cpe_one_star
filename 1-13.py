if __name__ == "__main__":
    while True:
        try:
            our , their = map(int, input().split())
            print(abs(their - our))
        except EOFError:
            break