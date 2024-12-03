left_column = []
right_column = []


def get_from_file(filename):
    with open(filename) as file:
        for line in file:
            left , right = line.split()
            left_column.append(int(left))
            right_column.append(int(right))


get_from_file("D1.txt")

def calc_similarity_score():
    similarity_score = 0   
    for i in left_column:
        j_count = 0
        for j in right_column:  
            if i == j:
                j_count += 1
        similarity_score+= i*j_count

    return similarity_score

print(calc_similarity_score())

