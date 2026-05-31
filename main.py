import tkinter as tk
from tkinter import ttk
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

logs = []

with open("sample_log.txt", "r") as file:
    for line in file:
        parts = line.strip().split()

        logs.append({
            "Date": parts[0],
            "Action": parts[1],
            "Status": parts[2],
            "IP": parts[3]
        })

df = pd.DataFrame(logs)

success_count = len(df[df["Status"] == "SUCCESS"])
failed_count = len(df[df["Status"] == "FAILED"])

root = tk.Tk()
root.title("Security Log Analyzer")
root.geometry("900x600")

title = tk.Label(
    root,
    text="Security Log Analyzer Dashboard",
    font=("Arial", 18, "bold")
)
title.pack(pady=10)

frame = ttk.Frame(root)
frame.pack(fill="both", expand=True)

tree = ttk.Treeview(
    frame,
    columns=("Date", "Action", "Status", "IP"),
    show="headings"
)

tree.heading("Date", text="Date")
tree.heading("Action", text="Action")
tree.heading("Status", text="Status")
tree.heading("IP", text="IP")

for _, row in df.iterrows():
    tree.insert(
        "",
        tk.END,
        values=(
            row["Date"],
            row["Action"],
            row["Status"],
            row["IP"]
        )
    )

tree.pack(fill="both", expand=True)

figure = Figure(figsize=(5, 3))
ax = figure.add_subplot(111)

ax.bar(
    ["SUCCESS", "FAILED"],
    [success_count, failed_count]
)

ax.set_title("Login Attempt Analysis")

canvas = FigureCanvasTkAgg(
    figure,
    master=root
)

canvas.draw()
canvas.get_tk_widget().pack()

root.mainloop()
