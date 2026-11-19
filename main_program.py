import pandas as pd

video_games_data = pd.read_csv("video_games_raw.csv")

#print title and allow user to inspect a game/row
print("VIDEO GAME CATALOG MANAGER")
row = int(input("Enter a row number to inspect: "))

selected_game = video_games_data.iloc[row - 1]

#display the game selected by the user
print("Selected Game:")
print("Title:", selected_game["Title"])
print("Platform:", selected_game["Platform"])
print("Genre:", selected_game["Genre"])
print("Rating:", selected_game["Rating"])
print("Current Status:", selected_game["Status"])

#user inputs new status
while True:
    new_status = input("Please enter a new status such as Backlog, Completed, Playing, or Dropped: ").capitalize()

    if new_status not in ["Backlog", "Completed", "Playing", "Dropped"]:
        print("Invalid input. Please enter Backlog, Completed, Playing, or Dropped. Try again.")
    else:
        break

video_games_data.at[row - 1,"Status"] = new_status

video_games_data["Recommended"] = "No"

#filter recommended games
video_games_data.loc[(video_games_data["Rating"] >= 8) & (video_games_data["Price"] <= 40), 
                                 "Recommended"] = "Yes"
#Display recommended games
print(video_games_data.query('Recommended == "Yes"')[["Title","Platform","Price","Rating"]])

video_games_data.to_csv("video_games_cleaned.csv", index=False)

#indicate the catalog has been updated
print("The catalog has been updated.")
print("Saved as video_games_cleaned.csv")

