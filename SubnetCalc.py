def netMask(cidr):
	mask = []
	for i in range(int(cidr)):
		result = 2 << (7 - i % 8 )
		mask.append(result)
	fill_res = list(filter(lambda n: n >> 8, mask))
	math_host_bit_length =  32 - int(cidr)
	index = 0
	for i in range(int(3)):
		fill_res_oktet = fill_res[index] - 1
		fill_res[index] = fill_res_oktet
		index = index + 1
	max_host = 2**int(math_host_bit_length)
	oktet_class_c = len(fill_res) - 1
	math_subnet_mask = fill_res[oktet_class_c] - max_host
	fill_res[oktet_class_c] = math_subnet_mask
	if(int(cidr) == int(24)):
		fill_res = [255, 255, 255, 0]
	print()
	print('===========================')
	print('= netmask :', fill_res)
	print('= host :'+ str(max_host))
	print()
	print('============================')
	print()
	print()
	


netMask(24)