def sum_of_squares(n):
	return sum([x**2 for x in range(n+1)])

def is_excited(input):
	if '!' in input:
		return True
	else:
		caps = 0
		for c in input:
			if c.isupper():
				caps += 1
			if caps > len(input)/2.0:
				return True
		return False

print is_excited("fdajldafkjl!")
print is_excited("fsdjklafafda")
print is_excited("DKSNKEAfafda")

print sum_of_squares(4)
