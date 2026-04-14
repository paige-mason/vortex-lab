# vortex-lab

The purpose of this program is to simulate a tornadic event based on historical data. It is intended for entertainment only and is not a tool for predicting real meteorological outcomes.

**Functions**

<ins>Title Screen</ins>
- using Tkinter, this function will:
  - display the title of the simulator
  - include start and end buttons
  - display a color background and an image of a tornado

<ins>User Inputs</ins>
- uses Tkinter
  - prompt user for state, month, temperature, and humidity inputs
    - includes a drop down menu for state and month, and text input fields for temperature and humidity in numerical values
  - "generate tornado event" button

 <ins>Load and Filter Tornado Data</ins>
 - load data from CSV, sourced from NOAA records
   - data is listed in strings and integers
 - return tornadoes matching state and month inputs
 - adjust Enhanced Fujita (EF) Scale rating probability based on inputs
 - if tornado is unlikely based on inputs, print "low chance of tornado formation"
   - likelihood based on number of tornadoes that occured in that state and month
 - generate simulated tornado
   - includes the state, month, EF rating, wind speed, path width, and fatalities

<ins>Animation</ins>
- uses Turtle
  - displays a scene to represent the generated tornado event, including:
    - sky and ground
    - houses and vehicles
    - tornado
  - When the animation begins, the tornado will start at the left side of the screen and move with rotation towards the houses and vehicles on the right
  - After the tornado has moved past the structures, they will change to reflect damage based on EF rating.

<ins>Display Simulated Tornado Report</ins>
- This function will display the generated report, including:
  - the location, including the city or county and state
  - month and day
  - EF Scale rating
  - wind speed
  - path width
  - fatalities
- Tkinter will be used to show "generate new tornado" and "quit to menu" buttons
