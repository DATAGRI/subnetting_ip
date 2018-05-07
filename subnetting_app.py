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

def bin_digi ():
    bin2 = [[128], [64],[32],[16],[8],[4],[2],[1]]
    bina = []

    i = 8
    while i > 0:
        i = i - 1
        num = int(input('ingrese numero binario'))
        if num == 1 or num == 0:
            bina.append(num)
    
    if bina[0] == 1:
        d1 = bin2[0][0]
    else: 
        d1 = 0

    if bina[1] == 1:
        d2 = bin2[1][0]
    else:
        d2 = 0
    
    if bina[2] == 1:
        d3 = bin2[2][0]
    else: 
        d3 = 0

    if bina[3] == 1:
        d4 = bin2[3][0]
    else:
        d4 = 0

    if bina[4] == 1:
        d5 = bin2[4][0]
    else: 
        d5 = 0

    if bina[5] == 1:
        d6 = bin2[5][0]
    else:
        d6 = 0
    if bina[6] == 1:
        d7 = bin2[6][0]
    else: 
        d7 = 0

    if bina[7] == 1:
        d8 = bin2[7][0]
    else:
        d8 = 0

    sum_dec = d1 + d2 + d3 +d4 +d5 +d6 + d7 + d8
    print(sum_dec)


#dig_bin()
bin_digi()
