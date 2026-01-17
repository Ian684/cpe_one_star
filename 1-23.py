if __name__ == "__main__":
    n = int(input())
    now = 1
    import math
    for _ in range(n):
        s1 = int(input() , 2)
        s2 = int(input() , 2)
        if math.gcd(s1 , s2) > 1:
            print(f"Pair #{now}: All you need is love!")
        else:
            print(f"Pair #{now}: Love is not all you need!")
        now += 1
        # 轉10進制，再gcd
        # 因為不能整除也就代表不會有減到變一樣
        # 而1一定會減到一樣且題目有禁止0 1