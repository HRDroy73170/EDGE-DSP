def add_mountain(mountain_list):
    name = input("Enter mountain name: ").strip()
    while True:
        height = input("Enter mountain height (in meters): ").strip()
        if height.isdigit() and int(height) > 0:
            break
        print("Please enter a valid positive number for height.")
    area = input("Enter mountain area: ").strip()
    location = input("Enter mountain location: ").strip()
    mountain = {
        "name": name,
        "height": height,
        "area": area,
        "location": location
    }
    mountain_list.append(mountain)
    try:
        with open("mountains.txt", "a") as file:
            file.write(f"{name},{height},{area},{location}\n")
        print("Mountain added successfully!")
    except IOError as e:
        print(f"Error saving mountain to file: {e}")

def view_mountains(mountain_list):
    if not mountain_list:
        print("No mountains to display.")
    else:
        for i, mountain in enumerate(mountain_list, start=1):
            print(f"{i}. Name: {mountain['name']}, Height: {mountain['height']} m, Area: {mountain['area']}, Location: {mountain['location']}")

def search_mountain(mountain_list):
    search_name = input("Enter the name of the mountain to search for: ").strip()
    for mountain in mountain_list:
        if mountain['name'].lower() == search_name.lower():
            print(f"Name: {mountain['name']}, Height: {mountain['height']} m, Area: {mountain['area']}, Location: {mountain['location']}")
            return
    print("Mountain not found.")

def edit_mountain(mountain_list):
    if not mountain_list:
        print("No mountains to edit.")
        return
    view_mountains(mountain_list)
    try:
        choice = int(input("Enter the number of the mountain to edit: ")) - 1
        if 0 <= choice < len(mountain_list):
            mountain = mountain_list[choice]
            mountain['name'] = input(f"Enter new name (current: {mountain['name']}): ").strip() or mountain['name']
            mountain['height'] = input(f"Enter new height (current: {mountain['height']}): ").strip() or mountain['height']
            mountain['area'] = input(f"Enter new area (current: {mountain['area']}): ").strip() or mountain['area']
            mountain['location'] = input(f"Enter new location (current: {mountain['location']}): ").strip() or mountain['location']
            update_file(mountain_list)
            print("Mountain updated successfully!")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Please enter a valid number.")

def delete_mountain(mountain_list):
    if not mountain_list:
        print("No mountains to delete.")
        return
    view_mountains(mountain_list)
    try:
        choice = int(input("Enter the number of the mountain to delete: ")) - 1
        if 0 <= choice < len(mountain_list):
            mountain_list.pop(choice)
            update_file(mountain_list)
            print("Mountain deleted successfully!")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Please enter a valid number.")

def update_file(mountain_list):
    try:
        with open("mountains.txt", "w") as file:
            for mountain in mountain_list:
                file.write(f"{mountain['name']},{mountain['height']},{mountain['area']},{mountain['location']}\n")
    except IOError as e:
        print(f"Error updating file: {e}")

def load_mountains():
    mountain_list = []
    try:
        with open("mountains.txt", "r") as file:
            for line in file:
                try:
                    name, height, area, location = line.strip().split(",")
                    mountain_list.append({
                        "name": name,
                        "height": height,
                        "area": area,
                        "location": location
                    })
                except ValueError:
                    print(f"Skipping malformed line: {line.strip()}")
    except FileNotFoundError:
        print("No mountains file found. Starting fresh.")
    return mountain_list

def main():
    mountain_list = load_mountains()
    while True:
        print("\n1. Add Mountain")
        print("2. View Mountains")
        print("3. Search Mountain")
        print("4. Edit")
        print("5. Delete Mountain")
        print("6. Exit")
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                add_mountain(mountain_list)
            elif choice == 2:
                view_mountains(mountain_list)
            elif choice == 3:
                search_mountain(mountain_list)
            elif choice == 4:
                edit_mountain(mountain_list)
            elif choice == 5:
                delete_mountain(mountain_list)
            elif choice == 6:
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
