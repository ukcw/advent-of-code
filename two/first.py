def first():
    score = 0
    with open("input.txt") as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            opponent, mine = line.split()
            opponentHand, myHand = ord(opponent) - 65, ord(mine) - 88
            if opponentHand == myHand:
                score += 3 + myHand + 1
            elif opponentHand == (myHand + 1) % 3:
                score += myHand + 1
            else:
                score += 6 + myHand + 1
    print(score)


if __name__ == "__main__":
    first()
