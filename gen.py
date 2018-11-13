def even(list1):
	for i in list1:
		if i%2 == 0:
			yield i
x = even(range(50))
for i in x:
	print i
