if __name__ == "__main__":
    n = int(input())
    texts = []
    count = {
        'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0,
        'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0,
        'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0
    }
    for i in range(n):
        texts.append(input())
    
    for text in texts:
        for a in range(len(text)):
            if text[a].upper() in count:
                count[text[a].upper()] += 1
            else:
                continue
    for k, v in sorted(count.items() , key=lambda x: (-x[1] , x[0])):
        if v != 0:
            print(k, v)
        else:
            break
    # while True:
    #     if max(count.values()) == 0:
    #         break
    #     print(max(count, key=count.get), max(count.values()))
    #     count[max(count, key=count.get)] = 0
