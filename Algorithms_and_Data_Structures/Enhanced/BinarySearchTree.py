#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File Name: BinarySearchTree.py
Author: Justin M. Smith
Created: 07/18/2024
Version: 1.0.0.0
Description: Binary search tree for electronic bid document with interface support

"""
# Imports
import tkinter as tk
import pandas as pd
import openpyxl
import time

#Node class definition
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

#Binary Search Tree class definition
class BinarySearchTree:
    
    def __init__(self):
        self.root = None

    #"keys" will store a tuple of data from a row of excel file
    def insert(self, keys):
        self.root = self.insertRecord(self.root, keys)

    def insertRecord(self, root, keys):
        if root is None:
            return Node(keys)
        #If key is less than value, insert left
        if keys < root.key:
            root.left = self.insertRecord(root.left, keys)
        #if key is larger than value, insert right
        else:
            root.right = self.insertRecord(root.right, keys)
        return root
    def search(self, key):
        return self.searchRecords(self.root, key)

    #Record search, BST was created using entire tuple - this does not work for bid ID!
    def searchRecords(self, root, key):
        #Enter column number for search term (0 for title, 1 for bidID)
        if root is None or root.key[1] == key:
            return root
        if key < root.key[1]:
            return self.searchRecords(root.left, key)
        else:
            return self.searchRecords(root.right, key)
    #Work around for searching for bid ID within tuples stored in BST
    def containsNumber(self, number):
        return self.containsNumberRecord(self.root, number)

    #Check if number exists within tuple
    def containsNumberRecord(self, root, number):
        if root is None:
            return False
        if number in root.key:
            return root
        return self.containsNumberRecord(root.left, number) or self.containsNumberRecord(root.right, number)

    def inOrder(self):

        result = []
        self.inOrderResult(self.root, result)
        return result

    def inOrderResult(self, root, result):

        if root:
            self.inOrderResult(root.left, result)
            result.append(root.key)
            self.inOrderResult(root.right, result)
            result.append(root.key)

def loadBids(path):

    bst = BinarySearchTree()

    #Load E-Bids file
    data = pd.read_excel(path, engine='openpyxl')

    #Find columns
    columns = data.columns.tolist()
    #print(columns)

    #Insert data into search tree
    for index, row in data.iterrows():
        keys = tuple(row[column] for column in columns)
        bst.insert(keys)

    return bst

#File Path
path = 'eBid_Monthly_Sales.xlsx'



#------------------------------------------------------------------------------------
#Create BST for data (FOR TESTING)
#bst = loadBids(path)

#FOR TESTING
#sortedElem = bst.inOrder()
#print("Elements: ", sortedElem)

#term = 79589
#startTime = time.time()
#result = bst.search(term)
#searchTime = time.time() - startTime

#if result:
#    print(f"Row with key {term} found in BST:",result.key)
#    print(f"Total Search Time: {searchTime:.4f} Seconds")
#else:
#    print(f"Row with key {term} not found!")

#------------------------------------------------------------------------------------

#GUI Functionality
    
guiRoot = tk.Tk()
guiRoot.title("E-Bid Search Utility - Justin Smith - 2024")
guiRoot.resizable(width=False, height=False)
#Widget Colors
bColor = '#f2f4f7'
tColor = '#01050d'
butColor = '#d7d8db'
entryColor = '#fafaf7'
#Window Creation
canvas = tk.Canvas(guiRoot, height=600, width=600, bg=bColor, relief='raised')
canvas.pack()
#Window Label
guiLabel = tk.Label(canvas, text="E-Bid Search Utility", fg=tColor, bg=bColor, font=('Segoe UI', 24))
guiLabel.place(relx=0.1, rely=0.1, relwidth=0.8)

#Load Bids Button Call
def callLoadBids():
    global bst
    #Keeps track of time elapsed for loadBids function
    startTime = time.time()
    #Call loadBids
    bst = loadBids(path)
    searchTime = time.time() - startTime
    #Display success and time elapsed
    resultLabel = tk.Label(canvas, text="Bids Loaded. Total Time: " + str(round(searchTime,4)) + " Seconds!", font=('Segoe UI', 10), fg=tColor, bg =butColor, borderwidth=2, relief="groove")
    resultLabel.place(height=50, width=300, x=250, y=120)  

#Button for Load Bids
loadBidsButton = tk.Button(canvas, text = "Load Bids", fg=tColor, bg=butColor, font=('Segoe UI', 14), command = callLoadBids)
loadBidsButton.place(height = 50, width = 150, x = 50, y = 120)

#Display all Bids Call
def callDisplayBids():
    startTime = time.time()
    sortedElem = bst.inOrder()
    searchTime = time.time() - startTime
    #List Box to store elements
    listBox = tk.Listbox(canvas)
    listBox.place(height=400, width=300, x=250, y=170)
    #Insert Elements
    for key in sortedElem:
        listBox.insert(tk.END, key)
    #Scroll Bar
    scrollBar = tk.Scrollbar(canvas, orient=tk.HORIZONTAL)
    scrollBar.config(command=listBox.xview)
    scrollBar.place(height=25, width=300, x=250, y=570)
    #Display success and time elapsed
    resultLabel = tk.Label(canvas, text="Bids Displayed. Total Time: " + str(round(searchTime,4)) + " Seconds!", font=('Segoe UI', 10), fg=tColor, bg =butColor, borderwidth=2, relief="groove")
    resultLabel.place(height=50, width=300, x=250, y=120)

    
#Button for Display Bids
displayBidsButton = tk.Button(canvas, text = "Display Bids", fg=tColor, bg=butColor, font=('Segoe UI', 14), command = callDisplayBids)
displayBidsButton.place(height = 50, width = 150, x = 50, y = 170)

#Entry Label for Bid ID Input
idLabel = tk.Label(canvas, text="Enter Bid ID", font=('Segoe UI', 14), fg=tColor, bg =bColor)
idLabel.place(height=50, width=150, x=50, y=250)    
idEntry = tk.Entry(canvas, font=('Segoe UI', 14))
idEntry.place(height=50, width=150, x=50, y=300)

#Search Bids Call
def callSearchBids():
    term = int(idEntry.get())
    print(term)
    startTime = time.time()
    #result = bst.search(term)
    result = bst.containsNumber(term)
    searchTime = time.time() - startTime
    #List Box to store elements
    listBox = tk.Listbox(canvas)
    listBox.place(height=400, width=300, x=250, y=170)
    
    #Display success and time elapsed
    if result:
        #Add result
        listBox.insert(tk.END, result.key)
        resultLabel = tk.Label(canvas, text="Bid Located. Total Time: " + str(round(searchTime,4)) + " Seconds!", font=('Segoe UI', 10), fg=tColor, bg =butColor, borderwidth=2, relief="groove")
        resultLabel.place(height=50, width=300, x=250, y=120)
    else:
        resultLabel = tk.Label(canvas, text="No Bids Found - Try Again!", font=('Segoe UI', 10), fg=tColor, bg =butColor, borderwidth=2, relief="groove")
        resultLabel.place(height=50, width=300, x=250, y=120)
     #Scroll Bar
    scrollBar = tk.Scrollbar(canvas, orient=tk.HORIZONTAL)
    scrollBar.config(command=listBox.xview)
    scrollBar.place(height=25, width=300, x=250, y=570)   
    
#Button for Search Bids
displayBidsButton = tk.Button(canvas, text = "Search Bids", fg=tColor, bg=butColor, font=('Segoe UI', 14), command = callSearchBids)
displayBidsButton.place(height = 50, width = 150, x = 50, y = 350)   


    
            
        

        


