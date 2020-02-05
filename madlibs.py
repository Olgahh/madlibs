def main():
	print('Mad libs where libs get mad.\n\nStart below:')
	time = input("Enter a number from 0 to 12: ")
	item = input("Enter a noun: ")
	name = input("Enter a name: ")
	scream = input("Enter any sentence: ")
	action = input("Enter an action: ")

	print("The story goes ...\n\n")

	print("""It was {} o'clock when I heard a knock on the door.\nI opened the door and there was a box full of {} with a note saying "From Mr. {}." \nJust as I closed the door I heard a scream "{}" \nI froze in place and all I could do is {} """.format(time,item,name.title(),scream.upper(),action))
	# write your code here



if __name__ == '__main__':
	main()
