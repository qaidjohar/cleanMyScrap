##################################################################
# Script: cleanMyScrap.py
#
# Author: Qaidjohar Jawadwala
# Email: qaidjawadwala[at]gmail[dot]com
#
# Description: This script moves unused directories and files to a Temp directory
#
# How to Run: python cleanMyScrap.py
#
##################################################################

import shutil	#Moving files and Derectories
import time		#Performing time related functions 
import os		#Performing OS functions

if __name__ == "__main__":
	#Accepting source directory input from the user
	source = raw_input("Enter Source Directory Path: ")
	#setting output directory as a Temp folder in source directory
	output = source+"/Temp"
	#Checking if the Source Directory entered by the user exists
	if os.path.isdir(source):
		#Checking for Temp directory in the source directory
		if not os.path.exists(source+"/Temp"):
			print "Creating a Temp directory..."
			#Creating a Temp Directory
			os.makedirs(source+"/Temp")
		else:
			print "Temp directory exists. Using the Existing Temp directory."
		flag = 0
		while flag == 0:
			try:
				#Accepting a threshold value for timestamp of the files to be transferred to Temp directory
				threshold = int(raw_input("Enter the threshold values for the files in days (Ex. 45): "))
				flag = 1
			except:
				print "Invalid value entered. Value should be an Integer. Please try again..."
		#Taking the current system time
		current_time = time.time()
		count = 0
		print "Total available Directories and Files: "+str(len(os.listdir(source)))
		#loop for all the files in the source directory
		for files in os.listdir(source):
			#checking the files for list modified time
			if os.stat(source+"/"+files).st_mtime < (current_time - threshold*86400):
				#moving files to Temp directory
				shutil.move(source+"/"+files,output)
				count += 1
		print "Total Directories and Files moved to Temp are "+str(count) 		
	else:
		print "Invalid directory path entered. Please try again using a valid directory path."
		print "Path to you Home directory:: "+ str(os.path.expanduser('~'))
