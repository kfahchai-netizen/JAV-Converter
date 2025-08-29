from tkinter import *
from tkinter import ttk
from random import choice
from Converter_module import convert_area, time_converter, convert_weight, convert_length, convert_temperature, convert_volume

#Fun facts for each unit
fun_facts = {
    "area": [
        "Did you know? The largest area ever recorded was about 3.5 million square miles!",
        "One acre is roughly equivalent to 4046.86 square meters.",
        "The square kilometer is used globally to measure large areas like cities or countries.",
        "Did you know? A square has the smallest perimeter for the largest area!"
    ],
    "time": [
        "Did you know? A second is defined based on the vibrations of cesium atoms.",
        "The longest time ever recorded by a human is the 6-year mission to Mars.",
        "A minute has exactly 60 seconds, but the definition of a second has changed over time!"
    ],
    "weight": [
        "Did you know? The kilogram was originally defined by the mass of a particular platinum cylinder.",
        "One ton is equal to 1,000 kilograms.",
        "A gram is the basic unit of mass in the metric system, and it’s approximately equal to the mass of one cubic centimeter of water."
    ],
    "length": [
        "Did you know? The longest length ever measured on Earth is the equator—40,075 kilometers!",
        "A kilometer is 1000 meters, and it’s the standard unit for measuring distance in many countries.",
        "The meter is the basic unit of length in the metric system, and it was originally defined by the distance between two lines on a platinum bar."
    ],
    "temperature": [
        "Did you know? The Fahrenheit scale was created by Daniel Gabriel Fahrenheit in 1724.",
        "Water freezes at 0°C (Celsius), 32°F (Fahrenheit), and 273.15K (Kelvin).",
        "The Kelvin scale starts at absolute zero, where all molecular movement stops."
    ],
    "volume": [
        "Did you know? A liter is equivalent to 1 cubic decimeter (dm³).",
        "The volume of an object can be calculated by multiplying its length, width, and height.",
        "In the metric system, the liter is used to measure both liquid and solid volumes."
    ]
}

#create display fun fact based on the category
def display_fun_fact(label, category):
    fact = choice(fun_facts[category])
    label.config(text=f"Fun Fact: {fact}")

#window creator
def create_window(title, size):
    root = Tk()
    root.title(title)
    root.geometry(size)
    root.configure(bg="#f2f9f1")
    return root

#label creator
def create_label(parent, text, font=None):
    label = Label(parent, text=text, font=font, bg="#f2f9f1")
    label.pack(pady=5)
    return label

#entry creation
def create_entry(parent):
    entry = Entry(parent)
    entry.pack()
    return entry

#option menu creator
def create_option_menu(parent, variable, options):
    menu = OptionMenu(parent, variable, *options)
    menu.pack()
    return menu

#result display
def display_result(label, result, unit):
    if result is not None:
        label.config(text=f"Result: {result} {unit}")
    else:
        label.config(text="Conversion not available.")

#perform conversion and put in the funfact
def perform_conversion(func, from_unit, to_unit, value, result_label, fun_fact_label, category):
    try:
        if value is None or value.strip() == "":
            result_label.config(text="Please enter a valid number.")
            return

        result = func(from_unit, to_unit, float(value))
        display_result(result_label, result, to_unit)
        display_fun_fact(fun_fact_label, category)  #show a unit specific fun fact
        
        #automatically save the history
        save_to_history_file(from_unit, to_unit, value, result)

    except ValueError:
        result_label.config(text="Please enter a valid number.")
    except Exception as e:
        result_label.config(text="An error occurred during conversion.")
        print(f"Error: {e}")

#save conversion history into a file
def save_to_history_file(from_unit, to_unit, value, result, time_format=None):
    with open("conversion_history.txt", "a") as file:
            file.write(f"Conversion: {value} {from_unit} to {result} {to_unit}\n")

#load the conversion history
def load_history():
    try:
        with open("conversion_history.txt", "r") as file:
            history = file.readlines()
        return history
    except FileNotFoundError:
        return []

