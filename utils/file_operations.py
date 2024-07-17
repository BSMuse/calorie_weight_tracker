import json
import os
import csv
from data.entry import DailyEntry
from data.profile import UserProfile


def load_data():
    if not os.path.exists('data.json'):
        return [], None

    with open('data.json', 'r') as file:
        data = json.load(file)
        entries = [DailyEntry(**entry) for entry in data['entries']]
        profile_data = data['profile']
        profile = UserProfile(
            current_weight=profile_data['current_weight'],
            goal_weight=profile_data['goal_weight'],
            age=profile_data['age'],
            height=profile_data['height'],
            gender=profile_data['gender'],
            activity_level=profile_data['activity_level']
        )
        return entries, profile


def save_data(entries, profile):
    data = {
        'entries': [entry.to_dict() for entry in entries],
        'profile': profile.to_dict()
    }
    with open('data.json', 'w') as file:
        json.dump(data, file)


def export_data_to_csv(entries, filename="calorie_weight_tracker.csv"):
    if not entries:
        print("No entries available to export.")
        return

    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Weight (lbs)", "Calories (kcal)", "Exercise Calories (kcal)"])
        for entry in entries:
            writer.writerow([entry.date, round(entry.weight, 1), entry.calories, entry.exercise_calories])

    print(f"Data exported to {filename} successfully!")
