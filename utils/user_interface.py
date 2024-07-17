from data.entry import DailyEntry
from data.profile import UserProfile
from utils.file_operations import save_data


def display_menu():
    print("Choose an option:")
    print("1. Create Entry")
    print("2. Delete Entry")
    print("3. Edit Profile")
    print("4. View Weekly Summary")
    print("5. View All Data")
    print("6. Export Data to CSV")
    print("7. Exit")



def add_entry(entries, profile):
    date = input("Enter the date (YYYY-MM-DD): ")
    weight = float(input("Enter your weight (lbs): "))
    calories = int(input("Enter your calorie intake (kcal): "))
    exercise_calories = int(input("Enter your exercise calories burned (kcal): "))
    entry = DailyEntry(date, weight, calories, exercise_calories)
    entries.append(entry)

    # Update TDEE based on the latest weight and average activity level
    profile.update_tdee(weight, entries)

    # Save data to file
    save_data(entries, profile)

    print("Entry added successfully!")
    print(f"New TDEE: {profile.tdee:.1f} kcal")


def delete_entry(entries, profile):
    if not entries:
        print("No entries available to delete.")
        return

    for index, entry in enumerate(entries):
        print(f"{index + 1}. {entry}")

    try:
        entry_number = int(input("Enter the number of the entry you want to delete: "))
        if 1 <= entry_number <= len(entries):
            deleted_entry = entries.pop(entry_number - 1)
            print(f"Deleted entry: {deleted_entry}")

            # Update TDEE based on the remaining entries
            if entries:
                profile.update_tdee(entries[-1].weight, entries)
            else:
                profile.update_tdee(profile.current_weight, entries)  # No entries left

            # Save data to file
            save_data(entries, profile)
        else:
            print("Invalid entry number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def edit_profile(profile):
    while True:
        try:
            current_weight = float(input(f"Enter your current weight (lbs) [{profile.current_weight}]: ") or profile.current_weight)
            if current_weight <= 0:
                raise ValueError("Weight must be a positive number.")
            break
        except ValueError as e:
            print(f"Invalid input for weight: {e}")

    while True:
        try:
            goal_weight = float(input(f"Enter your goal weight (lbs) [{profile.goal_weight}]: ") or profile.goal_weight)
            if goal_weight <= 0:
                raise ValueError("Goal weight must be a positive number.")
            break
        except ValueError as e:
            print(f"Invalid input for goal weight: {e}")

    while True:
        try:
            age = int(input(f"Enter your age [{profile.age}]: ") or profile.age)
            if age <= 0:
                raise ValueError("Age must be a positive integer.")
            break
        except ValueError as e:
            print(f"Invalid input for age: {e}")

    while True:
        try:
            height = int(input(f"Enter your height (cm) [{profile.height}]: ") or profile.height)
            if height <= 0:
                raise ValueError("Height must be a positive integer.")
            break
        except ValueError as e:
            print(f"Invalid input for height: {e}")

    while True:
        gender = input(f"Enter your gender (male/female) [{profile.gender}]: ").lower() or profile.gender
        if gender in ['male', 'female']:
            break
        else:
            print("Invalid input for gender. Please enter 'male' or 'female'.")

    activity_levels = [
        "1. Sedentary: Little to no exercise, mostly sitting (e.g., desk job)",
        "2. Lightly Active: Light exercise or sports 1-3 days a week (e.g., walking, light workouts)",
        "3. Moderately Active: Moderate exercise or sports 3-5 days a week (e.g., regular jogging, gym sessions)",
        "4. Very Active: Hard exercise or sports 6-7 days a week (e.g., intense workouts, training routines)",
        "5. Extra Active: Very hard exercise or physical job (e.g., construction work, athlete training daily)"
    ]

    activity_map = {
        1: 'sedentary',
        2: 'lightly_active',
        3: 'moderately_active',
        4: 'very_active',
        5: 'extra_active'
    }

    while True:
        print("Select your activity level:")
        for level in activity_levels:
            print(level)
        try:
            activity_choice = int(input(f"Enter the number corresponding to your activity level [{profile.activity_level.replace('_', ' ').capitalize()}]: ") or list(activity_map.keys())[list(activity_map.values()).index(profile.activity_level)])
            if activity_choice in activity_map:
                activity_level = activity_map[activity_choice]
                break
            else:
                raise ValueError("Invalid choice")
        except ValueError as e:
            print(f"Invalid input for activity level: {e}")

    profile.current_weight = current_weight
    profile.goal_weight = goal_weight
    profile.age = age
    profile.height = height
    profile.gender = gender
    profile.activity_level = activity_level
    profile.tdee = profile.calculate_tdee()

    # Save updated profile data
    save_data([], profile)
    print("Profile updated successfully!")


def view_weekly_summary(entries, profile):
    if not entries:
        print("No entries available.")
        return

    recent_entries = entries[-7:]
    total_weight = sum(entry.weight for entry in recent_entries)
    avg_weight = round(total_weight / len(recent_entries), 1)

    total_weight_loss = round(entries[0].weight - entries[-1].weight, 1)

    pounds_away = round(entries[-1].weight - profile.goal_weight, 1)

    print(f"Weekly average weight: {avg_weight} lbs")
    print(f"Total weight loss so far: {total_weight_loss} lbs")
    print(f"Pounds away from goal weight: {pounds_away} lbs")


def view_all_data(entries):
    if not entries:
        print("No entries available.")
        return

    print("All Data Entries:")
    for entry in entries:
        print(entry)


def create_user_profile():
    while True:
        try:
            current_weight = float(input("Enter your current weight (lbs): "))
            if current_weight <= 0:
                raise ValueError("Weight must be a positive number.")
            break
        except ValueError as e:
            print(f"Invalid input for weight: {e}")

    while True:
        try:
            goal_weight = float(input("Enter your goal weight (lbs): "))
            if goal_weight <= 0:
                raise ValueError("Goal weight must be a positive number.")
            break
        except ValueError as e:
            print(f"Invalid input for goal weight: {e}")

    while True:
        try:
            age = int(input("Enter your age: "))
            if age <= 0:
                raise ValueError("Age must be a positive integer.")
            break
        except ValueError as e:
            print(f"Invalid input for age: {e}")

    while True:
        try:
            height = int(input("Enter your height (cm): "))
            if height <= 0:
                raise ValueError("Height must be a positive integer.")
            break
        except ValueError as e:
            print(f"Invalid input for height: {e}")

    while True:
        gender = input("Enter your gender (male/female): ").lower()
        if gender in ['male', 'female']:
            break
        else:
            print("Invalid input for gender. Please enter 'male' or 'female'.")

    activity_levels = [
        "1. Sedentary: Little to no exercise, mostly sitting (e.g., desk job)",
        "2. Lightly Active: Light exercise or sports 1-3 days a week (e.g., walking, light workouts)",
        "3. Moderately Active: Moderate exercise or sports 3-5 days a week (e.g., regular jogging, gym sessions)",
        "4. Very Active: Hard exercise or sports 6-7 days a week (e.g., intense workouts, training routines)",
        "5. Extra Active: Very hard exercise or physical job (e.g., construction work, athlete training daily)"
    ]

    activity_map = {
        1: 'sedentary',
        2: 'lightly_active',
        3: 'moderately_active',
        4: 'very_active',
        5: 'extra_active'
    }

    while True:
        print("Select your activity level:")
        for level in activity_levels:
            print(level)
        try:
            activity_choice = int(input("Enter the number corresponding to your activity level: "))
            if activity_choice in activity_map:
                activity_level = activity_map[activity_choice]
                break
            else:
                raise ValueError("Invalid choice")
        except ValueError as e:
            print(f"Invalid input for activity level: {e}")

    profile = UserProfile(current_weight, goal_weight, age, height, gender, activity_level)
    save_data([], profile)  # Save the initial profile to data.json
    return profile
