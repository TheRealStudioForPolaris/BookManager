def extended_gcd(a, b):
    if b == 0:
        return 1, 0, a
    else:
        x, y, gcd = extended_gcd(b, a % b)
        return y, x - (a // b) * y, gcd

def compute_d(e, phi_n):
    x, y, _ = extended_gcd(e, phi_n)
    d = x % phi_n
    return d if d >= 0 else d + phi_n

# 示例参数
p = 61
q = 53
n = p * q               # n = 3233
phi_n = (p-1) * (q-1)   # φ(n) = 3120
e = 17                  # 公钥指数

d = compute_d(e, phi_n) # d = 2753
print("私钥d =", d)     # 输出：2753