# --- Task 2: Interactive Number Analyzer (With Bonus Features) ---

# List to store all numbers analyzed
analyzed_numbers = []

print("Welcome to the Interactive Number Analyzer")
print("Type 'exit' at any time to quit and see the summary.\n")

while True:
    user_input = input("Enter a number (or 'exit'): ").strip().lower()

    # Check if the user wants to stop
    if user_input == 'exit':
        break

    try:
        num = int(user_input)
        
        # Store the number in our list
        analyzed_numbers.append(num)

        print("\nAnalysis Results")
        print("------------------------")

        # 1. Check: Positive, Negative, or Zero
        if num > 0:
            status = "Positive"
        elif num < 0:
            status = "Negative"
        else:
            status = "Zero"
        print(f"Number is: {status}")

        # 2. Check: Even or Odd
        if num % 2 == 0:
            parity = "Even"
        else:
            parity = "Odd"
        print(f"Number is: {parity}")

        # 3. Check: Divisibility by both 3 and 5
        if num % 3 == 0 and num % 5 == 0:
            divisible = True
            print("Divisible by both 3 and 5: Yes")
        else:
            divisible = False
            print("Divisible by both 3 and 5: No")

        # 4. Check: Within Range 1-100
        if num >= 1 and num <= 100:
            in_range = True
            print("Within range (1-100): Yes")
        else:
            in_range = False
            print("Within range (1-100): No")

        # 5. Special Condition Logic
        if status == "Positive" and parity == "Even" and in_range:
            print("Special Condition: Matched (Positive, Even, and in Range)")

        print("------------------------\n")

    except ValueError:
        print("Error: Please enter a valid whole number or type 'exit'.\n")

# --- Final Summary ---
print("\nFinal Summary")
print("========================")
print(f"Total numbers analyzed: {len(analyzed_numbers)}")
print(f"Numbers entered: {analyzed_numbers}")
print("========================")
print("Thank you for using the Analyzer!")