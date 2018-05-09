def dec_bin ():
    dec1 = []
    bin1 = []
    try:
        d = int(input ('ingrese numero decimal: '))
        dec1.append(d)
    except:
        print('ingrese solo numeros entre 0 y 1')

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
      
    try:
        i = 8
        while i > 0:
            i = i - 1
            print('ingrese solo 8 bits')
            num = int(input('\ningrese numero binario: '))
            if num == 1 or num == 0:
                bina.append(num)
            else:
                print('\n solo ingrese numeros binarios (0 o 1)')

        j = 0
        for m in range(0, 8):
            if bina[m] == 1:
                d1 = bin2[j][0]
                dec.append(d1)
            else:
                d2 = 0               
                dec.append(d2)
            j = j + 1
    except:
        print('Ingrese solo numeros entre 0 y 1, no ingrese letras ni carateres espceciales, vuelva a intentarlo')
        #finally: 
        #bin_dec() nunca poner una una misma funcion dentro de su propia funcion (recursion), despues se vuelve infinito
        # esto mas bien sirve para llamar otra funcion difrente una vez el codigo ejecutado no tenga problemas  
    s = sum(dec)
    print(s)

dec_bin()
bin_dec()
