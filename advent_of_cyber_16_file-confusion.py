# Prompt: Use a (python) script to do the following:
# 1. extract all the files in the archives 
# 2. extract metadata from the files 
# 3. extract text from the files

#Answer the following questions:

# 1. How many files did you extract(excluding all the .zip files)
# 2. How many files contain Version: 1.1 in their metadata?
# 3. Which file contains the password?


# Assumption is we are working with the unzipped downloaded file from TryHackMe

# Import libraries to zip/unzip files and to read/capture metadata from said files
import os, zipfile
# Define variables to serve as counters for the number of files and number of files containing Version: 1.1 metadata
num_files = 0
num_meta = 0

# Create output directory 
if not os.path.exists("output"):
    os.mkdir("output")

# Loop through each subfolder
# os.walk() generates a 3-tuple for each directory it finds containing dirpath, dirnames, and filenames 
for dirpath, dirnames, files in os.walk('.'):
    for file_name in files:
        if file_name.endswith('.zip'):
            print(file_name)
            # zipped files can start being interacted with here
        else:
            # Ignore files that don't have .zip extension
            continue

# Increment the number of files variable for each file unzipped
# Extract the metadata of each file
# Increment the metadata variable for each file containing Version 1.1; otherwise continue the loop
# Print the values for both the number of files and metadata variable at the end of the loop
# Include a separate function to search for and display the file containing any resemblance of a password
