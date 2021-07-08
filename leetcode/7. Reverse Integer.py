def reverse(x: int) -> int:
    fir = 0
    neg = x < 0
    x = abs(x)
    while x:
        fir = fir * 10 + x % 10
        x = int(x / 10)
    if fir >= (2**31 - 1):
        return 0
    return -fir if neg else fir
