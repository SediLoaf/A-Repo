# dead easy but wanna learn to do it manually
# was not dead easy, pasting code 
def gcd(a, b):
	return a if not b else gcd(b, a%b)
def lcm(nums):
	r = 1
	for n in nums:
		r = n*r//gcd(n, r) # kinda makes sence
	return r
print(lcm([1,2,3,4,5,6]))