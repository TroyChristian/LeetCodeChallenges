def containsDuplicate(nums) -> bool:
    hash_table = {}
    for number in nums:
        if number not in hash_table:
            hash_table[number] = 1
        else:
            hash_table[number] += 1
        
    for i in hash_table.values():
        if i >= 2:
            return True
    return False
    
print(containsDuplicate([2,14,18,22,22]))
