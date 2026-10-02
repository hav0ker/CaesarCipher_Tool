# ℹ️Caesar Cipher Tool
A simple Python implementation of the Caesar cipher: encrypt and decrypt text by shifting letters a fixed number of positions through the alphabet

### How it works

Each letter is replaced by the letter key positions after it in the alphabet, wrapping around from Z back to A.
For example with a key of 3:
Plain:   A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
Cipher:  D E F G H I J K L M N O P Q R S T U V W X Y Z A B C

So HELLO WORLD becomes KHOOR ZRUOG. Decryption shifts each letter back by the same key.

### Implementation detail

The program uses a single string with uppercase and lowercase letters interleaved:


abcd = "AaBbCcDd...Zz"

Because every letter takes up two slots (upper, then lower), moving key * 2 positions shifts a letter by key places while keeping its case. The modulo % 52 handles wrap-around.

### Features
Encrypt and decrypt from one simple prompt-based interface
Preserves uppercase and lowercase letters
Leaves spaces, digits, and punctuation unchanged
No dependencies, just the Python standard library

### Requirements
Python 3.6 or newer

The program asks for a mode, a key, and the text.

### Encrypting:

Type D for decryption or E for encryption: E
Choose key(numbers 1-25): 3
Enter the text: Hello, World!
Khoor, Zruog!

### Decrypting:

Type D for decryption or E for encryption: D
Choose key(numbers 1-25): 3
Enter the text: Khoor, Zruog!
Hello, World!
Limitations
Only the 26 letters of the English alphabet are shifted. Accented and non-Latin characters are left unchanged.
There are only 25 meaningful keys (a key of 26 returns the original text), so the cipher can be broken by trying every shift.
It is also vulnerable to frequency analysis, since letter patterns in the language survive the shift.
