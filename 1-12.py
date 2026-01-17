if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        days = int(input())
        quantity = int(input())
        arr = []
        for _ in range(quantity):
            arr.append(int(input()))
        de = set()
        now_fr = 6
        now_sa = 7
        while True:
            if now_fr > days and now_sa > days:
                break
            elif now_fr > days and now_sa <= days:
                de.add(now_sa)
                break
            elif now_fr <= days and now_sa > days:
                de.add(now_sa)
                break
            de.add(now_fr)
            de.add(now_sa)
            now_fr += 7
            now_sa += 7
        total = set()
        for q in arr:
            i = 1
            while True:
                if q*i > days:break
                if q*i not in de:
                    total.add(q*i)
                i += 1
        print(len(total))
