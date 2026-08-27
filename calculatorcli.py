def calculate_sum(nums):
    total = 0
    for n in nums:
        total += n
    return total


def calculate_difference(nums):
    diff = nums[0]
    for n in nums[1:]:
        diff -= n
    return diff


def calculate_product(nums):
    return math.prod(nums)


def calculate_quotient(nums):
    quotient = nums[0]
    for n in nums[1:]:
        if n == 0:
            return "Error: Division by zero is undefined."
        quotient /= n
    return quotient


def prompt_for_numbers():
    while True:
        raw_input = input("Enter values separated by space: ").strip()
        tokens = raw_input.split()

        try:
            values = [float(item) for item in tokens]
        except ValueError:
            print("Invalid entry. Please use numeric values only.")
            continue

        if len(values) < 2:
            print("Operation requires at least two numbers.")
            continue

        return values


def display_menu():
    print("\n--- CLI CALCULATOR ---")
    print("[1] Add")
    print("[2] Subtract")
    print("[3] Multiply")
    print("[4] Divide")
    print("[5] Show Logs")
    print("[6] Quit")


past_results = []

while True:
    display_menu()
    user_selection = input("Select an option (1-6): ").strip()

    if user_selection == "6":
        print("Exiting application. Goodbye!")
        break

    elif user_selection == "5":
        if not past_results:
            print("History log is currently empty.")
        else:
            print("\n--- TRANSACTION HISTORY ---")
            for record in past_results:
                print(f"- {record}")

    elif user_selection in {"1", "2", "3", "4"}:
        values = prompt_for_numbers()

        operations_map = {
            "1": ("+", calculate_sum),
            "2": ("-", calculate_difference),
            "3": ("*", calculate_product),
            "4": ("/", calculate_quotient),
        }

        symbol, func = operations_map[user_selection]
        outcome = func(values)
        expression = f" {symbol} ".join(str(v) for v in values)

        print(f"Output: {outcome}")

        if not str(outcome).startswith("Error"):
            past_results.append(f"{expression} = {outcome}")

    else:
        print("Unrecognized option. Please pick a number between 1 and 6.")
