nums = [1,1,2]

size = len(nums)
insertIndex = 1
for i in range(1, size):
    # Found unique element
    if nums[i - 1] != nums[i]:      
        # Updating insertIndex in our main array
        nums[insertIndex] = nums[i] 
        # Incrementing insertIndex count by 1 
        insertIndex = insertIndex + 1

print(nums)
print(insertIndex)