import math
import os

OP_CODE ={"ADD":"18", "AND":"40", "COMP":"28", "DIV":"24", "J":"3C", "JEQ":"30", "JGT":"34", "JLT":"38", "JSUB":"48", \
"LDA":"00", "LDCH":"50", "LDL":"08", "LDX":"04", "MUL":"20", "OR":"44", "RD":"D8", "RSUB":"4C", "STA":"0C", "STCH":"54",\
 "STL":"14", "STSW":"E8", "STX":"10", "SUB":"1C", "TD":"E0", "TIX":"2C", "WD":"DC"}

def set_loc_counter(lines, out_file):

	for line in lines:	
		line = line.upper()
		line_sections = line.split("	")

		if line_sections[1] == "START":
			prog_name = line_sections[0]
			Start_add = format(int(line_sections[2][:-1]), '06x')
			loc_add = Start_add
			print(Start_add, "{0: <6}".format(prog_name), "{0: <5}".format(line_sections[1]), "{0: <6}".format(Start_add))
			output = Start_add + "\t" + "{0: <6}".format(prog_name) + "\t" + "{0: <5}".format(line_sections[1]) + "\t" + "{0: <6}".format(Start_add)+ "\n"
			out_file.write(output)
			
		elif line_sections[1] == "END":
			print(loc_add, "{0: <6}".format(line_sections[0]), "{0: <5}".format(line_sections[1]), "{0: <6}".format(Start_add))
			output = loc_add + "\t" + "{0: <6}".format(line_sections[0]) + "\t" + "{0: <5}".format(line_sections[1]) + "\t" + "{0: <6}".format(Start_add)+ "\n"
			out_file.write(output)
			return
			
		elif line_sections[1] == "RESW":
			print(loc_add, "{0: <6}".format(line_sections[0]), "{0: <5}".format(line_sections[1]), "{0: <6}".format(line_sections[2][:-1]), "\t", "no obj. code")
			loc_add = format(int(line_sections[2])*3 + int(loc_add, 16), '06x')
			output = loc_add + "\t" + "{0: <6}".format(line_sections[0]) + "\t" + "{0: <5}".format(line_sections[1]) + "\t" + "{0: <6}".format(line_sections[2][:-1])+ "\n"
			out_file.write(output)

		elif line_sections[1] == "RESB":
			print(loc_add, "{0: <6}".format(line_sections[0]), "{0: <5}".format(line_sections[1]), "{0: <6}".format(line_sections[2][:-1]), "\t", "no obj. code")
			loc_add = format(int(line_sections[2]) + int(loc_add, 16), '06x')
			output = loc_add + "\t" + "{0: <6}".format(line_sections[0]) + "\t" + "{0: <5}".format(line_sections[1]) + "\t" + "{0: <6}".format(line_sections[2][:-1])+ "\n"
			out_file.write(output)

		elif line_sections[1] == "BYTE":
			if line_sections[2][0] == "X":
				print(loc_add, "{0: <6}".format(line_sections[0]), "{0: <5}".format(line_sections[1]), "{0: <6}".format(line_sections[2][:-1]), "\t", line_sections[2][2:-2])
				loc_add = format(int(math.ceil(len(line_sections[2][2:-2])/2)) + int(loc_add, 16), '06x')
				output = loc_add + "\t" + "{0: <6}".format(line_sections[0]) + "\t" + "{0: <5}".format(line_sections[1]) + "\t" + "{0: <6}".format(line_sections[2][:-1])+ "\n"
				out_file.write(output)

			elif line_sections[2][0] == "C":
				print(loc_add, "{0: <6}".format(line_sections[0]), "{0: <5}".format(line_sections[1]), "{0: <6}".format(line_sections[2][:-1]), "\t", ''.join(str(format(ord(c),'x')) for c in line_sections[2][2:-2]))
				loc_add = format(int(len(line_sections[2][2:-2])) + int(loc_add, 16), '06x')
				output = loc_add + "\t" + "{0: <6}".format(line_sections[0]) + "\t" + "{0: <5}".format(line_sections[1]) + "\t" + "{0: <6}".format(line_sections[2][:-1])+ "\n"
				out_file.write(output)

		elif line_sections[1] == "WORD":
			print(loc_add, "{0: <6}".format(line_sections[0]), "{0: <5}".format(line_sections[1]), "{0: <6}".format(line_sections[2][:-1]), "\t", format(int(line_sections[2][:-1]), '06x'))
			loc_add = format(int(loc_add, 16) + 3, '06x')
			output = loc_add + "\t" + "{0: <6}".format(line_sections[0]) + "\t" + "{0: <5}".format(line_sections[1]) + "\n"
			out_file.write(output)

		else:
			print(loc_add, "{0: <6}".format(line_sections[0]), "{0: <5}".format(line_sections[1]), "{0: <6}".format(line_sections[2][:-1]))
			loc_add = format(int(loc_add, 16) + 3, '06x')
			output = loc_add + "\t" + "{0: <6}".format(line_sections[0]) + "\t" + "{0: <5}".format(line_sections[1]) + "\t" + "{0: <6}".format(line_sections[2][:-1])+ "\n"
			out_file.write(output)


def sym_table():
	pass


def obj_code(lines):
	for line in lines:	
		line_sections = line.split("	")


def sic_assembler(name):
	with open(name) as f:
		lines = f.readlines()
		# line_num = len(lines)
		with open(name+"pass1", "w") as fp1:
			set_loc_counter(lines, fp1)
			fp1.close()
		
		f.close()


def main():
	while(1):
		try:
			os.system("clear")
		except:
			os.system("cls")

		print("\t \t \tWELCOME TO SIC ASSEMBLER \n")
		print("1) Translate assembly program to SIC object code")
		print("0) EXIT")
		c = int(input("Please, Enter your choice: "))

		if c == 1 :
			c = input("Please, Enter Assembly code file name: ")
			input()
		elif c == 0:
			break
	

# main()
sic_assembler("inSIC.txt")