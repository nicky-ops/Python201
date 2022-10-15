with open('writing_files.txt', 'w') as file:
    file.write("Hello from Python 201")

#Append to an existing file
with open("writing_files.txt", 'a') as file:
    file.write("\nA second line")
    file.write("\n\tThis is tabbed!")