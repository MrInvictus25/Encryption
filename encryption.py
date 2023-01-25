#alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet = 'abcdefghijklmnopqrstuvwxyz'
cipher = ''
message = input("Enter your message: ")

for letter in message:
  #is_upper = alphabet.find(letter) == -1 
  is_upper = False
  if alphabet.find(letter) == -1:
    is_upper = True
  if letter.lower() in alphabet: 
    result = alphabet.find(letter.lower())
    #print(result)
    cipher += alphabet[result + 3].upper() if is_upper else alphabet[result + 3] # variable = [case true] if [candition] else [case false]
  else:
    cipher += letter
print(cipher)

