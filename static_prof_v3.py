# 计算奖金 version 1
# amount 利润
# rate:奖金比例 [0.1,0.075,0.015,0.001]
# degree 分段 [10,20,40,60,100]

def cacu_prof_v2(amount,rate,degree):

	# for d in degree:
	# 	print(d)
	# 	if amount <d:
	# 		print("dddddddd")
	# 		break
	# print("d = ",d)
	
	#找出第一个大于amount的degree的下标
	length = len(degree)
	for end_pos in range(length):
		print(end_pos)
		if amount < degree[end_pos]:
			break
	end_pos = end_pos -1
	print("end_pos = ",end_pos)

	# 正式计算
	bonus = 0
	if end_pos == 0:
		bonus = rate[0]*degree[0]
	else:
# 		bonus=	degree[0] * rate[0]+\
# 		(degree[1]- degree[0])*rate[1]+\
# 		(degree[2]- degree[1])*rate[2]+ \
# 		(degree[3]- degree[2])*rate[3]+\
# 		(degree[4]- degree[3])*rate[4]+\
# 		(amount- degree[4])*rate[5]
		bonus=rate[0]*degree[0]
		i = 0
		for i in range(1,end_pos-1):
			bonus = bonus + (degree[i]-degree[i-1])*rate[i]
		bonus = bonus + (amount- degree[i])*rate[i+1]
	return bonus
aa4 = cacu_prof_v2(8,[0.1,0.075,0.05,0.03,0.015,0.01,0.0008],[10,20,40,60,100,200])

print(aa4)

