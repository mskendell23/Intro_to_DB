
def main():
    # Prompt for user input
    Task = input("Enter your task: ")
    Priority = input("Enter the task’s priority (high/medium/low): ").lower()
    Time_bound = input("Is it time-bound? (yes or no): ").lower()

    # Generate a reminder based on priority using match-case
    match priority:
        case "high":
            reminder = f"🔴 HIGH PRIORITY: Don't forget to {task}."
        case "medium":
            reminder = f"🟠 MEDIUM PRIORITY: Remember to {task}."
        case "low":
            reminder = f"🟢 LOW PRIORITY: You can do {task} when convenient."
        case _:
            reminder = f"⚪ UNKNOWN PRIORITY: Task entered is '{task}'."

    # Adjust reminder if the task is time-bound
    if time_bound == "yes":
        reminder += " This is a time-sensitive task that requires immediate attention today!"

    # Print the customized reminder
    print("\nYour Reminder:")
    print(reminder)

if __name__ == "__main__":
    main()
