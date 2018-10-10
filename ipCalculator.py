def netMask(cidr):
	mask = []
	# for class C
	if(int(cidr) >= int(24)):
		for i in range(int(cidr)):
			result = 2 << (7 - i % 8)
			mask.append(result)
		fill_res = list(filter(lambda n: n >> 8, mask))
		index = 0
		for i in range(int(3)):
			fill_res_oktet = fill_res[index] - 1
			fill_res[index] = fill_res_oktet
			index = index + 1
		oktet_class_c = len(fill_res) - 1
		host_bit_length = 32 - int(cidr)
		max_host = 2**host_bit_length
		math_subnet_mask = fill_res[oktet_class_c] - max_host
		fill_res[oktet_class_c] = math_subnet_mask
	elif(int(cidr) == int(24)):
		fill_res = [255, 255, 255, 0]
	# for Class B
	if(int(cidr) < int(24) & int(cidr) >= int(17)):
		for i in range(int(cidr)):
			result = 2 << (7 - i % 8)
			mask.append(result)
		fill_res = list(filter(lambda n: n >> 8, mask))
		index = 0
		for i in range(int(2)):
			fill_res_oktet = fill_res[index] - 1
			fill_res[index] = fill_res_oktet
			index = index + 1
		oktet_class_b = len(fill_res) - 1
		a = 32 
		for i in range(int(24)):
			a = a - 1
		d = int(cidr) - a
		max_host = 2**d
		class_b = int(cidr) - 16
		next_class_b = 2**class_b 
		math_subnet_mask = fill_res[oktet_class_b] - next_class_b
		fill_res[oktet_class_b] = math_subnet_mask
		print(fill_res)
	elif(int(cidr) == int(16)):
		fill_res = [255, 255, 0, 0]
		print(fill_res)
	# for class a
	if(int(cidr) < int(16) & int(cidr) >= int(8)):
		for i in range(int(cidr)):
			result = 2 << (7 - i % 8)
			mask.append(result)
		fill_res = list(filter(lambda n: n >> 8, mask))
		index = 0 
		for i in range(int(1)):
			fill_res_oktet = fill_res[index] - 1
			fill_res[index] = fill_res_oktet
			index = index + 1
		oktet_class_a = len(fill_res) - 1
		a = int(32) - int(cidr)
		max_host = 2**a
		d = int(16) - int(cidr)
		math = 2**d
		math_subnet_mask = fill_res[oktet_class_a] - math
		fill_res[oktet_class_a] = math_subnet_mask
		print(fill_res)
	elif(int(cidr) == int(8)):
		fill_res = [255, 0, 0, 0]
		print(fill_res)
			
		
netMask(8)