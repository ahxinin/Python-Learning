# 星座计算

constellation = ('摩羯座', '水瓶座', '双鱼座', '白羊座', '金牛座', '双子座', '巨蟹座', '狮子座', '处女座', '天秤座', '天蝎座', '射手座')
constellation_date = ((1,19), (2,18), (3,20), (4,19), (5,20), (6,21), (7,22), (8,22), (9,22), (10,23), (11,22), (12,21))

(month, day) = (12,22)
# data_array = filter(lambda x : x < (month,day), constellation_date)
# print(constellation[len(list(data_array)) % 12])

# for cd in constellation_date:
#     if cd > (month, day):
#         print(constellation[len(cd)])
#         break
#     elif month == 12 and day > 21:
#         print(constellation[0])
#         break

num = 0
while constellation_date[num] < (month, day):
    if month == 12 and day > 21:
        break
    num += 1
print(constellation[num])