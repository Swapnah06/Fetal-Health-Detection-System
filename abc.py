def display_results(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.readlines()
        
        if not content:
            print("File is empty.")
        else:
            print("Detection Results:")
            for line in content:
                print(line.strip())
    
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Path to check.txt (Ensure it's in the current working directory)
file_path = "check.txt"
display_results(file_path) # type: ignore