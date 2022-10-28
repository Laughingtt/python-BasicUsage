
c = "IX"
d = {'I': 1, 'IV': 3, 'V': 5, 'IX': 8, 'X': 10, 'XL': 30, 'L': 50, 'XC': 80, 'C': 100, 'CD': 300, 'D': 500, 'CM': 800,
     'M': 1000}
s = 0
def run():
    a=1
    print(2)
    print(3)
run()
for i in c:
    s += d[i]
print(s)
