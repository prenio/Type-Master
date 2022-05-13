#Type matchups
#Will list all the type matchups possible


labels = {0:"Typeless", 1:"Normal", 2:"Fighting", 3:"Flying", 4:"Poison", 5:"Ground", 6:"Rock", 7:"Bug", 8:"Ghost", 9:"Steel", 10:"Fire", 11:"Water", 12:"Grass", 13:"Electric", 14:"Psychic", 15:"Ice", 16:"Dragon", 17:"Dark", 18:"Fairy"}

def Type_Matchups(number):
	type = labels[number]
	if type == "Typeless":
		return ["Typeless",{"Normal":1,"Fighting":1,"Flying":1,"Poison":1,"Ground":1,"Rock":1,"Bug":1,"Ghost":1,"Steel":1,"Fire":1,"Water":1,"Grass":1,"Electric":1,"Psychic":1,"Ice":1,"Dragon":1,"Dark":1,"Fairy":1}]
	elif type == "Normal":
		return ["Normal",{"Normal":1,"Fighting":2,"Flying":1,"Poison":1,"Ground":1,"Rock":1,"Bug":1,"Ghost":0,"Steel":1,"Fire":1,"Water":1,"Grass":1,"Electric":1,"Psychic":1,"Ice":1,"Dragon":1,"Dark":1,"Fairy":1}]
	elif type == "Fighting":
		return ["Fighting",{"Normal":1,"Fighting":1,"Flying":2,"Poison":1,"Ground":1,"Rock":0.5,"Bug":0.5,"Ghost":1,"Steel":1,"Fire":1,"Water":1,"Grass":1,"Electric":1,"Psychic":2,"Ice":1,"Dragon":1,"Dark":0.5,"Fairy":2}]
	elif type == "Flying":
		return ["Flying",{"Normal":1,"Fighting":0.5,"Flying":1,"Poison":1,"Ground":0,"Rock":2,"Bug":0.5,"Ghost":1,"Steel":1,"Fire":1,"Water":1,"Grass":0.5,"Electric":2,"Psychic":1,"Ice":2,"Dragon":1,"Dark":1,"Fairy":1}]
	elif type == "Poison":
		return ["Poison",{"Normal":1,"Fighting":0.5,"Flying":1,"Poison":0.5,"Ground":2,"Rock":1,"Bug":0.5,"Ghost":1,"Steel":1,"Fire":1,"Water":1,"Grass":0.5,"Electric":1,"Psychic":2,"Ice":1,"Dragon":1,"Dark":1,"Fairy":0.5}]
	elif type == "Ground":
		return ["Ground",{"Normal":1,"Fighting":1,"Flying":1,"Poison":0.5,"Ground":1,"Rock":0.5,"Bug":1,"Ghost":1,"Steel":1,"Fire":1,"Water":2,"Grass":2,"Electric":0,"Psychic":1,"Ice":2,"Dragon":1,"Dark":1,"Fairy":1}]
	elif type == "Rock":
		return ["Rock",{"Normal":0.5,"Fighting":2,"Flying":0.5,"Poison":0.5,"Ground":2,"Rock":1,"Bug":1,"Ghost":1,"Steel":2,"Fire":0.5,"Water":2,"Grass":2,"Electric":1,"Psychic":1,"Ice":1,"Dragon":1,"Dark":1,"Fairy":1}]
	elif type == "Bug":
		return ["Bug",{"Normal":1,"Fighting":0.5,"Flying":2,"Poison":1,"Ground":0.5,"Rock":2,"Bug":1,"Ghost":1,"Steel":1,"Fire":2,"Water":1,"Grass":0.5,"Electric":1,"Psychic":1,"Ice":1,"Dragon":1,"Dark":1,"Fairy":1}]
	elif type == "Ghost":
		return ["Ghost",{"Normal":0,"Fighting":0,"Flying":1,"Poison":0.5,"Ground":1,"Rock":1,"Bug":0.5,"Ghost":2,"Steel":1,"Fire":1,"Water":1,"Grass":1,"Electric":1,"Psychic":1,"Ice":1,"Dragon":1,"Dark":2,"Fairy":1}]
	elif type == "Steel":
		return ["Steel",{"Normal":0.5,"Fighting":2,"Flying":0.5,"Poison":0,"Ground":2,"Rock":0.5,"Bug":0.5,"Ghost":1,"Steel":0.5,"Fire":2,"Water":1,"Grass":0.5,"Electric":1,"Psychic":0.5,"Ice":0.5,"Dragon":0.5,"Dark":1,"Fairy":0.5}]
	elif type == "Fire":
		return ["Fire",{"Normal":1,"Fighting":1,"Flying":1,"Poison":1,"Ground":2,"Rock":2,"Bug":0.5,"Ghost":1,"Steel":0.5,"Fire":0.5,"Water":2,"Grass":0.5,"Electric":1,"Psychic":1,"Ice":0.5,"Dragon":1,"Dark":1,"Fairy":0.5}]
	elif type == "Water":
		return ["Water",{"Normal":1,"Fighting":1,"Flying":1,"Poison":1,"Ground":1,"Rock":1,"Bug":1,"Ghost":1,"Steel":0.5,"Fire":0.5,"Water":0.5,"Grass":2,"Electric":2,"Psychic":1,"Ice":0.5,"Dragon":1,"Dark":1,"Fairy":1}]
	elif type == "Grass":
		return ["Grass",{"Normal":1,"Fighting":1,"Flying":2,"Poison":2,"Ground":0.5,"Rock":2,"Bug":2,"Ghost":1,"Steel":1,"Fire":2,"Water":0.5,"Grass":0.5,"Electric":0.5,"Psychic":1,"Ice":2,"Dragon":1,"Dark":1,"Fairy":1}]
	elif type == "Electric":
		return ["Electric",{"Normal":1,"Fighting":1,"Flying":0.5,"Poison":1,"Ground":2,"Rock":1,"Bug":1,"Ghost":1,"Steel":0.5,"Fire":1,"Water":1,"Grass":1,"Electric":0.5,"Psychic":1,"Ice":1,"Dragon":1,"Dark":1,"Fairy":1}]
	elif type == "Psychic":
		return ["Psychic",{"Normal":1,"Fighting":0.5,"Flying":1,"Poison":1,"Ground":1,"Rock":1,"Bug":2,"Ghost":2,"Steel":1,"Fire":1,"Water":1,"Grass":1,"Electric":1,"Psychic":0.5,"Ice":1,"Dragon":1,"Dark":2,"Fairy":1}]
	elif type == "Ice":
		return ["Ice",{"Normal":1,"Fighting":2,"Flying":1,"Poison":1,"Ground":1,"Rock":2,"Bug":1,"Ghost":1,"Steel":2,"Fire":2,"Water":1,"Grass":1,"Electric":1,"Psychic":1,"Ice":0.5,"Dragon":1,"Dark":1,"Fairy":1}]
	elif type == "Dragon":
		return ["Dragon",{"Normal":1,"Fighting":1,"Flying":1,"Poison":1,"Ground":1,"Rock":1,"Bug":1,"Ghost":1,"Steel":1,"Fire":0.5,"Water":0.5,"Grass":0.5,"Electric":0.5,"Psychic":1,"Ice":2,"Dragon":2,"Dark":1,"Fairy":2}]
	elif type == "Dark":
		return ["Dark",{"Normal":1,"Fighting":2,"Flying":1,"Poison":1,"Ground":1,"Rock":1,"Bug":2,"Ghost":0.5,"Steel":1,"Fire":1,"Water":1,"Grass":1,"Electric":1,"Psychic":0,"Ice":1,"Dragon":1,"Dark":0.5,"Fairy":2}]
	elif type == "Fairy":
		return ["Fairy",{"Normal":1,"Fighting":0.5,"Flying":1,"Poison":2,"Ground":1,"Rock":1,"Bug":0.5,"Ghost":1,"Steel":2,"Fire":1,"Water":1,"Grass":1,"Electric":1,"Psychic":1,"Ice":1,"Dragon":0,"Dark":0.5,"Fairy":1}]

