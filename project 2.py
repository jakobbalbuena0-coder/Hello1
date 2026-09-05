# Pet Adoption Finder
# Jakob Balbuena

print("=== Pet Adoption Finder ===")

# List of pets
pets = ["Buddy", "Luna", "Max", "Bella"]

print("\nAvailable Pets:")

# Display each pet using its index
for i in range(len(pets)):
    print(i + 1, "-", pets[i])

# User chooses a pet
choice = int(input("\nEnter the number of the pet you want: ")) - 1

# Check if the choice is valid
if choice >= 0 and choice < len(pets):
    pet = pets[choice]

    # Element-level string manipulation
    first_letter = pet[0]

    print("\nYou selected:", pet)
    print("The first letter of the pet's name is:", first_letter)

    # Conditional logic
    if first_letter == "B":
        print("This pet gets a free toy!")
    elif first_letter == "L":
        print("This pet comes with a free leash!")
    else:
        print("This pet comes with free treats!")

else:
    print("Invalid selection. Please run the program again.")