import tkinter as tk
import pygame



#Main Window
HEIGTH = 800
WIDTH = 800

root = tk.Tk()

root.title("PHTL Master Calculator 2.1.2----Justin Smith---2020")

canvas = tk.Canvas(root, height=HEIGTH, width=WIDTH, bg='#a9b1b6', relief='raised' )
canvas.pack()


ocimage = tk.PhotoImage(file='ocean.ppm')


new_color = '#74add0'
bgcolor = '#74add0'


frame = tk.Frame(root, bg ='#74add0', relief='solid')
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

mainlabel = tk.Label(frame, text="PHTL Master Calculator", fg='#0c161c', bg ='#74add0', font=('fixedsys', 24))
mainlabel.place(relx=0.1, rely=0.1, relwidth=0.8)

colorlabel = tk.Label(frame, text="Change Background Color", fg='#0c161c', bg ='#74add0', font=('fixedsys', 8))
colorlabel.place(height=50, width=200, x=0, y=600)

def blumains():
    frame.configure(bg='#74add0')
    mainlabel.configure(bg='#74add0')
    colorlabel.configure(bg='#74add0')

def redmains():
    frame.configure(bg='#ff6666')
    mainlabel.configure(bg='#ff6666')
    colorlabel.configure(bg='#ff6666')

def grnmains():
    frame.configure(bg='#96de9d')
    mainlabel.configure(bg='#96de9d')
    colorlabel.configure(bg='#96de9d')

def stlmains():
    frame.configure(bg='#facdf4')
    mainlabel.configure(bg='#facdf4')
    colorlabel.configure(bg='#facdf4')

def ocmains():
    
    oclabel = tk.Label(canvas, image=ocimage)
    oclabel.place(x=0, y=0, relwidth=1, relheight=1)
    

blumain = tk.Button(frame, text="Blue", fg='#0c161c', bg='#d2d6d8', font=('fixedsys', 8),
                            command=blumains)
blumain.place(height=50, width=80, x=200, y=600)

redmain = tk.Button(frame, text="Red", fg='#0c161c', bg='#d2d6d8', font=('fixedsys', 8),
                            command=redmains)
redmain.place(height=50, width=80, x=280, y=600)

grnmain = tk.Button(frame, text="Green", fg='#0c161c', bg='#d2d6d8', font=('fixedsys', 8),
                            command=grnmains)
grnmain.place(height=50, width=80, x=360, y=600)

stlmain = tk.Button(frame, text="Pink", fg='#0c161c', bg='#d2d6d8', font=('fixedsys', 8),
                            command=stlmains)
stlmain.place(height=50, width=80, x=440, y=600)

ocmain = tk.Button(frame, text="Ocean", fg='#0c161c', bg='#d2d6d8', font=('fixedsys', 8),
                            command=ocmains)
ocmain.place(height=50, width=80, x=520, y=600)







#Speed Calculator

