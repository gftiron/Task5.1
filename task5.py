from tkinter import *
import tkinter.font
from gpiozero import LED


# Define LED pins and their corresponding colors
led_pins = {
    "Green": 14,
    "Red": 15,
    "Orange": 18
}

win = Tk()
win.title("LED Toggler")
myFont = tkinter.font.Font(family='Helvetica', size=12, weight="bold")

# Dictionary to hold LED objects
leds = {}

# Initialize LED objects for each color
for color, pin in led_pins.items():
    leds[color] = LED(pin)

def ledToggle(color):
    for led_color, led in leds.items():
        if led_color == color:
            led.toggle()  # Toggle the LED state (on/off)
        else:
            led.off()  # Turn off LEDs of other colors
    updateButtonText()


def updateButtonText():
    for color, led in leds.items():
        if led.is_lit:
            button_text = f"{color} LED on"
        else:
            button_text = f"{color} LED off"
        radio_buttons[color]["text"] = button_text

def radioClicked(color):
    ledToggle(color)

# Create radio buttons for each LED color
radio_buttons = {}
row_number = 0
for color, pin in led_pins.items():
    radio_button = Radiobutton(win, text=f"Turn {color} LED on", variable=None, value=1, font=myFont,
                               command=lambda c=color: radioClicked(c))
    radio_buttons[color] = radio_button
    radio_button.grid(row=row_number, column=0, padx=10, pady=5)
    row_number += 1

# Function to close the application
def closeApp():
    for led in leds.values():
        led.off()  # Turn off all LEDs
    win.destroy()  # Close the tkinter window

# Create an exit button
exitButton = Button(win, text="Exit", font=myFont, command=closeApp, bg='grey', height=1, width=6)
exitButton.grid(row=row_number, column=0, padx=10, pady=10)

win.protocol("WM_DELETE_WINDOW", closeApp)
win.mainloop()
