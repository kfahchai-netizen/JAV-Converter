import pygame
from tkinter import Tk, Label, Frame, StringVar, Radiobutton, Button, messagebox
from Gui_module import area_conversion_gui, time_conversion_gui, weight_conversion_gui, length_conversion_gui, temperature_converter_gui, volume_conversion_gui
from Gui_items_module import item_length_conversion_gui, item_area_conversion_gui, item_volume_conversion_gui, item_weight_conversion_gui, item_data_size_conversion_gui, dog_years_conversion_gui

#Sound import
pygame.mixer.init()

def play_button_sound():
    pygame.mixer.music.load("button-pressed.mp3")  
    pygame.mixer.music.play()

def main_window():
    root = Tk()
    root.title("JAV Unit Conversion")
    root.geometry('500x500')  #Window size
    root.configure(bg="#f2f9f1")  #color theme
    root.resizable(False, False)

    #title & subtitle
    lbl = Label(root, text="Welcome to JAV Unit Conversion!", font=("Arial", 16), bg="#f2f9f1", fg="black")
    lbl.pack(pady=10)
    lbl_subtitle = Label(root, text="Please select the unit you would like to convert", font=("Arial", 12), bg="#f2f9f1", fg="black")
    lbl_subtitle.pack(pady=5)

    #frame for buttons
    radio_frame = Frame(root, bg="#d4edd9")
    radio_frame.pack(pady=10)

    #frame
    standard_radio_frame = Frame(radio_frame, bg="#f2f9f1")
    item_radio_frame = Frame(radio_frame, bg="#f2f9f1")

    #button for selection
    def show_standard_conversion():
        standard_radio_frame.pack(fill="both", expand=True)
        item_radio_frame.pack_forget()

    def show_item_conversion():
        item_radio_frame.pack(fill="both", expand=True)
        standard_radio_frame.pack_forget()

    def show_standard_selection():
        selected_option = var.get()
        conversion_functions = {
            'Area': area_conversion_gui,
            'Length': length_conversion_gui,
            'Time': time_conversion_gui,
            'Weight': weight_conversion_gui,
            'Temperature': temperature_converter_gui,
            'Volume': volume_conversion_gui
        }
        conversion_functions.get(selected_option, lambda: None)()

    def show_item_converter_selection():
        selected_option = var.get()
        item_conversion_functions = {
            'Item Length': item_length_conversion_gui,
            'Item Area': item_area_conversion_gui,
            'Item Volume': item_volume_conversion_gui,
            'Item Weight': item_weight_conversion_gui,
            'Item Data Size': item_data_size_conversion_gui,
            'Dog Year': dog_years_conversion_gui
        }
        item_conversion_functions.get(selected_option, lambda: None)()

    #help
    def show_help():
        messagebox.showinfo("Help", "Select from the checkboxes then click submit for the unit you would like to convert!\nClick Toggle Fun for the Fun conversion!\nClick view history to view your past conversion, click clear history to clear you past conversion!")
        play_button_sound()  #play a sound

    #toggle fun
    is_on = True

    def toggle_theme():
        nonlocal is_on
        if is_on:
            toggle_button.configure(relief="sunken", bd=5)  #depth button thing
            root.configure(bg="pink")
            lbl.configure(bg="pink", fg="red4")
            lbl_subtitle.configure(bg="pink", fg="red4", text="Please select the \"FUN\" unit you would like to convert")  #change subtitle
            update_radio_button_colors("pink", "red4", "pink", "pink")
            update_button_colors("pink2", "black")
            button_frame.configure(bg="pink")  #change the button frame to pink
            var.set("Item Length")
            show_item_conversion()
            fun_mode_label.configure(text="Fun mode: On", fg="black", bg="pink")

            #Play "toggle-button-on.mp3"
            pygame.mixer.music.load("toggle-button-on.mp3")
            pygame.mixer.music.play()

            is_on = False
        else:
            toggle_button.configure(relief="raised", bd=2)  #button to default
            root.configure(bg="#f2f9f1")
            lbl.configure(bg="#f2f9f1", fg="black")
            lbl_subtitle.configure(bg="#f2f9f1", fg="black", text="Please select the unit you would like to convert")  #reset subtitke
            update_radio_button_colors("#f2f9f1", "black", "#f2f9f1", "#f2f9f1")
            update_button_colors("#d4edd9", "black")
            button_frame.configure(bg="#f2f9f1")  #revert button back to normal
            var.set("Length")
            show_standard_conversion()
            fun_mode_label.configure(text="Fun mode: Off", fg="black", bg="#f2f9f1")

            #play "toggle-button-off.mp3"
            pygame.mixer.music.load("toggle-button-off.mp3")
            pygame.mixer.music.play()

            is_on = True

    #update button color for all the scalar unit
    def update_radio_button_colors(radio_bg_color, radio_fg_color, frame_bg_color, select_color):
        for frame in [standard_radio_frame, item_radio_frame]:
            for widget in frame.winfo_children():
                if isinstance(widget, Radiobutton):
                    widget.configure(bg=radio_bg_color, fg=radio_fg_color, selectcolor=select_color)
        standard_radio_frame.configure(bg=frame_bg_color)
        item_radio_frame.configure(bg=frame_bg_color)

    #update button color/submit/toggle/close/help
    def update_button_colors(button_bg, button_fg):
        for button in [submit_button, toggle_button, close_button, help_button]:
            button.configure(bg=button_bg, fg=button_fg, highlightbackground=button_bg)

    #radiobutton
    var = StringVar(value="Length")
    standard_options = ["Length", "Area", "Time", "Weight", "Temperature", "Volume"]
    item_options = ["Item Length", "Item Area", "Item Volume", "Item Weight", "Item Data Size", "Dog Year"]

    def create_radio_buttons(options, frame, theme):
        for option in options:
            Radiobutton(frame, text=option, variable=var, value=option, bg=theme, fg="black", selectcolor="white").pack(anchor='center', pady=5)

    create_radio_buttons(standard_options, standard_radio_frame, "#f2f9f1")
    create_radio_buttons(item_options, item_radio_frame, "pink")

    #initial view
    show_standard_conversion()

    #control button
    button_frame = Frame(root, bg="#f2f9f1")
    button_frame.pack(pady=10)

    submit_button = Button(button_frame, text="Submit", command=lambda: [play_button_sound(), show_standard_selection() if var.get() in standard_options else show_item_converter_selection()])
    toggle_button = Button(button_frame, text="Toggle Fun", command=toggle_theme)
    close_button = Button(button_frame, text="Close", command=lambda: [play_button_sound(), root.destroy()])
    help_button = Button(button_frame, text="Help", command=lambda: [play_button_sound(), show_help()])
    #initial position of buttons
    submit_button.pack(side="left", padx=10)
    toggle_button.pack(side="left", padx=10)
    close_button.pack(side="left", padx=10)
    help_button.pack(side="left", padx=10)

    #fun mode state label
    fun_mode_label = Label(root, text="Fun mode: Off", font=("Arial", 12), bg="#f2f9f1", fg="black")
    fun_mode_label.pack(pady=10)

    #initial button colors
    update_button_colors("#d4edd9", "black")

    root.mainloop()

#run programme
if __name__ == "__main__":
    main_window()
