def second():
    totalOverlaps = 0

    with open("input.txt") as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip().split(",")
            firstPair = line[0].split("-")
            secondPair = line[1].split("-")
            firstPair = [int(firstPair[0]), int(firstPair[1])]
            secondPair = [int(secondPair[0]), int(secondPair[1])]
            if firstPair[0] < secondPair[0] and firstPair[1] >= secondPair[0]:
                totalOverlaps += 1
            elif firstPair[0] == secondPair[0]:
                totalOverlaps += 1
            else:
                if secondPair[0] < firstPair[0] and secondPair[1] >= firstPair[0]:
                    totalOverlaps += 1

    print(totalOverlaps)


if __name__ == "__main__":
    second()
