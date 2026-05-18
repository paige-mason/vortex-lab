# vortex-lab

## Description
Vortex Lab is a tornado simulator that generates a tornado event using user inputs and historical data from the National Oceanic and Atmospheric Administration (NOAA).

Users input:
- U.S. state
- month
- temperature
- humidity

The program then filters the historical data and returns:
- location (state and county)
- EF rating
- wind speed
- path width
- path length
- fatalities

The program displays an animation of the tornado event with damage visualization.

### Features
- GUI using Tkinter
- Turtle animation
- tests using Pytest

## How to Run
- install uv
- to run: uv run python main.py
- to run tests: uv run python tests