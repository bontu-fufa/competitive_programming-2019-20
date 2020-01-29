# isosceles triangle pattern with asterisk
size = 3
def space_generator(size):
	for column in range(size):
		print(" ",end="")
def star_generator(size):
	for column in range(size):
		print("*",end="")

for row in range(size):
	space_size = size-row
	space_generator(space_size)
	star_size= row*2+1
	star_generator(star_size)
	print()

