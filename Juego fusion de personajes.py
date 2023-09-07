from abc import ABC, abstractclassmethod

class Personaje(ABC):
    def __init__(self,nombre,vida,fuerza):
        self._nombre = nombre
        self._vida = vida
        self._fuerza = fuerza
        
    def __str__(self):
        return f"{self._nombre} ( Fuerza: {self._fuerza}, vida: {self._vida})"
    def __add__(self,otro_pj):
        n_nombre= self._nombre + "-" + otro_pj._nombre 
        nueva_fueza= int(self._fuerza) + int(otro_pj._fuerza)
        nueva_vida= int(self._vida) + int(otro_pj._vida)
        return f"{n_nombre} ( Fuerza: {nueva_fueza}, vida: {nueva_vida})"
    
    
## personajes de prueba      
poter = Personaje("Poter",100, 2000)
napoleon= Personaje("Napoleon", 150, 3000)
###


personajes=[]   # lista de personajes guardados


 ### funcion de creacion de personajes ###
def crearpersonaje():    
    nombre_personaje= input("Ingrese nombre del personaje:")
    vida_personaje= input("Ingrese la vida del personaje:")
    fuerza_personaje= input("Ingrese la fuerza del personaje")
    newpj= Personaje(nombre_personaje,vida_personaje,fuerza_personaje) # creamos el objeto personaje
    personajes.append(newpj)   ## añadimos los personajes a una lista
    print("Personaje creado y guardado")
    return personajes
 
def fusionar(lista):
    print("Personajes creados:")
    for j in range (len(lista)):
        print(f'\n {j+1}. Personaje: {lista[j]._nombre} ( Vida: {lista[j]._vida}, Fuerza: {lista[j]._fuerza})')
    pj1= int(input("\n Ingrese el numero del personaje para fucionar: "))
    print(f"\n \n ------ Pj1 seleccionado: {lista[pj1 -1]._nombre} ------")
    
    print("Personajes creados: \n")
    for j in range (len(lista)):
        print(f'\n {j+1}. Personaje: {lista[j]._nombre} ( Vida: {lista[j]._vida}, Fuerza: {lista[j]._fuerza})')
    pj2= int(input("\n Ingrese el numero del segundo personaje para fucionar: "))
    print(f"\n \n------ Pj2 seleccionado: {lista[pj2 -1]._nombre} ------ ")   
    print(lista[pj1 -1] + lista[pj2 -1])
    return 

## funcion mostrar personajes ##
def mostrarpj(lista):
    for j in range (len(lista)):
        print(f'\n {j+1}. Personaje: {lista[j]._nombre} ( Vida: {lista[j]._vida}, Fuerza: {lista[j]._fuerza})')
    return 


## funcion de menu
def menu():
    print("\n 1. Crear personaje \n 2. Fusionar Personaje \n 3. Mostrar personajes \n 4. Salir ")
    a = input("Selecionar Opcion:")
    if a == "1":
        crearpersonaje();           ## asignamos el perosnaje a variable temporal
    
    elif a == "2":
        fusionar(personajes)
    
    elif a == "3":  # Mostrar personajes
        mostrarpj(personajes)                
        
    elif a == "4":
        return False
    

a= True    
while a != False:
    a = menu()
    