def encontrarCosa (x):
    lst_cosas=["juguete","aguja","mesa","silla","pizarra"]
    encontre=False
    for i in lst_cosas :
        if i==x:
            print("lo encontre :",x, "en la posicion : ",lst_cosas.index(x))
            encontre=True
            break
    if encontre==False:
        print("no lo encontre")

encontrarCosa("pelota")