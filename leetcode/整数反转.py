num = -12300

lis_num = list(str(num))
symbol = False
if "-" in lis_num:
    lis_num.remove("-")
    symbol = True

if symbol:
    new_lis = list(reversed(lis_num))
    new_lis.insert(0, "-")
else:
    new_lis = list(reversed(lis_num))
res = "".join(new_lis)
print(int(res))

print(2**31)