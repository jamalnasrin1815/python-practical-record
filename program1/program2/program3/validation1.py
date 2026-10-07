password = input("Enter password: ")
# Check strength (only length)
if len(password) >= 8:
 print("Strong Password")
 # Simple encryption (reverse string)
 encrypted = password[::-1]
 # Store in file
 file = open("password.txt", "a")
 file.write(encrypted + "\n")
 file.close()
 print("Encrypted Password:", encrypted)
 print("Saved in file")
else:
 print("Weak Password (minimum 8 characters)")