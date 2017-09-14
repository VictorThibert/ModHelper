import role
from player import Player

class GameState:
	def __init__(self, number_of_players, roles, players):
		self.number_of_players = number_of_players
		self.turn_number = 0
		self.state = "day"
		self.roles = sorted(roles, key=lambda x: x.priority, reverse=True) # sort roles in order of their priority
		self.players = players

	def advance_turn(self):
		self.go_to_night()
		self.go_to_day()

	def go_to_night(self):
		self.turn_number += 1
		self.state = "night"
		print(self.turn_number)


		# perform night actions
		for role in self.roles:
			print(role)
			print("______")
			role.perform_action(self)

	def go_to_day(self):
		self.state = "day"
		print("Wake up")

	def is_game_over(self):
		return False

	# right now, doctor's protection	
	def protect_player(self, target, number_of_turns):
		if target in players:
			# retrieve player object
			players[target].protect(number_of_turns)


	# count number of alive players for a given true alignment
	def count_alignment(self, alignment):
		return sum(1 for player in self.players.values() if player.alignment == alignment and player.alive_status ==True)




def play(): # example

	r1 = role.Villager()
	r2 = role.Mafia()
	r3 = role.Doctor()
	r4 = role.Villager()

	roles = [r1, r2, r3, r4]

	# random assignment of roles
	p1 = Player("andrew", r1)
	p2 = Player("tim", r2)
	p3 = Player("aylmer", r3)
	p4 = Player("kaelan", r4)

	players = {"andrew": p1, "tim":p2, "aylmer":p3, "kaelan":p4}

	game = GameState(number_of_players=4, roles=roles, players=players)


#------------TESTING PURPOSES

r1 = role.Villager()
r2 = role.Mafia()
r3 = role.Doctor()
r4 = role.Villager()

roles = [r1, r2, r3, r4]

# random assignment of roles
p1 = Player("andrew", r1)
p2 = Player("tim", r2)
p3 = Player("aylmer", r3)
p4 = Player("kaelan", r4)

players = {"andrew": p1, "tim":p2, "aylmer":p3, "kaelan":p4}

game = GameState(number_of_players=4, roles=roles, players=players)