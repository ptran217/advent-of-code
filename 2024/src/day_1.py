# Day 1
def day_one_part_one(list1, list2):
    # Sort
    list1.sort()
    list2.sort()

    # Check list lengths
    if len(list1) != len(list2):
        print("Lists not equal in length for comparison")
    else:
        # Iterate through lists
        result = 0

        for idx, x in enumerate(list1):
            diff = abs(list1[idx] - list2[idx])
            result += diff

        print(result)

def day_one_part_two(list1, list2):
    # O(n^2)
    result = 0
    for idx, x in enumerate(list1):
        match_count = 0
        for idy, y in enumerate(list2):
            if x == y:
                match_count += 1
        result = result + x * match_count
    print(result)

def main():
    # Day 1

    # Read list from file
    list1 = []
    list2 = []

    with open('../data/input_1.txt', 'r') as file:
        for line in file:
            parts = line.split()
            list1.append(int(parts[0]))
            list2.append(int(parts[1]))

    day_one_part_one(list1, list2)
    day_one_part_two(list1, list2)

main()