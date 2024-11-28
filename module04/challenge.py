from typing import Dict

def get_valid_name() -> str:
    """
    Prompts the user to enter a valid name.

    :return: A valid name as a string
    """
    while True:
        try:
            user_name = input("Please, enter your name: ")

            if user_name.isdigit():
                raise ValueError("You typed a number! Please, enter a valid name.")
            elif len(user_name) == 0:
                raise ValueError("You did not type anything!")
            elif user_name.isspace():
                raise ValueError("You typed only spaces! Please, enter a valid name.")
            print(f"Valid name is {user_name}!")
            return user_name
        except ValueError as e:
            print(e)


def get_valid_float(prompt: str, error_message: str) -> float:
    """
    Prompts the user to enter a valid float value.

    :param prompt: Message to display to the user
    :param error_message: Error message to display for invalid input
    :return: A valid float
    """
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                raise ValueError(error_message)
            print(f"Valid value is {value}!")
            return value
        except ValueError as e:
            print(e)


def calculate_kpi(data: Dict[str, float]) -> float:
    """
    Calculates the KPI based on salary and bonus.

    :param data: A dictionary containing salary and bonus values
    :return: The calculated KPI
    """
    final_bonus = data["salary"] * (1 + data["bonus"])
    kpi = (data["salary"] + final_bonus) / 1000
    data["final_bonus"] = final_bonus
    return kpi


def main() -> None:
    """
    Main function to execute the program logic.
    """
    user_data: Dict[str, float] = {}

    # Collect user information
    user_data["name"] = get_valid_name()
    user_data["salary"] = get_valid_float("Please, enter your salary: ", "There is no negative salary!")
    user_data["bonus"] = get_valid_float("Please, enter your bonus: ", "There is no negative bonus!")

    # Calculate KPI and final bonus
    kpi = calculate_kpi(user_data)

    # Print the final information
    print(f"Your KPI is: {kpi:.2f}")
    print(
        f"{user_data['name']}, your salary is R${user_data['salary']:.2f} and your final bonus is R${user_data['final_bonus']:.2f}."
    )


if __name__ == "__main__":
    main()
