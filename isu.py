import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

def fetch_trade_data(league_size, scoring_type):
    """Fetch trade values from APIs based on league size and scoring type."""
    # Set PPR flag for scoring type
    if scoring_type == "PPR" :
        ppr = 1 
    else:
        ppr = 0

    # Fetch trade values
    trade_values_url = f"https://api.fantasycalc.com/values/current?isDynasty=false&numQbs=1&numTeams={league_size}&ppr={ppr}"
    trade_values = requests.get(trade_values_url).json()

    # Create dictionaries to store trade values
    try:
        trade_values_map = {}
        for player in trade_values:
            player_name = player['player']['name'].lower()
            overall_rank = player['overallRank']
            # Calculate trade value inversely proportional to overall rank
            trade_value = max(1, 200 - overall_rank)  # Higher rank = lower value
            trade_values_map[player_name] = trade_value
    except KeyError:
        st.error("Error: Unexpected response structure from the Trade Values API.")
        return []

    # Combine data into a list for easier processing
    combined_data = []
    for name, trade_value in trade_values_map.items():
        # Adjust trade value based on league size using a loop
        for size in range(6, 17):
            if league_size == size:
                trade_value *= 0.9 + (size - 6) * 0.02  # Scale adjustment based on league size
                break

        # Adjust trade value based on scoring type using if statements
        if scoring_type == "Standard":
            trade_value *= 1  # No adjustment for Standard
        elif scoring_type == "PPR":
            trade_value *= 1.1  # Increase value by 10% for PPR

        combined_data.append([name, trade_value])

    return combined_data

def analyze_trade(players_giving, players_getting, trade_data):
    """Analyze trade by calculating total values for giving and getting sides."""
    # Convert trade data into a dictionary for easier lookup
    trade_values_map = {item[0]: item[1] for item in trade_data}

    # Normalize user inputs and calculate values for both sides
    giving_value = sum(trade_values_map.get(player.lower(), 0) for player in players_giving)
    getting_value = sum(trade_values_map.get(player.lower(), 0) for player in players_getting)

    # Identify and warn about missing players
    missing_players = [player for player in (players_giving + players_getting) if player.lower() not in trade_values_map]
    if missing_players:
        st.warning(f"The following players were not found in the trade data: {', '.join(missing_players)}")

    # Provide a recommendation based on values
    if getting_value > giving_value:
        recommendation = "Accept"
    else:
        recommendation = "Decline"

    return giving_value, getting_value, recommendation

def create_trade_chart(giving_value, getting_value):
    """Create a bar chart to compare trade values."""
    labels = ['Giving', 'Getting']
    values = [giving_value, getting_value]

    fig, ax = plt.subplots()
    ax.bar(labels, values, color=['blue', 'green'])
    ax.set_title("Trade Value Comparison")
    ax.set_ylabel("Total Value")
    return fig

def display_recommendation(recommendation):
    """Display thumbs up or thumbs down based on recommendation."""
    if recommendation == "Accept":
        st.markdown("<h1 style='text-align: center;'>👍</h1>", unsafe_allow_html=True)
    else:
        st.markdown("<h1 style='text-align: center;'>👎</h1>", unsafe_allow_html=True)

# Streamlit Interface
st.title("Fantasy Football Trade Analyzer")

# Sidebar Inputs
scoring_type = st.sidebar.selectbox("Scoring Type", ["PPR", "Standard"])
league_size = st.sidebar.slider("League Size", 6, 16, step=1)

# Main Inputs
st.header("Trade Details")
players_giving = st.text_area("Players Giving (one per line)").splitlines()
players_getting = st.text_area("Players Getting (one per line)").splitlines()

if st.button("Analyze Trade"):
    try:
        # Fetch data based on user inputs
        trade_data = fetch_trade_data(league_size, scoring_type)

        # Analyze the trade
        giving_value, getting_value, recommendation = analyze_trade(players_giving, players_getting, trade_data)

        # Display results
        st.write(f"Total Value for Giving Side: {giving_value}")
        st.write(f"Total Value for Getting Side: {getting_value}")
        st.write(f"Recommendation: {recommendation}")

        # Display thumbs up or thumbs down
        display_recommendation(recommendation)

        # Display chart
        fig = create_trade_chart(giving_value, getting_value)
        st.pyplot(fig)

    except Exception as e:
        st.error(f"An error occurred: {e}")
