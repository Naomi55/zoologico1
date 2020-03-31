x=int(input("¿cuantos animales quieres?"))
passed = []
tipo=[]
classif=[]

subject=1
while subject <= x:
    score =input("Nombre del animal" +  "?")
    passed.append(score)
    score1 = input("typo de animal" +  "?")
    tipo.append(score1)
    score2 = input("Clasficación del animal" +  "?")
    classif.append(score2)
    subject=subject+1

print("La lista contiene")
print(passed)
print(score1)
print(score2)


score3 = input("Nuevo typo de animal" +  "?")
class Zoologico:
	def __init__(self, nombre, tipo):
		self.nombre = nombre
		self.tipo = tipo

	def set_brand(self,tipo):
		self.tipo = tipo
		print ("El nuevo tipo es" + self.tipo)
	
	def get_brand(self):
		print ("El tipo de animal actual es " + self.tipo)

def main():
	zoo = Zoologico("n","x")
	zoo.set_tipo(score3)
	zoo.get_tipo()


if __name__ == "__main__":
	main()
