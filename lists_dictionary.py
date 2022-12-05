def run():
	my_list = [1,'hi',True, 4.5]
	my_dict = {'firstname': 'Miguel', 
	'lastname': 'Garcia'}



	super_dict = {
		"natural_nums": [1,2,3,4,5],
		"integer_nums": [-1,-2,0,1,2,],
		"floating_nums": [1.1,4.5,6.43]
	}

	for key, value in super_dict.items():
		# print(key,"-", value)
		print(f"{key} - {value}")

	super_list = [# meter la info de un dicc a una list
		{'firstname': 'Miguel', 'lastname': 'Garcia'},
		{'firstname': 'susana', 'lastname': 'Garcia'},
		{'firstname': 'jose', 'lastname': 'Garcia'},
		{'firstname': 'camila', 'lastname': 'Guerro'}
	]
	
	for item in super_list:
		print(item["firstname"], "-" ,item["lastname"])
		# print(item.keys())


if __name__ == '__main__':
	run()