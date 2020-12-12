import fileinput

def part1():
    DX = [0,1,0,-1]
    DY = [1,0,-1,0]
    dir_ = 1
    x = 0 
    y = 0
    for line in List:
        D = line[0]
        A = int(line[1:])
        if D == 'N':
            y+=A
        elif D == 'S':
            y-=A
        elif D == 'E':
            x+=A
        elif D == 'W':
            x-=A
        elif D == 'L':
            dir_ = (dir_+3*(A//90))%4
        elif D == 'R':
            dir_ = (dir_+1*(A//90))%4
        elif D == 'F':
            x += DX[dir_]*A
            y += DY[dir_]*A
    return abs(x)+abs(y)

def part2():
    wx = 10
    wy = 1
    x = 0 
    y = 0

    for line in List:
        D = line[0]
        A = int(line[1:])
        if D == 'N':
            wy+=A
        elif D == 'S':
            wy-=A
        elif D == 'E':
            wx+=A
        elif D == 'W':
            wx-=A
        elif D == 'L':
            for _ in range(A//90):
                wx,wy = -wy,wx
        elif D == 'R':
            for _ in range(A//90):
                wx,wy = wy, -wx

        elif D == 'F':
            x += wx*A
            y += wy*A
    return abs(x)+abs(y)

if __name__ == "__main__":
    List = [l.strip() for l in fileinput.input('/input.txt')]

    print(part1())
    print(part2())
