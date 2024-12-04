def get_from_file(filename):
    data = []

    with open(filename) as file:
        for line in file:
            nums  = [int(num) for num in line.split()]
            data.append(nums)

    return data


def is_safe(row):
    if row == sorted(row) or row == sorted(row, reverse=True):
        for i in range(len(row) - 1):
            if abs(row[i] - row[i + 1]) not in [1, 2, 3]:
                    return False
        return True
    
    return False
        

def Q1(data):
    safe_count = 0

    for row in data:
        if is_safe(row):
            safe_count += 1

    return safe_count


def Q2(data):
    safe_count = 0

    for row in data:
        if is_safe(row):
            safe_count += 1
            continue

        else:
            for i in range(len(row)):
                temp = row[:i] + row[i+1:]
                if is_safe(temp):
                    safe_count += 1
                    break
       
    return safe_count



data = get_from_file("D2.txt")
# print(Q1(data))
print(Q2(data))