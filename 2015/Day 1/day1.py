#this is a test file for Day 1 AOC 2015


def part1(floor):
    for char in a:
        if char == '(':
            floor+=1
        elif char == ')':
            floor-=1
    return floor

def part2(floor):
    index = 1
    basement = 0
    for char in a:
        if char == '(':
            floor+=1
        elif char == ')':
            floor-=1
        index+=1
        if floor < basement:
            break
    return index

if __name__ == "__main__":
    
    f = open('input.txt')
    a = f.read()
    print(part1(0),part2(0))
    