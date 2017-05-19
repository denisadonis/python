# Proyecto: "base"
# Version: 0.0
# Autor: Denis Henriquez
# Fecha: dd/mm/yyyy

def crearArchivo():
	file = open("temp.dat", "w")
	file.close()

def escribirArchivo():
	file = open("temp.dat", "a")
	file.write(input("?") + "\n")
	file.close()

def leerArchivo():
	file = open("temp.dat", "r")
	line = file.readline()
	while line != "":
		print(line - "\n")
		line = file.readline()
	print(type(file))
	file.close()


def main():
	leerArchivo()

if __name__ == '__main__':
	main()