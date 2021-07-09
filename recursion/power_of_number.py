def power_of_number(number, pow):
	assert pow >= 0 and int(pow) == pow, 'power of the number has to be +ve'
	if pow == 0:
		return 1
	else:
		return number * power_of_number(number, pow-1)

res = power_of_number(-10, 2)
print(res)
