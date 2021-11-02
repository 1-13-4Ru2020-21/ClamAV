#1.feladatrész:
#Hozzon létre saját osztályt NewType azonosítóval és definiáljon benne adattagokat az adott emberek nevére, születési idejükre, korukra és nemükre.
#Készítse el az osztály konstruktorát, ami a forrásállomány egy sora alapján rögzíti az adott ember nevét, születési idejét, korát és nemét.
#A forrásállomány egy sora legyen a konstruktor paramétere!

class NewType :
	name =""
	year = 0
	age = 0
	sex = ""
	#Önálló
	def __init__(self, namek, yeark, agek, sexk):
		self.name = namek
		self.year = yeark
		self.age = agek
		self.sex = sexk
#2.feladatrész:
#Olvassa be a "people.txt" állományban található adatokat és tárolja el őket.
#A felhasználók adatait tárolja listában amelynek a típusa NewType legyen.
def Import():
	in_file = open("people.txt", 'r', encoding='utf-8')
	fejl = in_file.readline()
	line = in_file.readline()
	data = []
	while line != "" :
		line = line.replace("\n", '')
		#Önálló
		temp = line.split(';')
		#Önálló
		newline = NewType(temp[0], int(temp[1]), int(temp[2]), temp[3])
		data.append(newline)
		line = in_file.readline()
	in_file.close()
	return data
data = Import()
#Kiiratas :
for people in data:
    print('A személy neve: ', people.name, '\nA személy születési éve: ', people.year, '\nA személy kora: ', people.age, '\nA személy neme: ', people.sex )