def hawaii_scrabble_score(string):
	points = {'A':1,'K':2,'O':2,'I':3,'N':3,'E':4,'U':5,'H':6,'L':7,'M':8,'P':8,'W':9}
	point_list = [points.get(char,-1) for char in string]
	if -1 in point_list:
		return -1
	return sum(point_list)

print hawaii_scrabble_score('ALOHA')
print hawaii_scrabble_score('MAHALO')
print hawaii_scrabble_score('PYTHON')
