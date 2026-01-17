if __name__ == "__main__":
    num = int(input())
    for i in range(1 , num+1):
        table = {}
        arr = []
        for a in range(4):
            arr.append(list(map(int , input().split())))
        j = 0
        for a in arr:
            for b in a:
                table[j] = b
                j += 1
        q = int(input())
        brr = []
        for qq in range(q):
            brr.append(int(input()))
        print(f"Case {i}:")
        for aim in brr:
            result = float("inf")
            ans = []
            for base in range(2 , 37):
                use = aim
                count = 0
                while True:
                    if use == 0:
                        break
                    count += table[use%base]
                    use //= base
                if count < result:
                    result = count
                    ans = [str(base)]
                elif count == result:
                    ans.append(str(base))
                else:
                    continue
            print(f"Cheapest base(s) for number {aim}:{' '.join(ans)}")