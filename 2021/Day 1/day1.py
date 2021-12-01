f = open('input.txt')
a = f.read().strip().split('\n')
a_num = list(map(int,a))
#print(a_num)
depth = depth2 = 0

#part1 
for i in range(len(a_num)):
    if a_num[i] > a_num[i-1]:
        depth = depth + 1

print("Depth 1 =",depth)
#part 2
for i in range(len(a_num)-3):
    if a_num[i] < a_num[i+3]:
        depth2 = depth2 + 1
print("Depth 2 =",depth2)
