def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def inverse(a, m):
    g, x, y = egcd(a, m)

    return x % m


t = int(input())

for t_itr in range(t):
    abx = input().split()

    a = int(abx[0])

    b = int(abx[1])

    x = int(abx[2])

    if b < 0:
        a, b = inverse(a, x), -b
    print(pow(a, b, x))