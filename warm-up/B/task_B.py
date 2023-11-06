a, b, c, d = map(int, input().split())


def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def add_fractions(a, b, c, d):
    common_denominator = b * d
    
    numerator = a * d + c * b
    
    greatest_common_divisor = gcd(numerator, common_denominator)
    numerator //= greatest_common_divisor
    common_denominator //= greatest_common_divisor
    
    return numerator, common_denominator

result_numerator, result_denominator = add_fractions(a, b, c, d)

print(result_numerator, result_denominator)