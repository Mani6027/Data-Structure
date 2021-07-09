# Greatest common divisor of two numbers
# Euclidean algorithm
# GCD(48, 18)
# step1: 48/18 = 2 reminder 12
# step2: 18/12 = 1 reminder 6
# step3: 12/6 = 2 reminder 0

def gcd(num1, num2):
	assert int(num1) == num1 and int(num2) == num2, 'The numbers mst be integer only!'
	if num2 == 0:
		return num1
	# To handle negative number
	if num1 < 0:
		num1 = -1 * num1
	if num2 < 0:
		num2 = -1 * num2
	return gcd(num2, num1%num2)

res = gcd(48,-18)
print(res)