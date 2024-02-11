choice = input("Press 1 to set the key\nPress 2 to encrypt a message\nPress 3 to decrypt a message")
match choice:
    case "1":
        filename = "key_file.txt"
        data_to_write = None
        
        while isinstance(data_to_write, int) is False or not (1 <= data_to_write <= 25):
            try:
                data_to_write = int(input("Enter a key (1-25) for your Caesar cipher."))
            except ValueError:
                print("Invalid input. Please enter an integer.")
        
        with open(filename, "w") as f:
           f.write(str(data_to_write))
        
        print(f"File {filename} created successfully.")
    case "2":
        print()
    case "3":
        print()