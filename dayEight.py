
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caeser(direction, text, shift):
    end_text =  ""
    if direction =="decode":
        shift *= -1
    for letter in text: 
        if letter not in alphabet:
            end_text += letter
        else: 
            position = alphabet.index(letter)
            new_position = position + shift
            end_text += alphabet[new_position]
    print(f"Her's the {direction}d results: {end_text}")

new_shift = shift%26
print(new_shift)


caeser(direction=direction,text=text, shift=new_shift)