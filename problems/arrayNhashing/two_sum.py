def two_sum(target, nums):
    unique_dic = {}
        for i, num in enumerate(nums):
	        complement = target - num
	        if complement in unique_dic:
		        return[i, unique_dic[complement]]
	        unique_dic[num] = i
