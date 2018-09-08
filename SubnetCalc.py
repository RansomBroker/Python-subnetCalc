def netMask(cidr):
	hostBit = hostBitLength(cidr)
	maxHst = maxHost(hostBit)
	mask = []
	for i in range(int(cidr)):
		result = 2 << (7 - i % 8 )
		mask.append(result)
	fill_res = list(filter(lambda n: n >> 8, mask))
	index = 0
	for i in range(int(3)):
		fill_res_oktet = fill_res[index] - 1
		fill_res[index] = fill_res_oktet
		index = index + 1
	oktet_class_c = len(fill_res) - 1
	math_subnet_mask = fill_res[oktet_class_c] - maxHst
	fill_res[oktet_class_c] = math_subnet_mask
	if(int(cidr) == int(24)):
		fill_res = [255, 255, 255, 0]
	print()
	print()
	print(fill_res)
	print()
	return fill_res

def	hostBitLength(cidr):
	host_bit_length = 32 - int(cidr)
	return host_bit_length

def  maxHost(hostBitLength):
	math_max_host  = 2**int(hostBitLength)
	return math_max_host


def goToBit(netmask):
	net_mask = netMask(netmask)
	mask_in_bit_length = []
	for i in net_mask:
		convert_to_bin = bin(i)[2:]
		mask_in_bit_length.append(convert_to_bin)

netMask(30)

