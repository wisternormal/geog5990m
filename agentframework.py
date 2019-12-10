import random


class Agent:

	"""docstring for Agent"""

# initilize every agents
	def __init__(self,environment,agents,x,y):
		if (y == None):
			self.y = random.randint(0,99)
		else:
			self.y = y
		if (x == None):
			self.x = random.randint(0,99)
		else:
			self.x = x

		self.agents = agents
		self.environment = environment
		self.store = 0 # We'll come to this in a second.


# define tow agents' distance
	def distance_between(self,agent):
	    return ((self.x - agent.x)**2 +(self.y - agent.y)**2)**0.5

# agents communicate with the environment
	def eat(self): 

		if self.environment[self.y][self.x] > 10:
		    self.environment[self.y][self.x] -= 10
		    self.store += 10

# agents move randomly
	def move(self):
		if random.random() < 0.5:
			self.y = (self.y + 1) % 100
		else:
			self.y = (self.y - 1) % 100
		
		if random.random() < 0.5:
			self.x = (self.x + 1) % 100
		else:
			self.x = (self.x - 1) % 100

# agents communicate with each other
	def share_with_neighbours(self,neighbourhood):
		for agent in self.agents:
			distance = self.distance_between(agent)
			if distance <= neighbourhood:
				average = (self.store + agent.store)/2
				self.store,agent.store = average,average