def speed():
    speedtop = tk.Toplevel(root, bg ='#74add0', height=600, width=600)
    speedtop.title("Universal Speed Calculator")

    freqlabel = tk.Label(speedtop, text="Enter Frequency (kHz)", font=('fixedsys', 12), fg='#0c161c', bg ='#74add0')
    freqlabel.place(height=50, width=175, x=10, y=10)
    freqentry = tk.Entry(speedtop, font=('fixedsys', 24) )
    freqentry.place(height=50, width=175, x=10, y=50)
    dpilabel = tk.Label(speedtop, text="Enter Resolution (DPI)", font=('fixedsys', 12), fg='#0c161c', bg ='#74add0')
    dpilabel.place(height=50, width=175, x=10, y=90)
    dpientry = tk.Entry(speedtop, font=('fixedsys', 24))
    dpientry.place(height=50, width=175, x=10, y=130)

    colorlabels = tk.Label(speedtop, text="Change Background Color", fg='#0c161c', bg ='#74add0', font=('fixedsys', 8))
    colorlabels.place(height=50, width=200, x=0, y=500)

    def bluspeeds():
        speedtop.configure(bg='#74add0')
        freqlabel.configure(bg='#74add0')
        dpilabel.configure(bg='#74add0')
        colorlabels.configure(bg='#74add0')

    def grnspeeds():
        speedtop.configure(bg='#96de9d')
        freqlabel.configure(bg='#96de9d')
        dpilabel.configure(bg='#96de9d')
        colorlabels.configure(bg='#96de9d')

    def redspeeds():
        speedtop.configure(bg='#ff6666')
        freqlabel.configure(bg='#ff6666')
        dpilabel.configure(bg='#ff6666')
        colorlabels.configure(bg='#ff6666')

    def stlspeeds():
        speedtop.configure(bg='#facdf4')
        freqlabel.configure(bg='#facdf4')
        dpilabel.configure(bg='#facdf4')
        colorlabels.configure(bg='#facdf4')

    
        

    bluspeed = tk.Button(speedtop, text="Blue", fg='#0c161c', bg='#d2d6d8', font=('fixedsys', 8),
                            command=bluspeeds)
    bluspeed.place(height=50, width=80, x=200, y=500)

    grnspeed = tk.Button(speedtop, text="Green", fg='#0c161c', bg='#d2d6d8', font=('fixedsys', 8),
                            command=grnspeeds)
    grnspeed.place(height=50, width=80, x=360, y=500)

    redspeed = tk.Button(speedtop, text="Red", fg='#0c161c', bg='#d2d6d8', font=('fixedsys', 8),
                            command=redspeeds)
    redspeed.place(height=50, width=80, x=280, y=500)

    stlspeed = tk.Button(speedtop, text="Pink", fg='#0c161c', bg='#d2d6d8', font=('fixedsys', 8),
                            command=stlspeeds)
    stlspeed.place(height=50, width=80, x=440, y=500)


    def speedexit():
        speedtop.destroy()

    speedback = tk.Button(speedtop, text="Back", fg='#0c161c', bg='#d2d6d8', font=('fixedsys', 4),
                            command=speedexit)
    speedback.place(height=25, width=40, x=550, y=10)

    

    

    


    

    def speedcalc(self):
        freq = int(freqentry.get())
        dpi = int(dpientry.get())

        speedform = ((freq*1000) / dpi)
        webform = speedform * 5
        sledlabel = tk.Label(speedtop, text="Platen Speed = " + str(round(speedform, 2)) + " inches per second", font=('fixedsys', 16), fg='#0c161c', relief='solid')
        sledlabel.place(height=50, width=450, x=50, y=325)
        weblabel = tk.Label(speedtop, text="Web Speed = " + str(round(webform, 1)) + " feet per minute",
                             font=('fixedsys', 16), fg='#0c161c', relief='solid')
        weblabel.place(height=50, width=450, x=50, y=375)

    def speedcalcbut():
        freq = int(freqentry.get())
        dpi = int(dpientry.get())

        speedform = ((freq*1000) / dpi)
        webform = speedform * 5
        sledlabel = tk.Label(speedtop, text="Platen Speed = " + str(round(speedform, 2)) + " inches per second", font=('fixedsys', 16), fg='#0c161c', relief='solid')
        sledlabel.place(height=50, width=450, x=50, y=325)
        weblabel = tk.Label(speedtop, text="Web Speed = " + str(round(webform, 1)) + " feet per minute",
                             font=('fixedsys', 16), fg='#0c161c', relief='solid')
        weblabel.place(height=50, width=450, x=50, y=375)


        

    speedsub = tk.Button(speedtop, text="Submit", fg='#0c161c', bg='#d2d6d8', font=('fixedsys', 12),
                            command=speedcalcbut)
    speedsub.place(height=50, width=175, x=10, y=190)

    speedtop.bind('<Return>', speedcalc)
    

    def helpspeed():
        helptop = tk.Toplevel(speedtop, bg ='#74add0', height=250, width=250)
        helptop.title("Universal Speed Calculator---HELP")
        helplabel = tk.Label(helptop, text="Enter Print Frequency in kHz and Print (Process) Resolution in DPI. \n Hit Submit to Calculate Platen Speed in IPS or Webdrive Speed in FPM", font=('fixedsys', 16), fg='#0c161c', pady=50)
        helplabel.pack()

    speedhelp = tk.Button(speedtop, text="Help", fg='#0c161c', bg='#d2d6d8', font=('fixedsys', 12),
                            command=helpspeed)
    speedhelp.place(height=50, width=175, x=10, y=250)

    


