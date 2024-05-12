import tkinter as tk
from tkinter import filedialog, messagebox, Menu
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import seaborn as sns

def load_dataset():
    try:
        filename = filedialog.askopenfilename(
            title="Select a file", filetypes=(("CSV files", "*.csv"), ("All files", "*.*"))
        )
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
        # Creating a top-level window for visualization
        viz_window = tk.Toplevel()
        viz_window.title("Data Visualization")
        viz_window.geometry("1000x800")
        viz_window.configure(bg="#ADD8E6")  # Light blue background

        # Main frame for visualization window
        main_frame = tk.Frame(viz_window, bg="#0D47A1")  # Dark blue background
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        selected_column = tk.StringVar()
        column_label = tk.Label(
            main_frame,
            text="Select a column to visualize:",
            bg="#0D47A1",  # Dark blue background
            fg="#ADD8E6",  # Light blue text
            font=("Arial", 14, "bold")
        )
        column_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        column_menu = tk.OptionMenu(main_frame, selected_column, *df.columns)
        column_menu.config(font=("Arial", 14))
        column_menu.grid(row=0, column=1, padx=10, pady=10)

        viz_type = tk.StringVar()
        viz_type.set("Histogram")  
        viz_label = tk.Label(
            main_frame,
            text="Select visualization type:",
            bg="#0D47A1",  # Dark blue background
            fg="#ADD8E6",  # Light blue text
            font=("Arial", 14, "bold")
        )
        viz_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        viz_menu = tk.OptionMenu(main_frame, viz_type, "Histogram", "Scatter Plot")
        viz_menu.config(font=("Arial", 14))
        viz_menu.grid(row=1, column=1, padx=10, pady=10)

        visualize_button = tk.Button(
            main_frame,
            text="Visualize",
            width=20,
            height=2,
            command=lambda: visualize_data(df, selected_column.get(), viz_type.get(), main_frame),
            bg="#1565C0",  # Dark blue
            fg="#FFFFFF",  # White text
            font=("Arial", 14, "bold"),
            relief=tk.RAISED,
            bd=3,
        )
        visualize_button.grid(row=2, column=0, columnspan=2, pady=20)

        status_label = tk.Label(
            main_frame, text="", fg="#4CAF50", bg="#0D47A1", font=("Arial", 12, "italic")  # Green text on dark blue background
        )
        status_label.grid(row=3, column=0, columnspan=2, pady=10)

def visualize_data(df, column_name, viz_type, main_frame):
    try:
        plt.figure(figsize=(12, 8))

        if viz_type == "Histogram":
            sns.histplot(
                df[column_name],
                bins="auto",
                color="#0D47A1",  # Dark blue
                edgecolor="black",
                alpha=0.7,
            )
            plt.title("Histogram of " + column_name, fontsize=20)
            plt.xlabel(column_name, fontsize=16)
            plt.ylabel("Frequency", fontsize=16)
        elif viz_type == "Scatter Plot":
            sns.scatterplot(x=df.index, y=df[column_name])
            plt.title("Scatter Plot of " + column_name, fontsize=20)
            plt.xlabel("Index", fontsize=16)
            plt.ylabel(column_name, fontsize=16)

        plt.grid(True)
        plt.tick_params(labelsize=14)

        for widget in main_frame.winfo_children():
            if widget != "status_label":
                widget.destroy()

        canvas = FigureCanvasTkAgg(plt.gcf(), master=main_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    except KeyError:
        messagebox.showerror(
            "Error", f"Selected column '{column_name}' not found in the dataset."
        )
    except Exception as e:
        messagebox.showerror(
            "Error", f"An error occurred while visualizing the data: {str(e)}"
        )
    else:
        messagebox.showinfo("Success", "Visualization complete.")

root = tk.Tk()
root.title("Data Analysis and Visualization")
root.geometry("800x600")
root.configure(bg="#0D47A1")  # Dark blue background

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Load Dataset", command=analyze_and_visualize)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About")
menubar.add_cascade(label="Help", menu=helpmenu)
root.config(menu=menubar)

title_label = tk.Label(
    root,
    text="Data Analysis and Visualization",
    font=("Arial", 24, "bold"),
    bg="#0D47A1",  # Dark blue background
    fg="#FFFFFF",  # White text
)
title_label.pack(pady=10)

instructions_label = tk.Label(
    root,
    text="1. Click 'Load Dataset' to select a CSV file.\n2. Choose a column from the dropdown.\n3. Click 'Visualize' to see the histogram.",
    font=("Arial", 16),
    bg="#0D47A1",  # Dark blue background
    fg="#FFFFFF",  # White text
)
instructions_label.pack(pady=10)

load_button = tk.Button(
    root,
    text="Load Dataset",
    font=("Arial", 16),
    width=30,
    height=3,
    command=analyze_and_visualize,
    bg="#1565C0",  # Dark blue
    fg="#FFFFFF",  # White text
    relief=tk.RAISED,
    bd=3,
)
load_button.pack(pady=20)

plot_frame = tk.Frame(root, relief=tk.GROOVE, bd=2, bg="#FFFFFF")
plot_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

root.mainloop()
