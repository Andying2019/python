def cacu_prof_v4(amount,rate,degree):
    r = 0
    # degree = [1000000, 600000, 400000, 200000, 100000, 0]
    # rate = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
    for i in range(0, len(degree)):
        if amount > degree[i]:
            print(i)
            r += (amount - degree[i]) * rate[i]
            # print((amount - degree[i]) * rate[i])
            amount = degree[i]
    print(r)
    return r
aa4 = cacu_prof_v4(35,[0.1,0.075,0.05,0.03,0.015,0.01,0.0008],[10,20,40,60,100,200])

print(aa4)
