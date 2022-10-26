nums = [2, 5, 5, 11]
target = 10

dict = {}
for i, elem in enumerate(nums):
    if target - elem in dict:
        print(dict[target - elem], i)
    dict[elem] = i

