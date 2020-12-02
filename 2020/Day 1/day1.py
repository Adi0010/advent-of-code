
#Opens the file , converts the list of strings into integers
f = open('input.txt')
a = f.read().split()
a_num = list(map(int,a))
#print(a_num)

#It is similar to two_sum problem on leetcode
#But here we have to find values instead of indexes

def two_sum(a_num,target=2020):
    lookup = {}
    for i, num in enumerate(a_num):
        if target - num in lookup:
            return [a_num[lookup[target - num]]* a_num[i]]
        lookup[num] = i
    return([])

print(two_sum(a_num))

def find3Numbers(A, arr_size, sum): 
  
    # Sort the elements  
    A.sort() 
  
    # Now fix the first element  
    # one by one and find the 
    # other two elements  
    for i in range(0, arr_size-2): 
        l = i + 1 
          
        # index of the last element 
        r = arr_size-1 
        while (l < r): 
          
            if( A[i] + A[l] + A[r] == sum):
                return A[i]* A[l]* A[r]
              
            elif (A[i] + A[l] + A[r] < sum): 
                l += 1
            else: # A[i] + A[l] + A[r] > sum 
                r -= 1
  
    # If we reach here, then 
    # no triplet was found 
    return False

print(find3Numbers(a_num,len(a_num),2020))