import matplotlib.pyplot as plt


def season_points_chart(game_log, player_name, season):

    plt.figure(figsize=(14, 6))

    plt.plot(
        range(1, len(game_log) + 1),
        game_log["PTS"],
        marker="o",
        markersize=4,
        linewidth=2,
        label="Points"
    )

    average = game_log["PTS"].mean()

    plt.axhline(
        average,
        color="red",
        linestyle="--",
        linewidth=2,
        label=f"Season Average: {average:.1f} PPG"
    )

    plt.title(f"{player_name} - {season} Season Points Per Game", fontsize=16)

    plt.xlabel("Game Number", fontsize=12)
    plt.ylabel("Points", fontsize=12)

    plt.xticks(range(1, len(game_log) + 1, 5))

    plt.grid(True, linestyle="--", alpha=0.6)

    plt.legend()

    plt.tight_layout()

    plt.show()
