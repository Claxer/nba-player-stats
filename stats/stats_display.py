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

        if gp > 0:
            ppg = row["PTS"] / gp
            rpg = row["REB"] / gp
            apg = row["AST"] / gp
            spg = row["STL"] / gp
            bpg = row["BLK"] / gp
            mpg = row["MIN"] / gp
            tpg = row["TOV"] / gp
        else:
            ppg = rpg = apg = spg = bpg = mpg = tpg = 0

        print("=" * 60)

        if row["TEAM_ABBREVIATION"] == "TOT":
            print("Combined Season Statistics")
        else:
            print(f"Team: {row['TEAM_ABBREVIATION']}")

        print("=" * 60)

        print(f"Games Played      : {gp}")
        print(f"Minutes Per Game  : {mpg:.1f}")
        print(f"Points Per Game   : {ppg:.1f}")
        print(f"Rebounds Per Game : {rpg:.1f}")
        print(f"Assists Per Game  : {apg:.1f}")
        print(f"Steals Per Game   : {spg:.1f}")
        print(f"Blocks Per Game   : {bpg:.1f}")

        print()
        print("Season Totals")
        print("-" * 25)
        print(f"Points      : {row['PTS']}")
        print(f"Rebounds    : {row['REB']}")
        print(f"Assists     : {row['AST']}")
        print(f"Steals      : {row['STL']}")
        print(f"Blocks      : {row['BLK']}")
        print(f"Turnovers   : {row['TOV']}")
        print()