import hashlib
salt = b'mLy$zxVbn37hyG43875'

def main():
    while True:
        choice = input("1. Set the key to hash\n2. Encrypt a message\n3. Decrypt a message\n4. Brute force\n5. Exit\n\nEnter your choice: ")
        match choice:
            case "1":
                hash_key()
            case "2":
                encrypt_message()
            case "3":
                decrypt_message()
            case "4":
                brute_force()
            case "5":
                print("Exiting the program...")
                break
            case _:
                print("Invalid choice.\n")
        
def hash_key():
    filename = "hashed_key.txt"
        
    while True:
        try:
            data_to_write = int(input("Enter a key (1-25) for your Caesar cipher: "))
            if 1 <= data_to_write <= 25:
                break
            else:
                print("Invalid input. Please enter an integer between 1 and 25.")
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

    hashed_key = hashlib.sha256(str(data_to_write).encode('utf-8') + salt).hexdigest()
    
    with open(filename, "w") as f:
           f.write(hashed_key)
        
    print(f"{filename} set successfully.\n")

def dehash_key():
    try:
        with open("hashed_key.txt", "r") as f:
            hashed_key_str = f.read()
            hashed_key = bytes.fromhex(hashed_key_str)
            
            key_candidate = 1
            while True:
                hashed_candidate = hashlib.sha256(str(key_candidate).encode('utf-8') + salt).hexdigest()
                if bytes.fromhex(hashed_candidate) == hashed_key:
                    return key_candidate
                key_candidate += 1
    except FileNotFoundError:
        print("Key file not found. Please set the key first.\n")
        return None
        
def encrypt_message():
    key = dehash_key()
    answer = ""
    if key:
        message = input("Enter the message you want to encrypt: ")
        if message != "":  
            for i in range(len(message)):
                ch = message[i]
                if ch==" ":
                    answer+=" "
                elif (ch.isupper()):
                    answer += chr((ord(ch) + key-65) % 26 + 65)
                    
                elif (ch.islower()):
                    answer += chr((ord(ch) + key-97) % 26 + 97)
                    
                else:
                    answer += ch
                
            return print(f"'{message}' encrypted with the selected key is '{answer}'\n")
        else: encrypt_message()
    else: return

def decrypt_message():
    key = dehash_key()
    answer = ""
    if key:
        message = input("Enter the message you want to decrypt: ")
        letters="abcdefghijklmnopqrstuvwxyz"
        if message != "":
            for ch in message:

                if ch.isupper():
                    if ch.lower() in letters:
                        position = letters.find(ch.lower())
                        new_pos = (position - key) % 26
                        new_char = letters[new_pos]
                        answer += new_char.upper()
                elif ch.islower():
                    if ch in letters:
                        position = letters.find(ch)
                        new_pos = (position - key) % 26
                        new_char = letters[new_pos]
                        answer += new_char
                else:
                    answer += ch
            return print(f"'{message}' decrypted with the selected key is '{answer}'\n")
        else: decrypt_message()
    else: return

def brute_force():
    message = input("Enter the message you want to brute force: ")
    letters="abcdefghijklmnopqrstuvwxyz"
    
    for key in range(1, 26):
        answer = ""
        for ch in message:
            if ch.isupper():
                if ch.lower() in letters:
                    position = letters.find(ch.lower())
                    new_pos = (position - key) % 26
                    new_char = letters[new_pos]
                    answer += new_char.upper()
            elif ch.islower():
                if ch in letters:
                    position = letters.find(ch)
                    new_pos = (position - key) % 26
                    new_char = letters[new_pos]
                    answer += new_char
            else:
                answer += ch
        print(f"'{message}' decrypted with the key {key} is '{answer}'")
    print("Brute force complete.\n")

if __name__ == "__main__":
    main()