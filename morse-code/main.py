#This program takes a message in English as user input and translates it into Morse Code.


#Morse code dictionary with spaces built in at the end of each letter
morse_dict = {
    "a": "·− ", "b": "−··· ", "c": "−·−· ",
    "d": "−·· ", "e": "· ", "f": "··−· ",
    "g": "−−· ", "h": "···· ", "i": "·· ",
    "j": "·−−− ", "k": "−·− ", "l": "·−·· ",
    "m": "−− ", "n": "−· ", "o": "−−− ",
    "p": "·−−· ", "q": "−−·− ", "r": "·−· ",
    "s": "··· ", "t": "− ", "u": "··− ",
    "v": "···− ", "w": "·−− ", "x": "−··− ",
    "y": "−·−− ", "z": "−−·· ",
    ".": " ·−·−·− ", "!": "−·−·−−", "?": "··−−·· ",
    "1": "·−−−− ", "2": "··−−− ", "3": "···−− ",
    "4": "····− ", "5": "····· ", "6": "−···· ",
    "7": "−−··· ", "8": "−−−·· ", "9": "−−−−· ",
    "0": "−−−−− ",
    '"': "·−··−· ", ":": "−−−··· ", "'": "·−−−−· ",
    "-": "−····− ", "/": "−··−· ", "(": "−·−−· ",
    ")": "−·−−·− "
}

#USER MESSAGE
text = input("Enter your message:\n")
print(f"You entered: \n {text}")
text = text.lower()

#CREATE AN EMPTY STRING FOR THE ENCODED MESSAGE
message = ''

#LOOP THROUGH EACH LETTER IN THE MESSAGE AND PAIR IT WITH LETTERS IN DICTIONARY
for letter in text:
    if letter != ' ':
        message += morse_dict[letter]
    else:
        message += ' '

print(f"Your message in Morse Code: \n {message}")