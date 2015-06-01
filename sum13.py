def sum13(nums):
  res = 0
  for i in range(len(nums)):
    if nums[i] == 13:
      continue
    if i > 0 and  nums[i-1] == 13:
      continue
    else:
      print nums[i]
      res += nums[i]
  print res

sum13([1, 2, 13, 2, 1, 13])

