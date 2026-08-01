from nba_api.stats.endpoints import playercareerstats

def get_career_stats(player_id):

    career = playercareerstats.PlayerCareerStats(
        player_id=player_id
    )

    return career.get_data_frames()[0]