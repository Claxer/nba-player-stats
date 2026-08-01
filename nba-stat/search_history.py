history = []

def add_history(player):

    history.append(player)

def show_history():

    print("\nSearch History")
    print("----------------")

    if len(history) == 0:
        print("No searches yet.")

    else:
        for player in history:
            print(player)