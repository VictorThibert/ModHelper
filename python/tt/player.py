
# base class for a player

# ---------------------------------------------------------------------------------------------

import role

class Player:
	def __init__(self, name, role):
		self.name = name
		self.alive_status = True 
		self.role = role
		self.item = None
		self.protected_for = 0
		self.alignment = role.alignment
		self.perceived_alignment = role.perceived_alignment

	def set_role(self, role):
		self.role = role
		self.set_alignment(role.alignment)
		self.set_perceived_alignment(role.perceived_alignment)

	def set_alignment(self, alignment):
		self.alignment = alignment

	def set_perceived_alignment(self, perceived_alignment):
		self.perceived_alignment = perceived_alignment

	def kill(self):
		print(self.name, "is killed")
		self.alive_status = False

	def modkill(self):
		self.kill()

	def protect(self, number_of_turns):
		self.protected_for = number_of_turns

	def detect(self):
		return self.perceived_alignment

	def advance_turn(self): # temprorary ==============

		# decrement protection status
		self.protected_for = max(0, self.protected_for - 1) 

	def is_alive(self):
		return self.alive_status

	def __str__(self):
		return "Name: {} \nIs alive: {} \nRole: {} \nItems: {}".format(self.name, self.alive_status, self.role.name, self.item)