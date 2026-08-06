from player_info import get_player_info, display_player_info
from player_search import get_player_id
from nba_api_handler import get_player_stats
from stats_display import display_stats
from last10_games import get_last_10_games, get_season_games
from graphs import season_points_chart

print("\n==============================")
print("      NBA PLAYER STATS")
print("==============================")

while True:

    player_name = input("\nEnter NBA Player Name: ")

    player_id = get_player_id(player_name)

    if player_id:
        info = get_player_info(player_name)
        display_player_info(info)

        stats = get_player_stats(player_id)
        selected_season = display_stats(stats)

        games = get_last_10_games(player_id, selected_season)

        print("\n========== LAST 10 GAMES ==========")
        print(games[["GAME_DATE", "MATCHUP", "PTS", "REB", "AST"]])

        season_games = get_season_games(player_id, selected_season)

        season_points_chart(
            season_games,
            player_name,
            selected_season
        )

    else:
        print("Player not found.")

    while True:
        choice = input("\nWould you like to search for another player? (Y/N): ").strip().upper()

        if choice == "Y":
            break

        elif choice == "N":
            print("\n===================================")
            print(" Thank you for using NBA Player Stats!")
            print(" Have a great day!")
            print("===================================")
            exit()

        else:
            print("Invalid input. Please enter Y or N.")
