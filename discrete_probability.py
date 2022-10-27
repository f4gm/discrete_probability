e=2.7182818284590452353602874713526624977572470936999595749669676277240766303535475945713821785251664274
def vacio(valor):
    while True:
        if valor=="":
            print("\n====================================================================================================\n")
            print("{:^100}".format("ERROR"))
            print("{:^100}".format("NO PUEDE INGRESAR UN VALOR VACÍO\n"))
            print("====================================================================================================\n")
            valor=input("INGRESE UN VALOR CORRECTO:\n--> ")
        else:
            break
    return valor
def valida_numero(numero):
    while True:
        validanumero=True
        for i in numero.upper():
            if i==" " or i=="{" or i=="}" or i=="[" or i=="]" or i=="(" or i==")" or i=="*" or i=="+" or i=="/" or i=="=" or i=="#" or i=="'" or i=="°" or i=="¬" or i=="<" or i==">" or i=="!" or i=="¡" or i=="¿" or i=="?" or i=="A" or i=="B" or i=="C" or i=="D" or i=="E" or i=="F" or i=="G" or i=="H" or i=="I" or i=="J" or i=="K" or i=="L" or i=="M" or i=="N" or i=="Ñ" or i=="O" or i=="P" or i=="Q"or i=="R" or i=="S" or i=="T" or i=="U" or i=="V" or i=="X" or i=="Y" or i=="Z" or i==":" or i==";" or i=="," or i=="-" or i=="_":
                validanumero=False
        if validanumero and float(numero)>0:
            break
        else:
            print("\n====================================================================================================\n")
            print("{:^100}".format("ERROR"))
            print("{:^100}".format("SOLO PUEDE INGRESAR NÚMEROS POSITIVOS"))
            print("\n====================================================================================================\n")
        numero=vacio(input("INGRESE UN VALOR:\n--> "))
    return numero
def valida_entero(numero):
    while True:
        validanumero=True
        for i in numero.upper():
            if i=="." or i==" " or i=="{" or i=="}" or i=="[" or i=="]" or i=="(" or i==")" or i=="*" or i=="+" or i=="/" or i=="=" or i=="#" or i=="'" or i=="°" or i=="¬" or i=="<" or i==">" or i=="!" or i=="¡" or i=="¿" or i=="?" or i=="A" or i=="B" or i=="C" or i=="D" or i=="E" or i=="F" or i=="G" or i=="H" or i=="I" or i=="J" or i=="K" or i=="L" or i=="M" or i=="N" or i=="Ñ" or i=="O" or i=="P" or i=="Q"or i=="R" or i=="S" or i=="T" or i=="U" or i=="V" or i=="X" or i=="Y" or i=="Z" or i==":" or i==";" or i=="," or i=="-" or i=="_":
                validanumero=False
        if validanumero and int(numero)>=0:
            break
        else:
            print("\n====================================================================================================\n")
            print("{:^100}".format("ERROR"))
            print("{:^100}".format("SOLO PUEDE INGRESAR NÚMEROS ENTEROS POSITIVOS"))
            print("\n====================================================================================================\n")
        numero=vacio(input("INGRESE UN VALOR:\n--> "))
    return numero
def factorial(numero):
    f=1
    for i in range(0,numero):
        f=f*(i+1)
    return f
def combinatoria(n,r):
    combinatoria=(factorial(n))/(factorial(n-r)*factorial(r))
    return combinatoria
def valida_probabilidad(probabilidad):
    while True:
        if probabilidad>1 or probabilidad<0:
            print("\n====================================================================================================\n")
            print("{:^100}".format("ERROR"))
            print("{:^100}".format("NO EXISTEN PROBABILIDADES MAYORES A \"1\" NI NEGATIVAS\n"))
            print("====================================================================================================\n")
            probabilidad=float(valida_numero(vacio(input("INGRESE UN VALOR CORRECTO:\n--> "))))
        else:
            break
    return probabilidad
def binomial_individual(x,n,p):
    b=combinatoria(n,x)*(p**x)*((1-p)**(n-x))
    return b
def binomial(x,n,p):
    s=0
    for i in range(0,x+1):
        s=s+combinatoria(n,i)*(p**i)*((1-p)**(n-i))
    return s
def binomial_entre(minimo,maximo,n,p):
    binomial_entre=0
    for i in range(minimo,maximo+1):
        binomial_entre=binomial_entre+(combinatoria(n,i)*(p**i)*((1-p)**(n-i)))
    return binomial_entre
def valida_n_binomial(x,n):
    while True:
        if x>n:
            print("\n====================================================================================================\n")
            print("{:^100}".format("ERROR"))
            print("{:^100}".format("EL VALOR DE \"x\" O EL RANGO NO PUEDE SER MAYOR AL NÚMERO DE INTENTOS \"n\"\n"))
            print("====================================================================================================\n")
            x=int(valida_entero(vacio(input("INGRESE UN VALOR CORRECTO:\n--> "))))
        else:
            break
    return x
def hiper_individual(N,n,k,x):
    h=(combinatoria(k,x)*combinatoria(N-k,n-x))/combinatoria(N,n)
    return h
def hiper(N,n,k,x):
    h=0
    for i in range(0,x+1):
        h=h+(combinatoria(k,i)*combinatoria(N-k,n-i))/combinatoria(N,n)
    return h
def hiper_entre(N,n,k,maximo,minimo):
    h=0
    for i in range(minimo,maximo+1):
        h=h+(combinatoria(k,i)*combinatoria(N-k,n-i))/combinatoria(N,n)
    return h
def valida_n_hiper(N,n):
    while True:
        if N<n:
            print("\n====================================================================================================\n")
            print("{:^100}".format("ERROR"))
            print("{:^100}".format("EL VALOR DE \"n\" O LA MUESTRA NO PUEDE SER MAYOR A LA POBLACIÓN \"N\"\n"))
            print("====================================================================================================\n")
            n=int(valida_entero(vacio(input("INGRESE UN VALOR CORRECTO:\n--> "))))
        else:
            break
    return n
def valida_N_hiper(N):
    valida=1
    while valida:
        if N<=0:
            print("\n====================================================================================================\n")
            print("{:^100}".format("ERROR"))
            print("{:^100}".format("EL VALOR DE LA POBLACIÓN \"N\" DEBE SER MAYOR A \"0\"\n"))
            print("====================================================================================================\n")
            N=int(valida_entero(vacio(input("Ingrese el tamaño \"N\" de la población: "))))
        else:
            break
    return N
def valida_k_hiper(N,k):
    while N:
        if N<k:
            print("\n====================================================================================================\n")
            print("{:^100}".format("ERROR"))
            print("{:^100}".format("EL VALOR DE \"k\" NO PUEDE SER MAYOR A LA POBLACIÓN \"N\"\n"))
            print("====================================================================================================\n")
            k=int(valida_entero(vacio(input("INGRESE UN VALOR CORRECTO:\n--> "))))
        else:
            break
    return k
def valida_x_hiper(N,n,k,x):
    while N:
        if n>k and x>k:
            print("\n====================================================================================================\n")
            print("{:^100}".format("ERROR"))
            print("{:^100}".format("EL VALOR DE \"x\" NO PUEDE SER MAYOR A \"k\" SI ESTA ES MENOR A \"n\"\n"))
            print("====================================================================================================\n")
            x=int(valida_entero(vacio(input("INGRESE UN VALOR CORRECTO:\n--> "))))
        elif k>n and x>n:
            print("\n====================================================================================================\n")
            print("{:^100}".format("ERROR"))
            print("{:^100}".format("EL VALOR DE \"x\" NO PUEDE SER MAYOR A \"n\" SI ESTA ES MENOR A \"k\"\n"))
            print("====================================================================================================\n")
            x=int(valida_entero(vacio(input("INGRESE UN VALOR CORRECTO:\n--> "))))
        elif x>N:
            print("\n====================================================================================================\n")
            print("{:^100}".format("ERROR"))
            print("{:^100}".format("EL VALOR DE \"x\" NO PUEDE SER MAYOR A MAYOR A LA POBLACIÓN \"N\"\n"))
            print("====================================================================================================\n")
            x=int(valida_entero(vacio(input("INGRESE UN VALOR CORRECTO:\n--> "))))
        else:
            break
    return x
