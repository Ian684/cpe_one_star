if __name__ == "__main__":
    n = int(input())
    for i in range(1 , n + 1):
        x1 , y1 , x2 , y2 = map(int , input().split())
        count1 = x1
        count2 = x2 
        for c in range(x1 + y1 + 1):
            count1 += c
        for c in range(x2 + y2 + 1):
            count2 += c
        print(f"Case {i}: {count2 - count1}")