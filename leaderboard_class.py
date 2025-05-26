import json
import os
from datetime import datetime

class Leaderboard:
    file_path = "leaderboard.json"

    @staticmethod
    def save_score(subject_name, user_name, score, total, percentage):
        entry = {
            "name": user_name,
            "subject": subject_name,
            "score": f"{score}/{total}",
            "percentage": round(percentage, 2),
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        # Load existing leaderboard data
        if os.path.exists(Leaderboard.file_path):
            with open(Leaderboard.file_path, "r") as file:
                data = json.load(file)
        else:
            data = []

        data.append(entry)

        # Save updated data
        with open(Leaderboard.file_path, "w") as file:
            json.dump(data, file, indent=4)