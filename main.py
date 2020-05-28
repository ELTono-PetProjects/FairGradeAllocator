import utils
from classes import Project, Person

project_dict = {}

def main():
	
	option = print_menu()

	if option == "A":
		option_A()
	elif option == "C":
		option_C()
	elif option == "Q":
		option_Q()
	elif option == "V":
		option_V()
	else:
		option_S()

def print_menu():

	print("\nWelcome to Split-it\n")
	print("\t About \t\t (A)")
	print("\t Create Project  (C)")
	print("\t Enter Votes \t (V)")
	print("\t Show Projects \t (S)")
	print("\t Quit \t\t (Q)\n")
	
	return utils.get_menu_option()

def option_A():
	"""
	Print description of the tool
	"""
	print("""
		  This application is a fair grade allocator to help teams
		  correctly assign how much effort every team member did
		  """)
	main()

def option_C():
	"""
	This function allows the user to create a new project. 
	"""
	project_name = str(input("\nEnter the project name: "))
	number_members = utils.get_number_members()
	members = {}
	for i in range(number_members):
		member_name = str(input("\t Enter the name of team member {}: ".format(i+1)))
		members[member_name] = Person(member_name, {})

	project_dict[project_name] = Project(project_name, number_members, members)

	main()

def option_V():
	"""
	This option allows the user to record the votes for the project.
	"""
	project_name = str(input("\nEnter the project name: "))
	project = project_dict[project_name]
	print("There are {} team members".format(project.n_members))
	for member in project.team_members.values():
		while True:
			print("\n\tEnter {}'s votes, points must add up to 100:".format(member.name))
			for team_member in project.get_members_name():
				if team_member != member.name:	
					points = utils.get_score(member.name, team_member)
					member.votes[team_member] = points
			
			if sum(member.votes.values()) != 100:
				print("\t\tError!!! The points must add up to 100.")
				continue
			else:
				break

	project.calculate_point_allocation() 
				
	main()


def option_S():
	"""
	Show project point allocation to the user.
	"""
	project_name = input("\nEnter the project name: ")
	project = project_dict[project_name]
	print("There are {} team members \n".format(project.n_members))
	print("The point allocation based on votes is:")

	for member in project.team_members:
		print("\t{}: {}".format(member, project.point_allocation[member]))

	main()

def option_Q():
	quit()


if __name__ == '__main__':
	main()