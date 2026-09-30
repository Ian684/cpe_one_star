def main():
    a = {'0':0 , '1':2 , '2':4 , '3':6 , '4':8 , '5':1 , '6':3 , '7':5 , '8':7 , '9':9}
    b = {'0':0 , '1':1 , '2':2 , '3':3 , '4':4 , '5':5 , '6':6 , '7':7 , '8':8 , '9':9}
    t = int(input())
    for _ in range(t):
        card = input().split()
        count = 0
        for c in card:
            count += a[c[0]] + b[c[1]] + a[c[2]] + b[c[3]]
        if count % 10:
            print("Invalid")
        else:
            print("Valid")

if __name__ == "__main__":
    main()
