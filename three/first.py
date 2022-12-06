def first():
    sumOfPriorities = 0

    with open("input.txt") as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            mid = len(line) // 2
            ist = set(line[:mid]).intersection(set(line[mid:]))
            prt = ord(next(iter(ist)))
            if prt >= 97:
                sumOfPriorities += prt % 97 + 1
            else:
                sumOfPriorities += prt % 65 + 27

    f.close()
    print(sumOfPriorities)


if __name__ == "__main__":
    first()
