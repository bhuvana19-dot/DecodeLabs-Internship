
print("================================")
print("   AI Movie Recommendation System")
print("================================")

print("\nChoose your favorite movie genre:")
print("1. Comedy")
print("2. Action")
print("3. Romance")
print("4. Horror")

choice = input("\nEnter your choice (1-4): ")

if choice == "1":
    print("\nRecommended movies:")
    print("- 3 Idiots")
    print("- Home Alone")
    print("- The Mask")

elif choice == "2":
    print("\nRecommended movies:")
    print("- Avengers")
    print("- Mission Impossible")
    print("- John Wick")

elif choice == "3":
    print("\nRecommended movies:")
    print("- Titanic")
    print("- The Notebook")
    print("- La La Land")

elif choice == "4":
    print("\nRecommended movies:")
    print("- The Conjuring")
    print("- Insidious")
    print("- A Quiet Place")

else:
    print("\nInvalid choice! Please enter a number from 1 to 4.")
