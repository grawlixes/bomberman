from subprocess import call

for x in range(1050):
	input = open("input.txt", 'w')
	input.write("Too much agrement kills a chat.\n0 1 1 2 3 5\n1 y 771\n0 0 BearCat\n5 115\n3 5 4 6 2 1\n")
	input.write(str(x))
	input.close()
	print("Trial #: " + str(x))
	call(["./bomb", "input.txt"])
	print("\n")

