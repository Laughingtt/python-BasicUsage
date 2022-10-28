arr = [3,5,1]
sorted_arr = sorted(arr)
first = sorted_arr[0]
lis = []
for i in sorted_arr[1:]:
    res = first - i
    lis.append(res)
    first = i

if len(set(lis)) == 1:
    print("true")
else:
    print("false")