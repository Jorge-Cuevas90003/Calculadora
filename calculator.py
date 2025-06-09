import time
import re
import math

bienvenvenida=["","㊋","㊋","㊋","㊋","㊋","㊋","","🅱 ","🅸","🅴","🅽","🆅","🅴","🅽","🅸","🅳","🅾 ","㊌","㊌","㊌","㊌","㊌","㊌",""]
#Damos la bienvenida
for x in bienvenvenida:
  print(x,end=" ",flush=True)
  time.sleep(0.1)
print()
print("--------------------------------------------------------")
time.sleep(0.3)
print("Créditos: Creador del programa calculadora: ")
time.sleep(0.3)
nombres="Jorge Cuevas"

for y in nombres:
  print(y,end="",flush="True")
  time.sleep(0.03)
print()
print("--------------------------------------------------------")

while True:
  try:
    palabra=input("calculadora >> ")
    if palabra=="quit":
      print("Saliendo...")
      print("Adiós Usuario 🤙")
      break
    if (palabra=="-") or (palabra=="+") or (palabra=="/") or (palabra=="*") or (palabra=="sen") or (palabra=="cos") or (palabra=="tan"):
       print("ERROR! Expresion no valida, no existe una ecuación")
      
    numeros=["0"]
    operadores=[]
    comprobarparentesis=re.compile('-?\d+\.?\d*')
    
    for t in palabra.split():
      if comprobarparentesis.match(t):
          numeros.append(t)
    versihayespacios=0
    verificarparentesis=0
    for p in palabra:
      if p==" ":
        versihayespacios+=1
      if p=="(":
        verificarparentesis+=1
    verificarsignonegativo=0
    if versihayespacios==0 and verificarparentesis>0:
      for q in palabra:
        if q=="-":
          print("El numero no debe tener parentesis")
          verificarsignonegativo+=1
        if verificarsignonegativo==0:
           if comprobarparentesis.match(q):
             numeros.append(q) 
    posicion1=0
    numero=""
    for x in numeros:
      if x[len(x)-1]==")":
          posicion1=numeros.index(x)
          for m in x:
              if m==")":
                  numeros[posicion1]=numero
                  numero=""
                  break
              numero+=m
            
  # se definen los signos para poder operarlos más adelante.
    expresionmatematica=re.compile('[sct]')
    expresionmatematica2 = re.compile('[d]')
    expresionmatematica3 = re.compile('[f]')
    guardarcarater=""
    for b in palabra:
       if b=="+":
         operadores.append("+")
       if b=="-":
         operadores.append("-")
       if b == "%":
         operadores.append("%")
       if b=="/":
         operadores.append("/")
       if b=="*":
         operadores.append("*")
       if b=="t" and guardarcarater!="fac":
         guardarcarater=b
         continue
       if b=="c" and guardarcarater!="fa":
         guardarcarater=b
         continue
       if b == "d":
         guardarcarater = b
         continue
       if expresionmatematica2.match(guardarcarater):
         guardarcarater+=b
         if guardarcarater=="div":
           operadores.append(guardarcarater)
           guardarcarater="" 
       if b=="f":
         guardarcarater=b
         continue
       if expresionmatematica3.match(guardarcarater):
         guardarcarater+=b
         if guardarcarater=="fact!":
           operadores.append(guardarcarater)
           guardarcarater=""
           continue
           
       if b=="s" and guardarcarater!="co":
         guardarcarater=b
         continue
       if expresionmatematica.match(guardarcarater):
         guardarcarater+=b
        
         if guardarcarater=="sen":
           operadores.append(guardarcarater)
           guardarcarater=""
         if guardarcarater=="sqr ":
           operadores.append(guardarcarater)
           guardarcarater=""
         if guardarcarater=="sqroot":
           operadores.append(guardarcarater)
           guardarcarater=""
         if guardarcarater=="cos":
          operadores.append(guardarcarater)
          guardarcarater=""
         if guardarcarater=="tan":
           operadores.append(guardarcarater)
           guardarcarater=""
         
        
  
    VerificarError=0
    Suma=0
    Resta=0
    Division=0
    Multiplicacion=0
    seno=0
    Sqroot=0
    Sqr=0
    Coseno=0
    Tangente=0

    jerarquiadeoperacion=list(reversed(operadores))
    ultimonumero=len(numeros)-1
   
    Total=0
    for i in jerarquiadeoperacion:
       if i=="+":
         if palabra[0] != "(":
           print("ERROR! Expresion no valida no tiene parentesis al inicio")
         elif palabra[-1] != ")": 
           print("ERROR! Expresion no valida no tiene parentesis al final")
         elif palabra[-2] == " " :
           print("ERROR! Expresion no valida tiene un espacio antes del parentesis final")
         else: 
           if int(numeros[ultimonumero-1])==0:
             try:
               Suma=int(numeros[ultimonumero])+Resta+seno+Division+Multiplicacion+Sqroot+Sqr+Coseno+Tangente+Suma
            
               Total=Suma
            
             except:
              VerificarError=2
              continue
        #Definimos cada operación y agregamos el orden jerárquico para calcular las operaciones 
           else:
              try:
               Suma=int(numeros[ultimonumero])+int(numeros[ultimonumero-1])+Resta+seno+Division+Multiplicacion+Sqroot+Sqr+Coseno+Tangente+Suma
            
               Total=Suma
               ultimonumero-=2
              except:
               VerificarError=2
               continue
             
       if i=="-":
         if  palabra[0] != "(":
           print("ERROR! Expresion no valida no tiene parentesis al inicio")
         elif palabra[-1] != ")": 
           print("ERROR! Expresion no valida no tiene parentesis al final")
         elif palabra[-2] == " " :
           print("ERROR! Expresion no valida tiene un espacio antes del parentesis final")
         else:
           if int(numeros[ultimonumero-1])==0:
             try:
               Resta=(int(numeros[ultimonumero]))-((int(numeros[ultimonumero-1]))+Suma+seno+Division+Multiplicacion+Sqroot+Sqr+Coseno+Tangente+Resta)
               Total=Resta
             except:
              VerificarError=1
              continue 
           elif int(numeros[ultimonumero])==0:
             try:
               if jerarquiadeoperacion[0]=="sqr " and jerarquiadeoperacion[1]=="cos":
                 Resta=Coseno-(Sqr*2)
                 Total=Resta
               elif jerarquiadeoperacion[0]=="sqr " and jerarquiadeoperacion[1]=="sqroot":
                 Resta=Sqroot-(Sqr*2)
                 Total=Resta
               elif jerarquiadeoperacion[0]=="sqr " and jerarquiadeoperacion[1]=="sen":
                 Resta=seno-(Sqr*2)
                 Total=Resta
               elif jerarquiadeoperacion[0]=="sqr " and jerarquiadeoperacion[1]=="tan":
                 Resta=Tangente-(Sqr*2)
                 Total=Resta
               elif jerarquiadeoperacion[0]=="sqroot" and jerarquiadeoperacion[1]=="sqr ":
                 Resta=Sqr-(Sqroot*2)
                 Total=Resta
               elif jerarquiadeoperacion[0]=="sqroot" and jerarquiadeoperacion[1]=="sen":
                 Resta=seno-(Sqroot*2)
                 Total=Resta
               elif jerarquiadeoperacion[0]=="sqroot" and jerarquiadeoperacion[1]=="cos":
                 Resta=Coseno-(Sqroot*2)
                 Total=Resta
               elif jerarquiadeoperacion[0]=="sqroot" and jerarquiadeoperacion[1]=="tan":
                 Resta=Tangente-(Sqroot*2)
                 Total=Resta
               elif jerarquiadeoperacion[0]=="sen" and jerarquiadeoperacion[1]=="sqr ":
                 Resta=Sqr-(seno*2)
                 Total=Resta
               elif jerarquiadeoperacion[0]=="sen" and jerarquiadeoperacion[1]=="sqroot":
                 Resta=Sqroot-(seno*2)
                 Total=Resta
               elif jerarquiadeoperacion[0]=="sen" and jerarquiadeoperacion[1]=="cos":
                 Resta=Coseno-(seno*2)
                 Total=Resta
               elif jerarquiadeoperacion[0]=="sen" and jerarquiadeoperacion[1]=="tan":
                 Resta=Tangente-(seno*2)
                 Total=Resta
               elif jerarquiadeoperacion[0]=="cos" and jerarquiadeoperacion[1]=="sqr ":
                 Resta=Sqr-(Coseno*2)
                 Total=Resta
               elif jerarquiadeoperacion[0]=="cos" and jerarquiadeoperacion[1]=="sqroot":
                 Resta=Sqroot-(Coseno*2)
                 Total=Resta
               elif jerarquiadeoperacion[0]=="cos" and jerarquiadeoperacion[1]=="sen":
                 Resta=seno-(Coseno*2)
                 Total=Resta
               elif jerarquiadeoperacion[0]=="cos" and jerarquiadeoperacion[1]=="tan":
                 Resta=Tangente-(Coseno*2)
                 Total=Resta
               elif jerarquiadeoperacion[0]=="tan" and jerarquiadeoperacion[1]=="sqr ":
                 Resta=Sqr-(Tangente*2)
                 Total=Resta
               elif jerarquiadeoperacion[0]=="tan" and jerarquiadeoperacion[1]=="sqroot":
                 Resta=Sqroot-(Tangente*2)
                 Total=Resta
               elif jerarquiadeoperacion[0]=="tan" and jerarquiadeoperacion[1]=="sen":
                 Resta=seno-(Tangente*2)
                 Total=Resta
               elif jerarquiadeoperacion[0]=="tan" and jerarquiadeoperacion[1]=="cos":
                 Resta=Coseno-(Tangente)
                 Total=Resta
                 
             except:
               VerificarError=1
               continue
           else:
             try:  
               Resta=(int(numeros[ultimonumero-1]))-((int(numeros[ultimonumero]))+Suma+seno+Division+Multiplicacion+Sqroot+Sqr+Coseno+Tangente+Resta)
               Total=Resta
               ultimonumero-=2
             except:
              VerificarError=2
              continue  
       if i=="/":
         if palabra[0] != "(":
           print("ERROR! Expresion no valida no tiene parentesis al inicio")
         elif palabra[-1] != ")": 
           print("ERROR! Expresion no valida no tiene parentesis al final")
         elif palabra[-2] == " " :
           print("ERROR! Expresion no valida tiene un espacio antes del parentesis final")
         else:
          if int(numeros[ultimonumero-1])==0:
            try:
              Division=(int(numeros[ultimonumero]))/(int(numeros[ultimonumero-1])+Suma+Resta+seno+Multiplicacion+Sqr+Sqroot+Coseno+Tangente+Division)
              Total=Division
            except:
              VerificarError=1
              continue
          else:
              try:
               Division=(int(numeros[ultimonumero-1]))/(int(numeros[ultimonumero])+Suma+Resta+seno+Multiplicacion+Sqr+Coseno+Sqroot+Tangente+Division)
               Total=Division
               ultimonumero-=2
              except:
               VerificarError=1
               continue
       if i=="*":
         if palabra[0] != "(":
           print("ERROR! Expresion no valida no tiene parentesis al inicio")
         elif palabra[-1] != ")": 
           print("ERROR! Expresion no valida no tiene parentesis al final")
         elif palabra[-2] == " " :
           print("ERROR! Expresion no valida tiene un espacio antes del parentesis final")
         else:       
           try:
             Multiplicacion=(int(numeros[ultimonumero]))*(int(numeros[ultimonumero-1])+Suma+Resta+seno+Division+Sqroot+Sqr+Coseno+Tangente+Multiplicacion)
             Total=Multiplicacion
             ultimonumero-=2
           except:
               VerificarError=2
               continue
       if i=="sen":
         if palabra[0] != "(":
           print("ERROR! Expresion no valida no tiene parentesis al inicio")
         elif palabra[-1] != ")": 
           print("ERROR! Expresion no valida no tiene parentesis al final")
         elif palabra[-2] == " " :
           print("ERROR! Expresion no valida tiene un espacio antes del parentesis final")
         else:       
          try:
           seno=math.sin(int(numeros[ultimonumero]))+Suma+Resta+Division+Multiplicacion+Sqroot+Sqr+Coseno+Tangente+seno
           Total=seno
           ultimonumero-=1
          except:
               VerificarError=2
               continue 
       if i=="sqroot":
         if palabra[0] != "(":
           print("ERROR! Expresion no valida no tiene parentesis al inicio")
         elif palabra[-1] != ")": 
           print("ERROR! Expresion no valida no tiene parentesis al final")
         elif palabra[-2] == " " :
           print("ERROR! Expresion no valida tiene un espacio antes del parentesis final")
         else:       
           try:
             Sqroot=math.sqrt(int(numeros[ultimonumero]))+Suma+Resta+seno+Multiplicacion+Division+Sqr+Coseno+Tangente
             Total=Sqroot
             ultimonumero-=1
           except:
               VerificarError=3
               continue 
       if i=="sqr ":
         if palabra[0] != "(":
           print("ERROR! Expresion no valida no tiene parentesis al inicio")
         elif palabra[-1] != ")": 
           print("ERROR! Expresion no valida no tiene parentesis al final")
         elif palabra[-2] == " " :
           print("ERROR! Expresion no valida tiene un espacio antes del parentesis final")
         else: 
          try:
           Sqr=(int(numeros[ultimonumero])**2)+Suma+Resta+seno+Multiplicacion+Division+Coseno+Sqroot+Tangente
           Total=Sqr
           ultimonumero-=1
          except:
               VerificarError=2
               continue 
       if i=="cos":
         if palabra[0] != "(":
           print("ERROR! Expresion no valida no tiene parentesis al inicio")
         elif palabra[-1] != ")": 
           print("ERROR! Expresion no valida no tiene parentesis al final")
         elif palabra[-2] == " " :
           print("ERROR! Expresion no valida tiene un espacio antes del parentesis final")
         else:       
            try:
             Coseno=math.cos(int(numeros[ultimonumero]))+Suma+Resta+seno+Multiplicacion+Division+Sqr+Sqroot+Tangente
             Total=Coseno
             ultimonumero-=1
            except:
                 VerificarError=2
                 continue   
       if i=="tan":
         if palabra[0] != "(":
           print("ERROR! Expresion no valida no tiene parentesis al inicio")
         elif palabra[-1] != ")": 
           print("ERROR! Expresion no valida no tiene parentesis al final")
         elif palabra[-2] == " " :
           print("ERROR! Expresion no valida tiene un espacio antes del parentesis final")
         else:       
          try:
           Tangente=math.tan(int(numeros[ultimonumero]))+Suma+Resta+seno+Multiplicacion+Division+Sqr+Sqroot+Coseno
           Total=Tangente
           ultimonumero-=1
          except:
               VerificarError=2
               continue  \
      #Definimos las operaciones adicionales y comprobamos los errores que pudieran existir. 
       if i == "div":
         if palabra[0] != "(":
           print("ERROR! Expresion no valida no tiene parentesis al inicio")
         elif palabra[-1] != ")": 
           print("ERROR! Expresion no valida no tiene parentesis al final")
         elif palabra[-2] == " " :
           print("ERROR! Expresion no valida tiene un espacio antes del parentesis final")
         else:         
          div = (int(numeros[ultimonumero-1])) // (int(numeros[ultimonumero]))
          Total = div 
          ultimonumero-=2
       if i == "%":
         if palabra[0] != "(":
           print("ERROR! Expresion no valida no tiene parentesis al inicio")
         elif palabra[-1] != ")": 
           print("ERROR! Expresion no valida no tiene parentesis al final")
         elif palabra[-2] == " " :
           print("ERROR! Expresion no valida tiene un espacio antes del parentesis final")
         else:         
          residuo = (int(numeros[ultimonumero-1]))%(int(numeros[ultimonumero]))
          Total = residuo
       if i == "fact!":
         if palabra[0] != "(":
           print("ERROR! Expresion no valida no tiene parentesis al inicio")
         elif palabra[-1] != ")": 
           print("ERROR! Expresion no valida no tiene parentesis al final")
         elif palabra[-2] == " " :
           print("ERROR! Expresion no valida tiene un espacio antes del parentesis final")
         else:         
           fact = 1
           for x in range(1, int(numeros[ultimonumero]) + 1):
             fact = fact * x
           Total =fact
       
          
    if len(numeros)==2 and Total==0:
      Total=numeros[1]
  
    if VerificarError==0:
       print("Resultado:",Total) 
    elif VerificarError==1:
      print("ERROR! Division entre cero")
    elif VerificarError==2:
      print("ERROR! Expresion no valida")  
    elif VerificarError==3:
      print("ERROR! Raiz cuadrada negativa") 
  except:
     print("ERROR! Expresion no valida")  
     continue 
