def dig_bin ():
    dec1 = []
    bin1 = []
    d = int(input ('ingrese numero decimal: '))
    dec1.append(d)
    
    i = 9
    while i > 1:
        i = i - 1 
        b = int (dec1[0] % 2)
        bin1.append(b)
        div = dec1[0] / 2
        dec1[0] = div
        
    bin1.reverse()
    print(bin1)

def bina_digi ():
    pass


dig_bin()
#bin_dig()
