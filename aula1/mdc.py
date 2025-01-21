def mdc(x, y):
    if x == 0:
        return y
    elif y == 0:
        return x
    else:
        resto = x % y
        return mdc(y, resto)
    
print(mdc(12, 18))