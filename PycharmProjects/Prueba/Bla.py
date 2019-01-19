#Francisca Berrios Diaz
import estructura
from lista import*
import random

#Parte a)

def presente(dig,num):
    assert type(dig)==int and type(num)==int
    n = len(str(num))
    if n==1 and dig != num: #Caso Base
          return False
    elif dig==(num/(10**(n-1))):
          return True
    
    else: #Caso Recursivo
        return presente(dig,(num%10**(n-1)))



#Parte d)

def famas(num1,num2):
    assert type(num1)==int and type(num2)==int
    n1=len(str(num1))
    n2=len(str(num2))
    if num1==0 or num2==0: #Caso Base 
        return 0
    elif num1/(10**(n1-1))==num2/(10**(n2-1)): #Caso Recursivo
        return 1+famas((num1%(10**(n1-1))),(num2%(10**(n2-1))))
    elif num1/(10**(n1-1))!= num2/(10**(n2-1)):
        return famas((num1%(10**(n1-1))),(num2%(10**(n2-1))))
    else:
        return 0



#Parte e)

def coincidentes(num1,num2):
    assert type(num1)==int and type(num2)==int
    n1=len(str(num1))
    n2=num2%(10**(n1))
    if num1==0 and num2==0: #Caso Base 1
            return 1
    elif num1==0: #Caso Base 2
        return 0
    
    elif presente(num1/(10**(n1-1)),num2)== True \
         and num1/(10**(n1-1))!=n2/(10**(n1-1)) :#Caso Recursivo
        
            return 1+ coincidentes(num1%(10**(n1-1)),num2)
    else:
            return coincidentes(num1%(10**(n1-1)),num2)



#Parte g)
#validar: int int -> bool
#valida que un numero tiene exactamente n digitos distintos de 0 y ninguno se repite
#ej: validar(4,4619)==True
#    validar(4,5801)==False (hay un 0) 
#    validar(4,7121)==False (se repite el 1)
def validar(n,num):
    if presente(0,num)== True or len(str(num))!=n:
        return False
    elif len(str(num))==1 and len(str(num))==n and num!=0:
        return True
    else:
        num2=str(num)
        n_i=num2[0]
        if presente(int(n_i),int(num2[1:]))==False:
            return validar(n-1,int(num2[1:]))
        else:
            return False


assert validar(4,4619)==True
assert validar(4,5801)==False
assert validar(4,7121)==False


#Parte h)
#Juagada: numero(int) toques(int) famas(int)

estructura.crear("Jugada", "numero toques famas")

#Parte i)
# esCompatible: Jugada int -> bool
# retorna True si el numero x es compatible con la Jugada y False si no lo es
#ej: n=Jugada(2345,1,1)
# esCompatible(n,1394) devuelve True
# esCompatible(n,7945) devuelve False


def esCompatible(n,x):
    z=n.numero
    if famas(z,x)==n.famas and coincidentes(z,x)==n.toques:
        return True
    else:
        return False

n=Jugada(2345,1,1)
assert esCompatible(n,1394)==True
assert esCompatible(n,7945)==False


#Parte j)
#candidato: lista(any) int -> bool
#retorna True si el numero x es compatible con todas las Jugadas de la lista y False si no lo es
#ej: L= varios(Jugada(1394,1,1),Jugada(2865,0,2))
#    candidato(L,2345) entrega True
#    candidato(L,2951) entrega False

def candidato(L,x):
    if L==listaVacia:
        return False
    else:
        if esCompatible(cabeza(L),x)==True:
            if largo(L)==1:
                return True
            else:
                return candidato(cola(L),x)
        else:
            return False

H= varios(Jugada(1394,1,1),Jugada(2865,0,2))
assert candidato(H,2345)==True
assert candidato(H,2951)==False


#Parte k)
#encuentraX: int int lista(any) -> int
#retorna un x tal que: u<=x<=v, x es valido y x es candidato. Si no existe tal x, retorna 0
#ej: L=varios(Jugada(1394,1,1),Jugada(2865,0,2))
#    encuentraX(1500,2500,L) entrega el numero 1835
#    encuentraX(1500,1700,L) entrega el numero 0
        
def encuentraX(u,v,L):
    if u>=v:
        return 0
    elif L==listaVacia:
        return 0
    x=u+1
    if candidato(L,x)==True and validar(4,x)==True:
        return x
    else:
        u=u+1
        return encuentraX(u,v,L)

K=varios(Jugada(1394,1,1),Jugada(2865,0,2))
assert encuentraX(1500,2500,K)==1835
assert encuentraX(1500,1700,K)==0
        
    

#Parte l)
#encuentraX2: int int lista(any) -> int
#retorna un x tal que: u<=x<=v, x es valido y x es candidato. Si no existe tal x, retorna 0
#ej:L=varios(Jugada(1394,1,1),Jugada(2865,0,2))
#   encuentraX2(1000,4000,L) entrega el entero 1465
#   encuentraX2(1500,1700,L) entrega el entero 0


def encuentraX2(u,v,L):
    m=u+99
    if (v-u)<100:
        return encuentraX(u,v,L)
    else:
        if encuentraX(u,m,L)==0:
            u=u+100
            return encuentraX2(u,v,L)
        else:
            return encuentraX(u,m,L)

J=varios(Jugada(1394,1,1),Jugada(2865,0,2))
assert encuentraX2(1000,4000,J)==1465
assert encuentraX2(1500,1700,J)==0




#Parte m)


def candidatoFinal(L):
    w=random.randint(1234,9876)
    x=encuentraX2(w,9876,L)
    if x!= 0:
        return x
    else:
        return encuentraX2(1234,w,L)
    


#Parte n)


def toqueyfama(I):
        print I
        if I==listaVacia:
            x=random.randint(1000,9999)
            print 'Creo que es el ' + str(x)
            f=raw_input('Cuantas famas?')
            t=raw_input('Cuantos toques?')
            if int(f)==4:
                print('Lo descubri!')
            else:
                I= lista(Jugada(x,int(t),int(f)),I)
                return toqueyfama(I)
        else:
            print "lista no vacia=", I
            n=candidatoFinal(I)
            print 'Creo que es el ',n
            f=raw_input('Cuantas famas?')
            t=raw_input('Cuantos toques?')
            if int(f)==4:
                print('Lo descubri!')
            else:
                I=lista(Jugada(n,int(t),int(f)),I)
                return toqueyfama(I)
     
a=raw_input('Piense en un numero. Voy a adivinarlo. Preparado?')
j=listaVacia
if a.strip()=='si':
    toqueyfama(j)
    
    
                               
    
