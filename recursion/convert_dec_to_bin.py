def convert_decimal_to_bin(num):
	assert int(num) == num, 'The param must be an integer only!'
	if num == 0:
		return 0
	return (num % 2) + (10 * convert_decimal_to_bin(num // 2))

res = convert_decimal_to_bin(100)
print(res)
