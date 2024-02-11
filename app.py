def main():
    while True:
        choice = input("1. Set the key\n2. Encrypt a message\n3. Decrypt a message\n4. Exit\n\nEnter your choice: ")
        match choice:
            case "1":
                set_key()
            case "2":
                encrypt_message()
            case "3":
                decrypt_message()
            case "4":
                print("Exiting the program...")
                break
            case _:
                print("Invalid choice.\n")
        
def set_key():
    filename = "key_file.txt"
    data_to_write = None
        
    while isinstance(data_to_write, int) is False or not (1 <= data_to_write <= 25):
        try:
            data_to_write = int(input("Enter a key (1-25) for your Caesar cipher: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
        
    with open(filename, "w") as f:
           f.write(str(data_to_write))
        
    print(f"{filename} set successfully.\n")
        
def encrypt_message():
    message = input("Enter the message you want to encrypt: ")
    answer = ""
    key = None
    try:
        with open("key_file.txt", "r") as f:
            key_str = f.read()
            key = int(key_str)
    except FileNotFoundError:
        print("Error: Key file not found. Please set the key first.")
        return None
    
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
    print()

if __name__ == "__main__":
    main()