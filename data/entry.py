class DailyEntry:
    def __init__(self, date, weight, calories, exercise_calories):
        self.date = date
        self.weight = weight
        self.calories = calories
        self.exercise_calories = exercise_calories

    def to_dict(self):
        return {
            'date': self.date,
            'weight': self.weight,
            'calories': self.calories,
            'exercise_calories': self.exercise_calories
        }

    def __str__(self):
        return f"Date: {self.date}, Weight: {self.weight:.1f} lbs, Calories: {self.calories} kcal, Exercise Calories: {self.exercise_calories} kcal"

    def get_activity_level(self):
        if self.exercise_calories < 100:
            return 'sedentary'
        elif 100 <= self.exercise_calories <= 200:
            return 'lightly_active'
        elif 201 <= self.exercise_calories <= 400:
            return 'moderately_active'
        elif 401 <= self.exercise_calories <= 600:
            return 'very_active'
        else:
            return 'extra_active'
