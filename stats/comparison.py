from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats


def get_player_comparison(player_name):

    player = players.find_players_by_full_name(player_name)

    if not player:
        return None

    player_id = player[0]["id"]

    career = playercareerstats.PlayerCareerStats(player_id=player_id)
    df = career.get_data_frames()[0]

    if df.empty:
        return None

    latest = df.iloc[-1]

    return {
        "Name": player_name,
        "Season": latest["SEASON_ID"],
        "GP": latest["GP"],
        "PTS": round(latest["PTS"] / latest["GP"], 1),
        "REB": round(latest["REB"] / latest["GP"], 1),
        "AST": round(latest["AST"] / latest["GP"], 1),
        "STL": round(latest["STL"] / latest["GP"], 1),
        "BLK": round(latest["BLK"] / latest["GP"], 1),
        "FG%": round(latest["FG_PCT"] * 100, 1),
        "3P%": round(latest["FG3_PCT"] * 100, 1),
        "FT%": round(latest["FT_PCT"] * 100, 1),
    }

def compare_players():

    print("\n==============================")
    print("      PLAYER COMPARISON")
    print("==============================")

    player1 = input("Enter first player: ").strip()
    player2 = input("Enter second player: ").strip()

    stats1 = get_player_comparison(player1)
    stats2 = get_player_comparison(player2)

    if stats1 is None:
        print(f"\nPlayer '{player1}' was not found.")
        return

    if stats2 is None:
        print(f"\nPlayer '{player2}' was not found.")
        return

    print("\n===============================================================")
    print(f"{'STAT':<12}{stats1['Name']:<22}{stats2['Name']:<22}")
    print("===============================================================")

    print(f"{'Season':<12}{stats1['Season']:<22}{stats2['Season']:<22}")
    print(f"{'Games':<12}{stats1['GP']:<22}{stats2['GP']:<22}")
    print(f"{'PPG':<12}{stats1['PTS']:<22}{stats2['PTS']:<22}")
    print(f"{'RPG':<12}{stats1['REB']:<22}{stats2['REB']:<22}")
    print(f"{'APG':<12}{stats1['AST']:<22}{stats2['AST']:<22}")
    print(f"{'SPG':<12}{stats1['STL']:<22}{stats2['STL']:<22}")
    print(f"{'BPG':<12}{stats1['BLK']:<22}{stats2['BLK']:<22}")
    print(f"{'FG%':<12}{stats1['FG%']:<22}{stats2['FG%']:<22}")
    print(f"{'3P%':<12}{stats1['3P%']:<22}{stats2['3P%']:<22}")
    print(f"{'FT%':<12}{stats1['FT%']:<22}{stats2['FT%']:<22}")

    print("===============================================================")
