class Role:
	def __init__(self, name, description, priority):
		self.name = name
		self.description = description
		self.priority = priority

	def display_role(self):
		print("Name: ", self.name)
		print("Description: ", self.description)
		print("Priority: ", self.priority)



class GameState:
	def __init__(self, number_of_players, roles):
		self.number_of_players = number_of_players
		self.turn_number = 0
		self.roles = roles


class Player:
	def __init__(self, name):
		self.name = name
