# create a function called draw_stars() that takes a list of numbers and prints out *.
# a program should display the number of * 

#part 1

x= [4, 6, 1, 3, 5, 7, 25]
def draw_star(num_list):
	for num in num_list:
		print num*"*"
draw_star(x)

	

# part 2

y= [4,'Tom',1,'Michael',5,7,'Jimmy Smith']
def draw_star(my_list):
	for item in my_list:
		output = ''
		if type(item) is int:
			for i in range(item):
				output += '*'
		if type(item) is str:
			
			for i in range(len(item)):
				first_letter = item[0].lower()
				output += first_letter
		print output

draw_star(y)











