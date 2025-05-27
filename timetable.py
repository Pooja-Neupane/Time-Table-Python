from tabulate import tabulate
from colorama import Fore, Style, init
import os

init(autoreset=True)

def get_valid_input(prompt, allow_empty=False):
    while True:
        val = input(prompt).strip()
        if not val and not allow_empty:
            print(Fore.RED + "Input cannot be empty.")
        else:
            return val

def get_timetable():
    print(Fore.CYAN + "\n📋 Let's set up your weekly timetable:")
    
    # Use default days?
    default_days = input("Use default days (Mon-Fri)? (y/n): ").lower() == 'y'
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"] if default_days else []

    if not default_days:
        num_days = int(get_valid_input("Enter number of days: "))
        for _ in range(num_days):
            day = get_valid_input("- Enter day: ").capitalize()
            days.append(day)

    # Use default time slots?
    default_slots = input("Use default 5 periods? (y/n): ").lower() == 'y'
    time_slots = ["9:00-10:00", "10:00-11:00", "11:00-12:00", "12:00-1:00", "2:00-3:00"] if default_slots else []

    if not default_slots:
        num_periods = int(get_valid_input("Enter number of periods: "))
        for i in range(num_periods):
            slot = get_valid_input(f"- Time slot {i+1}: ")
            time_slots.append(slot)

    # Collect subjects
    timetable = []
    print(Fore.YELLOW + "\nNow enter the subjects for each time slot:")
    for time in time_slots:
        row = [time]
        for day in days:
            subject = get_valid_input(f"{Fore.GREEN}{day} | {time}: ")
            row.append(subject)
        timetable.append(row)

    return days, time_slots, timetable

def display_timetable(days, timetable):
    headers = ["Time"] + days
    table = tabulate(timetable, headers=headers, tablefmt="fancy_grid")
    print(Fore.MAGENTA + "\n📅 Your Weekly Timetable:\n")
    print(table)
    return table

def save_to_file(content):
    filename = "Weekly_Timetable.txt"
    with open(filename, "w") as f:
        f.write(content)
    print(Fore.GREEN + f"\n📝 Timetable saved successfully to '{filename}'.")

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.BLUE + Style.BRIGHT + "✨ Welcome to the Interactive Timetable Generator ✨")
    
    while True:
        days, time_slots, timetable = get_timetable()
        table_text = display_timetable(days, timetable)
        save = input("\nDo you want to save this timetable to a file? (y/n): ").lower()
        if save == 'y':
            save_to_file(table_text)

        again = input("\nDo you want to create another timetable? (y/n): ").lower()
        if again != 'y':
            print(Fore.CYAN + "\nThank you for using the Timetable Generator. Keep learning and shining! 💫")
            break

if __name__ == "__main__":
    main()
