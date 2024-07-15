#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File Name: labCalculator.py
Author: Justin M. Smith
Created: 07/09/2024
Version: 1.0.0.0
Description: GUI functionality for working lab calculator in an inkjet test lab

"""
# Imports
import tkinter as tk
from PIL import ImageTk, Image
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.image as image

# GUI Initialization/Variables
root = tk.Tk()
root.title("Lab Calculator 1.0.0.0 - Justin Smith - 2024")
root.resizable(width=False, height=False)
global bColor
global tColor
global butColor
global entryColor
bColor = '#f2f4f7'
tColor = '#01050d'
butColor = '#d7d8db'
entryColor = '#fafaf7'
canvas = tk.Canvas(root,height=800,width=800,bg =bColor, relief='raised')
canvas.pack()
mLabel = tk.Label(canvas, text = "Lab Calculator Menu", fg=tColor, bg =bColor, font=('Segoe UI', 24))
mLabel.place(relx=0.1, rely=0.1, relwidth=0.8)
#Load in logo image to be displayed in GUI
logo = tk.PhotoImage(file = 'logo4.png')
#Update image in GUI title bar
root.wm_iconphoto(False, logo)
       

#Theme Function - assignes colors to background, text, and button dependant on selection
def changeTheme(themeCheck):
    themeCheck = theme.get()
    global bColor
    global tColor
    global butColor
    global entryColor
    if themeCheck == "Light":
        bColor = '#f2f4f7'
        tColor = '#01050d'
        butColor = '#d7d8db'
        entryColor = '#fafaf7'
        mainScreen(bColor,tColor,butColor,entryColor)
    if themeCheck == "Dark":
        bColor = '#080808'
        tColor = '#fafafa'
        butColor = '#706d6d'
        entryColor = '#9e9b9b'
        mainScreen(bColor,tColor,butColor,entryColor)
    if themeCheck == "Forest":
        bColor = '#606c38'
        tColor = '#3c1518'
        butColor = '#9c6644'
        entryColor = '#e6ccb2'
        mainScreen(bColor,tColor,butColor,entryColor)
    if themeCheck == "Snow":
        bColor = '#a0eaf2'
        tColor = '#0c0d0d'
        butColor = '#02f5f5'
        entryColor = '#e3cdb8'
        mainScreen(bColor,tColor,butColor,entryColor)
        
#Theme Settings - Configures drop down for user selected theme
options = ["Light","Dark","Forest","Snow"]
global theme
theme = tk.StringVar()
theme.set("Choose Theme")
themeDrop = tk.OptionMenu(canvas, theme, *options,command=changeTheme)
themeDrop.place(height = 50, width = 150, x = 640, y = 700)
themeDrop.config(bg = butColor, fg = tColor)
#Logo Placement
logoLabel = tk.Label(canvas, image=logo)
logoLabel.place(x=15,y=735,width=50,height=50)

#Frame Creation - Creates a new frame with given title
def createFrame(title,bColor,tColor,butColor,entryColor):
    frame = tk.Frame(canvas,height = 800, width = 800, bg = bColor, relief = 'solid')
    frame.place(relx=0.0, rely=0.0, relwidth=1.0, relheight=1.0)
    mLabel = tk.Label(frame, text = title, fg=tColor, bg =bColor, font=('Segoe UI', 24))
    mLabel.place(relx=0.1, rely=0.1, relwidth=0.8)    


#Main Screen Function - Home screen for the GUI
def mainScreen(bColor,tColor,butColor,entryColor):
    createFrame("Lab Calculator Menu",bColor,tColor,butColor,entryColor)
    #Theme Settings
    options = ["Light","Dark","Forest","Snow"]
    theme.set("Choose Theme")
    themeDrop = tk.OptionMenu(canvas, theme, *options,command=changeTheme)
    themeDrop.place(height = 50, width = 150, x = 640, y = 700)
    themeDrop.config(bg = butColor, fg = tColor)
    #Logo Placement
    logoLabel = tk.Label(canvas, image=logo)
    logoLabel.place(x=15,y=735,width=50,height=50)
    #Drop Mass Button
    massButton = tk.Button(canvas, text = "Dropmass", fg=tColor, bg=butColor, font=('Segoe UI', 18), command = massScreen)
    massButton.place(height = 75, width = 250, x = 275, y = 180)
    #Speed Button
    speedButton = tk.Button(canvas, text = "Speed", fg=tColor, bg=butColor, font=('Segoe UI', 18), command = speedScreen)
    speedButton.place(height = 75, width = 250, x = 275, y = 260)
    #Trigger Delay Button
    tDelayButton = tk.Button(canvas, text = "Trigger Delay", fg=tColor, bg=butColor, font=('Segoe UI', 18), command = trigScreen)
    tDelayButton.place(height = 75, width = 250, x = 275, y = 340)
    #Waveform Converter Button
    waveButton = tk.Button(canvas, text = "WF Pulse Converter", fg=tColor, bg=butColor, font=('Segoe UI', 18), command = waveScreen)
    waveButton.place(height = 75, width = 250, x = 275, y = 420)
    #Temperature Converter Button
    tempButton = tk.Button(canvas, text = "Temp. Converter", fg=tColor, bg=butColor, font=('Segoe UI', 18), command = tempScreen)
    tempButton.place(height = 75, width = 250, x = 275, y = 500)
    
#Back/Home Function - Returns user to the home screen
def back():
    mainScreen(bColor,tColor,butColor,entryColor)

#Waveform Converter Screen Function - Brings user to the waveform conversion function
def tempScreen():
    createFrame("Temperature Converter",bColor,tColor,butColor,entryColor)
    #Back/Home Button
    backButton = tk.Button(canvas, text = "Home", fg=tColor, bg=butColor, font=('Segoe UI', 8), command = back)
    backButton.place(height = 50, width = 100, x = 690, y = 10)    
    #Logo Placement
    logoLabel = tk.Label(canvas, image=logo)
    logoLabel.place(x=15,y=735,width=50,height=50)
    #Temperature - Label and Entry
    tempLabel = tk.Label(canvas, text="Enter Temperature", font=('Segoe UI', 10), fg=tColor, bg =bColor)
    tempLabel.place(height=20, width=200, x=20, y=130)    
    tempEntry = tk.Entry(canvas, font=('Segoe UI', 14))
    tempEntry.place(height=20, width=125, x=60, y=150)
    #Entry Color Configuration
    tempEntry.configure({"background": entryColor})
    #Convert to C. Function
    def convertC():
        temp = float(tempEntry.get())
        tempC = float((temp - 32) * 5 / 9)
        #Result Label
        valLabel = tk.Label(canvas, text="Celcius: " + str(round(tempC)), font=('Segoe UI', 20), fg=tColor, bg =butColor, borderwidth=2, relief="groove")
        valLabel.place(height=50, width=300, x=250, y=230)       
    #Convert to F. Function
    def convertF():
        temp = float(tempEntry.get())
        tempF = float((temp * 9 / 5) + 32)
        #Result Label
        valLabel = tk.Label(canvas, text="Fahrenheit: " + str(round(tempF)), font=('Segoe UI', 20), fg=tColor, bg =butColor, borderwidth=2, relief="groove")
        valLabel.place(height=50, width=300, x=250, y=230)
    #C Calculation Button
    cButton = tk.Button(canvas, text = "To Celcius", fg=tColor, bg=butColor, font=('Segoe UI', 12), command = convertC)
    cButton.place(height = 50, width = 150, x = 45, y = 185) 
    #F Calculation Button
    csvButton = tk.Button(canvas, text = "To Fahrenheit", fg=tColor, bg=butColor, font=('Segoe UI', 12), command = convertF)
    csvButton.place(height = 50, width = 150, x = 45, y = 255) 

        
#Waveform Converter Screen Function - Brings user to the waveform conversion function
def waveScreen():
    createFrame("Waveform Pulse Converter",bColor,tColor,butColor,entryColor)
    #Back/Home Button
    backButton = tk.Button(canvas, text = "Home", fg=tColor, bg=butColor, font=('Segoe UI', 8), command = back)
    backButton.place(height = 50, width = 100, x = 690, y = 10)    
    #Logo Placement
    logoLabel = tk.Label(canvas, image=logo)
    logoLabel.place(x=15,y=735,width=50,height=50) 
    #Pulse Amplitude - Label and Entry
    ampLabel = tk.Label(canvas, text="Enter Pulse Amplitude", font=('Segoe UI', 10), fg=tColor, bg =bColor)
    ampLabel.place(height=20, width=200, x=20, y=130)    
    ampEntry = tk.Entry(canvas, font=('Segoe UI', 14))
    ampEntry.place(height=20, width=125, x=60, y=150)
    #Entry Color Configuration
    ampEntry.configure({"background": entryColor})    
    #Convert to .ini Function
    def convertIni():
        amp = float(ampEntry.get())
        if amp > 255:
            amp = 255
        value = (amp * 184) / 255
        #Result labels
        valLabel = tk.Label(canvas, text=".ini Amplitude: " + str(round(value)), font=('Segoe UI', 20), fg=tColor, bg =butColor, borderwidth=2, relief="groove")
        valLabel.place(height=50, width=300, x=250, y=230)
    #Convert to .csv Function
    def convertCsv():
        amp = float(ampEntry.get())
        if amp > 184:
            amp = 184
        value = (amp * 255) / 184
        #Result labels
        valLabel = tk.Label(canvas, text=".csv Amplitude: " + str(round(value)), font=('Segoe UI', 20), fg=tColor, bg =butColor, borderwidth=2, relief="groove")
        valLabel.place(height=50, width=300, x=250, y=230)
        
    #INI Calculation Button
    iniButton = tk.Button(canvas, text = "Convert to .ini", fg=tColor, bg=butColor, font=('Segoe UI', 12), command = convertIni)
    iniButton.place(height = 50, width = 150, x = 45, y = 185) 
    #CSV Calculation Button
    csvButton = tk.Button(canvas, text = "Convert to .csv", fg=tColor, bg=butColor, font=('Segoe UI', 12), command = convertCsv)
    csvButton.place(height = 50, width = 150, x = 45, y = 255)        
        
#Trigger Delay Screen Function - Brings user to the trigger delay function calculator
def trigScreen():
    createFrame("Trigger Delay Calculator",bColor,tColor,butColor,entryColor)
    #Back/Home Button
    backButton = tk.Button(canvas, text = "Home", fg=tColor, bg=butColor, font=('Segoe UI', 8), command = back)
    backButton.place(height = 50, width = 100, x = 690, y = 10)    
    #Logo Placement
    logoLabel = tk.Label(canvas, image=logo)
    logoLabel.place(x=15,y=735,width=50,height=50) 
    #Delay - Label and Entry
    delayLabel = tk.Label(canvas, text="Enter Trigger Delay at 1200dpi", font=('Segoe UI', 10), fg=tColor, bg =bColor)
    delayLabel.place(height=20, width=200, x=20, y=130)    
    delayEntry = tk.Entry(canvas, font=('Segoe UI', 14))
    delayEntry.place(height=20, width=125, x=60, y=150)
    #Entry Color Configuration
    delayEntry.configure({"background": entryColor})
    
    #Trigger Delay Function
    def trigCalc():
        delay = int(delayEntry.get())
        #Calculate alternative resolutions
        dpi2400 = delay * 2
        dpi900 = delay * (3 / 4)
        dpi600 = delay / 2
        dpi300 = delay / 4
        dpi400 = delay / 3
        #Result labels
        label2400 = tk.Label(canvas, text="2400dpi: " + str(round(dpi2400)), font=('Segoe UI', 20), fg=tColor, bg =butColor, borderwidth=2, relief="groove")
        label2400.place(height=50, width=300, x=250, y=230)
        label900 = tk.Label(canvas, text="900dpi: " + str(round(dpi900)), font=('Segoe UI', 20), fg=tColor, bg =butColor, borderwidth=2, relief="groove")
        label900.place(height=50, width=300, x=250, y=280) 
        label600 = tk.Label(canvas, text="600dpi: " + str(round(dpi600)), font=('Segoe UI', 20), fg=tColor, bg =butColor, borderwidth=2, relief="groove")
        label600.place(height=50, width=300, x=250, y=330) 
        label400 = tk.Label(canvas, text="400dpi: " + str(round(dpi400)), font=('Segoe UI', 20), fg=tColor, bg =butColor, borderwidth=2, relief="groove")
        label400.place(height=50, width=300, x=250, y=380)
        label300 = tk.Label(canvas, text="300dpi: " + str(round(dpi300)), font=('Segoe UI', 20), fg=tColor, bg =butColor, borderwidth=2, relief="groove")
        label300.place(height=50, width=300, x=250, y=430)

    #Trigger Calculation Button
    trigButton = tk.Button(canvas, text = "Calculate", fg=tColor, bg=butColor, font=('Segoe UI', 12), command = trigCalc)
    trigButton.place(height = 50, width = 100, x = 70, y = 185)     

#Speed Screen Function - Brings user to the speed function calculator
def speedScreen():
    createFrame("Speed Calculator",bColor,tColor,butColor,entryColor)
    #Back/Home Button
    backButton = tk.Button(canvas, text = "Home", fg=tColor, bg=butColor, font=('Segoe UI', 8), command = back)
    backButton.place(height = 50, width = 100, x = 690, y = 10)    
    #Logo Placement
    logoLabel = tk.Label(canvas, image=logo)
    logoLabel.place(x=15,y=735,width=50,height=50)    
    #Frequency - Label and Entry
    freqLabel = tk.Label(canvas, text="Enter Frequency (kHz)", font=('Segoe UI', 10), fg=tColor, bg =bColor)
    freqLabel.place(height=20, width=175, x=10, y=130)    
    freqEntry = tk.Entry(canvas, font=('Segoe UI', 14))
    freqEntry.place(height=20, width=100, x=50, y=150)
    #Resolution - Label and Entry
    resLabel = tk.Label(canvas, text="Enter Resolution (dpi)", font=('Segoe UI', 10), fg=tColor, bg =bColor)
    resLabel.place(height=20, width=175, x=10, y=170)    
    resEntry = tk.Entry(canvas, font=('Segoe UI', 14))
    resEntry.place(height=20, width=100, x=50, y=190)
    #Entry Color Configuration
    freqEntry.configure({"background": entryColor})
    resEntry.configure({"background": entryColor})
    #Speed Calculation Function
    def speedCalc():
        #Get entries
        freq = float(freqEntry.get())
        dpi = float(resEntry.get())
        #Calculate speed in inches/second
        ips = ((freq * 1000) / dpi)
        #Feet per minute
        fpm = ips * 5
        #Meter per second
        mps = fpm / 196.9
        #Meter per minute
        mpm = mps * 60
        #Display Results
        ipsLabel = tk.Label(canvas, text="Inches/Second: " + str(round(ips,2)), font=('Segoe UI', 20), fg=tColor, bg =butColor, borderwidth=2, relief="groove")
        ipsLabel.place(height=50, width=300, x=250, y=230)
        fpmLabel = tk.Label(canvas, text="Feet/Minute: " + str(round(fpm,2)), font=('Segoe UI', 20), fg=tColor, bg =butColor, borderwidth=2, relief="groove")
        fpmLabel.place(height=50, width=300, x=250, y=280) 
        mpsLabel = tk.Label(canvas, text="Meter/Second: " + str(round(mps,2)), font=('Segoe UI', 20), fg=tColor, bg =butColor, borderwidth=2, relief="groove")
        mpsLabel.place(height=50, width=300, x=250, y=330) 
        mpmLabel = tk.Label(canvas, text="Meter/Minute: " + str(round(mpm,2)), font=('Segoe UI', 20), fg=tColor, bg =butColor, borderwidth=2, relief="groove")
        mpmLabel.place(height=50, width=300, x=250, y=380)         

    #Speed Calculate Button
    spdCalcButton = tk.Button(canvas, text = "Calculate", fg=tColor, bg=butColor, font=('Segoe UI', 12), command = speedCalc)
    spdCalcButton.place(height = 50, width = 100, x = 50, y = 225)    

    
#Mass Screen Function - Brings user to the dropmass function calculator
def massScreen():
    createFrame("Dropmass Calculator",bColor,tColor,butColor,entryColor)
    #Back/Home Button
    backButton = tk.Button(canvas, text = "Home", fg=tColor, bg=butColor, font=('Segoe UI', 8), command = back)
    backButton.place(height = 50, width = 100, x = 690, y = 10)
    #Logo Placement
    logoLabel = tk.Label(canvas, image=logo)
    logoLabel.place(x=15,y=735,width=50,height=50)    
    #Number of Jets - Label and Entry
    numJetsLabel = tk.Label(canvas, text="Number of Jets", font=('Segoe UI', 10), fg=tColor, bg =bColor)
    numJetsLabel.place(height=20, width=175, x=10, y=130)    
    numJetsEntry = tk.Entry(canvas, font=('Segoe UI', 14))
    numJetsEntry.place(height=20, width=100, x=50, y=150)    
    #Number of Jets Out - Label and Entry
    jetsOutLabel = tk.Label(canvas, text="Jets Out", font=('Segoe UI', 10), fg=tColor, bg =bColor)
    jetsOutLabel.place(height=20, width=175, x=10, y=170)    
    jetsOutEntry = tk.Entry(canvas, font=('Segoe UI', 14))
    jetsOutEntry.place(height=20, width=100, x=50, y=190) 
    #Number of Pixels - Label and Entry
    pulseLabel = tk.Label(canvas, text="Number Pulses/Copies", font=('Segoe UI', 10), fg=tColor, bg =bColor)
    pulseLabel.place(height=20, width=175, x=10, y=210)    
    pulseEntry = tk.Entry(canvas, font=('Segoe UI', 14))
    pulseEntry.place(height=20, width=100, x=50, y=230)  
    #Number of Pixels - Label and Entry
    pixLabel = tk.Label(canvas, text="Number Pixels (1 if Pattern)", font=('Segoe UI', 10), fg=tColor, bg =bColor)
    pixLabel.place(height=20, width=175, x=10, y=250)    
    pixEntry = tk.Entry(canvas, font=('Segoe UI', 14))
    pixEntry.place(height=20, width=100, x=50, y=270)
    #Mass Measurement - Label and Entry
    massLabel = tk.Label(canvas, text="Enter Mass (Grams)", font=('Segoe UI', 10), fg=tColor, bg =bColor)
    massLabel.place(height=30, width=175, x=10, y=300)    
    massEntry = tk.Entry(canvas, font=('Segoe UI', 14))
    massEntry.place(height=40, width=100, x=50, y=330)

    #Entry Color Configuration
    numJetsEntry.configure({"background": entryColor})
    jetsOutEntry.configure({"background": entryColor})
    pulseEntry.configure({"background": entryColor})
    pixEntry.configure({"background": entryColor})
    massEntry.configure({"background": entryColor})

    #Mass Calculate Function
    def massCalc():
        #Get entry data
        jets = int(numJetsEntry.get())
        jetsOut = int(jetsOutEntry.get())
        fires = int(pulseEntry.get())
        pixels = int(pixEntry.get())
        mass = float(massEntry.get())
        #Calculate HADM
        dropMass = (mass*1000000000)/((jets-jetsOut)*pixels*fires)
        #Result Label
        resultLabel = tk.Label(canvas, text="HADM: " + str(round(dropMass,2)) + " ng", font=('Segoe UI', 20), fg=tColor, bg =butColor, borderwidth=2, relief="groove")
        resultLabel.place(height=50, width=250, x=50, y=440)
        resultLabelTwo = tk.Label(canvas, text="", font=('Segoe UI', 24), fg=tColor, bg =butColor, borderwidth=2, relief="groove")
        resultLabelTwo.place(height=50, width=250, x=50, y=490) 
        resultLabelThree = tk.Label(canvas, text="", font=('Segoe UI', 24), fg=tColor, bg =butColor, borderwidth=2, relief="groove")
        resultLabelThree.place(height=50, width=250, x=50, y=540)       
    #Mass Measurement - Button
    massCalcButton = tk.Button(canvas, text = "Calculate", fg=tColor, bg=butColor, font=('Segoe UI', 12), command = massCalc)
    massCalcButton.place(height = 50, width = 100, x = 50, y = 380)

    #BEST GUESS Functionality
    #Voltage Entries and Labels
    vOneLabel = tk.Label(canvas, text="Voltage 1", font=('Segoe UI', 10), fg=tColor, bg =bColor)
    vOneLabel.place(height=20, width=175, x=180, y=170)
    vOneEntry = tk.Entry(canvas, font=('Segoe UI', 14))
    vOneEntry.place(height=20, width=100, x=220, y=190)
    vTwoLabel = tk.Label(canvas, text="Voltage 2", font=('Segoe UI', 10), fg=tColor, bg =bColor)
    vTwoLabel.place(height=20, width=175, x=180, y=210)
    vTwoEntry = tk.Entry(canvas, font=('Segoe UI', 14))
    vTwoEntry.place(height=20, width=100, x=220, y=230)
    vThreeLabel = tk.Label(canvas, text="Voltage 3", font=('Segoe UI', 10), fg=tColor, bg =bColor)
    vThreeLabel.place(height=20, width=175, x=180, y=250)
    vThreeEntry = tk.Entry(canvas, font=('Segoe UI', 14))
    vThreeEntry.place(height=20, width=100, x=220, y=270)
    #Mass Entries and Labels
    mOneLabel = tk.Label(canvas, text="Mass 1 (grams)", font=('Segoe UI', 10), fg=tColor, bg =bColor)
    mOneLabel.place(height=20, width=175, x=350, y=170)
    mOneEntry = tk.Entry(canvas, font=('Segoe UI', 14))
    mOneEntry.place(height=20, width=100, x=390, y=190)
    mTwoLabel = tk.Label(canvas, text="Mass 2 (grams)", font=('Segoe UI', 10), fg=tColor, bg =bColor)
    mTwoLabel.place(height=20, width=175, x=350, y=210)
    mTwoEntry = tk.Entry(canvas, font=('Segoe UI', 14))
    mTwoEntry.place(height=20, width=100, x=390, y=230)
    mThreeLabel = tk.Label(canvas, text="Mass 3 (grams)", font=('Segoe UI', 10), fg=tColor, bg =bColor)
    mThreeLabel.place(height=20, width=175, x=350, y=250)
    mThreeEntry = tk.Entry(canvas, font=('Segoe UI', 14))
    mThreeEntry.place(height=20, width=100, x=390, y=270)
    #Mass Target Entry and Label
    intendedLabel = tk.Label(canvas, text="Intended Dropmass (ng)", font=('Segoe UI', 10), fg=tColor, bg =bColor)
    intendedLabel.place(height=20, width=175, x=520, y=210)
    intendedEntry = tk.Entry(canvas, font=('Segoe UI', 14))
    intendedEntry.place(height=20, width=100, x=560, y=230)
    #Entry Color Configuration
    vOneEntry.configure({"background": entryColor})
    vTwoEntry.configure({"background": entryColor})
    vThreeEntry.configure({"background": entryColor})
    mOneEntry.configure({"background": entryColor})
    mTwoEntry.configure({"background": entryColor})
    mThreeEntry.configure({"background": entryColor})
    intendedEntry.configure({"background": entryColor})
    
    #Best Guess Calculate Function
    def bestGuess():
        #Get entry data
        jets = int(numJetsEntry.get())
        jetsOut = int(jetsOutEntry.get())
        fires = int(pulseEntry.get())
        pixels = int(pixEntry.get())
        massOne = float(mOneEntry.get())
        massTwo = float(mTwoEntry.get())
        massThree = float(mThreeEntry.get())
        voltOne = float(vOneEntry.get())
        voltTwo = float(vTwoEntry.get())
        voltThree = float(vThreeEntry.get())
        intendedMass = float(intendedEntry.get())
        #Calculate drop masses
        hadmOne = (massOne*1000000000)/((jets-jetsOut)*pixels*fires)
        hadmTwo = (massTwo*1000000000)/((jets-jetsOut)*pixels*fires)
        hadmThree = (massThree*1000000000)/((jets-jetsOut)*pixels*fires)
        #Display individual Mass Results
        resultLabelOne = tk.Label(canvas, text="HADM 1: " + str(round(hadmOne,2)) + " ng", font=('Segoe UI', 20), fg=tColor, bg =butColor, borderwidth=2, relief="groove")
        resultLabelOne.place(height=50, width=250, x=50, y=440)        
        resultLabelTwo = tk.Label(canvas, text="HADM 2: " + str(round(hadmTwo,2)) + " ng", font=('Segoe UI', 20), fg=tColor, bg =butColor, borderwidth=2, relief="groove")
        resultLabelTwo.place(height=50, width=250, x=50, y=490) 
        resultLabelThree = tk.Label(canvas, text="HADM 3: " + str(round(hadmThree,2)) + " ng", font=('Segoe UI', 20), fg=tColor, bg =butColor, borderwidth=2, relief="groove")
        resultLabelThree.place(height=50, width=250, x=50, y=540)
        #Calculate Slope and Intercept Values
        slope = (hadmThree - hadmOne) / (voltThree - voltOne)
        intercept = hadmOne - slope * voltOne
        #Find target voltage
        targetVolt = (intendedMass - intercept) / slope
        #Display target voltage
        targetVoltLabel = tk.Label(canvas, text="Try: " + str(round(targetVolt,1)) + " volts", font=('Segoe UI', 20), fg=tColor, bg =butColor, borderwidth=2, relief="groove")
        targetVoltLabel.place(height=50, width=250, x=275, y=360)
        #Plot Voltage vs. Mass
        fig, ax = plt.subplots(facecolor=butColor)
        canvas2 = FigureCanvasTkAgg(fig, master=canvas)  
        canvas2.get_tk_widget().place(x=315,y=420,width=400,height=300)
        plt.axis('on')
        #Combine Values
        voltValues = [voltOne, voltTwo, voltThree]
        massValues = [hadmOne, hadmTwo, hadmThree]
        #Plot
        ax.plot(voltValues,massValues,color='red')
        ax.scatter(targetVolt,intendedMass,color='green')
        #Find limits
        xMin = voltOne - 2
        xMax = voltThree + 2
        yMin = hadmOne - 2
        yMax = hadmThree + 2
        #Plot formatting
        plt.xlim(xMin, xMax)
        plt.ylim(yMin, yMax)
        plt.xlabel('Voltage')
        plt.ylabel('HADM')
        plt.grid()
        

    #Best Guess Calculation Button
    bgCalcButton = tk.Button(canvas, text = "Calculate Voltage", fg=tColor, bg=butColor, font=('Segoe UI', 12), command = bestGuess)
    bgCalcButton.place(height = 50, width = 160, x = 275, y = 300)   

    

# Main Loop
mainScreen(bColor,tColor,butColor,entryColor)
root.mainloop()
