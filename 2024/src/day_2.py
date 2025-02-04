# Day 2
def day_two(report) -> bool:
    '''
    Function needs to:
        1. Check if subsequent points are continuously increasing or decreasing
        2. Check if they change within the acceptable tolerance (atleast 1, atmost 3)
    '''
    inc_flag = False
    dec_flag = False
    idx = 1
    # First check for increasing
    if report == sorted(report):
        inc_flag = True
    if report == sorted(report,reverse=True):
        dec_flag = True

    safe_flag = True

    if inc_flag or dec_flag:
        damp_count = 1
        while idx < len(report):
            diff = abs(report[idx] - report[idx-1])
            if diff < 1 or diff > 3:
                print("Change out of bounds:", report)
                safe_flag = False
                break
            idx += 1
    else:
        print("Not safe:", report)
        return False
    
    return safe_flag


def main():
    # Initialise 2d array
    data = []
    result = 0
    # Read file
    with open('../data/input_2.txt', 'r') as file:
        for line in file:
            report = line.split()
            report = [int(item) for item in report]
            data.append(report)
            
    
    for report in data:
        # Function
        if day_two(report):
            result += 1
    
    print(result)


main()