def second():
    sumOfPriorities = 0

    with open("input.txt") as f:
        lines = f.readlines()
        counter = 0
        group = []
        for line in lines:
            line = line.strip()
            if counter == 3:
                prt = ord(next(iter(set.intersection(*group))))
                if prt >= 97:
                    sumOfPriorities += prt % 97 + 1
                else:
                    sumOfPriorities += prt % 65 + 27
                counter = 0
                group = []
            group.append(set(line))
            counter += 1

        prt = ord(next(iter(set.intersection(*group))))
        if prt >= 97:
            sumOfPriorities += prt % 97 + 1
        else:
            sumOfPriorities += prt % 65 + 27
    f.close()
    print(sumOfPriorities)


if __name__ == "__main__":
    second()
