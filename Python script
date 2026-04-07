"""
Final Project: Vortex Lab
Description: Simulates a tornadic event based on historical NOAA data.
For entertainment and educational use only.
"""

# main.py

from ui import title_screen

def main():
  """Launch the program and show the title screen."""
  title_screen()

if __name__ == "__main__":
  main()

# ui.py

import tkinter as tk

def title_screen():
  """
  Display the title screen.

  Shows:
  - program title
  - color background with tornado image
  - 'Start' button that opens the input screen
  - 'Quit' button that exits the program
  """
  pass

def get_user_inputs():
  """
  Display the user input screen and ask for simulation parameters.

  Widgets:
    - Dropdown menu for U.S. state selection
    - Dropdown menu for month selection (January-December)
    - Text entry field for temperature (numeric, °F)
    - Text entry field for humidity (numeric, 0-100%)
    - "Generate Tornado Event" button

  Parameters:
    None

  Returns:
    dict: {
        "state": str, # state abbreviation, e.g. "IL"
        "month": int, # month number, 1-12
        "temperature": int,
        "humidity": int
    }

  Raises:
    ValueError: if user enters non-numeric values for temperature or humidity fields
  """
  pass

# data.py

import pandas as pd
import random

def load_and_filter_data(filepath, state, month):
  """
  Load tornado data CSV from NOAA and filter by state and month.

  CSV columns:
    state (str): two-letter uppercase state abbreviation
    month (int): month number 1-12
    ef_rating (int): EF Scale rating 0-5
    wind_speed (int): wind speed in mph
    path_width (int): path width in yards
    fatalities (int): number of fatalities
    county (str): county or area name

  Parameters:
    filepath (str): path to the CSV file, tornado_data.csv
    state (str): state abbreviation to filter by
    month (int): month number to filter by

  Returns:
    pandas.DataFrame: rows matching the given state and month
                      returns empty DataFrame if no matches found

  Prints "Low chance of tornado formation." If less than a minimum number of historical 
  records exist for the given state/month.
  """
  pass

def generate_tornado_event(filtered_data, temperature, humidity):
  """
  Generate a simulated tornado event from historical records and user inputs.

  EF rating probabilities are adjusted higher for higher temperature and humidity values.

  Parameters:
    filtered_data (pandas.DataFrame): filtered records from load_and_filtered data()
    temperature (int): surface temperature in °F
    humidity (int): relative humidity, 0-100

  Returns:
    dict: {
        "state": str, # state abbreviation
        "county": str, # county or area name
        "month": int, # month number
        "day": int, # random day in the month
        "ef_rating": int, # EF Scale 0-5
        "wind_speed": int, # mph
        "path_width": int, # yards
        "fatalities": int
    }
  pass

# animation.py

import turtle

def run_animation(ef_rating):
  """
  Run the Turtle graphics tornado animation.

  Animation sequence:
    1. draw background: sky, ground, houses, and vehicles
    2. Animate tornado entering from left side of screen, rotating and moving towards the right
    toward the structures.
    3. After the tornado passes, redraw structures to reflect damage based on ef_rating
      EF0: minor roof damage
      EF1-EF2: more significant roof damage, broken windows, houses shifted, vehicles overturned
      EF3-EF4: houses destroyed, vehicles thrown a significant distance
      EF5: total destruction

  Parameters:
    ef_rating (int): EF Scale rating 0-5

  Returns:
    None
  """
  pass

def draw_background():
  """
  Draw the sky and ground.
  """
  pass

def draw_structures():
  """
  Place houses and vehicles in their original state using turtle.stamp()

  Images of structures are registered as GIFs. E.g.:
    house.gif: intact house
    car.gif: intact car

  Parameters:
    None

  Returns:
    A tuple of (x, y) entries for each structure so draw_damaged() knows where 
    to re-stamp the damaged versions.
  """
  pass

def animate_tornado():
  """
  Animate the tornado moving across the screen with rotation.
  """
  pass

def draw_damage(ef_rating):
  """
  Replace structure images with damaged versions based on EF rating.

  Clears original structure stamps and re-stamps damaged image versions at the same 
  positions returned by draw_structures. Damage level is determined by ef_rating.

  Example GIFs:
    ef0_house.gif: EF0 damaged house
    ef34_car.gif: EF3-EF4 damaged car

  Parameters:
    ef_rating (int)

  Returns:
    None
  """
  pass

# ui.py

def display_report(event)
  """
  Display simulated tornado report in a Tkinter window.
  Called after run_animation().

  Parameters:
    event (dict): Tornado event data returned by generate_tornado_event().

  Displays:
    - Location (county, state)
    - Date (month and day)
    - EF Scale rating
    - Wind speed (mph)
    - path width (yards)
    - Fatalities
    - "Generate New Tornado" button: calls get_user_inputs()
    - "Quit to Menu" button: calls title_screen()

  Returns:
    None
  """
  pass
