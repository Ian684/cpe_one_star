if __name__ == "__main__":
    import math
    history = {}
    while True:
        try:
            n_ = int(input())
            n = int(str(n_)[::-1])
            prime = True
            if n_ < 2:
                print(f"{n_} is not prime.")
                continue
            if n_ not in history:
                for i in range(2, math.ceil(math.sqrt(n_))+1):
                    if n_ % i == 0:
                        prime = False
                        break
                if not prime:
                    history[n_] = False
                    print(f"{n_} is not prime.")
                    continue
            else:
                if not history[n_]:
                    print(f"{n_} is not prime.")
                    continue
            if n_ == n:
                print(f"{n_} is prime.")
                continue
            if n not in history:
                for i in range(2, math.ceil(math.sqrt(n))+1):
                    if n % i == 0:
                        history[n] = False
                        print(f"{n_} is prime.")
                        break
                else:
                    history[n] = True
                    print(f"{n_} is emirp.")
            else:
                if history[n]:
                    print(f"{n_} is emirp.")
                else:
                    print(f"{n_} is prime.")
        except EOFError:
            break
        # 回文注意 字典判斷 範圍所小至根號n + 1
        # n = a * b
        # 一定是 a > 根號n , b < 根號n
        # 只要檢查2到根號n + 1就好