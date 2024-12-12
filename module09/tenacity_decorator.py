from tenacity import retry, stop_after_attempt, wait_fixed

@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
def get_user_input():
    user_input = input("Enter 'ok' to continue: ")
    if user_input.lower() != 'ok':
        print("Incorrect input. Please try again.")
        raise ValueError("Incorrect input")
    else:
        print("Correct input. Continuing...")

# Call the function
try:
    get_user_input()
except Exception as e:
    print(f"Finally failed after several attempts: {e}")