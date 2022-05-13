types = ["Normal","Fighting","Flying","Poison","Ground","Rock","Bug","Ghost","Steel","Fire","Water","Grass","Electric","Psychic","Ice","Dragon","Dark","Fairy"]
x=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]

def createEffectivenessTypeless():
	i = 0
	advantages = {}
	while i != 18:
		advantages[types[i]] = 1
		i = i + 1
	print(advantages)


def createEffectiveness(lst):
	i = 0
	advantages = {}
	while i != 18:
		advantages[types[i]] = lst[i]
		i = i + 1
	print(advantages)

createEffectivenessTypeless()
createEffectiveness(x)