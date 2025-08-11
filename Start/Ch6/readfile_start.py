#
# Read and write files using the built-in Python file methods
# LinkedIn Learning Python course by Joe Marini
#

    
# Open the file and read the contents

    # use the read() function to read the entire file
file_r=open("new_text_file.txt","r")
print(file_r.read())
file_r.close()