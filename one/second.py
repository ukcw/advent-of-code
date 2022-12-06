import heapq


def second():

    minHeap = []

    with open("input.txt") as f:
        lines = f.readlines()
        calories = 0
        for line in lines:
            if line == "\n":
                print("before", minHeap)
                if len(minHeap) < 3:
                    heapq.heappush(minHeap, calories)
                else:
                    heapq.heappushpop(minHeap, calories)
                calories = 0
                print("after", minHeap)
            else:
                calories += int(line.strip())

    f.close()
    print(sum(minHeap))


if __name__ == "__main__":
    second()
