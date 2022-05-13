#Creates the types for the match
#Each type can return its name, its effectiveness (what is supereffective to itself), and the number associated with the type

import TypeEffectiveness, TypeMatchups

labels = {0:"Typeless", 1:"Normal", 2:"Fighting", 3:"Flying", 4:"Poison", 5:"Ground", 6:"Rock", 7:"Bug", 8:"Ghost", 9:"Steel", 10:"Fire", 11:"Water", 12:"Grass", 13:"Electric", 14:"Psychic", 15:"Ice", 16:"Dragon", 17:"Dark", 18:"Fairy"}

class Type:
	def __init__(self,name_effectiveness,number):
		self.name = name_effectiveness[0]
		self.effectiveness = name_effectiveness[1]
		self.number = number


