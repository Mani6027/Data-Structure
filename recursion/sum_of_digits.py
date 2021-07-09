# Sum of digit of positive number
def sum_of_digit(number):
	assert number>=0 and int(number) == number, 'This number has to be positive integer only'
	if number == 0:
		return 0
	else:
		return (number % 10)  + sum_of_digit(number//10)
res = sum_of_digit(11111)
print(res)