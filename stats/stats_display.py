def calculate_per_game(stat, gp):
    if gp == 0:
        return 0

    if stat is None:
        return "N/A"

    return round(stat / gp, 1)

def display_stats(stats):

    print("\nAvailable Seasons")
    print("=" * 30)

    seasons = stats["SEASON_ID"].tolist()

    for season in seasons:
        print(season)

    print()

    selected_season = input("Enter the season you want to view (Example: 2023-24): ")

    season_stats = stats[stats["SEASON_ID"] == selected_season]

    if season_stats.empty:
        print("Season not found.")
        return

    for _, row in season_stats.iterrows():

        gp = row["GP"]

        ppg = calculate_per_game(row["PTS"], gp)
        rpg = calculate_per_game(row["REB"], gp)
        apg = calculate_per_game(row["AST"], gp)
        spg = calculate_per_game(row["STL"], gp)
        bpg = calculate_per_game(row["BLK"], gp)
        mpg = calculate_per_game(row["MIN"], gp)
        tpg = calculate_per_game(row["TOV"], gp)

        print("=" * 60)

        if row["TEAM_ABBREVIATION"] == "TOT":
            print("Combined Season Statistics")
        else:
            print(f"Team: {row['TEAM_ABBREVIATION']}")

        print("=" * 60)

        print(f"Games Played      : {gp}")
        print(f"Minutes Per Game  : {mpg:}")
        print(f"Points Per Game   : {ppg:}")
        print(f"Rebounds Per Game : {rpg:}")
        print(f"Assists Per Game  : {apg:}")
        print(f"Steals Per Game   : {spg:}")
        print(f"Blocks Per Game   : {bpg:}")

        print()
        print("Season Totals")
        print("-" * 25)
        print(f"Points      : {row['PTS']}")
        print(f"Rebounds    : {row['REB']}")
        print(f"Assists     : {row['AST']}")
        steals = row["STL"] if row["STL"] is not None else "N/A"
        blocks = row["BLK"] if row["BLK"] is not None else "N/A"
        turnovers = row["TOV"] if row["TOV"] is not None else "N/A"

        print(f"Steals      : {steals}")
        print(f"Blocks      : {blocks}")
        print(f"Turnovers   : {turnovers}")
        print()

    return selected_season
