import tkinter as tk
from tkinter import ttk

STATES = [
    "Alabama", 
    "Alaska",
    "Arizona",
    "Arkansas",
    "California",
    "Colorado",
    "Connecticut",
    "Delaware",
    "Florida",
    "Georgia",
    "Hawaii",
    "Idaho",
    "Illinois",
    "Indiana",
    "Iowa",
    "Kansas",
    "Kentucky",
    "Louisiana",
    "Maine",
    "Maryland",
    "Massachusetts",
    "Michigan",
    "Minnesota",
    "Mississippi",
    "Missouri",
    "Montana",
    "Nebraska",
    "Nevada",
    "New Hampshire",
    "New Jersey",
    "New Mexico",
    "New York",
    "North Carolina",
    "North Dakota",
    "Ohio",
    "Oklahoma",
    "Oregon",
    "Pennsylvania",
    "Rhode Island",
    "South Carolina",
    "South Dakota",
    "Tennessee",
    "Texas",
    "Utah",
    "Vermont",
    "Virginia",
    "Washington",
    "West Virginia",
    "Wisconsin",
    "Wyoming",
]

MONTHS = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

def title_screen():
    root = tk.Tk()

    root.title("Vortex Lab")
    root.geometry("600x400")

    root.configure(bg="gray20")

    title_label = tk.Label(
        root,
        text="VORTEX LAB",
        font=("Arial", 24, "bold"),
        bg="gray20",
        fg="white"
    )

    title_label.pack(pady=40)

    # tornado image

    start_button = tk.Button(
        root,
        text="Start",
        command=lambda: start_program(root)
    )

    start_button.pack(pady=10)

    quit_button = tk.Button(
        root,
        text="Quit",
        command=root.destroy
    )

    quit_button.pack(pady=10)

    root.mainloop()

def start_program(root):
    root.destroy()

    user_inputs = get_user_inputs()
    print(user_inputs)

def get_user_inputs():
    root = tk.Tk()

    root.title("Sim Parameters")
    root.geometry("500x400")

    state_var = tk.StringVar()
    month_var = tk.StringVar()
    temp_var = tk.StringVar()
    humidity_var = tk.StringVar()

    user_inputs = {}

    state_label = tk.Label(root, text="Select State:")
    state_label.pack()

    state_dropdown = ttk.Combobox(
        root,
        textvariable=state_var,
        values=STATES,
        state="readonly"
    )

    state_dropdown.pack()

    state_dropdown.current(0)

    month_label = tk.Label(root, text="Select Month:")
    month_label.pack()

    month_dropdown = ttk.Combobox(
        root,
        textvariable=month_var,
        values=list(MONTHS.keys()),
        state="readonly"
    )

    month_dropdown.pack()

    month_dropdown.current(0)

    temp_label = tk.Label(root, text="Temperature (°F):")
    temp_label.pack()

    temp_entry = tk.Entry(root, textvariable=temp_var)
    temp_entry.pack()

    humidity_label = tk.Label(root, text="Humidity (%):")
    humidity_label.pack()

    humidity_entry = tk.Entry(root, textvariable=humidity_var)
    humidity_entry.pack()

    def submit_inputs():
        try:
            temperature = int(temp_var.get())
            humidity = int(humidity_var.get())

            user_inputs["state"] = state_var.get()
            user_inputs["month"] = MONTHS[month_var.get()]
            user_inputs["temperature"] = temperature
            user_inputs["humidity"] = humidity

            root.destroy()
        except ValueError:
            error_label.config(
                text="Temperature and humidity inputs must be numbers."
            )

        generate_button = tk.Button(
            root,
            text="Generate Tornado Event",
            command=submit_inputs
        )
    
        generate_button.pack(pady=20)

        error_label = tk.Label(
            root,
            text="",
            fg="red"
        )

        error_label.pack()
        root.mainloop()
        return user_inputs