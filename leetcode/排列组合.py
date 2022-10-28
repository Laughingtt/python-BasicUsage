lis = [0,1,2,4,5,8]
new_lis = []
for one in lis:
    # print(one)
    for two in lis:
        # print(two)
        for three in lis:
            # print(three)
            for four in lis:
                # print(four)
                for five in lis:
                    # print(five)
                    for six in lis:
                        # print(six)
                        new = str(one)+str(two)+str(three)+str(four)+str(five)+str(six)
                        new_lis.append(new)
for i in new_lis:
    if "5" in i:
        print(i)
print(len(new_lis),new_lis)
