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
* Search for another player
* Exit the program when finished

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

## How to Run

1. Clone or download the repository.
2. Install the required libraries:
