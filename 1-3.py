n = 1
while True :
    try:
        line = input()
        while "\"" in line:
            if n == 1:
                line = line[0:line.index("\"")]+"``"+line[line.index("\"")+1:]
                n = 2
            elif n == 2:
                line = line[0:line.index("\"")]+"''"+line[line.index("\"")+1:]
                n = 1
        print(line)
    except EOFError:
        break
# use traversal is faster