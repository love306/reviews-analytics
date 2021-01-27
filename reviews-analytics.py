data = []
reviews_average = 0
with open ('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		reviews_average += len(line)
		if len(data) % 10000 == 0:
			print(len(data))

print('字典共有', len(data),'筆資料')
print('每筆留言均長', reviews_average/len(data))
