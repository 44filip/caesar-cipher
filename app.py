def main():
    while True:
        choice = input("1. Set the key\n2. Encrypt a message\n3. Decrypt a message\n4. Exit\n\nEnter your choice: ")
        match choice:
            case "1":
                set_key()
            case "2":
                print()
            case "3":
                print()
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
        
    print(f"File {filename} created successfully.\n")
        
if __name__ == "__main__":
    main()