def poisson_individual(x,l):
    p=((e**(-l))*(l**x))/factorial(x)
    return p
def poisson(x,l):
    p=0
    for i in range(0,x+1):
        p=p+((e**(-l))*(l**i))/factorial(i)
    return p
def poisson_entre(maximo,minimo,l):
    p=0
    for i in range(minimo,maximo+1):
	    p=p+((e**(-l))*(l**i))/factorial(i)
    return p
def valida_lambda(l):
    while l:
        if l>0:
            break
        else:
            print("\n====================================================================================================\n")
            print("{:^100}".format("ERROR"))
            print("{:^100}".format("EL VALOR DE \"λ\" (LAMBDA) DEBE SER POSITIVO Y DIFERENTE DE \"0\"\n"))
            print("====================================================================================================\n")
            l=int(valida_numero(vacio(input("INGRESE UN VALOR CORRECTO:\n--> "))))
    return l
def valida_rango(maximo,minimo):
    while maximo:
        if minimo<=maximo:
            break
        else:
            print("\n====================================================================================================\n")
            print("{:^100}".format("ERROR"))
            print("{:^100}".format("EL LÍMITE SUPERIOR NO PUEDE SER MENOR QUE EL LÍMITE INFERIOR\n"))
            print("====================================================================================================\n")
            minimo=int(valida_entero(vacio(input("Ingrese el límite inferior del intervalo: "))))
    return minimo
