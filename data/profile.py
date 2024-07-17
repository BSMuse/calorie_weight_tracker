class UserProfile:
    def __init__(self, current_weight, goal_weight, age, height, gender, activity_level):
        self.current_weight = current_weight
        self.goal_weight = goal_weight
        self.age = age
        self.height = height
        self.gender = gender
        self.activity_level = activity_level
        self.tdee = self.calculate_tdee()

    def calculate_tdee(self):
        # Convert weight from lbs to kg
        weight_kg = self.current_weight / 2.20462

        if self.gender == 'male':
            bmr = 88.362 + (13.397 * weight_kg) + (4.799 * self.height) - (5.677 * self.age)
        else:
            bmr = 447.593 + (9.247 * weight_kg) + (3.098 * self.height) - (4.330 * self.age)

        activity_multipliers = {
            'sedentary': 1.2,
            'lightly_active': 1.375,
            'moderately_active': 1.55,
            'very_active': 1.725,
            'extra_active': 1.9
        }

        self.tdee = bmr * activity_multipliers[self.activity_level]
        return self.tdee

    def update_tdee(self, latest_weight, entries):
        self.current_weight = latest_weight
        if entries:
            self.activity_level = self.calculate_average_activity_level(entries)
        else:
            self.activity_level = 'sedentary'  # Default to sedentary if no entries
        self.tdee = self.calculate_tdee()

    def calculate_average_activity_level(self, entries):
        recent_entries = entries[-7:]
        total_exercise_calories = sum(entry.exercise_calories for entry in recent_entries)
        average_exercise_calories = total_exercise_calories / len(recent_entries) if recent_entries else 0

        if average_exercise_calories < 100:
            return 'sedentary'
        elif 100 <= average_exercise_calories <= 200:
            return 'lightly_active'
        elif 201 <= average_exercise_calories <= 400:
            return 'moderately_active'
        elif 401 <= average_exercise_calories <= 600:
            return 'very_active'
        else:
            return 'extra_active'

    def to_dict(self):
        return {
            'current_weight': self.current_weight,
            'goal_weight': self.goal_weight,
            'age': self.age,
            'height': self.height,
            'gender': self.gender,
            'activity_level': self.activity_level,
            'tdee': self.tdee
        }

    def __str__(self):
        return (f"Current Weight: {self.current_weight:.1f} lbs, Goal Weight: {self.goal_weight:.1f} lbs, "
                f"TDEE: {self.tdee:.1f} kcal, Activity Level: {self.activity_level.replace('_', ' ').capitalize()}")
