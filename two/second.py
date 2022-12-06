def second():
    score = 0
    with open("input.txt") as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            opponent, mine = line.split()
            opponentHand, myHand = ord(opponent) - 65, ord(mine) - 88
            if myHand == 0:
                score += (opponentHand + 2) % 3 + 1
            elif myHand == 1:
                score += 3 + opponentHand + 1
            else:
                score += 6 + (opponentHand + 1) % 3 + 1
    print(score)


if __name__ == "__main__":
    second()
