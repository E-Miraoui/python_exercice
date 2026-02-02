# Ask the user for inputs
first_name = input("Enter your first name: ")
city = input("Enter your city: ")
hobby = input("Enter your favorite hobby: ")
dream_job = input("Enter your dream job: ")

# Display formatted outputs
print("\n--- User Profile ---")

# 1. Simple sentence
print("Hello", first_name + "!")

# 2. Using f-strings
print(f"You live in {city} and you enjoy {hobby}.")

# 3. Uppercase formatting
print(f"Your dream job is: {dream_job.upper()}")

# 4. Reordered formatting
print(f"{first_name} dreams of becoming a {dream_job} while enjoying {hobby} in {city}.")
