left_column = []
right_column = []
distance = 0 


def get_from_file():
    with open("D1.txt") as file:
        for line in file:
            left , right = line.split()
            left_column.append(int(left))
            right_column.append(int(right))

# print("Left column:", left_column)
# print("Right column:", right_column)

def sort_columns(): 
    left_column.sort()
    right_column.sort()


def calculate_distance(): 
    for i in range(len(left_column)):
        distance += abs(left_column[i] - right_column[i])

    return distance


get_from_file("D1.txt")
sort_columns()
print(calculate_distance())


