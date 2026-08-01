favorites = []

def add_favorite(player):

    favorites.append(player)

def show_favorites():

    print("\nFavorite Players")

    for player in favorites:
        print(player)