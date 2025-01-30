import requests
from bs4 import BeautifulSoup

# URLs for NBA, NFL, MLB, and NHL stats
url_stats_nba = "https://www.basketball-reference.com/leagues/NBA_2024_per_game.html"
url_stats_nfl = "https://www.pro-football-reference.com/years/2024/passing.htm"
url_stats_mlb = "https://www.baseball-reference.com/leagues/MLB_2024_batting.shtml"  # Batting stats URL update
url_stats_nhl = "https://www.hockey-reference.com/leagues/NHL_2024_skaters.html"

# Function to scrape top NBA player stats
def get_top_player_stats_nba(num_players=5):
    print("Scraping Top NBA Player Stats...\n")
    
    try:
        response = requests.get(url_stats_nba)
        response.raise_for_status()  # Check if request was successful
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the stats table
        table = soup.find('table', {'id': 'per_game_stats'})
        if table:
            rows = table.find_all('tr')[1:num_players + 1]  # Get the top players
            for row in rows:
                cols = row.find_all('td')
                if cols:
                    player_name = cols[0].text.strip()
                    points = cols[28].text.strip()  # Points per game (PTS column)
                    assists = cols[23].text.strip()  # Assists per game (AST column)
                    rebounds = cols[21].text.strip()  # Rebounds per game (TRB column)
                    print(f"{player_name}: {points} PPG, {assists} APG, {rebounds} RPG")
        else:
            print("Could not find the player stats table.")
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching NBA player stats: {e}")

# Function to scrape top NFL player stats
def get_top_player_stats_nfl(num_players=5):
    print("Scraping Top NFL Player Stats...\n")
    
    try:
        response = requests.get(url_stats_nfl)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the stats table
        table = soup.find('table', {'id': 'passing'})
        if table:
            rows = table.find_all('tr')[1:num_players + 1]
            for row in rows:
                cols = row.find_all('td')
                if cols:
                    player_name = cols[0].text.strip()
                    pass_yards = cols[1].text.strip()  # Passing yards
                    touchdowns = cols[2].text.strip()  # Touchdowns
                    interceptions = cols[3].text.strip()  # Interceptions
                    print(f"{player_name}: {pass_yards} Yards, {touchdowns} TDs, {interceptions} INTs")
        else:
            print("Could not find the player stats table.")
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching NFL player stats: {e}")

# Function to scrape top MLB player stats
def get_top_player_stats_mlb(num_players=5):
    print("Scraping Top MLB Player Stats...\n")
    
    try:
        response = requests.get(url_stats_mlb)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the stats table
        table = soup.find('table', {'class': 'stats_table'})
        if table:
            rows = table.find_all('tr')[1:num_players + 1]
            for row in rows:
                cols = row.find_all('td')
                if cols:
                    player_name = cols[0].text.strip()
                    avg = cols[1].text.strip()  # Batting Average
                    home_runs = cols[3].text.strip()  # Home Runs
                    rbi = cols[4].text.strip()  # RBIs
                    print(f"{player_name}: {avg} AVG, {home_runs} HR, {rbi} RBI")
        else:
            print("Could not find the player stats table.")
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching MLB player stats: {e}")

# Function to scrape top NHL player stats
def get_top_player_stats_nhl(num_players=5):
    print("Scraping Top NHL Player Stats...\n")
    
    try:
        response = requests.get(url_stats_nhl)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the stats table
        table = soup.find('table', {'class': 'stats_table'})
        if table:
            rows = table.find_all('tr')[1:num_players + 1]
            for row in rows:
                cols = row.find_all('td')
                if cols:
                    player_name = cols[0].text.strip()
                    goals = cols[1].text.strip()  # Goals
                    assists = cols[2].text.strip()  # Assists
                    points = cols[3].text.strip()  # Points
                    print(f"{player_name}: {goals} G, {assists} A, {points} P")
        else:
            print("Could not find the player stats table.")
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching NHL player stats: {e}")

# Run the functions with desired number of players
get_top_player_stats_nba(num_players=5)  # NBA
get_top_player_stats_nfl(num_players=5)  # NFL
get_top_player_stats_mlb(num_players=5)  # MLB
get_top_player_stats_nhl(num_players=5)  # NHL
