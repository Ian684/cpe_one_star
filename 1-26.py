if __name__ == "__main__":
    n = int(input())
    trash = input()
    for i in range(n):
        count = {}
        quantity = 0
        while True:
            try:
                name = input()
                if name == '' and n != 1:
                    break
                quantity += 1
                if name in count:
                    count[name] += 1
                else:
                    count[name] = 1
            except EOFError:
                break
        for key , value in sorted(count.items() , key = lambda x : x[0]):
            print(f"{key} {(value/quantity)*100:.4f}")
        print()
    
            