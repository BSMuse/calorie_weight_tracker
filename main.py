from utils.file_operations import load_data, export_data_to_csv
from utils.user_interface import display_menu, add_entry, delete_entry, edit_profile, view_weekly_summary, view_all_data, create_user_profile

def main():
    entries, profile = load_data()
    if profile is None:
        profile = create_user_profile()

    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_entry(entries, profile)
        elif choice == '2':
            delete_entry(entries, profile)
        elif choice == '3':
            edit_profile(profile)
        elif choice == '4':
            view_weekly_summary(entries, profile)
        elif choice == '5':
            view_all_data(entries)
        elif choice == '6':
            export_data_to_csv(entries)
        elif choice == '7':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
