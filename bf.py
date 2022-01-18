import time

#string that stores the code
src = "+++++[>+++++[>++++>++++<<-]>+++>+<<<-]>>.>...<++......."

#size of the data array
array_length = 30000

#data array
array = [0] * array_length
#pointer that keeps track of the active cell of the array
pointer = 0

#set to 1 to print out additional info while interpreting the code and to sleep for .5s between every command
info = 0

def interpret_bf(pointer, array, input):
	x = 0
	while x < len(input):
		if input[x] == "+":
			if info == 1:
				print("+ -> add 1 to cell", pointer)
			array[pointer] += 1
			if array[pointer] > 255:
				array[pointer] = 0

		elif input[x] == "-":
			if info == 1:
				print("- -> substract 1 from cell", pointer)
			array[pointer] -= 1
			if array[pointer] < 0:
				array[pointer] = 255
		
		elif input[x] == ">":
			if info == 1:
				print("> -> increase pointer by 1")
			pointer += 1
			if pointer >= array_length:
				pointer = 0
		
		elif input[x] == "<":
			if info == 1:
				print("< -> decrease pointer by 1 to ", pointer - 1)
			pointer -= 1
			if pointer < 0:
				pointer = array_length - 1
		
		elif input[x] == "[":
			if info == 1:
				print("[ -> start a loop")

			temp = array[pointer]
			
			#variable that stores the code that should be looped
			looped_code = ""

			#first pos in loop
			start_pos = x + 1

			loop_length = 0

			#counts how many loops are inside of the current loop
			loop_counter = 0

			#searches the next ], adds all the commands before it to looped_code and sets loop_length
			for b in range(len(input) - start_pos):
				#increases loop_counter if the start of an inner loop is found
				if input[start_pos + b] == "[":
					loop_counter += 1

				if input[start_pos + b] == "]":
					if loop_counter == 0:
						break
					#decreases loop_counter if the end of an inner loop is found
					else:
						loop_counter -= 1
				looped_code += input[start_pos + b]
				loop_length = b + 1
			
			#executes the code inside of the loop as long as temp > 0
			while array[pointer] > 0:
				interpret_bf(pointer, array, looped_code)

			#jumps to the end of the loop, so that the looped code wont be executed again
			x += loop_length

		elif input[x] == "]":
			if info == 1:
				print("] -> end of loop")
			pass
		
		elif input[x] == ".":
			if info == 1:
				print(". -> print cell", pointer)
			print(chr(array[pointer]), end="")
		
		elif input[x] == ",":
			if info == 1:
				print(", -> input to cell", pointer)
			pass

		x += 1

		if info == 1:
			time.sleep(.2)

interpret_bf(pointer, array, src)

f = input("")