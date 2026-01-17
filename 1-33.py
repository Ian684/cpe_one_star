if __name__ == "__main__":
    n = int(input())
    count = {}
    for i in range(n):
        country , first_name , last_name = input().split()
        if country in count:
            count[country] += 1
        else:
            count[country] = 1
    count = sorted(count.items())
    for key , value in count:
        print(key , value)