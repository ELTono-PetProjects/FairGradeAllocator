
def get_menu_option():
	"""
	Get the menu option selected by the user.
	"""

	while True:
		option = str(input("\tPlease choose an option and press <Enter>: "))
		if option.upper() not in ["A", "C", "V", "S", "Q"]:
			print("\t\tError!!!. Please choose one of the valid options in the program\n")
		else:
			break
	return option.upper()

def get_number_members():
	"""
	Get the number of members in the project inserted by the user. 
	"""
	while True:
		try:
			number_members = int(input("Enter the number of members in the project: "))
		except ValueError:
			print("\tError!!! Please introduce a valid number")
			continue

		if number_members < 1:
			print("\tError!!! The number of members need to be > 0")
		else:
			break
	return number_members

def get_score(member, teammate):
	"""
	Get the score given by the member

	Args:
		member (str): Name of the member giving the vote.
		teammate (str): Name of the memeber receiving that score.

	Returns:
		score (int): The score given to the member.
	"""

	while True:
		try:
			score = int(input("\tEnter {}'s points for {}: ".format(member, teammate)))
		except ValueError:
			print("\tError!!! You need input a valid number")
			continue
		else:
			break

	return score






