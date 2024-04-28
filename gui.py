import tkinter as tk
from tkinter import filedialog
import main

actualDir = "./saves/save1"
fileName = "all-locations.txt"
configDir = "config.json"

def select_txt_file():
    global fileName
    fileName = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])

def select_config_file():
    global configDir
    configDir = filedialog.askopenfilename(filetypes=[("Json files", "*.json")])

def drawGraphButton():
    data = main.readData(fileName)
    colors, languages = main.getGraphColorsAndLabels(configDir)
    main.drawGraph(colors, languages, data)

def createGUI():
    select_button = tk.Button(root, text="Select .txt File", command=select_txt_file)
    select_button.pack(padx=10, pady=10)

    select_config_button = tk.Button(root, text="Select .json File", command=select_config_file)
    select_config_button.pack(padx=10, pady=10)

    execute_button = tk.Button(root, text="Draw Graph", command=drawGraphButton)
    execute_button.pack(padx=10, pady=10)

# Create the main window
root = tk.Tk()
root.title("Selectable List")

# Run the GUI event loop
createGUI()
root.mainloop()