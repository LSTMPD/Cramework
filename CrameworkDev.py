from colorama import init
from colorama import Fore, Back, Style
import binascii
import base64
import PizzaCryptDev
init()

print(Fore.CYAN + Style.BRIGHT)

print(" ____________________________  ")
print("/                            \ ")
print("\          Cramework         / ")
print("!             By             ! ")
print("/           LSTMPD           \ ")
print("\____________________________/ ")
print("")
print("1) Base64")
print("2) Hex")
print("3) PizzaCrypt")
print("")

def exitter():
    raw_input("Press Enter to exit")
    quit()

def WritingToFile(string, file, mode):
    try:
        file = open(file, mode)
        file.write(string)
        file.close()
        print("Done! \n")
        exitter()
    except Exception as e:
        print(e)

def WritingKeyToFile(string, file, mode):
    try:
        file = open(file, mode)
        file.write(string)
        file.close()
        print("Done! \n")
        exitter()
    except Exception as e:
        print(e)

        exitter()

def Codebreaker():
    raw_input("Please choose a valid option")
    quit()

selection = raw_input("Which tool would you like to use?: ")
if selection == "1":
    print("")
    print(Fore.YELLOW + Style.BRIGHT + "MODE SELECTION")
    print("1) Encoding")
    print("2) Decoding")
    base64mode = raw_input("Which mode would you like to use?: ")
    if base64mode == "1":
        print("")
        print(Fore.GREEN)
        encoded = base64.b64encode(raw_input("Text to be encoded: "))
        print("")
        WritingToFile(encoded, "output.txt", "w")

    if base64mode == "2":
        print("")
        print(Fore.GREEN)
        decoded = base64.b64decode(raw_input("String to decode: "))
        WritingToFile(decoded, "output.txt", "w")
    else:
        Codebreaker()

if selection == "2":
    print("")
    print(Fore.YELLOW + Style.BRIGHT + "MODE SELECTION")
    print("1) Encoding")
    print("2) Decoding")
    hexmode = raw_input("Which mode would you like to use?: ")

    if hexmode == "1":
        encodedhex = binascii.hexlify(raw_input("String to encode: "))
        print(Fore.GREEN)
        WritingToFile(encodedhex, "output.txt", "w")

    if hexmode == "2":
        decodedhex = binascii.unhexlify(raw_input("String to decode: "))
        print(Fore.GREEN)
        WritingToFile(decodedhex, "output.txt", "w")
    else:
        Codebreaker()

if selection == "3":
    print("")
    print(Fore.YELLOW + Style.BRIGHT + "MODE SELECTION")
    print("1) Encoding")
    print("2) Decoding")
    pizzacmode = raw_input("Which mode would you like to use?: ")

    if pizzacmode == "1":
        data = PizzaCryptDev.encrypt(raw_input("String to encrypt: "))
        print "Key :" + data['key'] + "\n"
        print "Encrypted text: " + data['encrypted']
        WritingToFile("String: " + data['encrypted'] + "\n " + "Key: " + data['key'], "output.txt", "w")
        exitter()



else:
    Codebreaker()
