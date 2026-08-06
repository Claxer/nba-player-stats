from nba_api.stats.static import players
from nba_api.stats.endpoints import commonplayerinfo


def get_player_info(player_name):
    player = players.find_players_by_full_name(player_name)

    if not player:
        return None

    player_id = player[0]["id"]

    info = commonplayerinfo.CommonPlayerInfo(player_id=player_id)

    df = info.get_data_frames()[0]

    return {
        "Name": df["DISPLAY_FIRST_LAST"][0],
        "Team": df["TEAM_NAME"][0],
        "Position": df["POSITION"][0],
        "Height": df["HEIGHT"][0],
        "Weight": df["WEIGHT"][0] + " lbs",
        "Jersey": df["JERSEY"][0],
        "Birthdate": df["BIRTHDATE"][0][:10],
        "Experience": df["SEASON_EXP"][0],
        "College": df["SCHOOL"][0],
        "Country": df["COUNTRY"][0]
    }

def display_player_info(info):

    if info is None:
        print("Player information not found.")
        return

    print("\n==============================")
    print("      PLAYER INFORMATION")
    print("==============================")

    for key, value in info.items():
        print(f"{key:<12}: {value}")
