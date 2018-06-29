#Encoding UTF-8

#connected modules
import os
import sys
import psutil
import time 

print("+---------------------+")
print("| Console Healper 1.0 |")
print("+---------------------+")
name = input(" Enter your username: ")
print(" Welcome, ", name)

ans = ''

while ans != 'n':
	ans = input(" Would you like to continue? ('y' - YES; 'n'/'q' - QUIT): ")
	if ans == 'y':
		#if_yes()
		print(" Great! Choose what to do: ")
		print(" [1] - show current directory and files")
		print(" [2] - show system info")
		print(" [3] - show current processes IDs")
		print(" [4] - execute a command or an external script in a subshell")
		choice = int(input(" Enter 1/2/3/4: "))
		if choice == 1:
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
			print(" Enter a command or path to program: ")
			os.system(input())
		else:
			pass
					
	elif ans == 'q' or 'n':
		ans = 'n'
		#if_no()
		#input("Press any key to exit: ")
		#termination():
		print("Termination...")
		time.sleep(2)
		print("Goodbye!")
		time.sleep(1)
		
	else:
		#if_undef()
		print("Undefined choice. Retry next time.")
		#termination():	
		print("Termination...")
		time.sleep(2)
		print("Goodbye!")
		time.sleep(1)
