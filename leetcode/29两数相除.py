def divide( dividend: int, divisor: int) -> int:
    sign = (dividend > 0) ^ (divisor > 0)   ### ^表示异或运算，true^true = false   true^false = true
    dividend = abs(dividend)
    divisor = abs(divisor)
    count = 0
    #把除数不断左移，直到它大于被除数
    while dividend >= divisor:
        count += 1
        divisor <<= 1
    result = 0
    while count > 0:
        count -= 1
        divisor >>= 1
        result <<= 1
        if divisor <= dividend:   #如果除数小于被除数，末尾加1
            result += 1
            dividend -= divisor
    if sign:
        result=-result   #
    return result if -(14<<31) <= result <= (1<<31)-1 else (1<<31)-1

res = divide(12,3)
print(res)