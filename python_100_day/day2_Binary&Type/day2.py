for i in range(100, 999, 1):
    hund = i // 100
    tens = (i-hund*100) // 10
    unit = (i-hund*100-tens*10)
    number = int(str(hund)+str(tens)+str(unit))
    if hund**3 + tens**3 + unit**3 ==  number:
        print('we find the Narcissistic number:', number) 