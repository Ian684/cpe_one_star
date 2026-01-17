if __name__ == "__main__":
    import math
    while True:
        a , b = map(int , input().split())
        if a == 0 and b == 0:
            break
        a , b = math.ceil(math.sqrt(a)) , math.floor(math.sqrt(b))
        print(b - a + 1)