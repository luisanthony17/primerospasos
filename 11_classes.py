### Classes ###

'''class MyEmptyPerson:
    pass

print(MyEmptyPerson)
print(MyEmptyPerson())'''

class Person:
    def __init__(self,name,surname,alias= "sin alias"):
       self.name=name  #privado es inmutable
       self.surname = surname
       self.alias = alias
       self.fullname= f"{name} {surname} {alias}"  #publico se puede editar
   
    def caminar(self):
        print(self.name + " esta caminando")

    def corriendo(self):
        print(self.fullname , " esta corriendo")

my_person = Person("luis","chavez")
print(my_person.name,my_person.surname,my_person.alias)
#print(f"{my_person.name} {my_person.surname}")
my_person.caminar()

my_person_other= Person("luis","chumbes","luian")
print(my_person_other.fullname)
my_person_other.corriendo()
###se le da otra txta fullname ya que el tipado es debil y cambia de metodo pero si o si primero se tiene que definir el fullname primero.
my_person_other.fullname= "pepe come manzanas"
print(my_person_other.fullname)

my_person_other.fullname= 777
print(my_person_other.fullname)

  
