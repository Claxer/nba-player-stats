from nba_api.stats.endpoints import playercareerstats


def get_career_stats(player_id):
    """
    Returns career totals and career averages.
    """

    career = playercareerstats.PlayerCareerStats(player_id=player_id)

    df = career.get_data_frames()[0]

    # Only regular season rows
    df = df[df["LEAGUE_ID"] == "00"]

    games = df["GP"].sum()

    if games == 0:
        return None

    totals = {
        "Games": games,
        "Points": df["PTS"].sum(),
        "Rebounds": df["REB"].sum(),
        "Assists": df["AST"].sum(),
        "Steals": df["STL"].sum(),
        "Blocks": df["BLK"].sum(),
        "Turnovers": df["TOV"].sum(),
        "Minutes": df["MIN"].sum(),
        "FG Made": df["FGM"].sum(),
        "FG Attempted": df["FGA"].sum(),
        "3PT Made": df["FG3M"].sum(),
        "3PT Attempted": df["FG3A"].sum(),
        "FT Made": df["FTM"].sum(),
        "FT Attempted": df["FTA"].sum()
    }

    averages = {
        "PPG": totals["Points"] / games,
        "RPG": totals["Rebounds"] / games,
        "APG": totals["Assists"] / games,
        "SPG": totals["Steals"] / games,
        "BPG": totals["Blocks"] / games,
        "TOPG": totals["Turnovers"] / games,
        "MPG": totals["Minutes"] / games
    }

    return totals, averages


def display_career_stats(totals, averages):
    """
    Displays career totals and career averages.
    """

    print("\n" + "=" * 50)
    print("CAREER TOTALS")
    print("=" * 50)

    print(f"Games Played : {totals['Games']}")
    print(f"Points       : {totals['Points']:,}")
    print(f"Rebounds     : {totals['Rebounds']:,}")
    print(f"Assists      : {totals['Assists']:,}")
    print(f"Steals       : {totals['Steals']:,}")
    print(f"Blocks       : {totals['Blocks']:,}")
    print(f"Turnovers    : {totals['Turnovers']:,}")
    print(f"Minutes      : {totals['Minutes']:,}")

    print("\nShooting Totals")
    print("-" * 50)
    print(f"FG Made      : {totals['FG Made']:,}")
    print(f"FG Attempted : {totals['FG Attempted']:,}")
    print(f"3PT Made     : {totals['3PT Made']:,}")
    print(f"3PT Attempted: {totals['3PT Attempted']:,}")
    print(f"FT Made      : {totals['FT Made']:,}")
    print(f"FT Attempted : {totals['FT Attempted']:,}")

    print("\n" + "=" * 50)
    print("CAREER AVERAGES")
    print("=" * 50)

    print(f"PPG : {averages['PPG']:.1f}")
    print(f"RPG : {averages['RPG']:.1f}")
    print(f"APG : {averages['APG']:.1f}")
    print(f"SPG : {averages['SPG']:.1f}")
    print(f"BPG : {averages['BPG']:.1f}")
    print(f"TOPG: {averages['TOPG']:.1f}")
    print(f"MPG : {averages['MPG']:.1f}")

    print("=" * 50)
