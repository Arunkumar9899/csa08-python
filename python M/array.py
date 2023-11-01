def num_identical_pairs(nums):
    count = 0
    for i in range(len(nums)):
        for j in range(i + 1,len(nums)):
            if nums[i] == nums[j]:
                count += 1
                return count
            nums =[1,2,3,4,5]
            good_pairs = num_identical_pairs(nums)
            print("Number of good pairs: ")
