#Encoding UTF-8

#connected modules
import os
import sys
import shutil
import psutil
import time

print("+---------------------+")
print("| Console Healper 1.0 |")
print("+---------------------+")
name = input(" Enter your username: ")
print(" Welcome, ", name)

ans = ''

while ans != 'n':
	print('')
	ans = input(" Would you like to continue? ('y' - YES; 'n'/'q' - QUIT): ")
	if ans == 'y':
		#if_yes()
		print(" Great! Choose what to do: ")
		print(" [0] - Execute a command or an external script in a Subshell")
		print(" [1] - Show current directory and files")
		print(" [2] - Show system info")
		print(" [3] - Show current processes IDs")
#		print(" [4*] - Copying files in necessary directory")
		print(" [4] - Copying all files in current directory")
#		print(" [5] - ")
		choice = int(input(" Enter 0/1/2/3/4: "))
		
		if choice == 0:
			print("S u b S h e l l")
			print(" Enter a command or a path/to/script: ")
			os.system(input())
			
		elif choice == 1:
			print("Current directory: ", os.getcwd())
			print("Files: ", os.listdir())
		
		elif choice == 2:
			print(" S y s t e m   i n f o:")
			print(" Number of processors: ", psutil.cpu_count())
			print(" Platform: ", sys.platform)
			print(" File system encoding: ", sys.getfilesystemencoding())
			print(" Current user: ", os.getlogin())
		
		elif choice == 3:
			print("Current processes IDs: ", psutil.pids())
		
		elif choice == 4:
#			direc = input("Enter a path to files: ")
#			print(direc)
			f_list = os.listdir() #(direc)
			print(f_list)
			print("Copying... ")
			time.sleep(0.5)
			i = 0
			while i < len(f_list):
				if os.path.isfile(f_list[i]):
					newfile = f_list[i]+'.copy'
					shutil.copy(f_list[i], newfile) #copying
					print(i, " - OK")
				i += 1
	
		elif choice == 5:
			print("S u b S h e l l")
			print(" Enter a command or a path/to/script: ")
			os.system(input())
		
		else:
			pass
	
	elif ans == 'q' or 'n':
		ans = 'n'
		#if_no()
		#termination():
		print("Termination...")
		time.sleep(1)
		print("Goodbye!")
		time.sleep(1)
		
	else:
		#if_undef()
		print("Undefined choice. Retry next time.")
		#termination():	
		print("Termination...")
		time.sleep(1)
		print("Goodbye!")
		time.sleep(1)
