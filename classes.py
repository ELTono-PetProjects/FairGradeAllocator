
class Project:
	"""
	Class to represent a Project object. It stores name, number of memebers and team members.
	"""
	def __init__(self, name, n_members, team_members):
		"""
		Args:
			name (str): Name of the project.
			n_members (int): Number of members in the project.
			team_members (dict): A dictionary where the keys are the team member's name (str) and
								 the values correspond to the Person object of that member.
		"""
		self._name = name
		self._n_members = n_members
		self._team_members = team_members
		self._point_allocation = {}

	@property
	def name(self):
		return self._name
	
	@name.setter
	def name(self, value):
		self._name = name

	@property
	def n_members(self):
		return self._n_members
	
	@n_members.setter
	def n_members(self, value):
		self._n_members = value

	@property
	def team_members(self):
		return list(self._team_members.keys())

	def calculate_point_allocation(self):
		"""
		Obtain the final share of the score for each member in the project.
		"""

		for member in self.team_members.values():
			teammate_ratio = []
			for teammate in [self.team_members[teammates] 
							 for teammates in self.team_members 
							 if teammates != member.name]:

				other_teammate_name = [name for name in teammate.votes.keys() if name != member.name][0]
				teammate_ratio.append(teammate.votes[other_teammate_name]/teammate.votes[member.name])
			self.point_allocation[member.name] = int(100 / (1 + sum(teammate_ratio)))

			
class Person:
	"""
	Person object containing its name and votes to his teammates.
	"""
	def __init__(self, name, votes):
		"""
		Args:
			name (str): Name of the person
			votes (dict): A dictionary, where the keys correspond to the team member's name (str) and
						  the values to the score (int) the person gave to that teammate.
		"""
		self.name = name
		self.votes = votes

	def get_vote(self, person_name):
		"""
		Get the score given to that person.

		Args:
			person_name (str): Name of the teammate.

		Returns:
			int: Score given to the teammate.
		"""
		if str(person_name) not in self.votes:
			return print("That member is not in this project")
		else:
			return self.votes[person_name]

if __name__ == "__main__":

	print("hola")

