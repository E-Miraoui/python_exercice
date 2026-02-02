# Ask the user for inputs
weather = input("Enter the current weather (hot / cold / rainy): ").lower()
diet = input("Enter your diet preference (vegetarian / non-vegetarian): ").lower()

# Meal recommendation logic
if weather == "hot" and diet == "vegetarian":
    print("Meal Recommendation: A fresh salad with lemonade")
elif weather == "cold" and diet == "non-vegetarian":
    print("Meal Recommendation: A hot bowl of chicken soup")
elif weather == "rainy":
    print("Meal Recommendation: A warm cup of tea with a snack")
else:
    print("Meal Recommendation: Rice with vegetables")
