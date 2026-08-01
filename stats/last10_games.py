from nba_api.stats.endpoints import playergamelog

def get_last_10_games(player_id, season='2025-26'):

    gamelog = playergamelog.PlayerGameLog(
        player_id=player_id,
        season=season
    )

    games = gamelog.get_data_frames()[0]

    return games.head(10)