#Dropmass Calculator
def mass():
    masstop = tk.Toplevel(root, bg ='#74add0', height=600, width=600)
    masstop.title("Universal Dropmass Calculator")

    jetlabel = tk.Label(masstop, text="Number of Jets", font=('fixedsys', 12), fg='#0c161c', bg ='#74add0')
    jetlabel.place(height=50, width=175, x=10, y=10)
    jetentry = tk.Entry(masstop, font=('fixedsys', 24))
    jetentry.place(height=50, width=175, x=10, y=50)
    jetoutlabel = tk.Label(masstop, text="Number of Jets Out", font=('fixedsys', 12), fg='#0c161c', bg ='#74add0')
    jetoutlabel.place(height=50, width=175, x=10, y=90)
    jetoutentry = tk.Entry(masstop, font=('fixedsys', 24))
    jetoutentry.place(height=50, width=175, x=10, y=130)
    copylabel = tk.Label(masstop, text="Number of Copies/Fires", font=('fixedsys', 12), fg='#0c161c', bg ='#74add0')
    copylabel.place(height=50, width=175, x=10, y=170)
    copyentry = tk.Entry(masstop, font=('fixedsys', 24))
    copyentry.place(height=50, width=175, x=10, y=210)
    pixellabel = tk.Label(masstop, text="Number of Pixels", font=('fixedsys', 12), fg='#0c161c', bg ='#74add0')
    pixellabel.place(height=50, width=175, x=10, y=250)
    pixelentry = tk.Entry(masstop, font=('fixedsys', 24))
    pixelentry.place(height=50, width=175, x=10, y=290)
    gramlabel = tk.Label(masstop, text="Mass in Grams:", font=('fixedsys', 12), fg='#0c161c', bg ='#74add0')
    gramlabel.place(height=50, width=175, x=10, y=330)
    gramentry = tk.Entry(masstop, font=('fixedsys', 24))
    gramentry.place(height=50, width=175, x=10, y=370)

    colorlabelm = tk.Label(masstop, text="Change Background Color", fg='#0c161c', bg ='#74add0', font=('fixedsys', 8))
    colorlabelm.place(height=50, width=200, x=0, y=500)


    def blumasses():
        masstop.configure(bg='#74add0')
        jetlabel.configure(bg='#74add0')
        jetoutlabel.configure(bg='#74add0')
        copylabel.configure(bg='#74add0')
        pixellabel.configure(bg='#74add0')
        gramlabel.configure(bg='#74add0')
        colorlabelm.configure(bg='#74add0')

    def grnmasses():
        masstop.configure(bg='#96de9d')
        jetlabel.configure(bg='#96de9d')
        jetoutlabel.configure(bg='#96de9d')
        copylabel.configure(bg='#96de9d')
        pixellabel.configure(bg='#96de9d')
        gramlabel.configure(bg='#96de9d')
        colorlabelm.configure(bg='#96de9d')

    def redmasses():
        masstop.configure(bg='#ff6666')
        jetlabel.configure(bg='#ff6666')
        jetoutlabel.configure(bg='#ff6666')
        copylabel.configure(bg='#ff6666')
        pixellabel.configure(bg='#ff6666')
        gramlabel.configure(bg='#ff6666')
        colorlabelm.configure(bg='#ff6666')

    def stlmasses():
        masstop.configure(bg='#facdf4')
        jetlabel.configure(bg='#facdf4')
        jetoutlabel.configure(bg='#facdf4')
        copylabel.configure(bg='#facdf4')
        pixellabel.configure(bg='#facdf4')
        gramlabel.configure(bg='#facdf4')
        colorlabelm.configure(bg='#facdf4')

    



    blumass = tk.Button(masstop, text="Blue", fg='#0c161c', bg='#d2d6d8', font=('fixedsys', 8),
                            command=blumasses)
    blumass.place(height=50, width=80, x=200, y=500)

    grnmass = tk.Button(masstop, text="Green", fg='#0c161c', bg='#d2d6d8', font=('fixedsys', 8),
                            command=grnmasses)
    grnmass.place(height=50, width=80, x=360, y=500)

    redmass = tk.Button(masstop, text="Red", fg='#0c161c', bg='#d2d6d8', font=('fixedsys', 8),
                            command=redmasses)
    redmass.place(height=50, width=80, x=280, y=500)

    stlmass = tk.Button(masstop, text="Pink", fg='#0c161c', bg='#d2d6d8', font=('fixedsys', 8),
                            command=stlmasses)
    stlmass.place(height=50, width=80, x=440, y=500)


    def massexit():
        masstop.destroy()

    massback = tk.Button(masstop, text="Back", fg='#0c161c', bg='#d2d6d8', font=('fixedsys', 4),
                            command=massexit)
    massback.place(height=25, width=40, x=550, y=10)


    def masscalc(self):
        jets = int(jetentry.get())
        jetsout = int(jetoutentry.get())
        fires = int(copyentry.get())
        pixels = int(pixelentry.get())
        grams = float(gramentry.get())
        hadm = (grams * 1000000000) / ((jets - jetsout) * pixels * fires)

        hadmlabel = tk.Label(masstop, text="HADM: " + str(round(hadm, 2)) + " ng", font=('fixedsys', 20), fg='#0c161c', relief='solid')
        hadmlabel.place(height=50, width=300, x=230, y=210)

    def masscalcbut():
        jets = int(jetentry.get())
        jetsout = int(jetoutentry.get())
        fires = int(copyentry.get())
        pixels = int(pixelentry.get())
        grams = float(gramentry.get())
        hadm = (grams * 1000000000) / ((jets - jetsout) * pixels * fires)

        hadmlabel = tk.Label(masstop, text="HADM: " + str(round(hadm, 2)) + " ng", font=('fixedsys', 20), fg='#0c161c', relief='solid')
        hadmlabel.place(height=50, width=300, x=230, y=210)






    masssub = tk.Button(masstop, text="Submit", fg='#0c161c', bg='#d2d6d8', font=('fixedsys', 12),
                         command=masscalcbut)
    masssub.place(height=50, width=175, x=10, y=430)
    masstop.bind('<Return>', masscalc)

    def helpmass():
        helpmtop = tk.Toplevel(masstop, bg ='#74add0', height=250, width=250)
        helpmtop.title("Universal Dropmass Calculator---HELP")
        helpmlabel = tk.Label(helpmtop, text="Enter Total # of Jets In Printhead \n\n Enter # of Jets Out in Printhead \n\n Enter Copies/Fires to be Printed/Fired \n\n Enter Pixels in Dropmass Image (if on Char, Enter 1) \n\n Take Mass Measurement and Enter Mass in Grams \n\n Hit Submit to Calculate Head Average Drop Mass in ng.", font=('fixedsys', 16), fg='#0c161c', pady=50)
        helpmlabel.pack()

    masshelp = tk.Button(masstop, text="Help", fg='#0c161c', bg='#d2d6d8', font=('fixedsys', 12),
                            command=helpmass)
    masshelp.place(height=50, width=175, x=195, y=430)


