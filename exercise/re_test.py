import re


p = re.compile("(\d+)-(\d+)-(\d+)")
r = p.match("2020-07-01").groups()
print(r)

phone = "13245679 #abc"
p2 = re.sub("#.*$", "", phone)
print(p2)