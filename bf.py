#string that stores the code
src = "+++[>+<-]>."

array = [0] * 30000
pointer = 0

#set to 1 to print out additional info while interpreting the code
info = 1

def aaa(pointer, array, input):
	x = 0
	while x < len(input):
		if input[x] == "+":
			if info == 1:
				print("+ -> add 1 to cell", pointer)
			array[pointer] += 1

		elif input[x] == "-":
			if info == 1:
				print("- -> substract 1 from cell", pointer)
			array[pointer] -= 1
		
		elif input[x] == ">":
			if info == 1:
				print("> -> increase pointer by 1")
			pointer += 1
		
		elif input[x] == "<":
			if info == 1:
				print("< -> decrease pointer by 1")
			pointer -= 1
		
		elif input[x] == "[":
			if info == 1:
				print("[ -> start a loop")

			temp = array[pointer]
			
			#variable that stores the code that should be looped
			looped_code = ""

			#first pos in loop
			start_pos = x + 1

			loop_length = 0

			#searches the next ], adds all the commands before it to looped_code and sets loop_length
			for b in range(len(input) - start_pos):
				if input[start_pos + b] == "]":
					break
				looped_code += input[start_pos + b]
				loop_length = b + 1
			
			#executes the code inside of the loop as long as temp > 0
			while array[pointer] > 0:
				aaa(pointer, array, looped_code)

			#jumps to the end of the loop, so that the looped code wont be executed again
			x += loop_length

		elif input[x] == "]":
			if info == 1:
				print("] -> end of loop")
			pass
		
		elif input[x] == ".":
			if info == 1:
				print(". -> print cell", pointer)
			print(array[pointer])
		
		elif input[x] == ",":
			if info == 1:
				print(", -> input to cell", pointer)
			pass

		x += 1

aaa(pointer, array, src)