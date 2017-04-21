from subprocess import call

for x in range(721):
	phase6 = open("phase6.txt", 'r')

	input = open("input.txt", 'w')
	input.write("Too much agrement kills a chat.\n0 1 1 2 3 5\n1 y 771\n0 0\n5 115\n")

	if x == 0:
		input.write(phase6.readline())
	elif x == 1:
		phase6.readline()
		input.write(phase6.readline())
	else:
		for y in range(x-1):
			phase6.readline()
		input.write(phase6.readline())
	phase6.close()
	input.close()
	print("Trial #:" + str(x))
	call(["./bomb", "input.txt"])

