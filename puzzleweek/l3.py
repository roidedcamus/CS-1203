def gcd(a, b):
  while b != 0:
    a, b = b, a % b
  return a

nums = []
for i in range (2,1203):
  if gcd(i,1203) == 1:
    nums.append(i)

print(len(nums))

largest = 0
ans = 0 

for num in nums:
    for i in range(1,800):
        if pow(num,i,1203) == 1:
            if largest < i:
                ans = largest
                largest = i

            break

print(ans)
    



