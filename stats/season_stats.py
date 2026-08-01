from nba_api.stats.endpoints import playercareerstats

def get_current_season(player_id):

    stats = playercareerstats.PlayerCareerStats(
        player_id=player_id
    )

    df = stats.get_data_frames()[0]

    return df.tail(1)