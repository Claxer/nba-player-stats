# NBA Player Stats

## Description

A beginner-friendly Python project that allows users to search for NBA players and view their statistics, player information, recent game performance, and season graphs using the NBA API.

## Features

* Search for an NBA player
* Display player information (team, position, height, weight, jersey number, experience, college, country, and birthdate)
* Select the season to view
* Display player statistics
* Display stats from multiple teams if a player was traded
* Show combined statistics
* Handle historical seasons where some statistics (such as steals and blocks) were not officially recorded
* Display the player's last 10 games
* Display a graph of points scored during the selected season
* Display career totals (games, points, rebounds, assists, steals, blocks, turnovers, minutes, and shooting totals)
* Calculate and display career averages (PPG, RPG, APG, SPG, BPG, TOPG, and MPG)
* Search for another player
* Exit the program when finished

## Main Menu

```text
==============================
      NBA PLAYER STATS
==============================
1. Search Player
2. Career Statistics
3. Current Season
4. Last 10 Games
5. Awards
6. League Leaders
7. Standings
8. Compare Players
9. Exit
```

## Technologies Used

* Python 3
* NBA API
* PyCharm
* GitHub

## What I Learned

* Working with APIs
* Using Python functions
* Handling user input
* Using loops
* Working with data
* Handling invalid input
* Organizing a Python project
* Creating graphs with Matplotlib
* Using pandas DataFrames
* Separating a program into multiple Python files (modules)
* Retrieving and displaying player information from an API
* Handling missing data for historical NBA seasons
* Calculating career totals and career averages from multiple seasons
* Creating and using additional Python modules for new features
* Displaying structured career statistics separately from season statistics
* Creating a menu-driven console application
* Organizing code into reusable functions
* Comparing data from multiple NBA players
* Improving program navigation and user experience
* Building modular Python applications

## The Requirements to Run

* nba_api
* pandas
* matplotlib
* requests

## Project Structure

* `main.py` – Runs the program.
* `player_search.py` – Searches for NBA players.
* `player_info.py` – Retrieves and displays player information.
* `nba_api_handler.py` – Retrieves player data from the NBA API.
* `stats_display.py` – Displays player statistics.
* `last10_games.py` – Retrieves the player's last 10 games.
* `graphs.py` – Displays graphs of player performance.
* `career_stats.py` – Calculates and displays career totals and career averages.
* `comparison.py` – Compares two NBA players side-by-side.

## How to Run

1. Clone the repository.

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
```

2. Navigate to the project folder.

```bash
cd YOUR_REPOSITORY
```

3. Install the required libraries.

```bash
pip install nba_api pandas matplotlib requests
```

4. Run the program.

```bash
python main.py
```
