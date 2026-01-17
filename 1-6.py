def fib(num , fib_number):
    i = len(fib_number) - 1
    while i >= 0 and fib_number[i] > num:
        i -= 1
    result = []
    valid = True
    for k in range(i , -1 , -1):
        if valid and fib_number[k] <= num:
            result.append('1')
            num -= fib_number[k]
            valid = False
        else:
            result.append('0')
            valid = True
    return ''.join(result)
def fib_number_calculate(arr):
    while arr[-1] + arr[-2] <= 1000000000:
        arr.append(arr[-1] + arr[-2])
    return arr
if __name__ == "__main__":
    n = int(input())
    fib_number = fib_number_calculate([1 , 2])
    for i in range(n):
        num = int(input())
        print(f"{num} = {fib(num , fib_number)} (fib)")