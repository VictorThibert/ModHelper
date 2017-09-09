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
	def __init__(self, number_of_players, roles, players):
		self.number_of_players = number_of_players
		self.turn_number = 0
		self.roles = roles
		self.players = players

	def advance_turn(self):
		self.go_to_night()
		self.go_to_day()

	def go_to_night(self):
		self.turn_number += 1
		print(self.turn_number)

	def go_to_day(self):
		print("Wake up")



class Player:
	def __init__(self, name, role):
		self.name = name
		self.alive_status = True 
		self.role = role
		self.item = None
		self.protected_for = 0

	def set_role(self, role):
		self.role = role

	def kill(self):
		self.alive_status = False

	def protect(self, number_of_turns):
		self.protect_for = number_of_turns

	def advance_turn(self):
		self.protect_for = self.protect_for - 1



def simulate_basic_game():
	villager1 = Role("villager", "Good guy", 0)
	villager2 = Role("villager", "Good guy", 0)
	mafia = Role("mafia", "Bad guy", 10)
	roles = [villager1, villager2, mafia]
	
	alice = Player("alice", villager1)
	bob = Player("bob", villager2)
	charlie = Player("charlie", mafia)
	players = [alice, bob, charlie]

	test_game = GameState(3, roles, players)
	test_game.advance_turn()
	test_game.advance_turn()

simulate_basic_game()