#Mass Calibrate
def calibrate():
    calitop = tk.Toplevel(root, bg ='#74add0', height=600, width=600)
    calitop.title("Mass Calibrate Calculator")
    v1label = tk.Label(calitop, text="Voltage # 1 (low)", font=('fixedsys', 12), fg='#0c161c', bg ='#74add0')
    v1label.place(height=50, width=175, x=10, y=10)
    v1entry = tk.Entry(calitop, font=('fixedsys', 24))
    v1entry.place(height=50, width=175, x=10, y=50)
    v2label = tk.Label(calitop, text="Voltage # 2 (mid)", font=('fixedsys', 12), fg='#0c161c', bg ='#74add0')
    v2label.place(height=50, width=175, x=10, y=90)
    v2entry = tk.Entry(calitop, font=('fixedsys', 24))
    v2entry.place(height=50, width=175, x=10, y=130)
    v3label = tk.Label(calitop, text="Voltage # 3 (high)", font=('fixedsys', 12), fg='#0c161c', bg ='#74add0')
    v3label.place(height=50, width=175, x=10, y=170)
    v3entry = tk.Entry(calitop, font=('fixedsys', 24))
    v3entry.place(height=50, width=175, x=10, y=210)
    targetlabel = tk.Label(calitop, text="Target Mass (ng)", font=('fixedsys', 12), fg='#0c161c', bg ='#74add0')
    targetlabel.place(height=50, width=175, x=10, y=250)
    targetentry = tk.Entry(calitop, font=('fixedsys', 24))
    targetentry.place(height=50, width=175, x=10, y=290)
    m1label = tk.Label(calitop, text="Voltage 1 Mass (ng)", font=('fixedsys', 12), fg='#0c161c', bg ='#74add0')
    m1label.place(height=50, width=175, x=300, y=10)
    m1entry = tk.Entry(calitop, font=('fixedsys', 24))
    m1entry.place(height=50, width=175, x=300, y=50)
    m2label = tk.Label(calitop, text="Voltage 2 Mass (ng)", font=('fixedsys', 12), fg='#0c161c', bg ='#74add0')
    m2label.place(height=50, width=175, x=300, y=90)
    m2entry = tk.Entry(calitop, font=('fixedsys', 24))
    m2entry.place(height=50, width=175, x=300, y=130)
    m3label = tk.Label(calitop, text="Voltage 3 Mass (ng)", font=('fixedsys', 12), fg='#0c161c', bg ='#74add0')
    m3label.place(height=50, width=175, x=300, y=170)
    m3entry = tk.Entry(calitop, font=('fixedsys', 24))
    m3entry.place(height=50, width=175, x=300, y=210)

    colorlabelc = tk.Label(calitop, text="Change Background Color", fg='#0c161c', bg ='#74add0', font=('fixedsys', 8))
    colorlabelc.place(height=50, width=200, x=0, y=500)

    def blucali():
        calitop.configure(bg='#74add0')
        v1label.configure(bg='#74add0')
        v2label.configure(bg='#74add0')
        v3label.configure(bg='#74add0')
        targetlabel.configure(bg='#74add0')
        m1label.configure(bg='#74add0')
        m2label.configure(bg='#74add0')
        m3label.configure(bg='#74add0')
        colorlabelc.configure(bg='#74add0')

    def grncali():
        calitop.configure(bg='#96de9d')
        v1label.configure(bg='#96de9d')
        v2label.configure(bg='#96de9d')
        v3label.configure(bg='#96de9d')
        targetlabel.configure(bg='#96de9d')
        m1label.configure(bg='#96de9d')
        m2label.configure(bg='#96de9d')
        m3label.configure(bg='#96de9d')
        colorlabelc.configure(bg='#96de9d')

    def redcali():
        calitop.configure(bg='#ff6666')
        v1label.configure(bg='#ff6666')
        v2label.configure(bg='#ff6666')
        v3label.configure(bg='#ff6666')
        targetlabel.configure(bg='#ff6666')
        m1label.configure(bg='#ff6666')
        m2label.configure(bg='#ff6666')
        m3label.configure(bg='#ff6666')
        colorlabelc.configure(bg='#ff6666')

    def stlcali():
        calitop.configure(bg='#facdf4')
        v1label.configure(bg='#facdf4')
        v2label.configure(bg='#facdf4')
        v3label.configure(bg='#facdf4')
        targetlabel.configure(bg='#facdf4')
        m1label.configure(bg='#facdf4')
        m2label.configure(bg='#facdf4')
        m3label.configure(bg='#facdf4')
        colorlabelc.configure(bg='#facdf4')


    blucali = tk.Button(calitop, text="Blue", fg='#0c161c', bg='#d2d6d8', font=('fixedsys', 8),
                            command=blucali)
    blucali.place(height=50, width=80, x=200, y=500)

    grncali = tk.Button(calitop, text="Green", fg='#0c161c', bg='#d2d6d8', font=('fixedsys', 8),
                            command=grncali)
    grncali.place(height=50, width=80, x=360, y=500)

    redcali = tk.Button(calitop, text="Red", fg='#0c161c', bg='#d2d6d8', font=('fixedsys', 8),
                            command=redcali)
    redcali.place(height=50, width=80, x=280, y=500)

    stlcali = tk.Button(calitop, text="Pink", fg='#0c161c', bg='#d2d6d8', font=('fixedsys', 8),
                            command=stlcali)
    stlcali.place(height=50, width=80, x=440, y=500)


    def caliexit():
        calitop.destroy()

    caliback = tk.Button(calitop, text="Back", fg='#0c161c', bg='#d2d6d8', font=('fixedsys', 4),
                            command=caliexit)
    caliback.place(height=25, width=40, x=550, y=10)

    

    def calibrated(self):
        v1 = float(v1entry.get())

        v3 = float(v3entry.get())
        m1 = float(m1entry.get())
        m3 = float(m3entry.get())
        slope = (m3 - m1) / (v3 - v1)
        target = float(targetentry.get())
        intercept = m1 - slope * v1

        vtarget = (target - intercept) / slope
        vollabel = tk.Label(calitop, text="Try " + str(round(vtarget, 1)) + " volts", font=('fixedsys', 20), fg='#0c161c',
                             relief='solid')
        vollabel.place(height=50, width=300, x=200, y=400)

    def calibratedbut():
        v1 = float(v1entry.get())

        v3 = float(v3entry.get())
        m1 = float(m1entry.get())
        m3 = float(m3entry.get())
        slope = (m3 - m1) / (v3 - v1)
        target = float(targetentry.get())
        intercept = m1 - slope * v1

        vtarget = (target - intercept) / slope
        vollabel = tk.Label(calitop, text="Try " + str(round(vtarget, 1)) + " volts", font=('fixedsys', 20), fg='#0c161c',
                             relief='solid')
        vollabel.place(height=50, width=300, x=200, y=400)

    calsub = tk.Button(calitop, text="Submit", fg='#0c161c', bg='#d2d6d8', font=('fixedsys', 12),
                        command=calibratedbut)
    calsub.place(height=50, width=175, x=10, y=350)

    calitop.bind('<Return>', calibrated)

    def helpcal():
        calhtop = tk.Toplevel(calitop, bg ='#74add0', height=250, width=250)
        calhtop.title("Mass Calibrate Calculator---HELP")
        helpclabel = tk.Label(calhtop, text="Use this Calculator with the Universal Dropmass Calculator \n\n Pick Three Stable Voltages to Perform Dropmass at \n\n Enter the Voltages, Lowest to Highest \n\n Enter the Dropmass Target in ng. \n\n Perform Dropmasses at Each Voltage and Enter the HADM (ng) in for Each Respective Voltage \n\n Click Submit to Calculate a Predicted Voltage to Achieve the Requested Target.", font=('fixedsys', 16), fg='#0c161c', pady=50)
        helpclabel.pack()

    calhelp = tk.Button(calitop, text="Help", fg='#0c161c', bg='#d2d6d8', font=('fixedsys', 12),
                            command=helpcal)
    calhelp.place(height=50, width=175, x=10, y=425)


