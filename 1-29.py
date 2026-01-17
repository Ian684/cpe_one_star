if __name__ == "__main__":
    while True:
        try:
            arr = []
            a = input()
            b = input()
            # 1
            # for i in range(len(a)):
            #     for j in range(len(b)):
            #         if a[i] == b[j]:
            #             arr.append(a[i])
            #             a = a[:i] + "0" + a[i+1:]
            #             b = b[:j] + "0" + b[j+1:]
            #             break
            # print("".join(sorted(arr)))
            # 2
            check_a = {}
            check_b = {}
            for i in range(len(a)):
                if a[i] in check_a:
                    check_a[a[i]] += 1
                else:
                    check_a[a[i]] = 1
            for i in range(len(b)):
                if b[i] in check_b:
                    check_b[b[i]] += 1
                else:
                    check_b[b[i]] = 1
            for key in sorted(check_a):
                if key in check_b:
                    print(key*min(check_a[key], check_b[key]), end="")
            print()
        except EOFError:
            break