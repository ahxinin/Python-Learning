# 生肖计算

zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'
year = 2020
birth_year = int(input('输入出生年份'))
rate = 12
if (year - birth_year) % 12 == 0:
    print('今年是你的本命年')
print('你的生肖是：%s' % zodiac[birth_year % rate])