def main():
    while True:
        choice = input("1. Set the key\n2. Encrypt a message\n3. Decrypt a message\n4. Brute Force\n5. Exit\n\nEnter your choice: ")
        match choice:
            case "1":
                set_key()
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
        
def set_key():
    filename = "key_file.txt"
    data_to_write = None
        
    while True:
        try:
            data_to_write = int(input("Enter a key (1-25) for your Caesar cipher: "))
            if 1 <= data_to_write <= 25:
                break
            else:
                print("Invalid input. Please enter an integer between 1 and 25.")
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

    with open(filename, "w") as f:
           f.write(str(data_to_write))
        
    print(f"{filename} set successfully.\n")
        
def encrypt_message():
    key = read_key()
    message = input("Enter the message you want to encrypt: ")
    answer = ""
    
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
    
    return print(f"'{message}' encrypted with the key {key} is '{answer}'\n")
    

def decrypt_message():
    key = read_key()
    message = input("Enter the message you want to decrypt: ")
    answer = ""
    letters="abcdefghijklmnopqrstuvwxyz"

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
    return print(f"'{message}' decrypted with the key {key} is '{answer}'\n")

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
    
def read_key():
    try:
        with open("key_file.txt", "r") as f:
            key_str = f.read()
            key = int(key_str)
    except FileNotFoundError:
        print("Error: Key file not found. Please set the key first.")
        return None
    return key

if __name__ == "__main__":
    main()