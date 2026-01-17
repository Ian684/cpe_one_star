if __name__ == "__main__":
    arr = []
    while True:
        a , b = map(int, input().split())
        if a == 0 and b == 0:
            break
        count = 0
        carry = 0
        while True:
            a_one = a % 10
            b_one = b % 10
            a //= 10
            b //= 10
            if a_one + b_one + carry >= 10:
                count += 1
                carry = 1
            else:
                carry = 0
            if a == 0 or b == 0:
                if carry + a % 10 + b % 10 >= 10:
                    count += 1
                break
        arr.append(count)
        
    for i in arr:
        if i == 0:
            print("No carry operation.")
            continue
        elif i == 1:
            print("1 carry operation.")
            continue
        print(f"{i} carry operations.")