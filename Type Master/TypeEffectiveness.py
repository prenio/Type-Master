#Returns a dictionary of types and their advantages.
#Also returns a dictionary of types and the file location to the label.


#These type_numbers are arbitrarily given to the types
#Its only for consistency
types = ["Normal","Fighting","Flying","Poison","Ground","Rock","Bug","Ghost","Steel","Fire","Water","Grass","Electric","Psychic","Ice","Dragon","Dark","Fairy"]
type_numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]


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


#Returns the file location for the type image
def returnImage(type):
	jpgFiles = {"Typeless":'Type Labels\\typeless.jpg',"Normal": 'Type Labels\\normal.jpg',"Fighting":'Type Labels\\fighting.jpg' ,"Flying":'Type Labels\\flying.jpg' ,"Poison":'Type Labels\\poison.jpg' ,"Ground":'Type Labels\\ground.jpg' ,"Rock":'Type Labels\\rock.jpg' ,"Bug": 'Type Labels\\bug.jpg',"Ghost":'Type Labels\\ghost.jpg' ,"Steel":'Type Labels\\steel.jpg' ,"Fire":'Type Labels\\fire.jpg' ,"Water":'Type Labels\\water.jpg' ,"Grass":'Type Labels\\grass.jpg' ,"Electric":'Type Labels\\electric.jpg' ,"Psychic":'Type Labels\\psychic.jpg' ,"Ice":'Type Labels\\ice.jpg' ,"Dragon":'Type Labels\\dragon.jpg' ,"Dark":'Type Labels\\dark.jpg' ,"Fairy":'Type Labels\\fairy.jpg' }
	return jpgFiles[type]