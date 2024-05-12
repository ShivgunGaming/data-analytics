import tkinter as tk
from tkinter import filedialog, messagebox, Menu
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import seaborn as sns

def load_dataset():
    try:
        filename = filedialog.askopenfilename(title="Select a file", filetypes=(("CSV files", "*.csv"), ("All files", "*.*")))
        if filename:
            df = pd.read_csv(filename)
            return df
        else:
            return None
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while loading the dataset: {str(e)}")
        return None

def analyze_and_visualize():
    df = load_dataset()
    if df is not None:
        visualize_data(df)

def visualize_data(df):
    try:
        plt.figure(figsize=(8, 6))
        sns.histplot(df.iloc[:, 0], bins='auto', color='blue', edgecolor='black', alpha=0.7)
        plt.title('Histogram of First Column', fontsize=16)
        plt.xlabel('First Column', fontsize=14)
        plt.ylabel('Frequency', fontsize=14)
        plt.grid(True)
        plt.tick_params(labelsize=12)

        plt.show()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while visualizing the data: {str(e)}")

root = tk.Tk()
root.title("Data Analysis and Visualization")
root.geometry("500x400")

def about():
    messagebox.showinfo("About", "This is a simple data analysis and visualization GUI application.")

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Load Dataset", command=analyze_and_visualize)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=about)
menubar.add_cascade(label="Help", menu=helpmenu)
root.config(menu=menubar)

title_label = tk.Label(root, text="Data Analysis and Visualization", font=("Arial", 20, "bold"))
title_label.pack(pady=10)

instructions_label = tk.Label(root, text="1. Click 'Load Dataset' to select a CSV file.\n2. Choose a column from the dropdown.\n3. Click 'Visualize' to see the histogram.", font=("Arial", 12))
instructions_label.pack(pady=10)

load_button = tk.Button(root, text="Load Dataset", command=analyze_and_visualize)
load_button.pack(pady=20)

root.mainloop()
