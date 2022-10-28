strs = ["c","c"]
first = strs[0]
for i in range(len(first)):
    forward = first[:i + 1]
    for k in [j[:i + 1] for j in strs]:
        if k != forward:
            break
    else:
        print("相同:",forward)
        res = forward