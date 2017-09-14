
# base class for all roles
# figure out priorities 

# ---------------------------------------------------------------------------------------------

import player 

class Role:
	def __init__(self, name, description, priority, alignment, action):
		self.name = name
		self.description = description
		self.priority = priority
		self.alignment = alignment
		self.action = action

	def __str__(self):
		return "Name: {} \nDescription: {} \nPriority: {} \nAlignment: {}".format(self.name, self.description, self.priority, self.alignment)

	def perform_action(self, gamestate):
		self.action(gamestate)

# ---------------------------------------------------------------------------------------------

class Evil(Role):
	def __init__(self, name, description, priority, action):
		super().__init__(name, description, priority, 1, action) # for now, alignment 1 means evil

class Good(Role):
	def __init__(self, name, description, priority, action):
		super().__init__(name, description, priority, 0, action) # for now, alignment 0 means good

# ---------------------------------------------------------------------------------------------

class Mafia(Evil):
	def action(self, gamestate):
		print("I am mafia")

	def __init__(self):
		super().__init__(name="mafia", description="Together, the mafia get to choose one kill per night.", priority=10, action=self.action) # arbitrary priority for now

class Villager(Good):
	def action(self, gamestate):
		print("I am villager")

	def __init__(self):
		super().__init__(name="villager", description="Have no power.", priority=0, action=self.action)

class Doctor(Good):
	def action(self, gamestate):
		target = input("Who would you like to protect?")
		gamestate.protect_player(target, 1)
		print("Doctor has chosen to protect: ", target)

	def __init__(self):
		super().__init__(name="doctor", description="Chooses one person per night to protect. Cannot choose the same person twice in a row. ", priority=15, action=self.action)

class Detective(Good):
	def action(self):
		print("I am detective")

	def __init__(self):
		super().__init__(name="detective", description="Investigates a player at night to figure out their alignment.", priority=5, action=self.action)
