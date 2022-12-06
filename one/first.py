def first():
    maxCalories = 0
    with open("input.txt") as f:
        lines = f.readlines()
        calories = 0
        for line in lines:
            if line == "\n":
                maxCalories = max(calories, maxCalories)
                calories = 0
            else:
                calories += int(line.strip())

    f.close()
    print(maxCalories)


if __name__ == "__main__":
    first()
