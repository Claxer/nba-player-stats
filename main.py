from menu import main_menu
from player_info import get_player_info, display_player_info
from player_search import get_player_id
from nba_api_handler import get_player_stats
from stats_display import display_stats
from career_stats import get_career_stats, display_career_stats
from last10_games import get_last_10_games, get_season_games
from graphs import season_points_chart
from comparison import compare_players

def search_player():

    player_name = input("\nEnter NBA Player Name: ").strip()

    player_id = get_player_id(player_name)

    if not player_id:
        print("\nPlayer not found.")
        return

    info = get_player_info(player_name)
    display_player_info(info)

    stats = get_player_stats(player_id)
    selected_season = display_stats(stats)

    if selected_season is None:
        return

    career = get_career_stats(player_id)

    if career:
        totals, averages = career
        display_career_stats(totals, averages)

    games = get_last_10_games(player_id, selected_season)

    print("\n========== LAST 10 GAMES ==========")
    print(games[["GAME_DATE", "MATCHUP", "PTS", "REB", "AST"]])

    season_games = get_season_games(player_id, selected_season)

    season_points_chart(
        season_games,
        player_name,
        selected_season
    )

def career_statistics():

    player_name = input("\nEnter NBA Player Name: ").strip()

    player_id = get_player_id(player_name)

    if not player_id:
        print("\nPlayer not found.")
        return

    career = get_career_stats(player_id)

    if career is None:
        print("\nNo career statistics available.")
        return

    totals, averages = career

    display_career_stats(totals, averages)

def current_season():

    player_name = input("\nEnter NBA Player Name: ").strip()

    player_id = get_player_id(player_name)

    if not player_id:
        print("\nPlayer not found.")
        return

    stats = get_player_stats(player_id)

    selected_season = display_stats(stats)

    if selected_season is None:
        return

def last_10_games():

    player_name = input("\nEnter NBA Player Name: ").strip()

    player_id = get_player_id(player_name)

    if not player_id:
        print("\nPlayer not found.")
        return

    stats = get_player_stats(player_id)

    selected_season = display_stats(stats)

    if selected_season is None:
        return

    games = get_last_10_games(player_id, selected_season)

    print("\n========== LAST 10 GAMES ==========")
    print(games[["GAME_DATE", "MATCHUP", "PTS", "REB", "AST"]])

def coming_soon():

    print("\n===================================")
    print("This feature is coming soon.")
    print("===================================")

def main():

    while True:

        main_menu()

        choice = input("\nSelect an option: ").strip()

        if choice == "1":
            search_player()

        elif choice == "2":
            career_statistics()

        elif choice == "3":
            current_season()

        elif choice == "4":
            last_10_games()

        elif choice == "5":
            coming_soon()

        elif choice == "6":
            coming_soon()

        elif choice == "7":
            coming_soon()

        elif choice == "8":
            compare_players()

        elif choice == "9":

            print("\n===================================")
            print(" Thank you for using NBA Player Stats!")
            print(" Have a great day!")
            print("===================================")
            break

        else:
            print("\nInvalid option. Please try again.")

        input("\nPress Enter to return to the Main Menu...")


if __name__ == "__main__":
    main()
