Cards = ['w/b/s/o', 'w', 's/b', 's'] #for testing can make it raw input
make = "WWSS"			#this is the final answer I am seeing if the cards can make


def sort(cards, make):
	for i in cards:
		i.split("/")
		cards.sort()  #sorting so it'll hit faster
		need = list(make)
		need.sort()
		while len(need) > 0:   #loop until each one has been verified
			for i in cards:
				if not [n for n in need]:   #if one is impossible whole thing fails
					print("nope")
				else:
					need.remove(n)  #progress 
		print("it works!")	#if none left to check then it works

sort(Cards, make)