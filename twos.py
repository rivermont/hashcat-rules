work1 = open('one_liners.txt')
work2 = open('one_liners.txt')
doc = open('twos.rule', 'w')

doc.write(':\n')

for line in work1:
	work2.seek(0)
	for line1 in work2:
		doc.write(line.strip() + ' ' + line1)

work1.close()
work2.close()
doc.close()
