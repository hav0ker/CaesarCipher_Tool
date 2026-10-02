abcd = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
output = []

choice = input("Type D for decryption or E for encryption: ").strip().upper()
key = int(input("Choose key(numbers 1-25): "))

if key < 1 or key > 26:
    raise SystemExit("Invalid key!!!")

text = input("Enter the text: ").strip()

def Encrypt(text):
    for letter in text:
        if letter in abcd:
            get_letter = (abcd.index(letter) + key * 2) % 52
            output.append(abcd[get_letter])
        else:
            output.append(letter)
    print("".join(output))
    
def Decrypt(text):
    for letter in text:
        if letter in abcd:
            get_letter = (abcd.index(letter) - key * 2) % 52
            output.append(abcd[get_letter])
        else:
            output.append(letter)
    print("".join(output))

if choice == "E":
    Encrypt(text)    
elif choice == "D":
    Decrypt(text)
else:
    raise SystemExit("Invalid character")