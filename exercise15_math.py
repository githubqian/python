def math_divisive (n,m):
	if n%m == 0:
		return True
		
	else:
		return False
		
def math_mean (numbers):
	sum = 0
	for mun in numbers:
		sum = sum + mun
	return sum/len(numbers)
	
	
def math_medium (numbers):
	if len(numbers) == 0:
		return None
	if len(numbers) == 1:
		return numbers[0]
	else:
		sorted_numbers = sorted(numbers)
		print sorted_numbers
		if len(sorted_numbers)%2 == 0:
			return (sorted_numbers[len(sorted_numbers)/2 -1] + sorted_numbers[len(sorted_numbers)/2])/2
		else:
			return sorted_numbers[len(sorted_numbers)/2]

	


if __name__ == '__main__':
	
		
	# print math_divisive(10,1)		
	# print math_divisive(10,2)
	# print math_divisive(10,3)
	# print math_divisive(10,4)
	# print math_divisive(10,5)
	# print math_divisive(10,6)
	# print math_divisive(21,2)
	# print math_divisive(21,3)
	# print math_divisive(21,7)
	# print math_divisive(21,21)

	# print math_mean ([10,11,20,99,200,33,56,80])
	print math_medium ([10,11,20,99,200,33,56,80])
	print math_medium ([10.00,11.00,20.00,99.00,200.00,33.00,56.00,80.00])
	print math_medium ([10.00,11.00,20.00,99.00,200.00,33.10,56.77,80.00])	
	print math_medium ([10,11,20,99,200,33,56,80,75])	