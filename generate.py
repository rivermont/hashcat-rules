ascii = '''ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+-=`~[]\{}|;':",./<>?'''
nums = '''1234567890'''

work = open('one_liners.txt', 'w')

#Functions with no arguments
functions_0 = '''lucCtrdf{}[]qkKE'''

#Functions with 1 character argument
functions_1_char = '''$^@'''

#Functions with 1 number argument
functions_1_num = '''TpD'zZ'''

#Functions with 2 character arguments
functions_2_char = '''s'''

#Functions with 2 number arguments
functions_2_num = '''xO'''

#Functions with 1 character arg and 1 number arg
functions_1_each = '''io'''

for function in functions_0:
	work.write(function + '\n')

for function in functions_1_char:
	for char in ascii:
		work.write(function + char + '\n')

for function in functions_1_num:
	for num in nums:
		work.write(function + num + '\n')

for function in functions_2_char:
	for char in ascii:
		for char1 in ascii:
			work.write(function + char + char1 + '\n')

for function in functions_2_num:
	for num in nums:
		for num1 in nums:
			work.write(function + num + num1 + '\n')

for function in functions_1_each:
	for num in nums:
		for char in ascii:
			work.write(function + num + char + '\n')

work.close()
