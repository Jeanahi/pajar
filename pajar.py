def encontrarCosa(x):
    lst_cosas=["juguete","aguja","mesa","silla","pizarra"]
    i=0
    j=len(lst_cosas)
    encontre=False
    while i<j :
        if lst_cosas[i]==x :
            print ("Encontre :",x, "en la posicion :",i ) #se puede poner tamb lst_cosas [i]porque es igual que X
            encontre=True
            break
        i=i+1
    if encontre==False :
        print("no lo encontre")
       
encontrarCosa("silla")