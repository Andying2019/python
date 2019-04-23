# 计算奖金 version 1
# amount 利润
# rate:奖金比例 [0.1,0.075,0.015,0.001]
# degree 分段 [10,20,40,60,100]

def cacu_prof_v2(amount,rate,degree):
	if amount <0:
		print("输入错误！")
		return "请输入大于零的值"
	elif amount<=degree[0]:
		bonus=rate[0]*amount

	elif amount<=degree[1]:
		bonus=	degree[0] * rate[0]+\
				(amount- degree[0])*rate[1]

	elif amount<=degree[2]:
		# print("case2")
		# print("degree[0]+rate[0]+(degree[1]- degree[0])*rate[1]+(amount- degree[1])*rate[2] = ")
		# print("%f+%f+(%f-%f)*%f+(%f-%f)*%f"%(degree[0],rate[0],degree[1],degree[0],rate[1],amount,degree[1],rate[2])  )
		bonus=	degree[0]*rate[0]+\
				(degree[1]- degree[0])*rate[1]+\
				(amount- degree[1])*rate[2]

	elif amount<=degree[3]:
		bonus=rate[0]*degree[0]+\
				(degree[1]- degree[0])*rate[1]+\
				(degree[2]- degree[1])*rate[2] +\
				(amount- degree[2])*rate[3]

	elif amount<=degree[4]:
		bonus=	degree[0] * rate[0]+\
				(degree[1]- degree[0])*rate[1]+\
				(degree[2]- degree[1])*rate[2]+ \
				(degree[3]- degree[2])*rate[3]+\
				(amount- degree[3])*rate[4]

	elif amount>degree[4]:
		bonus=	degree[0] * rate[0]+\
		(degree[1]- degree[0])*rate[1]+\
		(degree[2]- degree[1])*rate[2]+ \
		(degree[3]- degree[2])*rate[3]+\
		(degree[4]- degree[3])*rate[4]+\
		(amount- degree[4])*rate[5]

	return bonus
aa2=cacu_prof_v2(45,[0.1,0.075,0.05,0.03,0.015,0.01],[10,20,40,60,100])
print(aa2)

aa3=cacu_prof_v2(150,[0.1,0.065,0.05,0.03,0.0135,0.01,0.0008],[10,20,40,60,100,200])
print(aa3)



