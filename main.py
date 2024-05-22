#Caesar Cipher 

#from artwork import logo
#print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_number, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_number *= -1
  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_number
      end_text +=alphabet[new_position]
    else:
      end_text += char
    
  print(f"The {cipher_direction}d text is {end_text}")

should_continue = True
while should_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
    
  shift = shift % 26
  
  caesar(start_text = text, shift_number=  shift, cipher_direction = direction)
  again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if again == "no":
    should_continue = False
    print("Bye-Bye! Have a good day!")