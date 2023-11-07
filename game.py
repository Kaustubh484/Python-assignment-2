# Advanced Text-Based Adventure Game in Python

# Define the game's story and structure
game_story = {
    "start": {
        "text": "You wake up in a mysterious forest. What do you do?",
        "choices": {
            "1": "Explore deeper into the forest.",
            "2": "Head back to the clearing."
        }
    },
    "explore_forest": {
        "text": "You discover a hidden cave. Do you enter it?",
        "choices": {
            "1": "Enter the cave.",
            "2": "Keep exploring the forest."
        }
    },
    "enter_cave": {
        "text": "Inside the cave, you find a chest. Open it?",
        "choices": {
            "1": "Open the chest.",
            "2": "Leave it and keep exploring."
        }
    },
    "treasure_found": {
        "text": "You find a treasure chest filled with gold and jewels. You have succeeded!",
        "end_game": True
    },
    "cave_monster": {
        "text": "A fierce monster guards the chest. You were defeated!",
        "end_game": True
    }
}

# Initialize player's state
current_scene = "start"
inventory = []

# Main game loop
while True:
    scene = game_story[current_scene]
    print(scene["text"])
    choices = scene["choices"]
    for choice_num, choice_text in choices.items():
        print(f"{choice_num}: {choice_text}")

    choice = input("Enter the number of your choice: ")

    if choice in choices:
        next_scene = current_scene  # Initialize to the same scene

        if current_scene == "start" and choice == "1":
            next_scene = "explore_forest"
        elif current_scene == "start" and choice == "2":
            next_scene = "end_game"
        elif current_scene == "explore_forest" and choice == "1":
            next_scene = "enter_cave"
        elif current_scene == "explore_forest" and choice == "2":
            next_scene = "end_game"
        elif current_scene == "enter_cave" and choice == "1":
            next_scene = "treasure_found"
        elif current_scene == "enter_cave" and choice == "2":
            next_scene = "end_game"

        current_scene = next_scene

    elif "end_game" in scene:
        print(scene["text"])
        break

    else:
        print("Invalid choice. Please try again.")

# Display different endings based on the player's progress
if current_scene == "treasure_found":
    print("Congratulations! You have found the treasure and emerged victorious!")
elif current_scene == "cave_monster":
    print("Oh no! You have met an unfortunate end in your adventure.")
