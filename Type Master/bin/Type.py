import TypeEffectiveness

class Type:
	def __init__(self):
		self.name = "Typeless"
		self.effectiveness = TypeEffectiveness.createEffectivenessTypeless()

	def __init__(self,name,advantages):
		self.name = name
		self.effectiveness = TypeEffectiveness.createEffectiveness(advantages)


		