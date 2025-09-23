# 📱 Phone Number Formatter
#
# 1. Ask the user to enter a U.S. phone number in **any format**.
phone_number = input("Enter a U.S. phone number: ")

# 2. Use .strip() to remove any leading/trailing spaces.
cleaned = phone_number.strip()

# 3. Replace common separators (-, (, ), .) with spaces.
for ch in ["-", "(", ")", ".", ","]:
    cleaned = cleaned.replace(ch, " ")

# 4. Use .split() to break into chunks, then .join() to merge the digits.
parts = cleaned.split()
digits_only = "".join(parts)

# 5. Check if the cleaned number has **exactly 10 digits**.
if len(digits_only) == 10:
    # 6. If yes, format it like this: (123) 456-7890
    formatted_number = f"({digits_only[0:3]}) {digits_only[3:6]}-{digits_only[6:]}"
    print(f"Formatted number: {formatted_number}")
else:
    # 7. If not, print an error message: "Please enter exactly 10 digits."
    print("Please enter exactly 10 digits.")
