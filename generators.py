nums = [1,2,3,4,5,6]

def evens(stream):
    for n in stream:
        if n % 2 == 0:
            yield n

gennums = evens(nums) 
print(gennums)

for num in gennums:
    print(num)