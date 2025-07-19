# file_handling.py

# 1. Writing to a file
with open("notes.txt", "w") as file:
    file.write("Hey Suren,\n")
    file.write("Welcome to the AI WORLD!\n")
    file.write("This is a sample file created using Python.\n")

print("File written successfully.")

# 2. Reading from the file
with open("notes.txt", "r") as file:
    content = file.read()

print("\n--- File Content ---")
print(content)
