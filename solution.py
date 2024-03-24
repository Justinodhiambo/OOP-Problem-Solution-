def calculate_score(participant):
    """
    Calculate the total score for a participant based on the points assigned to each food item.
    """
    return participant["chickenwings"] * 5 + participant["hamburgers"] * 3 + participant["hotdogs"] * 2

def generate_scoreboard(participants):
    """
    Generate a scoreboard sorted by score, with ties broken alphabetically by name.
    """
    scoreboard = []
    for participant in participants:
        score = calculate_score(participant)
        scoreboard.append({"name": participant["name"], "score": score})
    
    # Sort the scoreboard by score (descending) and name (ascending)
    scoreboard.sort(key=lambda x: (-x["score"], x["name"]))
    return scoreboard

scoreboard = generate_scoreboard(participants)
for entry in scoreboard:
    print(entry)
