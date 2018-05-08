def dec_bin ():
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

def bin_dec ():
    bin2 = [[128], [64],[32],[16],[8],[4],[2],[1]]
    bina = []
    dec = []

    i = 8
    while i > 0:
        i = i - 1
        num = int(input('ingrese numero binario'))
        if num == 1 or num == 0:
            bina.append(num)
        else:
            print('\n solo ingrese numeros binarios (0 o 1)')
    
    j = 0
    for m in range(0,8):
        
        if bina[m] == 1:
            d1 = bin2[j][0]
            dec.append(d1)
        else: 
            d2 = 0
            dec.append(d2)
        j = j +1
    s = sum(dec)
    print(dec,s)

    #sum_dec = d1 + d2 + d3 +d4 +d5 +d6 + d7 + d8
    #print(sum_dec)


#dec_bin()
bin_dec()
