from tabulate import tabulate
from colorama import Fore, Style, init
import os

init(autoreset=True)

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_valid_input(prompt, allow_empty=False):
    while True:
        val = input(prompt).strip()
        if not val and not allow_empty:
            print(Fore.RED + "Input cannot be empty.")
        else:
            return val

def get_integer_input(prompt):
    while True:
        try:
            return int(get_valid_input(prompt))
        except ValueError:
            print(Fore.RED + "Please enter a valid number.")

def choose_days():
    default_days = input(Fore.CYAN + "Use default days (Mon-Fri)? (y/n): ").lower() == 'y'
    if default_days:
        return ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    
    days = []
    num_days = get_integer_input("Enter number of days: ")
    for _ in range(num_days):
        day = get_valid_input("- Enter day name: ").capitalize()
        days.append(day)
    return days

def choose_time_slots():
    default_slots = input(Fore.CYAN + "Use default 5 periods? (y/n): ").lower() == 'y'
    if default_slots:
        return ["9:00-10:00", "10:00-11:00", "11:00-12:00", "12:00-1:00", "2:00-3:00"]
    
    time_slots = []
    num_periods = get_integer_input("Enter number of periods: ")
    for i in range(num_periods):
        slot = get_valid_input(f"- Time slot {i+1}: ")
        time_slots.append(slot)
    return time_slots

def input_timetable(days, time_slots):
    print(Fore.YELLOW + "\nNow enter the subjects for each time slot:")
    timetable = []

    for time in time_slots:
        row = [time]
        for day in days:
            subject = get_valid_input(f"{Fore.GREEN}{day} | {time}: ")
            row.append(subject)
        timetable.append(row)
    return timetable

def display_timetable(days, timetable):
    headers = ["Time"] + days
    table = tabulate(timetable, headers=headers, tablefmt="fancy_grid")
    print(Fore.MAGENTA + "\n📅 Your Weekly Timetable:\n")
    print(table)
    return table

def save_to_file(content):
    default_name = "Weekly_Timetable.txt"
    filename = input(Fore.CYAN + f"\nEnter filename to save (default: {default_name}): ").strip()
    filename = filename if filename else default_name

    try:
        with open(filename, "w") as f:
            f.write(content)
        print(Fore.GREEN + f"\n📝 Timetable saved successfully to '{filename}'.")
    except Exception as e:
        print(Fore.RED + f"❌ Failed to save file: {e}")

def main():
    clear_console()
    print(Fore.BLUE + Style.BRIGHT + "✨ Welcome to the Interactive Timetable Generator ✨\n")

    while True:
        days = choose_days()
        time_slots = choose_time_slots()
        timetable = input_timetable(days, time_slots)
        table_text = display_timetable(days, timetable)

        if input(Fore.CYAN + "\nDo you want to save this timetable? (y/n): ").lower() == 'y':
            save_to_file(table_text)

        if input(Fore.CYAN + "\nCreate another timetable? (y/n): ").lower() != 'y':
            print(Fore.GREEN + "\nThank you for using the Timetable Generator. Keep learning and shining! 💫")
            break

if __name__ == "__main__":
    main()
