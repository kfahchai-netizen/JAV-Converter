from tkinter import *
from tkinter import ttk
from Converter_items_module import (
    convert_item_length,
    convert_item_area,
    convert_item_volume,
    convert_item_weight,
    convert_item_data_size,
    convert_human_to_dog,
    convert_dog_to_human,
)
from Gui_module import save_to_history_file, load_history, display_history, refresh_history_window, clear_history

def create_window(title, size):
    root = Tk()
    root.title(title)
    root.geometry(size)
    root.configure(bg="#f2f9f1")
    return root

def create_label(parent, text, font=None):
    label = Label(parent, text=text, font=font, bg="#f2f9f1")
    label.pack(pady=5)
    return label

def create_entry(parent):
    entry = Entry(parent)
    entry.pack()
    return entry

def create_option_menu(parent, variable, options):
    menu = OptionMenu(parent, variable, *options)
    menu.pack()
    return menu

def display_result(label, input_value, converted_value, from_unit, to_unit):
    if converted_value is not None:
        label.config(
            text=f"{input_value} {from_unit} is equal to {converted_value} {to_unit}"
        )
    else:
        label.config(text="Conversion not available.")

def perform_conversion(func, from_item, to_item, input_value, result_label, time_format=None):
    try:
        if not input_value or input_value.strip() == "":
            result_label.config(text="Please enter a valid number.")
            return

        value = float(input_value)
        #perform conversion
        result = func(from_item, to_item, value)
        if result is not None:
            #pass the input and converted values along with units
            display_result(result_label, value, result, from_item, to_item)
            
            #save to history
            save_to_history_file(from_item, to_item, value, result)
        else:
            result_label.config(text="Conversion not available.")
    except ValueError:
        result_label.config(text="Please enter a valid number.")
    except Exception as e:
        result_label.config(text="An error occurred during conversion.")
        print(f"Error: {e}")


def create_conversion_gui(conversion_type, from_items, to_items, func):
    root = create_window(f"{conversion_type} Conversion", "900x450")
    create_label(root, f"{conversion_type} Conversion", ("Arial", 16, "bold"))

    from_item = StringVar(root, from_items[0])  #default value is the first item
    to_item = StringVar(root, to_items[1])  #default value is different from 'from_item'
    create_label(root, "From Item:")
    create_option_menu(root, from_item, from_items)
    create_label(root, "To Item:")
    create_option_menu(root, to_item, to_items)

    create_label(root, "Enter Value:")
    user_input = create_entry(root)

    result_label = create_label(root, "", ("Arial", 12, "bold"))
    #converision button
    Button(
        root,
        text="Convert",
        command=lambda: perform_conversion(
            func, from_item.get(), to_item.get(), user_input.get(), result_label
        ),
        bg="#8fc79a",
        fg="white",
        font=("Arial", 12, "bold"),
    ).pack(pady=10)

    #history conversion button
    Button(
        root,
        text="Show History",
        command=display_history,
        bg="#f1a74a",
        fg="white",
        font=("Arial", 12, "bold"),
    ).pack(pady=10)

    Button(root, text="Back", command=root.destroy, bg="#e57b7b", fg="white", font=("Arial", 12, "bold")).pack(pady=10)

    root.mainloop()

def dog_years_conversion_gui():
    root = create_window("Dog ↔ Human Years Conversion", "900x450")
    create_label(root, "Dog ↔ Human Years Conversion", ("Arial", 16, "bold"))

    from_unit = StringVar(root, "Dog")  #default value "Dog"
    to_unit = StringVar(root, "Human")  #default value "Human"
    create_label(root, "From Unit:")
    create_option_menu(root, from_unit, ["Dog", "Human"])
    create_label(root, "To Unit:")
    create_option_menu(root, to_unit, ["Dog", "Human"])

    create_label(root, "Enter Value:")
    user_input = create_entry(root)

    result_label = create_label(root, "", ("Arial", 12, "bold"))

    def perform_convert_dog_human_years():
        try:
            value = float(user_input.get().strip())  #user input value
            if from_unit.get() == "Dog" and to_unit.get() == "Human":
                result = convert_dog_to_human(value)
                display_result(result_label, value, result, "Dog years", "Human years")
                #save to history
                save_to_history_file("Dog", "Human", value, result)
            elif from_unit.get() == "Human" and to_unit.get() == "Dog":
                result = convert_human_to_dog(value)
                display_result(result_label, value, result, "Human years", "Dog years")
                #save to history
                save_to_history_file("Human", "Dog", value, result)
            else:
                result_label.config(text="Conversion not available.")
        except ValueError:
            result_label.config(text="Please enter a valid number.")
        except Exception as e:
            result_label.config(text="An error occurred.")
            print(f"Error: {e}")

    Button(
        root,
        text="Convert",
        command=perform_convert_dog_human_years,
        bg="#8fc79a",
        fg="white",
        font=("Arial", 12, "bold"),
    ).pack(pady=10)

    #display conversion history
    Button(
        root,
        text="Show History",
        command=display_history,
        bg="#f1a74a",
        fg="white",
        font=("Arial", 12, "bold"),
    ).pack(pady=10)

    Button(root, text="Back", command=root.destroy, bg="#e57b7b", fg="white", font=("Arial", 12, "bold")).pack(pady=10)

#conversion GUIs
def item_length_conversion_gui():
    create_conversion_gui(
        "Length",
        ["Ant", "Guitar", "Red blood cell", "Eiffel tower", "Moon diameter"],
        ["Ant", "Guitar", "Red blood cell", "Eiffel tower", "Moon diameter"],
        convert_item_length,
    )

def item_area_conversion_gui():
    create_conversion_gui(
        "Area",
        ["Malaysia", "Swinburne", "Computer screen", "Bacteria", "Grain of salt"],
        ["Malaysia", "Swinburne", "Computer screen", "Bacteria", "Grain of salt"],
        convert_item_area,
    )

def item_volume_conversion_gui():
    create_conversion_gui(
        "Volume",
        ["Adult human blood", "Pacific ocean seawater", "Earth volume", "Water bottle", "Water droplet"],
        ["Adult human blood", "Pacific ocean seawater", "Earth volume", "Water bottle", "Water droplet"],
        convert_item_volume,
    )

def item_weight_conversion_gui():
    create_conversion_gui(
        "Weight",
        ["Elephant", "Mouse", "Aeroplane", "Ringgit bill", "Mount everest"],
        ["Elephant", "Mouse", "Aeroplane", "Ringgit bill", "Mount everest"],
        convert_item_weight,
    )

def item_data_size_conversion_gui():
    create_conversion_gui(
        "Data Size",
        ["copy of Dark souls 3", "Avengers: end game movie", "Swinburne logo png file", "Entire Wikipedia", "Ps5 storage"],
        ["copy of Dark souls 3", "Avengers: end game movie", "Swinburne logo png file", "Entire Wikipedia", "Ps5 storage"],
        convert_item_data_size,
    )
