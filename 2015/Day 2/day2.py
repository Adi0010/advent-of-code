import fileinput
part1, part2 = 0, 0
with open('/Users/adityakoli/Desktop/Projects/advent-of-code/2015/Day 2/input.txt') as input:
    for line in input:
        l,w,h = [int(i) for i in line.split('x')]
        area = 2*l*w + 2*w*h + 2*h*l
        slack = min(l*w, w*h, h*l)
        part1 += area + slack
        ribbon  = 2* min(l+w , w+h , h+l)
        bow = l*w*h
        part2 += ribbon+bow
    print(part1)
    print(part2)