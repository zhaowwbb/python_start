import json
import os

DATA_FILE = 'data.json'
def load_data():
    if not os.path.exists(DATA_FILE):
        print(f"Data file '{DATA_FILE}' not found. Starting with empty data.")
        return {}
    with open(DATA_FILE, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            print(f"Error decoding JSON from '{DATA_FILE}'. Starting with empty data.")
            return {}   
        except Exception as e:
            print(f"Error loading data: {e}. Starting with empty data.")
            return {}

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f)  

def print_data(data):
    if not data:
        print("No data found.")
    else:
        for key, value in data.items():
            print(f"{key}: {value}")        

def show_menu():
    print("Menu:")
    print("1. View data")
    print("2. Add/Update data")
    print("3. Delete data")
    print("4. Exit")

def main():
    # print("Hello, World!")
    data = load_data()
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            print_data(data)
        elif choice == "2":
            key = input("Enter key: ")
            value = input("Enter value: ")
            data[key] = value
            save_data(data)
        elif choice == "3":
            key = input("Enter key to delete: ")
            if key in data:
                del data[key]
                save_data(data)
            else:
                print("Key not found.")
        elif choice == "4":
            break
        else:
            print("Invalid choice.")
if __name__ == "__main__":
    main()