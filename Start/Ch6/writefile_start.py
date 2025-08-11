# LinkedIn Learning Python course by Joe Marini
# write files using the built-in Python file methods


# Open a file for writing and create it if it doesn't exist
create_f=open("new_text_file.txt","w+")

# Open the file for appending text to the end


# write some lines of data to the file
contents="this is a new text"
create_f.write(contents)
create_f.close()
create_f=open("new_text_file.txt", "a+")
create_f.write("some additional")
# close the file when done
create_f.close()