print("\n====================================================================================================\n")
print("{:^100}".format("CALCULADORA DE DISTRIBUCIONES DE PROBABILIDAD EN VARIABLE DISCRETA\n"))
print("====================================================================================================\n")
print("{:^100}".format("BIENVENIDO\n"))
print("{:^100}".format("POR FAVOR ELIJA UNA DISTRIBUCIÓN\n"))
print("INGRESE 1 ---> DISTRIBUCIÓN BINOMIAL\nINGRESE 2 ---> DISTRIBUCIÓN HIPERGEOMÉTRICA\nINGRESE 3 ---> DISTRIBUCIÓN POISSON\nINGRESE 4 ---> PARA CERRAR EL PROGRAMA\n")
seleccion=vacio(input("---> "))
while seleccion:
    if seleccion=="1":
        print("\n====================================================================================================\n")
        print("{:^100}".format("DISTRIBUCIÓN BINOMIAL\n"))
        print("====================================================================================================\n")
        print("{:^100}".format("POR FAVOR ELIJA LA OPERACIÓN QUE DESEA CALCULAR\n"))
        print("INGRESE 1 ---> BINOMIAL PUNTUAL P(X=a)\nINGRESE 2 ---> BINOMIAL ACUMULADA P(X<=a)\nINGRESE 3 ---> BINOMIAL ENTRE DOS VALORES P(a<=x<=b)\nINGRESE 4 ---> VALOR ESPERADO Y VARIANZA\nINGRESE 5 ---> PARA CALCULAR UNA DISTRIBUCION DIFERENTE\n")
        acceso=vacio(input("--> "))
        print("")
        while acceso:
            if acceso=="1":
                n=int(valida_entero(vacio(input("Ingrese el número de ensayos \"n\": "))))
                x=valida_n_binomial(int(valida_entero(vacio(input("Ingrese el valor de \"x\" al cual desea calcular la probabilidad: ")))),n)
                p=valida_probabilidad(float(valida_numero(vacio(input("Ingrese la probabilidad de éxito \"p\": ")))))
                print("\n====================================================================================================\n")
                print("{:^100}".format("¿LA INFORMACIÓN QUE HA INGRESADO ES CORRECTA?"))
                print("\n====================================================================================================\n")
                decision=vacio(input("INGRESE \"SI\" O \"NO\" PARA CONFIRMAR LA INFORMACIÓN: "))
                while decision:
                    if decision.upper()=="SI":
                        print("\n====================================================================================================\n")
                        print("{:^100}".format("||   RESULTADO   ||\n"))
                        print("{:^100}".format("La probabilidad de ocurrencia de "+str(x)+" éxitos entre los "+str(n)+" ensayos, con una"))
                        print("{:^100}".format("probabilidad de éxito de "+str(p)+" es: "+format(binomial_individual(x,n,p),'.10f')))
                        break
                    elif decision.upper()=="NO":
                        print("\n====================================================================================================\n")
                        print("{:^100}".format("VUELVA A INGRESAR LA INFORMACIÓN"))
                        print("\n====================================================================================================\n")
                        n=int(valida_entero(vacio(input("Ingrese el número de ensayos \"n\": "))))
                        x=valida_n_binomial(int(valida_entero(vacio(input("Ingrese el valor de \"x\" al cual desea calcular la probabilidad: ")))),n)
                        p=valida_probabilidad(float(valida_numero(vacio(input("Ingrese la probabilidad de éxito \"p\": ")))))
                        print("\n====================================================================================================\n")
                        print("{:^100}".format("¿LA INFORMACIÓN QUE HA INGRESADO ES CORRECTA?"))
                        print("\n====================================================================================================\n")
                        decision=vacio(input("INGRESE \"SI\" O \"NO\" PARA CONFIRMAR LA INFORMACIÓN: "))
                    else:
                        print("\n====================================================================================================\n")
                        print("{:^100}".format("ERROR"))
                        print("{:^100}".format("INGRESE UNA PALABRA VÁLIDA\n"))
                        print("====================================================================================================\n")
                        decision=vacio(input("INGRESE \"SI\" O \"NO\" PARA CONFIRMAR LA INFORMACIÓN: "))
                print("\n====================================================================================================\n")
                print("{:^100}".format("NUEVO CÁLCULO\n"))
                print("====================================================================================================\n")
                print("{:^100}".format("POR FAVOR ELIJA LA OPERACIÓN QUE DESEA CALCULAR\n"))
                print("INGRESE 1 ---> BINOMIAL PUNTUAL P(X=a)\nINGRESE 2 ---> BINOMIAL ACUMULADA P(X<=a)\nINGRESE 3 ---> BINOMIAL ENTRE DOS VALORES P(a<=x<=b)\nINGRESE 4 ---> VALOR ESPERADO Y VARIANZA\nINGRESE 5 ---> PARA CALCULAR UNA DISTRIBUCION DIFERENTE\n")
                acceso=vacio(input("--> "))
                print("")
            elif acceso=="2":
                n=int(valida_entero(vacio(input("Ingrese el número de ensayos \"n\": "))))
                x=valida_n_binomial(int(valida_entero(vacio(input("Ingrese el valor de \"x\" hasta el cual desea calcular la probabilidad: ")))),n)
                p=valida_probabilidad(float(valida_numero(vacio(input("Ingrese la probabilidad de éxito \"p\": ")))))
                print("\n====================================================================================================\n")
                print("{:^100}".format("¿LA INFORMACIÓN QUE HA INGRESADO ES CORRECTA?"))
                print("\n====================================================================================================\n")
                decision=vacio(input("INGRESE \"SI\" O \"NO\" PARA CONFIRMAR LA INFORMACIÓN: "))
                while decision:
                    if decision.upper()=="SI":
                        print("\n====================================================================================================\n")
                        print("{:^100}".format("||   RESULTADO   ||\n"))
                        print("{:^100}".format("La probabilidad de ocurrencia de máximo "+str(x)+" éxitos entre los "+str(n)+" ensayos con una"))
                        print("{:^100}".format("probabilidad de éxito de "+str(p)+" es: "+format(binomial(x,n,p),'.10f')))
                        break
                    elif decision.upper()=="NO":
                        print("\n====================================================================================================\n")
                        print("{:^100}".format("VUELVA A INGRESAR LA INFORMACIÓN"))
                        print("\n====================================================================================================\n")
                        n=int(valida_entero(vacio(input("Ingrese el número de ensayos \"n\": "))))
                        x=valida_n_binomial(int(valida_entero(vacio(input("Ingrese el valor de \"x\" hasta el cual desea calcular la probabilidad: ")))),n)
                        p=valida_probabilidad(float(valida_numero(vacio(input("Ingrese la probabilidad de éxito \"p\": ")))))
                        print("\n====================================================================================================\n")
                        print("{:^100}".format("¿LA INFORMACIÓN QUE HA INGRESADO ES CORRECTA?"))
                        print("\n====================================================================================================\n")
                        decision=vacio(input("INGRESE \"SI\" O \"NO\" PARA CONFIRMAR LA INFORMACIÓN: "))
                    else:
                        print("\n====================================================================================================\n")
                        print("{:^100}".format("ERROR"))
                        print("{:^100}".format("INGRESE UNA PALABRA VÁLIDA\n"))
                        print("====================================================================================================\n")
                        decision=vacio(input("INGRESE \"SI\" O \"NO\" PARA CONFIRMAR LA INFORMACIÓN: "))
                print("\n====================================================================================================\n")
                print("{:^100}".format("NUEVO CÁLCULO\n"))
                print("====================================================================================================\n")
                print("{:^100}".format("POR FAVOR ELIJA LA OPERACIÓN QUE DESEA CALCULAR\n"))
                print("INGRESE 1 ---> BINOMIAL PUNTUAL P(X=a)\nINGRESE 2 ---> BINOMIAL ACUMULADA P(X<=a)\nINGRESE 3 ---> BINOMIAL ENTRE DOS VALORES P(a<=x<=b)\nINGRESE 4 ---> VALOR ESPERADO Y VARIANZA\nINGRESE 5 ---> PARA CALCULAR UNA DISTRIBUCION DIFERENTE\n")
                acceso=vacio(input("--> "))
                print("")
            elif acceso=="3":
                n=int(valida_entero(vacio(input("Ingrese el número de ensayos \"n\": "))))
                maximo=valida_n_binomial(int(valida_entero(vacio(input("Ingrese el límite superior del intervalo: ")))),n)
                minimo=valida_rango(maximo,valida_n_binomial(int(valida_entero(vacio(input("Ingrese el límite inferior del intervalo: ")))),n))
                p=valida_probabilidad(float(valida_numero(vacio(input("Ingrese la probabilidad de éxito \"p\": ")))))
                print("\n====================================================================================================\n")
                print("{:^100}".format("¿LA INFORMACIÓN QUE HA INGRESADO ES CORRECTA?"))
                print("\n====================================================================================================\n")
                decision=vacio(input("INGRESE \"SI\" O \"NO\" PARA CONFIRMAR LA INFORMACIÓN: "))
                while decision:
                    if decision.upper()=="SI":
                        print("\n====================================================================================================\n")
                        print("{:^100}".format("||   RESULTADO   ||\n"))
                        print("{:^100}".format("La probabilidad de ocurrencia entre "+str(minimo)+" y "+str(maximo)+" éxitos entre "+str(n)+" ensayos con una"))
                        print("{:^100}".format("probabilidad de éxito de "+str(p)+" es: "+format(binomial_entre(minimo,maximo,n,p),'.10f')))
                        break
                    elif decision.upper()=="NO":
                        print("\n====================================================================================================\n")
                        print("{:^100}".format("VUELVA A INGRESAR LA INFORMACIÓN"))
                        print("\n====================================================================================================\n")
                        n=int(valida_entero(vacio(input("Ingrese el número de ensayos \"n\": "))))
                        maximo=valida_n_binomial(int(valida_entero(vacio(input("Ingrese el límite superior del intervalo: ")))),n)
                        minimo=valida_rango(maximo,valida_n_binomial(int(valida_entero(vacio(input("Ingrese el límite inferior del intervalo: ")))),n))
                        p=valida_probabilidad(float(valida_numero(vacio(input("Ingrese la probabilidad de éxito \"p\": ")))))
                        print("\n====================================================================================================\n")
                        print("{:^100}".format("¿LA INFORMACIÓN QUE HA INGRESADO ES CORRECTA?"))
                        print("\n====================================================================================================\n")
                        decision=vacio(input("INGRESE \"SI\" O \"NO\" PARA CONFIRMAR LA INFORMACIÓN: "))
                    else:
                        print("\n====================================================================================================\n")
                        print("{:^100}".format("ERROR"))
                        print("{:^100}".format("INGRESE UNA PALABRA VÁLIDA\n"))
                        print("====================================================================================================\n")
                        decision=vacio(input("INGRESE \"SI\" O \"NO\" PARA CONFIRMAR LA INFORMACIÓN: "))
                print("\n====================================================================================================\n")
                print("{:^100}".format("NUEVO CÁLCULO\n"))
                print("====================================================================================================\n")
                print("{:^100}".format("POR FAVOR ELIJA LA OPERACIÓN QUE DESEA CALCULAR\n"))
                print("INGRESE 1 ---> BINOMIAL PUNTUAL P(X=a)\nINGRESE 2 ---> BINOMIAL ACUMULADA P(X<=a)\nINGRESE 3 ---> BINOMIAL ENTRE DOS VALORES P(a<=x<=b)\nINGRESE 4 ---> VALOR ESPERADO Y VARIANZA\nINGRESE 5 ---> PARA CALCULAR UNA DISTRIBUCION DIFERENTE\n")
                acceso=vacio(input("--> "))
                print("")
            elif acceso=="4":
                n=int(valida_entero(vacio(input("Ingrese el número de ensayos \"n\": "))))
                p=valida_probabilidad(float(valida_numero(vacio(input("Ingrese la probabilidad de éxito \"p\": ")))))
                print("\n====================================================================================================\n")
                print("{:^100}".format("¿LA INFORMACIÓN QUE HA INGRESADO ES CORRECTA?"))
                print("\n====================================================================================================\n")
                decision=vacio(input("INGRESE \"SI\" O \"NO\" PARA CONFIRMAR LA INFORMACIÓN: "))
                while decision:
                    if decision.upper()=="SI":
                        valor_esperado_binom=n*p
                        varianza_binom=n*p*(1-p)
                        print("\n====================================================================================================\n")
                        print("{:^100}".format("||   RESULTADO   ||\n"))
                        print("{:^100}".format("E(X)="+str(valor_esperado_binom)))
                        print("{:^100}".format("V(X)="+str(varianza_binom)))
                        break
                    elif decision.upper()=="NO":
                        print("\n====================================================================================================\n")
                        print("{:^100}".format("VUELVA A INGRESAR LA INFORMACIÓN"))
                        print("\n====================================================================================================\n")
                        n=int(valida_entero(vacio(input("Ingrese el número de ensayos \"n\": "))))
                        p=valida_probabilidad(float(valida_numero(vacio(input("Ingrese la probabilidad de éxito \"p\": ")))))
                        print("\n====================================================================================================\n")
                        print("{:^100}".format("¿LA INFORMACIÓN QUE HA INGRESADO ES CORRECTA?"))
                        print("\n====================================================================================================\n")
                        decision=vacio(input("INGRESE \"SI\" O \"NO\" PARA CONFIRMAR LA INFORMACIÓN: "))
                    else:
                        print("\n====================================================================================================\n")
                        print("{:^100}".format("ERROR"))
                        print("{:^100}".format("INGRESE UNA PALABRA VÁLIDA\n"))
                        print("====================================================================================================\n")
                        decision=vacio(input("INGRESE \"SI\" O \"NO\" PARA CONFIRMAR LA INFORMACIÓN: "))
                print("\n====================================================================================================\n")
                print("{:^100}".format("NUEVO CÁLCULO\n"))
                print("====================================================================================================\n")
                print("{:^100}".format("POR FAVOR ELIJA LA OPERACIÓN QUE DESEA CALCULAR\n"))
                print("INGRESE 1 ---> BINOMIAL PUNTUAL P(X=a)\nINGRESE 2 ---> BINOMIAL ACUMULADA P(X<=a)\nINGRESE 3 ---> BINOMIAL ENTRE DOS VALORES P(a<=x<=b)\nINGRESE 4 ---> VALOR ESPERADO Y VARIANZA\nINGRESE 5 ---> PARA CALCULAR UNA DISTRIBUCION DIFERENTE\n")
                acceso=vacio(input("--> "))
                print("")
            elif acceso=="5":
                print("====================================================================================================\n")
                print("{:^100}".format("TAREA FINALIZADA\n"))
                print("====================================================================================================\n")
                break
            else:
                print("====================================================================================================\n")
                print("{:^100}".format("ERROR, POR FAVOR INGRESE LOS NÚMEROS CONTEMPLADOS EN LA LISTA\n"))
                print("====================================================================================================\n")
                print("INGRESE 1 ---> BINOMIAL PUNTUAL P(X=a)\nINGRESE 2 ---> BINOMIAL ACUMULADA P(X<=a)\nINGRESE 3 ---> BINOMIAL ENTRE DOS VALORES P(a<=x<=b)\nINGRESE 4 ---> VALOR ESPERADO Y VARIANZA\nINGRESE 5 ---> PARA CALCULAR UNA DISTRIBUCION DIFERENTE\n")
                acceso=vacio(input("--> "))
                print("")
        print("{:^100}".format("POR FAVOR ELIJA UNA DISTRIBUCIÓN\n"))
        print("INGRESE 1 ---> DISTRIBUCIÓN BINOMIAL\nINGRESE 2 ---> DISTRIBUCIÓN HIPERGEOMÉTRICA\nINGRESE 3 ---> DISTRIBUCIÓN POISSON\nINGRESE 4 ---> PARA CERRAR EL PROGRAMA\n")
        seleccion=vacio(input("--> "))
    elif seleccion=="2":
        print("\n====================================================================================================\n")
        print("{:^100}".format("DISTRIBUCIÓN HIPERGEOMÉTRICA\n"))
        print("====================================================================================================\n")
        print("{:^100}".format("POR FAVOR ELIJA LA OPERACIÓN QUE DESEA CALCULAR\n"))
        print("INGRESE 1 ---> HIPERGEOMÉTRICA PUNTUAL P(X=a)\nINGRESE 2 ---> HIPERGEOMÉTRICA ACUMULADA P(X<=a)\nINGRESE 3 ---> HIPERGEOMÉTRICA ENTRE DOS VALORES P(a<=x<=b)\nINGRESE 4 ---> VALOR ESPERADO Y VARIANZA\nINGRESE 5 ---> PARA CALCULAR UNA DISTRIBUCIÓN DIFERENTE\n")
        acceso=vacio(input("--> "))
        print("")
        while acceso:
            if acceso=="1":
                N=valida_N_hiper(int(valida_entero(vacio(input("Ingrese el tamaño \"N\" de la población: ")))))
                n=valida_n_hiper(N,int(valida_entero(vacio(input("Ingrese el tamaño \"n\" de la muestra: ")))))
                k=valida_k_hiper(N,int(valida_entero(vacio(input("Ingrese el número de elementos del tipo \"k\": ")))))
                x=valida_x_hiper(N,n,k,int(valida_entero(vacio(input("Ingrese el valor de \"x\" que quiere calcular: ")))))
                print("\n====================================================================================================\n")
                print("{:^100}".format("¿LA INFORMACIÓN QUE HA INGRESADO ES CORRECTA?"))
                print("\n====================================================================================================\n")
                decision=vacio(input("INGRESE \"SI\" O \"NO\" PARA CONFIRMAR LA INFORMACIÓN: "))
                while decision:
                    if decision.upper()=="SI" and (N-k)>=(n-x):
                        print("\n====================================================================================================\n")
                        print("{:^100}".format("||   RESULTADO   ||\n"))
                        print("{:^100}".format("Si en una población de tamaño "+str(N)+" se tienen "+str(k)+" con una caracterítica en particular y se"))
                        print("{:^100}".format("extraen al azar "+str(n)+" elementos de la población. La probabilidad de obtener exactamente "+str(x)))
                        print("{:^100}".format("con la característica particular es: "+format(hiper_individual(N,n,k,x),'.10f')))
                        break
                    elif decision.upper()=="NO" and ((N-k)>=(n-x) or (N-k)<(n-x)):
                        print("\n====================================================================================================\n")
                        print("{:^100}".format("VUELVA A INGRESAR LA INFORMACIÓN"))
                        print("\n====================================================================================================\n")
                        N=valida_N_hiper(int(valida_entero(vacio(input("Ingrese el tamaño \"N\" de la población: ")))))
                        n=valida_n_hiper(N,int(valida_entero(vacio(input("Ingrese el tamaño \"n\" de la muestra: ")))))
                        k=valida_k_hiper(N,int(valida_entero(vacio(input("Ingrese el número de elementos del tipo \"k\": ")))))
                        x=valida_x_hiper(N,n,k,int(valida_entero(vacio(input("Ingrese el valor de \"x\" que quiere calcular: ")))))
                        print("\n====================================================================================================\n")
                        print("{:^100}".format("¿LA INFORMACIÓN QUE HA INGRESADO ES CORRECTA?"))
                        print("\n====================================================================================================\n")
                        decision=vacio(input("INGRESE \"SI\" O \"NO\" PARA CONFIRMAR LA INFORMACIÓN: "))
                    elif decision.upper()=="SI" and (N-k)<(n-x):
                        print("\n====================================================================================================\n")
                        print("{:^100}".format("ERROR"))
                        print("{:^100}".format("RECUERDE QUE N-k DEBE SER MAYOR QUE n-x. VUELVA A INGRESAR LA INFORMACIÓN"))
                        print("\n====================================================================================================\n")
                        N=valida_N_hiper(int(valida_entero(vacio(input("Ingrese el tamaño \"N\" de la población: ")))))
                        n=valida_n_hiper(N,int(valida_entero(vacio(input("Ingrese el tamaño \"n\" de la muestra: ")))))
                        k=valida_k_hiper(N,int(valida_entero(vacio(input("Ingrese el número de elementos del tipo \"k\": ")))))
                        x=valida_x_hiper(N,n,k,int(valida_entero(vacio(input("Ingrese el valor de \"x\" que quiere calcular: ")))))
                        print("\n====================================================================================================\n")
                        print("{:^100}".format("¿LA INFORMACIÓN QUE HA INGRESADO ES CORRECTA?"))
                        print("\n====================================================================================================\n")
                        decision=vacio(input("INGRESE \"SI\" O \"NO\" PARA CONFIRMAR LA INFORMACIÓN: "))
                    else:
                        print("\n====================================================================================================\n")
                        print("{:^100}".format("ERROR"))
                        print("{:^100}".format("INGRESE UNA PALABRA VÁLIDA\n"))
                        print("====================================================================================================\n")
                        decision=vacio(input("INGRESE \"SI\" O \"NO\" PARA CONFIRMAR LA INFORMACIÓN: "))
                print("\n====================================================================================================\n")
                print("{:^100}".format("NUEVO CÁLCULO\n"))
                print("====================================================================================================\n")
                print("{:^100}".format("POR FAVOR ELIJA LA OPERACIÓN QUE DESEA CALCULAR\n"))
                print("INGRESE 1 ---> HIPERGEOMÉTRICA PUNTUAL P(X=a)\nINGRESE 2 ---> HIPERGEOMÉTRICA ACUMULADA P(X<=a)\nINGRESE 3 ---> HIPERGEOMÉTRICA ENTRE DOS VALORES P(a<=x<=b)\nINGRESE 4 ---> VALOR ESPERADO Y VARIANZA\nINGRESE 5 ---> PARA CALCULAR UNA DISTRIBUCIÓN DIFERENTE\n")
                acceso=vacio(input("--> "))
                print("")
            elif acceso=="2":
                N=valida_N_hiper(int(valida_entero(vacio(input("Ingrese el tamaño \"N\" de la población: ")))))
                n=valida_n_hiper(N,int(valida_entero(vacio(input("Ingrese el tamaño \"n\" de la muestra: ")))))
                k=valida_k_hiper(N,int(valida_entero(vacio(input("Ingrese el número de elementos del tipo \"k\": ")))))
                x=valida_x_hiper(N,n,k,int(valida_entero(vacio(input("Ingrese el valor de \"x\" hasta el cual quiere calcular: ")))))
                rango_valido=True
                for i in range(0,x+1):
                    if (N-k)<(n-i):
                        rango_valido=False
                print("\n====================================================================================================\n")
                print("{:^100}".format("¿LA INFORMACIÓN QUE HA INGRESADO ES CORRECTA?"))
                print("\n====================================================================================================\n")
                decision=vacio(input("INGRESE \"SI\" O \"NO\" PARA CONFIRMAR LA INFORMACIÓN: "))
                while decision:
                    if decision.upper()=="SI" and rango_valido==True:
                        print("\n====================================================================================================\n")
                        print("{:^100}".format("||   RESULTADO   ||\n"))
                        print("{:^100}".format("Si en una población de tamaño "+str(N)+" se tienen "+str(k)+" elementos con una característica en particular"))
                        print("{:^100}".format("y se extraen como máximo "+str(x)+" elementos con una caraterística en particular es: "+format(hiper(N,n,k,x),'.10f')))
                        break
                    elif decision.upper()=="NO" and (rango_valido==True or rango_valido==False):
                        rango_valido=True
                        print("\n====================================================================================================\n")
                        print("{:^100}".format("VUELVA A INGRESAR LA INFORMACIÓN"))
                        print("\n====================================================================================================\n")
                        N=valida_N_hiper(int(valida_entero(vacio(input("Ingrese el tamaño \"N\" de la población: ")))))
                        n=valida_n_hiper(N,int(valida_entero(vacio(input("Ingrese el tamaño \"n\" de la muestra: ")))))
                        k=valida_k_hiper(N,int(valida_entero(vacio(input("Ingrese el número de elementos del tipo \"k\": ")))))
                        x=valida_x_hiper(N,n,k,int(valida_entero(vacio(input("Ingrese el valor de \"x\" hasta el cual quiere calcular: ")))))
                        for i in range(0,x+1):
                            if (N-k)<(n-i):
                                rango_valido=False
                        print("\n====================================================================================================\n")
                        print("{:^100}".format("¿LA INFORMACIÓN QUE HA INGRESADO ES CORRECTA?"))
                        print("\n====================================================================================================\n")
                        decision=vacio(input("INGRESE \"SI\" O \"NO\" PARA CONFIRMAR LA INFORMACIÓN: "))
                    elif decision.upper()=="SI" and rango_valido==False:
                        rango_valido=True
                        print("\n====================================================================================================\n")
                        print("{:^100}".format("ERROR"))
                        print("{:^100}".format("RECUERDE QUE N-k DEBE SER MAYOR QUE n-x. VUELVA A INGRESAR LA INFORMACIÓN"))
                        print("\n====================================================================================================\n")
                        N=valida_N_hiper(int(valida_entero(vacio(input("Ingrese el tamaño \"N\" de la población: ")))))
                        n=valida_n_hiper(N,int(valida_entero(vacio(input("Ingrese el tamaño \"n\" de la muestra: ")))))
                        k=valida_k_hiper(N,int(valida_entero(vacio(input("Ingrese el número de elementos del tipo \"k\": ")))))
                        x=valida_x_hiper(N,n,k,int(valida_entero(vacio(input("Ingrese el valor de \"x\" hasta el cual quiere calcular: ")))))
                        for i in range(0,x+1):
                            if (N-k)<(n-i):
                                rango_valido=False
                        print("\n====================================================================================================\n")
                        print("{:^100}".format("¿LA INFORMACIÓN QUE HA INGRESADO ES CORRECTA?"))
                        print("\n====================================================================================================\n")
                        decision=vacio(input("INGRESE \"SI\" O \"NO\" PARA CONFIRMAR LA INFORMACIÓN: "))
                    else:
                        print("\n====================================================================================================\n")
                        print("{:^100}".format("ERROR"))
                        print("{:^100}".format("INGRESE UNA PALABRA VÁLIDA\n"))
                        print("====================================================================================================\n")
                        decision=vacio(input("INGRESE \"SI\" O \"NO\" PARA CONFIRMAR LA INFORMACIÓN: "))
                print("\n====================================================================================================\n")
                print("{:^100}".format("NUEVO CÁLCULO\n"))
                print("====================================================================================================\n")
                print("{:^100}".format("POR FAVOR ELIJA LA OPERACIÓN QUE DESEA CALCULAR\n"))
                print("INGRESE 1 ---> HIPERGEOMÉTRICA PUNTUAL P(X=a)\nINGRESE 2 ---> HIPERGEOMÉTRICA ACUMULADA P(X<=a)\nINGRESE 3 ---> HIPERGEOMÉTRICA ENTRE DOS VALORES P(a<=x<=b)\nINGRESE 4 ---> VALOR ESPERADO Y VARIANZA\nINGRESE 5 ---> PARA CALCULAR UNA DISTRIBUCIÓN DIFERENTE\n")
                acceso=vacio(input("--> "))
                print("")
            elif acceso=="3":
                N=valida_N_hiper(int(valida_entero(vacio(input("Ingrese el tamaño \"N\" de la población: ")))))
                n=valida_n_hiper(N,int(valida_entero(vacio(input("Ingrese el tamaño \"n\" de la muestra: ")))))
                k=valida_k_hiper(N,int(valida_entero(vacio(input("Ingrese el número de elementos del tipo \"k\": ")))))
                maximo=valida_x_hiper(N,n,k,int(valida_entero(vacio(input("Ingrese el límite superior del intervalo: ")))))
                minimo=valida_rango(maximo,valida_x_hiper(N,n,k,int(valida_entero(vacio(input("Ingrese el límite inferior del intervalo: "))))))
                rango_valido=True
                for i in range(minimo,maximo+1):
                    if (N-k)<(n-i):
                        rango_valido=False
                print("\n====================================================================================================\n")
                print("{:^100}".format("¿LA INFORMACIÓN QUE HA INGRESADO ES CORRECTA?"))
                print("\n====================================================================================================\n")
                decision=vacio(input("INGRESE \"SI\" O \"NO\" PARA CONFIRMAR LA INFORMACIÓN: "))
                while decision:
                    if decision.upper()=="SI" and rango_valido==True:
                        print("\n====================================================================================================\n")
                        print("{:^100}".format("||   RESULTADO   ||\n"))
                        print("{:^100}".format("La probabilidad de que entre "+str(minimo)+" y "+str(maximo)+" elementos pertenezcan al tipo k en una"))
                        print("{:^100}".format("población de "+str(N)+" y una muestra de "+str(n)+" es: "+format(hiper_entre(N,n,k,maximo,minimo),'.10f')))
                        break
                    elif decision.upper()=="NO" and (rango_valido==True or rango_valido==False):
                        print("\n====================================================================================================\n")
                        print("{:^100}".format("VUELVA A INGRESAR LA INFORMACIÓN"))
                        print("\n====================================================================================================\n")
                        N=valida_N_hiper(int(valida_entero(vacio(input("Ingrese el tamaño \"N\" de la población: ")))))
                        n=valida_n_hiper(N,int(valida_entero(vacio(input("Ingrese el tamaño \"n\" de la muestra: ")))))
                        k=valida_k_hiper(N,int(valida_entero(vacio(input("Ingrese el número de elementos del tipo \"k\": ")))))
                        maximo=valida_x_hiper(N,n,k,int(valida_entero(vacio(input("Ingrese el límite superior del intervalo: ")))))
                        minimo=valida_rango(maximo,valida_x_hiper(N,n,k,int(valida_entero(vacio(input("Ingrese el límite inferior del intervalo: "))))))
                        rango_valido=True
                        for i in range(minimo,maximo+1):
                            if (N-k)<(n-i):
                                rango_valido=False
                        print("\n====================================================================================================\n")
                        print("{:^100}".format("¿LA INFORMACIÓN QUE HA INGRESADO ES CORRECTA?"))
                        print("\n====================================================================================================\n")
                        decision=vacio(input("INGRESE \"SI\" O \"NO\" PARA CONFIRMAR LA INFORMACIÓN: "))
                    elif decision.upper()=="SI" and rango_valido==False:
                        rango_valido=True
                        print("\n====================================================================================================\n")
                        print("{:^100}".format("ERROR"))
                        print("{:^100}".format("RECUERDE QUE N-k DEBE SER MAYOR QUE n-x. VUELVA A INGRESAR LA INFORMACIÓN"))
                        print("\n====================================================================================================\n")
                        N=valida_N_hiper(int(valida_entero(vacio(input("Ingrese el tamaño \"N\" de la población: ")))))
                        n=valida_n_hiper(N,int(valida_entero(vacio(input("Ingrese el tamaño \"n\" de la muestra: ")))))
                        k=valida_k_hiper(N,int(valida_entero(vacio(input("Ingrese el número de elementos del tipo \"k\": ")))))
                        maximo=valida_x_hiper(N,n,k,int(valida_entero(vacio(input("Ingrese el límite superior del intervalo: ")))))
                        minimo=valida_rango(maximo,valida_x_hiper(N,n,k,int(valida_entero(vacio(input("Ingrese el límite inferior del intervalo: "))))))
                        for i in range(minimo,maximo+1):
                            if (N-k)<(n-i):
                                rango_valido=False
                        print("\n====================================================================================================\n")
                        print("{:^100}".format("¿LA INFORMACIÓN QUE HA INGRESADO ES CORRECTA?"))
                        print("\n====================================================================================================\n")
                        decision=vacio(input("INGRESE \"SI\" O \"NO\" PARA CONFIRMAR LA INFORMACIÓN: "))
                    else:
                        print("\n====================================================================================================\n")
                        print("{:^100}".format("ERROR"))
                        print("{:^100}".format("INGRESE UNA PALABRA VÁLIDA\n"))
                        print("====================================================================================================\n")
                        decision=vacio(input("INGRESE \"SI\" O \"NO\" PARA CONFIRMAR LA INFORMACIÓN: "))
                print("\n====================================================================================================\n")
                print("{:^100}".format("NUEVO CÁLCULO\n"))
                print("====================================================================================================\n")
                print("{:^100}".format("POR FAVOR ELIJA LA OPERACIÓN QUE DESEA CALCULAR\n"))
                print("INGRESE 1 ---> HIPERGEOMÉTRICA PUNTUAL P(X=a)\nINGRESE 2 ---> HIPERGEOMÉTRICA ACUMULADA P(X<=a)\nINGRESE 3 ---> HIPERGEOMÉTRICA ENTRE DOS VALORES P(a<=x<=b)\nINGRESE 4 ---> VALOR ESPERADO Y VARIANZA\nINGRESE 5 ---> PARA CALCULAR UNA DISTRIBUCIÓN DIFERENTE\n")
                acceso=vacio(input("--> "))
                print("")
            elif acceso=="4":
                N=valida_N_hiper(int(valida_entero(vacio(input("Ingrese el tamaño \"N\" de la población: ")))))
                n=valida_n_hiper(N,int(valida_entero(vacio(input("Ingrese el tamaño \"n\" de la muestra: ")))))
                k=valida_k_hiper(N,int(valida_entero(vacio(input("Ingrese el número de elementos del tipo \"k\": ")))))
                print("\n====================================================================================================\n")
                print("{:^100}".format("¿LA INFORMACIÓN QUE HA INGRESADO ES CORRECTA?"))
                print("\n====================================================================================================\n")
                decision=vacio(input("INGRESE \"SI\" O \"NO\" PARA CONFIRMAR LA INFORMACIÓN: "))
                while decision:
                    if decision.upper()=="SI":
                        valor_esperado_hiper=n*k/N
                        varianza_hiper=(n*k*(N-k)*(N-n))/((N**2)*(N-1))
                        print("\n====================================================================================================\n")
                        print("{:^100}".format("||   RESULTADO   ||\n"))
                        print("{:^100}".format("E(X)="+str(valor_esperado_hiper)))
                        print("{:^100}".format("V(X)="+str(varianza_hiper)+"\n"))
                        break
                    elif decision.upper()=="NO":
                        print("\n====================================================================================================\n")
                        print("{:^100}".format("VUELVA A INGRESAR LA INFORMACIÓN"))
                        print("\n====================================================================================================\n")
                        N=valida_N_hiper(int(valida_entero(vacio(input("Ingrese el tamaño \"N\" de la población: ")))))
                        n=valida_n_hiper(N,int(valida_entero(vacio(input("Ingrese el tamaño \"n\" de la muestra: ")))))
                        k=valida_k_hiper(N,int(valida_entero(vacio(input("Ingrese el número de elementos del tipo \"k\": ")))))
                        print("\n====================================================================================================\n")
                        print("{:^100}".format("¿LA INFORMACIÓN QUE HA INGRESADO ES CORRECTA?"))
                        print("\n====================================================================================================\n")
                        decision=vacio(input("INGRESE \"SI\" O \"NO\" PARA CONFIRMAR LA INFORMACIÓN: "))
                    else:
                        print("\n====================================================================================================\n")
                        print("{:^100}".format("ERROR"))
                        print("{:^100}".format("INGRESE UNA PALABRA VÁLIDA\n"))
                        print("====================================================================================================\n")
                        decision=vacio(input("INGRESE \"SI\" O \"NO\" PARA CONFIRMAR LA INFORMACIÓN: "))
                print("\n====================================================================================================\n")
                print("{:^100}".format("NUEVO CÁLCULO\n"))
                print("====================================================================================================\n")
                print("{:^100}".format("POR FAVOR ELIJA LA OPERACIÓN QUE DESEA CALCULAR\n"))
                print("INGRESE 1 ---> HIPERGEOMÉTRICA PUNTUAL P(X=a)\nINGRESE 2 ---> HIPERGEOMÉTRICA ACUMULADA P(X<=a)\nINGRESE 3 ---> HIPERGEOMÉTRICA ENTRE DOS VALORES P(a<=x<=b)\nINGRESE 4 ---> VALOR ESPERADO Y VARIANZA\nINGRESE 5 ---> PARA CALCULAR UNA DISTRIBUCIÓN DIFERENTE\n")
                acceso=vacio(input("--> "))
                print("")
            elif acceso=="5":
                print("====================================================================================================\n")
                print("{:^100}".format("TAREA FINALIZADA\n"))
                print("====================================================================================================\n")
                break
            else:
                print("====================================================================================================\n")
                print("{:^100}".format("ERROR, POR FAVOR INGRESE LOS NÚMEROS CONTEMPLADOS EN LA LISTA\n"))
                print("====================================================================================================\n")
                print("INGRESE 1 ---> HIPERGEOMÉTRICA PUNTUAL P(X=a)\nINGRESE 2 ---> HIPERGEOMÉTRICA ACUMULADA P(X<=a)\nINGRESE 3 ---> HIPERGEOMÉTRICA ENTRE DOS VALORES P(a<=x<=b)\nINGRESE 4 ---> VALOR ESPERADO Y VARIANZA\nINGRESE 5 ---> PARA CALCULAR UNA DISTRIBUCIÓN DIFERENTE\n")
                acceso=vacio(input("--> "))
                print("")
        print("{:^100}".format("POR FAVOR ELIJA UNA DISTRIBUCIÓN\n"))
        print("INGRESE 1 ---> DISTRIBUCIÓN BINOMIAL\nINGRESE 2 ---> DISTRIBUCIÓN HIPERGEOMÉTRICA\nINGRESE 3 ---> DISTRIBUCIÓN POISSON\nINGRESE 4 ---> PARA CERRAR EL PROGRAMA\n")
        seleccion=vacio(input("---> "))
    elif seleccion=="3":
        print("\n====================================================================================================\n")
        print("{:^100}".format("DISTRIBUCIÓN POISSON\n"))
        print("====================================================================================================\n")
        print("{:^100}".format("POR FAVOR ELIJA LA OPERACIÓN QUE DESEA CALCULAR\n"))
        print("INGRESE 1 ---> POISSON PUNTUAL P(X=a)\nINGRESE 2 ---> POISSON ACUMULADA P(X<=a)\nINGRESE 3 ---> POISSON ENTRE DOS VALORES P(a<=x<=b)\nINGRESE 4 ---> VALOR ESPERADO Y VARIANZA\nINGRESE 5 ---> PARA CALCULAR UNA DISTRIBUCIÓN DIFERENTE\n")
        acceso=vacio(input("--> "))
        print("")
        while acceso:
            if acceso=="1":
                l=valida_lambda(float(valida_numero(vacio(input("Ingrese \"λ\" (Lambda): ")))))
                x=int(valida_entero(vacio(input("Ingrese el valor de \"x\" al cual desea calcular la probabilidad: "))))
                print("\n====================================================================================================\n")
                print("{:^100}".format("¿LA INFORMACIÓN QUE HA INGRESADO ES CORRECTA?"))
                print("\n====================================================================================================\n")
                decision=vacio(input("INGRESE \"SI\" O \"NO\" PARA CONFIRMAR LA INFORMACIÓN: "))
                while decision:
                    if decision.upper()=="SI":
                        print("\n====================================================================================================\n")
                        print("{:^100}".format("||   RESULTADO   ||\n"))
                        print("{:^100}".format("La probabilidad de ocurrencia de "+str(x)+" sucesos con una tasa de ocurrencia promedio"))
                        print("{:^100}".format("lambda (λ) igual a "+str(l)+" es: "+format(poisson_individual(x,l),'.10f')))
                        break
                    elif decision.upper()=="NO":
                        print("\n====================================================================================================\n")
                        print("{:^100}".format("VUELVA A INGRESAR LA INFORMACIÓN"))
                        print("\n====================================================================================================\n")
                        l=valida_lambda(float(valida_numero(vacio(input("Ingrese \"λ\" (Lambda): ")))))
                        x=int(valida_entero(vacio(input("Ingrese el valor de \"x\" al cual desea calcular la probabilidad: "))))
                        print("\n====================================================================================================\n")
                        print("{:^100}".format("¿LA INFORMACIÓN QUE HA INGRESADO ES CORRECTA?"))
                        print("\n====================================================================================================\n")
                        decision=vacio(input("INGRESE \"SI\" O \"NO\" PARA CONFIRMAR LA INFORMACIÓN: "))
                    else:
                        print("\n====================================================================================================\n")
                        print("{:^100}".format("ERROR"))
                        print("{:^100}".format("INGRESE UNA PALABRA VÁLIDA\n"))
                        print("====================================================================================================\n")
                        decision=vacio(input("INGRESE \"SI\" O \"NO\" PARA CONFIRMAR LA INFORMACIÓN: "))
                print("\n====================================================================================================\n")
                print("{:^100}".format("NUEVO CÁLCULO\n"))
                print("====================================================================================================\n")
                print("{:^100}".format("POR FAVOR ELIJA LA OPERACIÓN QUE DESEA CALCULAR\n"))
                print("INGRESE 1 ---> POISSON PUNTUAL P(X=a)\nINGRESE 2 ---> POISSON ACUMULADA P(X<=a)\nINGRESE 3 ---> POISSON ENTRE DOS VALORES P(a<=x<=b)\nINGRESE 4 ---> VALOR ESPERADO Y VARIANZA\nINGRESE 5 ---> PARA CALCULAR UNA DISTRIBUCIÓN DIFERENTE\n")
                acceso=vacio(input("--> "))
                print("")
            elif acceso=="2":
                l=valida_lambda(float(valida_numero(vacio(input("Ingrese \"λ\" (Lambda): ")))))
                x=int(valida_entero(vacio(input("Ingrese el valor de \"x\" hasta el cual desea calcular la probabilidad: "))))
                print("\n====================================================================================================\n")
                print("{:^100}".format("¿LA INFORMACIÓN QUE HA INGRESADO ES CORRECTA?"))
                print("\n====================================================================================================\n")
                decision=vacio(input("INGRESE \"SI\" O \"NO\" PARA CONFIRMAR LA INFORMACIÓN: "))
                while decision:
                    if decision.upper()=="SI":
                        print("\n====================================================================================================\n")
                        print("{:^100}".format("||   RESULTADO   ||\n"))
                        print("{:^100}".format("La probabilidad de ocurrencia de hasta "+str(x)+" sucesos con una tasa de ocurrencian promedio"))
                        print("{:^100}".format("lambda (λ) igual a "+str(l)+" es: "+format(poisson(x,l),'.10f')))
                        break
                    elif decision.upper()=="NO":
                        print("\n====================================================================================================\n")
                        print("{:^100}".format("VUELVA A INGRESAR LA INFORMACIÓN"))
                        print("\n====================================================================================================\n")
                        l=valida_lambda(float(valida_numero(vacio(input("Ingrese \"λ\" (Lambda): ")))))
                        x=int(valida_entero(vacio(input("Ingrese el valor de \"x\" hasta el cual desea calcular la probabilidad: "))))
                        print("\n====================================================================================================\n")
                        print("{:^100}".format("¿LA INFORMACIÓN QUE HA INGRESADO ES CORRECTA?"))
                        print("\n====================================================================================================\n")
                        decision=vacio(input("INGRESE \"SI\" O \"NO\" PARA CONFIRMAR LA INFORMACIÓN: "))
                    else:
                        print("\n====================================================================================================\n")
                        print("{:^100}".format("ERROR"))
                        print("{:^100}".format("INGRESE UNA PALABRA VÁLIDA\n"))
                        print("====================================================================================================\n")
                        decision=vacio(input("INGRESE \"SI\" O \"NO\" PARA CONFIRMAR LA INFORMACIÓN: "))
                print("\n====================================================================================================\n")
                print("{:^100}".format("NUEVO CÁLCULO\n"))
                print("====================================================================================================\n")
                print("{:^100}".format("POR FAVOR ELIJA LA OPERACIÓN QUE DESEA CALCULAR\n"))
                print("INGRESE 1 ---> POISSON PUNTUAL P(X=a)\nINGRESE 2 ---> POISSON ACUMULADA P(X<=a)\nINGRESE 3 ---> POISSON ENTRE DOS VALORES P(a<=x<=b)\nINGRESE 4 ---> VALOR ESPERADO Y VARIANZA\nINGRESE 5 ---> PARA CALCULAR UNA DISTRIBUCIÓN DIFERENTE\n")
                acceso=input("--> ")
                print("")
            elif acceso=="3":
                l=valida_lambda(float(valida_numero(vacio(input("Ingrese \"λ\" (Lambda): ")))))
                maximo=int(valida_entero(input("Ingrese el límite superior del intervalo: ")))
                minimo=valida_rango(maximo,int(valida_entero(vacio(input("Ingrese el límite inferior del intervalo: ")))))
                print("\n====================================================================================================\n")
                print("{:^100}".format("¿LA INFORMACIÓN QUE HA INGRESADO ES CORRECTA?"))
                print("\n====================================================================================================\n")
                decision=vacio(input("INGRESE \"SI\" O \"NO\" PARA CONFIRMAR LA INFORMACIÓN: "))
                while decision:
                    if decision.upper()=="SI":
                        print("\n====================================================================================================\n")
                        print("{:^100}".format("||   RESULTADO   ||\n"))
                        print("{:^100}".format("La probabilidad de ocurrencia entre "+str(minimo)+" hasta "+str(maximo)+" con una tasa de ocurrencia"))
                        print("{:^100}".format("lambda (λ) igual a "+str(l)+" es: "+format(poisson_entre(maximo,minimo,l),'.10f')))
                        break
                    elif decision.upper()=="NO":
                        print("\n====================================================================================================\n")
                        print("{:^100}".format("VUELVA A INGRESAR LA INFORMACIÓN"))
                        print("\n====================================================================================================\n")
                        l=valida_lambda(float(valida_numero(vacio(input("Ingrese \"λ\" (Lambda): ")))))
                        maximo=int(valida_entero(input("Ingrese el límite superior del intervalo: ")))
                        minimo=valida_rango(maximo,int(valida_entero(vacio(input("Ingrese el límite inferior del intervalo: ")))))
                        print("\n====================================================================================================\n")
                        print("{:^100}".format("¿LA INFORMACIÓN QUE HA INGRESADO ES CORRECTA?"))
                        print("\n====================================================================================================\n")
                        decision=vacio(input("INGRESE \"SI\" O \"NO\" PARA CONFIRMAR LA INFORMACIÓN: "))
                    else:
                        print("\n====================================================================================================\n")
                        print("{:^100}".format("ERROR"))
                        print("{:^100}".format("INGRESE UNA PALABRA VÁLIDA\n"))
                        print("====================================================================================================\n")
                        decision=vacio(input("INGRESE \"SI\" O \"NO\" PARA CONFIRMAR LA INFORMACIÓN: "))
                print("\n====================================================================================================\n")
                print("{:^100}".format("NUEVO CÁLCULO\n"))
                print("====================================================================================================\n")
                print("{:^100}".format("POR FAVOR ELIJA LA OPERACIÓN QUE DESEA CALCULAR\n"))
                print("INGRESE 1 ---> POISSON PUNTUAL P(X=a)\nINGRESE 2 ---> POISSON ACUMULADA P(X<=a)\nINGRESE 3 ---> POISSON ENTRE DOS VALORES P(a<=x<=b)\nINGRESE 4 ---> VALOR ESPERADO Y VARIANZA\nINGRESE 5 ---> PARA CALCULAR UNA DISTRIBUCIÓN DIFERENTE\n")
                acceso=vacio(input("--> "))
                print("")
            elif acceso=="4":
                l=valida_lambda(float(valida_numero(vacio(input("Ingrese \"λ\" (Lambda): ")))))
                print("\n====================================================================================================\n")
                print("{:^100}".format("¿LA INFORMACIÓN QUE HA INGRESADO ES CORRECTA?"))
                print("\n====================================================================================================\n")
                decision=vacio(input("INGRESE \"SI\" O \"NO\" PARA CONFIRMAR LA INFORMACIÓN: "))
                while decision:
                    if decision.upper()=="SI":
                        print("\n====================================================================================================\n")
                        print("{:^100}".format("||   RESULTADO   ||\n"))
                        print("{:^100}".format("E(X)="+str(l)))
                        print("{:^100}".format("V(X)="+str(l)))
                        break
                    elif decision.upper()=="NO":
                        print("\n====================================================================================================\n")
                        print("{:^100}".format("VUELVA A INGRESAR LA INFORMACIÓN"))
                        print("\n====================================================================================================\n")
                        l=valida_lambda(float(valida_numero(vacio(input("Ingrese \"λ\" (Lambda): ")))))
                        print("\n====================================================================================================\n")
                        print("{:^100}".format("¿LA INFORMACIÓN QUE HA INGRESADO ES CORRECTA?"))
                        print("\n====================================================================================================\n")
                        decision=vacio(input("INGRESE \"SI\" O \"NO\" PARA CONFIRMAR LA INFORMACIÓN: "))
                    else:
                        print("\n====================================================================================================\n")
                        print("{:^100}".format("ERROR"))
                        print("{:^100}".format("INGRESE UNA PALABRA VÁLIDA\n"))
                        print("====================================================================================================\n")
                        decision=vacio(input("INGRESE \"SI\" O \"NO\" PARA CONFIRMAR LA INFORMACIÓN: "))
                print("\n====================================================================================================\n")
                print("{:^100}".format("NUEVO CÁLCULO\n"))
                print("====================================================================================================\n")
                print("{:^100}".format("POR FAVOR ELIJA LA OPERACIÓN QUE DESEA CALCULAR\n"))
                print("INGRESE 1 ---> POISSON PUNTUAL P(X=a)\nINGRESE 2 ---> POISSON ACUMULADA P(X<=a)\nINGRESE 3 ---> POISSON ENTRE DOS VALORES P(a<=x<=b)\nINGRESE 4 ---> VALOR ESPERADO Y VARIANZA\nINGRESE 5 ---> PARA CALCULAR UNA DISTRIBUCIÓN DIFERENTE\n")
                acceso=vacio(input("--> "))
                print("")
            elif acceso=="5":
                print("====================================================================================================\n")
                print("{:^100}".format("TAREA FINALIZADA\n"))
                print("====================================================================================================\n")
                break
            else:
                print("====================================================================================================\n")
                print("{:^100}".format("ERROR, POR FAVOR INGRESE LOS NÚMEROS CONTEMPLADOS EN LA LISTA\n"))
                print("====================================================================================================\n")
                print("INGRESE 1 ---> POISSON PUNTUAL P(X=a)\nINGRESE 2 ---> POISSON ACUMULADA P(X<=a)\nINGRESE 3 ---> POISSON ENTRE DOS VALORES P(a<=x<=b)\nINGRESE 4 ---> VALOR ESPERADO Y VARIANZA\nINGRESE 5 ---> PARA CALCULAR UNA DISTRIBUCIÓN DIFERENTE\n")
                acceso=vacio(input("--> "))
                print("")
        print("{:^100}".format("POR FAVOR ELIJA UNA DISTRIBUCIÓN\n"))
        print("INGRESE 1 ---> DISTRIBUCIÓN BINOMIAL\nINGRESE 2 ---> DISTRIBUCIÓN HIPERGEOMÉTRICA\nINGRESE 3 ---> DISTRIBUCIÓN POISSON\nINGRESE 4 ---> PARA CERRAR EL PROGRAMA\n")
        seleccion=vacio(input("---> "))
    elif seleccion=="4":
        print("\n====================================================================================================\n")
        print("{:^100}".format("PROGRAMA FINALIZADO\n"))
        print("====================================================================================================\n")
        break
    else:
        print("\n====================================================================================================\n")
        print("{:^100}".format("ERROR, POR FAVOR INGRESE LOS NÚMEROS CONTEMPLADOS EN LA LISTA\n"))
        print("====================================================================================================\n")
        print("INGRESE 1 ---> DISTRIBUCIÓN BINOMIAL\nINGRESE 2 ---> DISTRIBUCIÓN HIPERGEOMÉTRICA\nINGRESE 3 ---> DISTRIBUCIÓN POISSON\nINGRESE 4 ---> PARA CERRAR EL PROGRAMA\n")
        seleccion=vacio(input("--> "))
