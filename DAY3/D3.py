import re

def D3Q1(filename):
    data = []

    with open(filename) as file:
        for line in file:
            regex = re.findall('mul\([0-9]+,[0-9]+\)',line)
            for i in regex:
               numbers_in_regex = re.findall(r'\d+', i)
               number1, number2 = map(int, numbers_in_regex)
               data.append(number1*number2)

    total = 0
    for each_value in data:
        total+=each_value
    print(total)

D3Q1("D3.txt")
