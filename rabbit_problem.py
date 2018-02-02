#to make the rabbits
class Rabbit():
	def __init__(self, gender, age):
		self.gender = gender
		self.age = age

# to breed, ages first
def breed(rabbits):
	for r in rabbits:
		r.age +=1
		if r.age == 96:
			rabbits.remove(r)
		elif r.age > 3 and r.gender == "female":
			x = 0
			while x < 10:
				rabbits.append(Rabbit("female",2))
				x +=1
			while x<17:
				rabbits.append(Rabbit("male" , 2))
				x +=1


#the given rabbits
r1 = Rabbit("female", 4)
r2 = Rabbit("female", 4)
r3 = Rabbit("male", 4)
rabbits = [r1, r2, r3]

#run it
count=0
while len(rabbits) < 10000:
		breed(rabbits)
		count +=1

print(len(rabbits))
print(count)





