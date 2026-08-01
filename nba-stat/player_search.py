from nba_api.stats.static import players

def get_player_id(player_name):
    player = players.find_players_by_full_name(player_name)

    if player:
        return player[0]["id"]

    return None