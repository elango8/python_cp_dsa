def maxProduct(nums):
  
    max_so_far = nums[0]
    min_so_far = nums[0]
    result = nums[0]

    
    for num in nums[1:]:
        temp_max = max(num, num * max_so_far, num * min_so_far)
        temp_min = min(num, num * max_so_far, num * min_so_far)

       
        max_so_far, min_so_far = temp_max, temp_min

       
        result = max(result, max_so_far)

    return result