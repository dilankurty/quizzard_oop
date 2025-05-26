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

    @staticmethod
    def display(subject_filter=None):
        if not os.path.exists(Leaderboard.file_path):
            print("📉 No leaderboard data available.")
            return

        with open(Leaderboard.file_path, "r") as file:
            data = json.load(file)

        if subject_filter:
            data = [entry for entry in data if entry["subject"].lower() == subject_filter.lower()]

        if not data:
            print("📉 No scores recorded for this subject yet.")
            return
        
        sorted_data = sorted(data, key=lambda x: x["percentage"], reverse=True)

        print("\n🏆 Leaderboard")
        print(f"{'Rank':<6}{'Name':<20}{'Subject':<20}{'Score':<10}{'Percent':<10}{'Date'}")
        print("-" * 75)
        for rank, entry in enumerate(sorted_data[:10], start=1):
            print(f"{rank:<6}{entry['name']:<20}{entry['subject']:<20}{entry['score']:<10}{entry['percentage']:<10}{entry['date']}")