#clear conversion history
def clear_history():
    with open("conversion_history.txt", "w") as file:
        file.truncate(0)
    refresh_history_window()

#refresh history
def refresh_history_window():
    global history_window
    history = load_history()

    #clear the existing content
    for widget in history_window.winfo_children():
        widget.destroy()

    #display new history
    if not history:
        create_label(history_window, "No conversion history found.", ("Arial", 14))
    else:
        for record in history:
            create_label(history_window, record.strip(), ("Arial", 12))

    #clear history and close button
    Button(history_window, text="Clear History", command=clear_history, bg="#7bc6ff", fg="white", font=("Arial", 12, "bold")).pack(pady=10)
    Button(history_window, text="Close", command=history_window.destroy, bg="#e57b7b", fg="white", font=("Arial", 12, "bold")).pack(pady=10)

#display conversion history in another window
def display_history():
    global history_window

    #one window open at a time
    if 'history_window' in globals() and history_window.winfo_exists():
        return

    history_window = Toplevel()
    history_window.title("Conversion History")

    #text frame and scroll bar
    frame = Frame(history_window)
    frame.pack(fill=BOTH, expand=True)

    #display history text
    text_widget = Text(frame, wrap=WORD, font=("Arial", 12), bg="#f2f9f1")
    text_widget.pack(side=LEFT, fill=BOTH, expand=True)

    #scroll bar linked to text
    scrollbar = Scrollbar(frame, command=text_widget.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    text_widget.config(yscrollcommand=scrollbar.set)

    #load and display history
    history = load_history()
    if not history:
        text_widget.insert(END, "No conversion history found.\n")
    else:
        for record in history:
            text_widget.insert(END, record)

    text_widget.config(state=DISABLED)  #read only text

    #buttons
    Button(history_window, text="Clear History", command=clear_history, bg="#7bc6ff", fg="white", font=("Arial", 12, "bold")).pack(pady=10)
    Button(history_window, text="Close", command=history_window.destroy, bg="#e57b7b", fg="white", font=("Arial", 12, "bold")).pack(pady=10)

#Area conversion GUI
def area_conversion_gui():
    root = create_window("Area Unit Conversion", "900x450")
    create_label(root, "Area Conversion", ("Arial", 16, "bold"))

    from_unit = StringVar(root, "m²")
    to_unit = StringVar(root, "km²")
    create_label(root, "From Unit:"); create_option_menu(root, from_unit, ["m²", "km²", "cm²", "mm²", "µm²"])
    create_label(root, "To Unit:"); create_option_menu(root, to_unit, ["m²", "km²", "cm²", "mm²", "µm²"])

    create_label(root, "Enter Value:")
    user_input = create_entry(root)

    result_label = create_label(root, "", ("Arial", 12, "bold"))
    fun_fact_label = create_label(root, "", ("Arial", 12, "italic"))

    Button(root, text="Convert", command=lambda: perform_conversion(convert_area, from_unit.get(), to_unit.get(), user_input.get(), result_label, fun_fact_label, "area"), bg="#8fc79a", fg="white", font=("Arial", 12, "bold")).pack(pady=10)
    Button(root, text="View History", command=display_history, bg="#f1a74a", fg="white", font=("Arial", 12, "bold")).pack(pady=10)
    Button(root, text="Back", command=root.destroy, bg="#e57b7b", fg="white", font=("Arial", 12, "bold")).pack(pady=10)

#Time conversion GUI
def time_conversion_gui():
    root = create_window("Time Conversion", "900x450")
    create_label(root, "Time Conversion", ("Arial", 16, "bold"))

    conversion_choice = StringVar(root)
    conversion_choice.set("24 to 12 hours")
    OptionMenu(root, conversion_choice, "24 to 12 hours", "12 to 24 hours").pack()

    Label(root, text="Select Time:", bg="#f2f9f1").pack(pady=5)

    hours = StringVar(root)
    hour_dropdown = ttk.Combobox(root, textvariable=hours, state="readonly", width=5)
    hour_dropdown['values'] = tuple(range(24))
    hour_dropdown.set("0")
    hour_dropdown.pack()

    minutes = StringVar(root)
    minute_dropdown = ttk.Combobox(root, textvariable=minutes, state="readonly", width=5)
    minute_dropdown['values'] = tuple(range(60))
    minute_dropdown.set("0")
    minute_dropdown.pack()

    meridian_choice = StringVar(root)
    meridian_choice.set("AM")
    meridian_dropdown = OptionMenu(root, meridian_choice, "AM", "PM")

    result_label = Label(root, text="", bg="#f2f9f1", font=("Arial", 12, "bold"), wraplength=400, justify=LEFT)
    result_label.pack(pady=10)

    fun_fact_label = create_label(root, "", ("Arial", 12, "italic"))

    def toggle_meridian_option(*args):
        if conversion_choice.get() == "12 to 24 hours":
            meridian_dropdown.pack()
            hour_dropdown['values'] = tuple(range(1, 13))
            hour_dropdown.set("1")
        else:
            meridian_dropdown.pack_forget()
            hour_dropdown['values'] = tuple(range(24))
            hour_dropdown.set("0")

    conversion_choice.trace("w", toggle_meridian_option)

    def perform_time_conversion():
        try:
            conversion_type = '1' if conversion_choice.get() == "24 to 12 hours" else '2'
            hour = int(hours.get())
            minute = int(minutes.get())
            meridian = meridian_choice.get() if conversion_type == '2' else None

            time_str = f"{hour:02}:{minute:02}"
            result = time_converter(conversion_type, time_str, meridian)
            result_label.config(text=f"Converted Time: {result}")
            display_fun_fact(fun_fact_label, "time")

            #determine the time format (for time conversions only)
            time_format = "12-hour" if conversion_choice.get() == "12 to 24 hours" else "24-hour"

            #save the time conversion result to history with the time format
            save_to_history_file("Time", time_format, time_str, result, time_format=time_format)
        except Exception as e:
            result_label.config(text="An error occurred during conversion.")
            print(f"Error: {e}")

    Button(root, text="Convert", command=perform_time_conversion, bg="#8fc79a", fg="white", font=("Arial", 12, "bold")).pack(pady=10)
    Button(root, text="View History", command=display_history, bg="#f1a74a", fg="white", font=("Arial", 12, "bold")).pack(pady=10)
    Button(root, text="Back", command=root.destroy, bg="#e57b7b", fg="white", font=("Arial", 12, "bold")).pack(pady=10)

#Weight conversion GUI
def weight_conversion_gui():
    root = create_window("Weight Conversion", "900x450")
    create_label(root, "Weight Conversion", ("Arial", 16, "bold"))

    from_unit = StringVar(root, "g")
    to_unit = StringVar(root, "kg")
    create_label(root, "From Unit:"); create_option_menu(root, from_unit, ["g", "kg", "mg", "t"])
    create_label(root, "To Unit:"); create_option_menu(root, to_unit, ["g", "kg", "mg", "t"])

    create_label(root, "Enter Value:")
    user_input = create_entry(root)

    result_label = create_label(root, "", ("Arial", 12, "bold"))
    fun_fact_label = create_label(root, "", ("Arial", 12, "italic"))

    Button(root, text="Convert", command=lambda: perform_conversion(convert_weight, from_unit.get(), to_unit.get(), user_input.get(), result_label, fun_fact_label, "weight"), bg="#8fc79a", fg="white", font=("Arial", 12, "bold")).pack(pady=10)
    Button(root, text="View History", command=display_history, bg="#f1a74a", fg="white", font=("Arial", 12, "bold")).pack(pady=10)
    Button(root, text="Back", command=root.destroy, bg="#e57b7b", fg="white", font=("Arial", 12, "bold")).pack(pady=10)

#Length conversion GUI
def length_conversion_gui():
    root = create_window("Length Conversion", "900x450")
    create_label(root, "Length Conversion", ("Arial", 16, "bold"))

    from_unit = StringVar(root, "m")
    to_unit = StringVar(root, "km")
    create_label(root, "From Unit:"); create_option_menu(root, from_unit, ["m", "km", "cm", "mm", "micrometer"])
    create_label(root, "To Unit:"); create_option_menu(root, to_unit, ["m", "km", "cm", "mm", "micrometer"])

    create_label(root, "Enter Value:")
    user_input = create_entry(root)

    result_label = create_label(root, "", ("Arial", 12, "bold"))
    fun_fact_label = create_label(root, "", ("Arial", 12, "italic"))

    Button(root, text="Convert", command=lambda: perform_conversion(convert_length, from_unit.get(), to_unit.get(), user_input.get(), result_label, fun_fact_label, "length"), bg="#8fc79a", fg="white", font=("Arial", 12, "bold")).pack(pady=10)
    Button(root, text="View History", command=display_history, bg="#f1a74a", fg="white", font=("Arial", 12, "bold")).pack(pady=10)
    Button(root, text="Back", command=root.destroy, bg="#e57b7b", fg="white", font=("Arial", 12, "bold")).pack(pady=10)

#Temperature conversion GUI
def temperature_converter_gui():
    root = create_window("Temperature Conversion", "900x450")
    create_label(root, "Temperature Conversion", ("Arial", 16, "bold"))

    from_unit = StringVar(root, "Celsius")
    to_unit = StringVar(root, "Fahrenheit")
    create_label(root, "From Unit:"); create_option_menu(root, from_unit, ["Celsius", "Fahrenheit", "Kelvin"])
    create_label(root, "To Unit:"); create_option_menu(root, to_unit, ["Celsius", "Fahrenheit", "Kelvin"])

    create_label(root, "Enter Value:")
    user_input = create_entry(root)

    result_label = create_label(root, "", ("Arial", 12, "bold"))
    fun_fact_label = create_label(root, "", ("Arial", 12, "italic"))

    Button(root, text="Convert", command=lambda: perform_conversion(convert_temperature, from_unit.get(), to_unit.get(), user_input.get(), result_label, fun_fact_label, "temperature"), bg="#8fc79a", fg="white", font=("Arial", 12, "bold")).pack(pady=10)
    Button(root, text="View History", command=display_history, bg="#f1a74a", fg="white", font=("Arial", 12, "bold")).pack(pady=10)
    Button(root, text="Back", command=root.destroy, bg="#e57b7b", fg="white", font=("Arial", 12, "bold")).pack(pady=10)

#Volume conversion GUI
def volume_conversion_gui():
    root = create_window("Volume Conversion", "900x450")
    create_label(root, "Volume Conversion", ("Arial", 16, "bold"))

    from_unit = StringVar(root, "L")
    to_unit = StringVar(root, "mL")
    create_label(root, "From Unit:"); create_option_menu(root, from_unit, ["L", "mL", "cm³", "m³","mm³","km³"])
    create_label(root, "To Unit:"); create_option_menu(root, to_unit, ["L", "mL", "cm³", "m³","mm³","km³"])

    create_label(root, "Enter Value:")
    user_input = create_entry(root)

    result_label = create_label(root, "", ("Arial", 12, "bold"))
    fun_fact_label = create_label(root, "", ("Arial", 12, "italic"))

    Button(root, text="Convert", command=lambda: perform_conversion(convert_volume, from_unit.get(), to_unit.get(), user_input.get(), result_label, fun_fact_label, "volume"), bg="#8fc79a", fg="white", font=("Arial", 12, "bold")).pack(pady=10)
    Button(root, text="View History", command=display_history, bg="#f1a74a", fg="white", font=("Arial", 12, "bold")).pack(pady=10)
    Button(root, text="Back", command=root.destroy, bg="#e57b7b", fg="white", font=("Arial", 12, "bold")).pack(pady=10)

