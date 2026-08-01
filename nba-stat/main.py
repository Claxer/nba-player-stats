from player_search import get_player_id
from nba_api_handler import get_player_stats
from stats_display import display_stats

print("==============================")
print("      NBA PLAYER STATS")
print("==============================")

while True:

    player_name = input("\nEnter NBA Player Name: ")

    player_id = get_player_id(player_name)

    if player_id:
        stats = get_player_stats(player_id)
        display_stats(stats)
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