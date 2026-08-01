def export(stats):

    stats.to_csv("player_stats.csv", index=False)

    print("Statistics saved to player_stats.csv")