def extra():

    extratop = tk.Toplevel(root, bg ='#74add0', height=600, width=600)
    extratop.title("Extra Features")

    def extraexit():
            extratop.destroy()

    extraback = tk.Button(extratop, text="Back", fg='#0c161c', bg='#d2d6d8', font=('fixedsys', 4),
                            command=extraexit)
    extraback.place(height=25, width=40, x=550, y=10)











    

    def delay():



        

        delaytop = tk.Toplevel(extratop, bg ='#74add0', height=600, width=600)
        delaytop.title("Trigger Delay")
        d1label = tk.Label(delaytop, text="Enter Delay for 1200 dpi", font=('fixedsys', 12), fg='#0c161c', bg ='#74add0')
        d1label.place(height=50, width=200, x=10, y=10)
        d1entry = tk.Entry(delaytop, font=('fixedsys', 24))
        d1entry.place(height=50, width=175, x=10, y=50)
        


        def dcalc(self):


            d1 = int(d1entry.get())

            dpi2400 = d1 * 2
            dpi900 = d1 * (3 / 4)
            dpi600 = d1 / 2
            dpi300 = d1 / 4
            dpi400 = d1 / 3
            



            dlabel2400 = tk.Label(delaytop, text="2400 DPI = " + str(round((dpi2400))), font=('fixedsys', 16), fg='#0c161c',
                             relief='solid')
            dlabel2400.place(height=50, width=500, x=50, y=150)
            dlabel900 = tk.Label(delaytop, text="900 DPI = " + str(round((dpi900))), font=('fixedsys', 16), fg='#0c161c',
                             relief='solid')
            dlabel900.place(height=50, width=500, x=50, y=200)
            dlabel600 = tk.Label(delaytop, text="600 DPI = " + str(round((dpi600))), font=('fixedsys', 16), fg='#0c161c',
                             relief='solid')
            dlabel600.place(height=50, width=500, x=50, y=250)
            dlabel400 = tk.Label(delaytop, text="400 DPI = " + str(round((dpi400))), font=('fixedsys', 16), fg='#0c161c',
                             relief='solid')
            dlabel400.place(height=50, width=500, x=50, y=300)
            dlabel300 = tk.Label(delaytop, text="300 DPI = " + str(round((dpi300))), font=('fixedsys', 16), fg='#0c161c',
                             relief='solid')
            dlabel300.place(height=50, width=500, x=50, y=350)





        def dcalcbut():

            d1 = int(d1entry.get())

            dpi2400 = d1 * 2
            dpi900 = d1 * (3 / 4)
            dpi600 = d1 / 2
            dpi300 = d1 / 4
            dpi400 = d1 / 3


            dlabel2400 = tk.Label(delaytop, text="2400 DPI = " + str(round((dpi2400))), font=('fixedsys', 16), fg='#0c161c',
                             relief='solid')
            dlabel2400.place(height=50, width=500, x=50, y=150)
            dlabel900 = tk.Label(delaytop, text="900 DPI = " + str(round((dpi900))), font=('fixedsys', 16), fg='#0c161c',
                             relief='solid')
            dlabel900.place(height=50, width=500, x=50, y=200)
            dlabel600 = tk.Label(delaytop, text="600 DPI = " + str(round((dpi600))), font=('fixedsys', 16), fg='#0c161c',
                             relief='solid')
            dlabel600.place(height=50, width=500, x=50, y=250)
            dlabel400 = tk.Label(delaytop, text="400 DPI = " + str(round((dpi400))), font=('fixedsys', 16), fg='#0c161c',
                             relief='solid')
            dlabel400.place(height=50, width=500, x=50, y=300)
            dlabel300 = tk.Label(delaytop, text="300 DPI = " + str(round((dpi300))), font=('fixedsys', 16), fg='#0c161c',
                             relief='solid')
            dlabel300.place(height=50, width=500, x=50, y=350)

















        dsub = tk.Button(delaytop, text="Submit", fg='#0c161c', bg='#d2d6d8', font=('fixedsys', 12),
                         command=dcalcbut)
        dsub.place(height=50, width=175, x=195, y=50)
        delaytop.bind('<Return>', dcalc)


        def dcalchelp():
            delayhelptop = tk.Toplevel(delaytop, bg ='#74add0', height=400, width=400)
            delayhelptop.title("Trigger Delay Calculator---HELP")
            dhlabel = tk.Label(delayhelptop, text="Enter trigger delay for 1200 dpi. \n Click Submit to reveal delays to use for other process resolutions", font=('fixedsys', 16), fg='#0c161c', pady=50)
            dhlabel.pack()
            

            

        dhelp = tk.Button(delaytop, text="Help", fg='#0c161c', bg='#d2d6d8', font=('fixedsys', 12),
                         command=dcalchelp)
        dhelp.place(height=50, width=175, x=375, y=50)

       
            
        



        def delayexit():
            delaytop.destroy()

        delayback = tk.Button(delaytop, text="Back", fg='#0c161c', bg='#d2d6d8', font=('fixedsys', 4),
                            command=delayexit)
        delayback.place(height=25, width=40, x=550, y=10)


        delayback = tk.Button(delaytop, text="Back", fg='#0c161c', bg='#d2d6d8', font=('fixedsys', 4),
                            command=delayexit)
        delayback.place(height=25, width=40, x=550, y=10)



    
    def waveform():



        

        wftop = tk.Toplevel(extratop, bg ='#74add0', height=600, width=600)
        wftop.title("Waveform Converter")
        wflabel1 = tk.Label(wftop, text="Enter Pulse Amplitude for .INI", font=('fixedsys', 12), fg='#0c161c', bg ='#74add0')
        wflabel1.place(height=50, width=400, x=80, y=10)
        wfentry1 = tk.Entry(wftop, font=('fixedsys', 24))
        wfentry1.place(height=50, width=175, x=200, y=50)

        def wf1calc():

            w1 = float(wfentry1.get())

            w1value = (w1 * 255) / 184


            w1label = tk.Label(wftop, text="CSV Pulse Amplitude = " + str(round((w1value))), font=('fixedsys', 12), fg='#0c161c',
                             relief='solid')
            w1label.place(height=50, width=300, x=140, y=170)

        def wf1calcent(self):

            w1 = float(wfentry1.get())

            w1value = (w1 * 255) / 184


            w1label = tk.Label(wftop, text="CSV Pulse Amplitude = " + str(round((w1value))), font=('fixedsys', 12), fg='#0c161c',
                             relief='solid')
            w1label.place(height=50, width=300, x=140, y=170)


        wflabel2 = tk.Label(wftop, text="Enter Pulse Amplitude for .CSV", font=('fixedsys', 12), fg='#0c161c', bg ='#74add0')
        wflabel2.place(height=50, width=400, x=80, y=300)
        wfentry2 = tk.Entry(wftop, font=('fixedsys', 24))
        wfentry2.place(height=50, width=175, x=200, y=360)

        def wf2calc():

            w2 = float(wfentry2.get())

            w2value = (w2 * 184) / 255


            w2label = tk.Label(wftop, text="INI Pulse Amplitude = " + str(round((w2value))), font=('fixedsys', 12), fg='#0c161c',
                             relief='solid')
            w2label.place(height=50, width=300, x=140, y=480)

        def wf2calcent(self):

            w2 = float(wfentry2.get())

            w2value = (w2 * 184) / 255


            w2label = tk.Label(wftop, text="INI Pulse Amplitude = " + str(round((w2value))), font=('fixedsys', 12), fg='#0c161c',
                             relief='solid')
            w2label.place(height=50, width=300, x=140, y=480)

            

            

            









        wfbut1 = tk.Button(wftop, text="Submit", fg='#0c161c', bg='#d2d6d8', font=('fixedsys', 12),
                           command=wf1calc)
        wfbut1.place(height=50, width=175, x=200, y=110)
        wftop.bind('<Return>', wf1calcent)

        wfbut2 = tk.Button(wftop, text="Submit", fg='#0c161c', bg='#d2d6d8', font=('fixedsys', 12),
                           command=wf2calc)
        wfbut2.place(height=50, width=175, x=200, y=420)
        wftop.bind('<Return>', wf2calcent)

        def wfhelp():
            wfhelptop = tk.Toplevel(wftop, bg ='#74add0', height=400, width=400)
            wfhelptop.title("WF Converter---HELP")
            wflabel = tk.Label(wfhelptop, text="The amplitude scale maximum of a .INI WF file is 184. \n The amplitude scale maximum of a .CSV WF file is 255. \n Use this converter to determine the amplitude levels when \n converting between the two formats.", font=('fixedsys', 16), fg='#0c161c', pady=50)
            wflabel.pack()
            

            

        wfhelp = tk.Button(wftop, text="Help", fg='#0c161c', bg='#d2d6d8', font=('fixedsys', 12),
                         command=wfhelp)
        wfhelp.place(height=25, width=40, x=550, y=50)

        def wfexit():
            wftop.destroy()

        wfback = tk.Button(wftop, text="Back", fg='#0c161c', bg='#d2d6d8', font=('fixedsys', 4),
                            command=wfexit)
        wfback.place(height=25, width=40, x=550, y=10)
                


    def tempcalc():

        temptop = tk.Toplevel(extratop, bg ='#74add0', height=600, width=600)
        temptop.title("Temperature Converter")
        tlabel1 = tk.Label(temptop, text="Enter Temperature in F", font=('fixedsys', 12), fg='#0c161c', bg ='#74add0')
        tlabel1.place(height=50, width=400, x=80, y=10)
        tentry1 = tk.Entry(temptop, font=('fixedsys', 24))
        tentry1.place(height=50, width=175, x=200, y=50)

        def t1calc():

            t1 = float(tentry1.get())

            t1value = float((t1 - 32) * 5 / 9)


            t1label = tk.Label(temptop, text="Temperature in C = " + str(round(t1value, 1)) + " degrees", font=('fixedsys', 12), fg='#0c161c',
                             relief='solid')
            t1label.place(height=50, width=300, x=140, y=170)

        


        tlabel2 = tk.Label(temptop, text="Enter Temperature in C", font=('fixedsys', 12), fg='#0c161c', bg ='#74add0')
        tlabel2.place(height=50, width=400, x=80, y=300)
        tentry2 = tk.Entry(temptop, font=('fixedsys', 24))
        tentry2.place(height=50, width=175, x=200, y=360)

        def t2calc():

            t2 = float(tentry2.get())

            t2value = (t2 * 9 / 5) + 32


            t2label = tk.Label(temptop, text="Temperature in F = " + str(round(t2value, 1)) + " degrees", font=('fixedsys', 12), fg='#0c161c',
                             relief='solid')
            t2label.place(height=50, width=300, x=140, y=480)

        

            

            

            









        tbut1 = tk.Button(temptop, text="Submit", fg='#0c161c', bg='#d2d6d8', font=('fixedsys', 12),
                           command=t1calc)
        tbut1.place(height=50, width=175, x=200, y=110)
        

        tbut2 = tk.Button(temptop, text="Submit", fg='#0c161c', bg='#d2d6d8', font=('fixedsys', 12),
                           command=t2calc)
        tbut2.place(height=50, width=175, x=200, y=420)
        

        def thelp():
            thelptop = tk.Toplevel(temptop, bg ='#74add0', height=400, width=400)
            thelptop.title("Temp. Converter---HELP")
            tlabel = tk.Label(thelptop, text="Converts F to C and vise versa", font=('fixedsys', 16), fg='#0c161c', pady=50)
            tlabel.pack()
            

            

        thelp = tk.Button(temptop, text="Help", fg='#0c161c', bg='#d2d6d8', font=('fixedsys', 12),
                         command=thelp)
        thelp.place(height=25, width=40, x=550, y=50)

        def texit():
            temptop.destroy()

        tback = tk.Button(temptop, text="Back", fg='#0c161c', bg='#d2d6d8', font=('fixedsys', 4),
                            command=texit)
        tback.place(height=25, width=40, x=550, y=10)
        

        
            





























        
        

    triggerbutton = tk.Button(extratop, text="Trigger Delay", fg='#0c161c', bg='#d2d6d8', font=('fixedsys', 12), command=delay)
    triggerbutton.place(height=50, width=175, x=215, y=200,)

    wfbutton = tk.Button(extratop, text="Waveform Converter", fg='#0c161c', bg='#d2d6d8', font=('fixedsys', 12), command=waveform)
    wfbutton.place(height=50, width=175, x=215, y=260,)

    tempbutton = tk.Button(extratop, text="Temperature Converter", fg='#0c161c', bg='#d2d6d8', font=('fixedsys', 12), command=tempcalc)
    tempbutton.place(height=50, width=175, x=215, y=320,)

    
    

    

    

    
    

    

    

    
    

    

#Main Window Calc Buttons

speedbutton = tk.Button(frame, text="Universal Speed", fg='#0c161c', bg='#d2d6d8', font=('fixedsys', 12), command=speed)
speedbutton.place(height=50, width=175, x=240, y=200,)

massbutton = tk.Button(frame, text="Universal Dropmass", fg='#0c161c', bg='#d2d6d8', font=('fixedsys', 12), command=mass)
massbutton.place(height=50, width=175, x=240, y=300,)

calbutton = tk.Button(frame, text="Mass Calibrate", fg='#0c161c', bg='#d2d6d8', font=('fixedsys', 12), command=calibrate)
calbutton.place(height=50, width=175, x=240, y=400,)

extrabutton = tk.Button(frame, text="More...", fg='#0c161c', bg='#d2d6d8', font=('fixedsys', 12), command=extra)
extrabutton.place(height=50, width=175, x=240, y=500,)







root.mainloop()
