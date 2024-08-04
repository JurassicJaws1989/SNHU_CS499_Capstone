#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File Name: BidDatabase.py
Author: Justin M. Smith
Created: 07/31/2024
Version: 1.0.0.0
Description: Database Utility to Interact with Electronic Bid Data Sheet
"""

import tkinter as tk
from tkinter import ttk
import pandas as pd

# Define a password for demonstration purposes
PASSWORD = "station"  # Replace this with a more secure method in a real application

class BidDatabaseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("E-Bid Database Utility - Justin Smith - 2024")
        self.root.resizable(width=False, height=False)

        # Widget Colors
        self.bColor = '#d5d5d5'
        self.tColor = '#060606'
        self.butColor = '#ababac'

        # Setup the main application window
        self.setup_main_window()

        # Store initial column widths
        self.column_widths = {}
        
    def setup_main_window(self):
        self.canvas = tk.Canvas(self.root, height=800, width=1000, bg=self.bColor, relief='raised')
        self.canvas.pack()

        # Window Label
        self.guiLabel = tk.Label(self.canvas, text="E-Bid Database Utility", fg=self.tColor, bg=self.bColor, font=('Segoe UI', 24))
        self.guiLabel.place(x=50, y=10, height=50, width=325)

        # Read Data
        self.df = self.load_data('eBid_Monthly_Sales.xlsx')

        # Create Treeview widget
        self.tree = ttk.Treeview(self.canvas)
        self.vsb = ttk.Scrollbar(self.canvas, orient="vertical", command=self.tree.yview)
        self.hsb = ttk.Scrollbar(self.canvas, orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=self.vsb.set, xscrollcommand=self.hsb.set)

        # Place elements
        self.tree.place(x=300, y=200, width=600, height=500)
        self.vsb.place(height=500, x=900, y=200, anchor='ne')
        self.hsb.place(width=600, x=300, y=695, anchor='sw')

        # Populate the Treeview
        self.populate_tree(self.df)

        # Sort by column
        self.column_var = tk.StringVar(value='Auction Title ')
        self.radio_frame = tk.Frame(self.canvas,bg=self.bColor)
        self.radio_frame.place(x=450, y=130, height=50, width=400)
        self.create_radio_buttons()

        # Sort label
        self.sortLabel = tk.Label(self.canvas, text="Sort by", font=('Segoe UI', 12), fg=self.tColor, bg=self.bColor)
        self.sortLabel.place(height=50, width=150, x=500, y=80)

        # Search Entry
        self.searchEntry = tk.Entry(self.canvas, font=('Segoe UI', 10))
        self.searchEntry.place(height=25, width=125, x=25, y=200)
        self.entryLabel = tk.Label(self.canvas, text="Enter Term", font=('Segoe UI', 12), fg=self.tColor, bg=self.bColor)
        self.entryLabel.place(height=50, width=125, x=25, y=150)

        # Search by Drop Down
        self.dropList = ['Auction Title ','Auction ID','Department ','Close Date ']
        self.searchOption = tk.StringVar(value='Auction Title ')
        self.searchDrop = tk.OptionMenu(self.canvas, self.searchOption, *self.dropList)
        self.searchDrop.place(height = 25, width = 125, x = 150, y = 200)
        self.searchDrop.config(fg=self.tColor, bg=self.bColor)

        # Search Button
        self.searchButton = tk.Button(self.canvas, text = "Search", fg=self.tColor, bg=self.butColor, font=('Segoe UI', 12), command = self.perform_search)
        self.searchButton.place(height=25, width=125, x=25, y=230)

    def load_data(self, file):
        try:
            #Select Columns
            #return pd.read_excel(file, sheet_name='eBid_Monthly_Sales', header=0, index_col=None, usecols=[0,1,2,3,4,7])
            #All Data
            return pd.read_excel(file, sheet_name='eBid_Monthly_Sales', header=0, index_col=None)
        except Exception as e:
            print(f"Error loading file: {e}")
            return pd.DataFrame()  # Return an empty DataFrame on error

    def populate_tree(self, dataframe):
        # Clear existing content
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Store column widths
        column_widths = {col: self.tree.column(col, 'width') for col in self.tree["columns"]}
        
        # Set column headers
        self.columns = list(dataframe.columns)
        self.tree["columns"] = list(dataframe.columns)
        for col in dataframe.columns:
            self.tree.heading(col, text=col)
            #self.tree.column(col, width=column_widths.get(col, 100), anchor='w')
            self.tree.column(col, stretch=False, width=100, anchor='w')
        
        # Insert rows
        for _, row in dataframe.iterrows():
            self.tree.insert("", "end", values=list(row))

        
        self.tree["displaycolumns"] = self.columns

        # Hide the first implicit column if necessary
        if len(self.tree["columns"]) > 0:
            self.tree.column("#0", width=0, stretch=tk.NO)  

    def sort_by_column(self, column):
        sorted_df = self.df.sort_values(by=column, ascending=True)
        self.populate_tree(sorted_df)

    def on_radio_select(self):
        selected_column = self.column_var.get()
        if selected_column:
            self.sort_by_column(selected_column)

    def create_radio_buttons(self):
        tk.Radiobutton(self.radio_frame, text="Title", variable=self.column_var, value='Auction Title ', command=self.on_radio_select).pack(side=tk.LEFT)
        tk.Radiobutton(self.radio_frame, text="ID", variable=self.column_var, value='Auction ID', command=self.on_radio_select).pack(side=tk.LEFT)
        tk.Radiobutton(self.radio_frame, text="Dept.", variable=self.column_var, value='Department ', command=self.on_radio_select).pack(side=tk.LEFT)
        tk.Radiobutton(self.radio_frame, text="Close Date", variable=self.column_var, value='Close Date ', command=self.on_radio_select).pack(side=tk.LEFT)

    def perform_search(self):
        search_term = self.searchEntry.get().lower()
        search_by = self.searchOption.get()
        filtered_df = self.df[self.df[search_by].astype(str).str.lower().str.contains(search_term)]
        self.populate_tree(filtered_df)

class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("300x150")

        self.canvas = tk.Canvas(self.root, height=150, width=300, bg='#f2f4f7', relief='raised')
        self.canvas.pack()

        # Create and place widgets for login
        self.label = tk.Label(self.canvas, text="Enter Password", font=('Segoe UI', 14), bg='#f2f4f7')
        self.label.place(x=50, y=20)

        self.password_entry = tk.Entry(self.canvas, show='*', font=('Segoe UI', 12))
        self.password_entry.place(x=50, y=60, width=200)

        self.login_button = tk.Button(self.canvas, text="Login", command=self.check_password, font=('Segoe UI', 12))
        self.login_button.place(x=100, y=100)

    def check_password(self):
        if self.password_entry.get() == PASSWORD:
            self.root.destroy()  # Close the login window
            self.open_main_app()
        else:
            self.label = tk.Label(self.canvas, text="Incorrect - Try Again", font=('Segoe UI', 14), bg='#f2f4f7')
            self.label.place(x=50, y=20)

    def open_main_app(self):
        main_root = tk.Tk()
        BidDatabaseApp(main_root)
        main_root.mainloop()

if __name__ == "__main__":
    login_root = tk.Tk()
    login_window = LoginWindow(login_root)
    login_root.mainloop()
