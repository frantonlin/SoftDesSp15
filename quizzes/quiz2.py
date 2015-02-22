def filter_out_negative_numbers(numbers):
	out = []
	for number in numbers:
		if number >= 0:
			out.append(number)
	return out

def in_language(string):
	num_a = 0
	num_b = 0
	for char in string:
		if char == 'a':
			num_a += 1
		elif char != 'b':
			return False
		else:
			break
	for i in range(-1,-len(string),-1):
		if string[i] == 'b':
			num_b +=1
		else:
			break
	return num_a == num_b


print filter_out_negative_numbers([-2.0, 5.0, 10.0, -100.0, 5.0])

print in_language('aaabbb')

