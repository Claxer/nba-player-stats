from nba_api.stats.static import players

def get_team(player):

    print("\nCurrent Team")
    print("------------------")

    print(player["team_name"])