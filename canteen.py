
from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import *
from PyQt5.QtWidgets import QMessageBox
import pandas as pd
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        #--------------------------------------------MAIN WINDOW-------------------------------------------
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 800)
        MainWindow.setMinimumSize(1200,800) 
        MainWindow.setMaximumSize(1200,800) #Setting the minimum and maximum size of window to avoid resizing by user

        icon = QtGui.QIcon() 
        icon.addPixmap(QtGui.QPixmap("image002.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off) 
        MainWindow.setWindowIcon(icon) #Setting the NTU logo as the icon in the MainWindow bar 

        self.centralwidget = QtWidgets.QWidget(MainWindow) #Creating a central widget which is the focus of the main window

        self.frame = QtWidgets.QFrame(self.centralwidget) #Creating a frame for the main window 
        self.frame.setGeometry(QtCore.QRect(0, 0, 1200, 800)) #Setting the size of the frame 

        self.bgpic = QtWidgets.QLabel(self.frame) #Creating the Background picture object
        self.bgpic.setGeometry(QtCore.QRect(-10, -470, 1250, 1500)) # Setting the size of the background picture object
        self.bgpic.setPixmap(QtGui.QPixmap("image001.jpg")) #Retrieving the image
        self.bgpic.setScaledContents(True) #Scaling contents according to the frame

        self.Ntulogo = QtWidgets.QLabel(self.frame)
        self.Ntulogo.setGeometry(QtCore.QRect(525, 180, 121, 141))
        self.Ntulogo.setPixmap(QtGui.QPixmap("image002.png"))
        self.Ntulogo.setScaledContents(True)

        font = QtGui.QFont() #Setting the font for WELCOME 
        font.setFamily("Futura") #Font type
        font.setPointSize(24) #Font size
        font.setBold(True)  #Bold

        self.Welcome = QtWidgets.QLabel(self.frame)
        self.Welcome.setGeometry(QtCore.QRect(125, 350, 900, 75))
        self.Welcome.setFont(font)
        self.Welcome.setAutoFillBackground(True) #Filling the background of WELCOME
        self.Welcome.setFrameShape(QtWidgets.QFrame.Box) 
        self.Welcome.setFrameShadow(QtWidgets.QFrame.Raised) #Setting border to the WELCOME object    
        self.Welcome.setText("   Welcome to NTU Canteen System") #The Text inside WELCOME Object

        self.Continuebutton = QtWidgets.QPushButton(self.frame)
        self.Continuebutton.setGeometry(QtCore.QRect(515, 440, 141, 31))
        self.Continuebutton.setText("Press to Continue")
        self.Continuebutton.setShortcut("Return") #Setting shortcut so button is activated when ENTER is pressed on the keyboard
    
        #--------------------------------------------MENU and TAB WINDOW-------------------------------------------

        MainWindow.setCentralWidget(self.centralwidget) #???????

        self.frame1 = QtWidgets.QFrame(self.centralwidget) #Creating the frame of MENU Window
        self.frame1.setGeometry(QtCore.QRect(0, 0, 1200, 800))

        self.tabWidget = QtWidgets.QTabWidget(self.frame1) #Creating the frame for the Tabs
        self.tabWidget.setGeometry(QtCore.QRect(0, 10, 750, 620))#Setting size of the frame
        self.tabWidget.setIconSize(QtCore.QSize(20,20)) #Setting size of the Icon 
        
        self.labelfont = QtGui.QFont() #Setting the LABEL font for Menu Window
        self.labelfont.setFamily("Lucida Bright") 
        self.labelfont.setPointSize(15)
        self.labelfont.setBold(True)

        self.textfont = QtGui.QFont() #Setting the CONTENT font for Menu Window
        self.textfont.setFamily("Sylfaen")
        self.textfont.setPointSize(11)

        #----------------------------------------MCDONALDS TAB-------------------------------------
        

        self.McD = QtWidgets.QWidget()
        self.tabWidget.addTab(self.McD,icon,"McDonalds") #Creating the McDonalds Tab

        self.mcdbgpic = QtWidgets.QLabel(self.McD)
        self.mcdbgpic.setGeometry(QtCore.QRect(-150, -50, 975,850)) #Setting the size of the background picture
        self.mcdbgpic.setPixmap(QtGui.QPixmap("McDonalds bg.jpg")) #Retrieving the background picture
        self.mcdbgpic.setScaledContents(True) #Scaling the background picture for entire proportion

        self.mcdlogo = QtWidgets.QLabel(self.McD)
        self.mcdlogo.setGeometry(QtCore.QRect(320, 20, 131, 111)) 
        self.mcdlogo.setPixmap(QtGui.QPixmap("McDonalds logo.png")) 
        self.mcdlogo.setScaledContents(True) 

        self.mcdmenu = QtWidgets.QLabel(self.McD)
        self.mcdmenu.setGeometry(QtCore.QRect(105, 160, 186, 41))
        self.mcdmenu.setFont(self.labelfont) #Setting the font for McD Menu object
        self.mcdmenu.setAutoFillBackground(True) #Filling the background of McD Menu 
        self.mcdmenu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mcdmenu.setFrameShadow(QtWidgets.QFrame.Raised)  #Setting border to the McD Menu Object
        self.mcdmenu.setText("    Menu    ") #The Text inside McD Menu Object

        self.mcdmenutext = QtWidgets.QTextEdit(self.McD)
        self.mcdmenutext.setGeometry(QtCore.QRect(70, 220, 295, 225))
        self.mcdmenutext.setFont(self.textfont)
        self.mcdmenutext.setAutoFillBackground(True)
        self.mcdmenutext.setReadOnly(True)

        self.mcdprice = QtWidgets.QLabel(self.McD)
        self.mcdprice.setGeometry(QtCore.QRect(440, 160, 186, 41))
        self.mcdprice.setFont(self.labelfont)
        self.mcdprice.setAutoFillBackground(True)
        self.mcdprice.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mcdprice.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mcdprice.setText("    Price   ")

        self.mcdpricetext = QtWidgets.QTextEdit(self.McD)
        self.mcdpricetext.setGeometry(QtCore.QRect(435, 220, 200, 225))
        self.mcdpricetext.setFont(self.textfont)
        self.mcdpricetext.setReadOnly(True)

        icon = QtGui.QIcon() #Creating the icon for McD Tab 
        icon.addPixmap(QtGui.QPixmap("McDonalds logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        
        #-----------------------------------------PIZZA HUT EXPRESS TAB----------------------------------------

        self.PizzaHut = QtWidgets.QWidget()
        self.tabWidget.addTab(self.PizzaHut,icon, "Pizza Hut Express")

        self.pizzabgpic = QtWidgets.QLabel(self.PizzaHut)
        self.pizzabgpic.setGeometry(QtCore.QRect(-150, -50, 975,850))
        self.pizzabgpic.setPixmap(QtGui.QPixmap("Pizza Hut Express bg.jpg"))
        self.pizzabgpic.setScaledContents(True)

        self.pizzalogo = QtWidgets.QLabel(self.PizzaHut)
        self.pizzalogo.setGeometry(QtCore.QRect(320, 30, 140, 120))
        self.pizzalogo.setAutoFillBackground(False)
        self.pizzalogo.setPixmap(QtGui.QPixmap("Pizza Hut Express logo.png"))
        self.pizzalogo.setScaledContents(True)

        self.pizzamenu = QtWidgets.QLabel(self.PizzaHut)
        self.pizzamenu.setGeometry(QtCore.QRect(105, 160, 186, 41))
        self.pizzamenu.setFont(self.labelfont)
        self.pizzamenu.setAutoFillBackground(True)
        self.pizzamenu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pizzamenu.setFrameShadow(QtWidgets.QFrame.Raised) 
        self.pizzamenu.setText("    Menu    ") 

        self.pizzamenutext = QtWidgets.QTextEdit(self.PizzaHut)
        self.pizzamenutext.setGeometry(QtCore.QRect(70, 220, 255, 225))
        self.pizzamenutext.setFont(self.textfont)
        self.pizzamenutext.setReadOnly(True)

        self.pizzaprice = QtWidgets.QLabel(self.PizzaHut)
        self.pizzaprice.setGeometry(QtCore.QRect(440, 160, 186, 41))
        self.pizzaprice.setFont(self.labelfont)
        self.pizzaprice.setAutoFillBackground(True)
        self.pizzaprice.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pizzaprice.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pizzaprice.setText("    Price   ")    
        
        self.pizzapricetext = QtWidgets.QTextEdit(self.PizzaHut)
        self.pizzapricetext.setGeometry(QtCore.QRect(435, 220, 200, 225))
        self.pizzapricetext.setFont(self.textfont)
        self.pizzapricetext.setReadOnly(True)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Pizza Hut Express logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        
        #-----------------------------------------BAKERY CUISINE TAB------------------------------------------

        self.Bakery = QtWidgets.QWidget()
        self.Bakery.setObjectName("Bakery")

        self.bakerybgpic = QtWidgets.QLabel(self.Bakery)
        self.bakerybgpic.setGeometry(QtCore.QRect(-150, -50, 975,850))
        self.bakerybgpic.setPixmap(QtGui.QPixmap("Bakery Cuisine bg.jpg"))
        self.bakerybgpic.setScaledContents(True)

        self.bakerylogo = QtWidgets.QLabel(self.Bakery)
        self.bakerylogo.setGeometry(QtCore.QRect(250, -15, 250, 220))
        self.bakerylogo.setPixmap(QtGui.QPixmap("Bakery Cuisine logo.png"))
        self.bakerylogo.setScaledContents(True)

        self.bakerymenu = QtWidgets.QLabel(self.Bakery)
        self.bakerymenu.setGeometry(QtCore.QRect(105, 160, 186, 41))
        self.bakerymenu.setFont(self.labelfont)
        self.bakerymenu.setAutoFillBackground(True)
        self.bakerymenu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bakerymenu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bakerymenu.setText("    Menu    ")

        self.bakerymenutext = QtWidgets.QTextEdit(self.Bakery)
        self.bakerymenutext.setGeometry(QtCore.QRect(70, 220, 258, 225))
        self.bakerymenutext.setFont(self.textfont)
        self.bakerymenutext.setReadOnly(True)

        self.bakeryprice = QtWidgets.QLabel(self.Bakery)
        self.bakeryprice.setGeometry(QtCore.QRect(440, 160, 186, 41))
        self.bakeryprice.setFont(self.labelfont)
        self.bakeryprice.setAutoFillBackground(True)
        self.bakeryprice.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bakeryprice.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bakeryprice.setText("    Price   ")

        self.bakerypricetext = QtWidgets.QTextEdit(self.Bakery)
        self.bakerypricetext.setGeometry(QtCore.QRect(435, 220, 200, 225))
        self.bakerypricetext.setFont(self.textfont)
        self.bakerypricetext.setReadOnly(True)
        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Bakery Cuisine logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.tabWidget.addTab(self.Bakery,icon, "Bakery Cuisine")
        
        #---------------------------------------------MINI WOK TAB-------------------------------------------

        self.Miniwok = QtWidgets.QWidget()

        self.wokbgpic = QtWidgets.QLabel(self.Miniwok)
        self.wokbgpic.setGeometry(QtCore.QRect(-150, -50, 975,850))
        self.wokbgpic.setPixmap(QtGui.QPixmap("MiniWok bg.jpg"))
        self.wokbgpic.setScaledContents(True)

        self.woklogo = QtWidgets.QLabel(self.Miniwok)
        self.woklogo.setGeometry(QtCore.QRect(280, -10, 210, 190))
        self.woklogo.setAutoFillBackground(False)
        self.woklogo.setPixmap(QtGui.QPixmap("MiniWok logo.png"))
        self.woklogo.setScaledContents(True)

        self.wokmenu = QtWidgets.QLabel(self.Miniwok)
        self.wokmenu.setGeometry(QtCore.QRect(105, 160, 186, 41))
        self.wokmenu.setFont(self.labelfont)
        self.wokmenu.setAutoFillBackground(True)
        self.wokmenu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.wokmenu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.wokmenu.setText("    Menu    ")

        self.wokmenutext = QtWidgets.QTextEdit(self.Miniwok)
        self.wokmenutext.setGeometry(QtCore.QRect(70, 220, 280, 225))
        self.wokmenutext.setFont(self.textfont)
        self.wokmenutext.setReadOnly(True)

        self.wokprice = QtWidgets.QLabel(self.Miniwok)
        self.wokprice.setGeometry(QtCore.QRect(440, 160, 186, 41))
        self.wokprice.setFont(self.labelfont)
        self.wokprice.setAutoFillBackground(True)
        self.wokprice.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.wokprice.setFrameShadow(QtWidgets.QFrame.Raised)
        self.wokprice.setText("    Price   ")

        self.wokpricetext = QtWidgets.QTextEdit(self.Miniwok)
        self.wokpricetext.setGeometry(QtCore.QRect(435, 220, 200, 225))
        self.wokpricetext.setFont(self.textfont)
        self.wokpricetext.setReadOnly(True)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("MiniWok logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.tabWidget.addTab(self.Miniwok,icon, "MiniWok")
        
        #------------------------------------------DRINKS STALL TAB-----------------------------------------

        self.beverage = QtWidgets.QWidget()
        self.beverage.setObjectName("beverage")

        self.drinksbgpic = QtWidgets.QLabel(self.beverage)
        self.drinksbgpic.setGeometry(QtCore.QRect(-150, -50, 975,850))
        self.drinksbgpic.setPixmap(QtGui.QPixmap("Beverages bg.jpg"))
        self.drinksbgpic.setScaledContents(True)

        self.drinkslogo = QtWidgets.QLabel(self.beverage)
        self.drinkslogo.setGeometry(QtCore.QRect(280, 0, 200, 180))
        self.drinkslogo.setPixmap(QtGui.QPixmap("Beverages logo.png"))
        self.drinkslogo.setScaledContents(True)

        self.drinkmenu = QtWidgets.QLabel(self.beverage)
        self.drinkmenu.setGeometry(QtCore.QRect(105, 160, 186, 41))
        self.drinkmenu.setFont(self.labelfont)
        self.drinkmenu.setAutoFillBackground(True)
        self.drinkmenu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.drinkmenu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.drinkmenu.setText("    Menu    ")

        self.drinkmenutext = QtWidgets.QTextEdit(self.beverage)
        self.drinkmenutext.setGeometry(QtCore.QRect(70, 220, 255, 225))
        self.drinkmenutext.setFont(self.textfont)
        self.drinkmenutext.setReadOnly(True)

        self.drinkprice = QtWidgets.QLabel(self.beverage)
        self.drinkprice.setGeometry(QtCore.QRect(440, 160, 186, 41))
        self.drinkprice.setFont(self.labelfont)
        self.drinkprice.setAutoFillBackground(True)
        self.drinkprice.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.drinkprice.setFrameShadow(QtWidgets.QFrame.Raised)
        self.drinkprice.setText("    Price   ")

        self.drinkpricetext = QtWidgets.QTextEdit(self.beverage)
        self.drinkpricetext.setGeometry(QtCore.QRect(435, 220, 200, 225))
        self.drinkpricetext.setFont(self.textfont)
        self.drinkpricetext.setTabChangesFocus(False)
        self.drinkpricetext.setReadOnly(True)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Beverages logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.tabWidget.addTab(self.beverage,icon, "Beverages")
        
        #--------------------------------------------DATE AND TIME FRAME---------------------------------------------

        self.TimeDate = QtWidgets.QFrame(self.frame1)

        self.TimeDate.setGeometry(QtCore.QRect(750, 30, 425, 600))
        self.TimeDate.setFrameShape(QtWidgets.QFrame.Box)
        self.TimeDate.setFrameShadow(QtWidgets.QFrame.Raised)
        self.TimeDate.setLineWidth(9)
        self.TimeDate.setToolTip("Edit Time/Date to View Menus On Different Date and Time")

        self.Calenderbg = QtWidgets.QLabel(self.TimeDate)
        self.Calenderbg.setGeometry(QtCore.QRect(13, 13, 403, 578))
        self.Calenderbg.setPixmap(QtGui.QPixmap("timebg.jpg"))
        self.Calenderbg.setScaledContents(True)


        self.Calender = QtWidgets.QCalendarWidget(self.TimeDate)
        self.Calender.setGeometry(QtCore.QRect(13, 275,400, 250))
        self.Calender.setToolTip("Select the Date")
        now = date.today()
        self.Calender.setMinimumDate(QtCore.QDate(now))

        self.Resettimebutton = QtWidgets.QPushButton(self.TimeDate)
        self.Resettimebutton.setGeometry(QtCore.QRect(150, 210, 112, 32))
        self.Resettimebutton.setText("Reset Time")
                
        self.minutecombobox = QtWidgets.QComboBox(self.TimeDate)
        self.minutecombobox.setGeometry(QtCore.QRect(230, 170, 80, 30))
        self.minutecombobox.setObjectName("minutecombobox")
        for i in range(0,60):
            self.minutecombobox.addItem("")
            self.minutecombobox.setItemText(i, str(i))

        self.hourcombobox = QtWidgets.QComboBox(self.TimeDate)
        self.hourcombobox.setGeometry(QtCore.QRect(230, 130, 80, 30))
        self.hourcombobox.setObjectName("hourcombobox")
        for i in range(0,24):
            self.hourcombobox.addItem("")
            self.hourcombobox.setItemText(i, str(i))
            
        self.hours = QtWidgets.QLabel(self.TimeDate)
        self.hours.setGeometry(QtCore.QRect(70, 130, 130, 26))
       
        self.hours.setFont(self.textfont)
        self.hours.setText("   Hours:")

        self.minutes = QtWidgets.QLabel(self.TimeDate)
        self.minutes.setGeometry(QtCore.QRect(70, 170, 130, 26))
       
        self.minutes.setFont(self.textfont)      
        self.minutes.setText("   Minutes:")

        self.Time = QtWidgets.QLabel(self.TimeDate)
        self.Time.setGeometry(QtCore.QRect(70, 80, 275, 35))
        self.Time.setFont(font)
        self.Time.setAutoFillBackground(True)
        self.Time.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Time.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Time.setFont(self.labelfont)
        self.Time.setText("          Time")

        self.Backbutton = QtWidgets.QPushButton(self.TimeDate)
        self.Backbutton.setGeometry(QtCore.QRect(235, 555, 112, 32))
        self.Backbutton.setText("Back")
        self.Backbutton.setShortcut("Backspace")
        
        #---------------------------------------------STORE INFORMATION FRAME---------------------------------------
        
        self.storeinfo = QtWidgets.QFrame(self.frame1)
        self.storeinfo.setGeometry(QtCore.QRect(0, 635, 540, 141))
        self.storeinfo.setFrameShape(QtWidgets.QFrame.Panel)
        self.storeinfo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.storeinfo.setLineWidth(13)
        self.storeinfo.setToolTip("Store Information")

        self.storeinfobg = QtWidgets.QLabel(self.storeinfo)
        self.storeinfobg.setGeometry(QtCore.QRect(13, 15, 514, 114))
        self.storeinfobg.setText("")
        self.storeinfobg.setPixmap(QtGui.QPixmap("storeinfobg.jpg"))
        self.storeinfobg.setScaledContents(True)

        self.Storeinfo = QtWidgets.QLabel(self.storeinfo)
        self.Storeinfo.setGeometry(QtCore.QRect(60, 40, 400, 35))

        self.Storeinfo.setFont(self.labelfont)
        self.Storeinfo.setAutoFillBackground(True)
        self.Storeinfo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Storeinfo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Storeinfo.setText("       Store Information")

        self.storeinfo = QtWidgets.QPushButton(self.storeinfo)
        self.storeinfo.setGeometry(QtCore.QRect(150, 80, 215, 30))
        self.storeinfo.setCheckable(True)
        self.storeinfo.setChecked(True)
        self.storeinfo.setAutoRepeat(False)
        self.storeinfo.setText("Press for Store Information")
        self.storeinfo.setShortcut("Ctrl+I")

        #-------------------------------------------------WAITING TIME FRAME----------------------------------------
        
        self.Waitingtime = QtWidgets.QFrame(self.frame1)
        self.Waitingtime.setGeometry(QtCore.QRect(540, 635, 638, 141))
        self.Waitingtime.setFrameShape(QtWidgets.QFrame.Panel)
        self.Waitingtime.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Waitingtime.setLineWidth(13)

        self.Waitingtimebg = QtWidgets.QLabel(self.Waitingtime)
        self.Waitingtimebg.setGeometry(QtCore.QRect(13, 15, 612, 114))
        self.Waitingtimebg.setLineWidth(-2)
        self.Waitingtimebg.setText("")
        self.Waitingtimebg.setPixmap(QtGui.QPixmap("waitingbg.jpg"))
        self.Waitingtimebg.setScaledContents(True)

        self.waitingtime = QtWidgets.QLabel(self.Waitingtime)
        self.waitingtime.setGeometry(QtCore.QRect(180, 30, 305, 40))

        self.waitingtime.setFont(self.labelfont)
        self.waitingtime.setAutoFillBackground(True)
        self.waitingtime.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.waitingtime.setFrameShadow(QtWidgets.QFrame.Raised)
        self.waitingtime.setText("      Waiting Time")

        self.numberofppl = QtWidgets.QLabel(self.Waitingtime)
        self.numberofppl.setGeometry(QtCore.QRect(70, 75, 500, 40))
        self.numberofppl.setFont(self.textfont)
        self.numberofppl.setText("   Enter the number of people:")

        self.Continuewaitingtimebutton = QtWidgets.QPushButton(self.Waitingtime)
        self.Continuewaitingtimebutton.setGeometry(QtCore.QRect(500, 86, 112, 32))
        self.Continuewaitingtimebutton.setCheckable(True)
        self.Continuewaitingtimebutton.setChecked(True)
        self.Continuewaitingtimebutton.setText("Continue")
        self.Continuewaitingtimebutton.setShortcut( "Return")

        self.numberofppltext = QtWidgets.QLineEdit(self.Waitingtime)
        self.numberofppltext.setGeometry(QtCore.QRect(380, 86, 91, 30))

        #---------------------------------------------------------

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        MainWindow.setWindowTitle("NTU Canteen System")
        self.cur_time()
        self.frame1.hide()

        self.Continuebutton.clicked.connect(self.go)
        self.Backbutton.clicked.connect(self.back)
        self.storeinfo.clicked.connect(lambda : self.dispinfo("display"))
        self.Resettimebutton.clicked.connect(self.cur_time)
        self.tabWidget.currentChanged.connect(self.updatemenu)
        self.hourcombobox.currentIndexChanged.connect(self.updatemenu)
        self.minutecombobox.currentIndexChanged.connect(self.updatemenu)

        self.Calender.clicked.connect(self.updatemenu)
        self.Continuewaitingtimebutton.clicked.connect(self.waiting_time)
        


    def go(self):
        self.frame1.show()
        self.frame.hide()
        self.cur_time()
        self.updatemenu()


    def back(self):
        self.frame.show()
        self.frame1.hide()
        MainWindow.setWindowTitle("NTU Canteen System")
        

    def cur_time(self):
        now = date.today()
        self.Calender.setSelectedDate(QtCore.QDate(now))
        
        now = datetime.now()
        to = now.strftime("%H")
        self.hourcombobox.setCurrentIndex((int(to)))
        
        to = now.strftime("%M")
        self.minutecombobox.setCurrentIndex((int(to)))
        

    def stalls(self):

        data=pd.read_csv("Stalls.csv")

        McD_morn=list(data['Before 12PM'].values[0].split(", "))
        McD_eve=list(data['After 12PM'].values[0].split(", "))
        Pizza_Hut=list(data['Same menu'].values[1].split(", "))
        Mini_wok_weekday=list(data['Same menu'].values[2].split(", "))
        Mini_wok_weekend=list(data['Same menu'].values[3].split(", "))
        Juice_shop=list(data['Same menu'].values[4].split(", "))
        Bakery_cuisine=list(data['Same menu'].values[5].split(", "))

        dict={"Mcd1":McD_morn,"Mcd2":McD_eve,"Pizza Hut Express":Pizza_Hut,
              "MiniWok1":Mini_wok_weekday,"MiniWok2":Mini_wok_weekend,
              "Beverages":Juice_shop,"Bakery Cuisine":Bakery_cuisine}
        return dict

    def updatemenu(self):
        
        store=self.tabWidget.tabText(self.tabWidget.currentIndex())
        MainWindow.setWindowTitle(store +" Menu")

        hr=self.hourcombobox.currentIndex()
       	mint=self.minutecombobox.currentIndex()
       	time=hr*100+mint

        if self.Calender.selectedDate() == self.Calender.minimumDate() and time<int(datetime.now().strftime("%H%M")):
        	if ( int(datetime.now().strftime("%H%M"))-time )<5:
        		self.cur_time()
        		return
        	else:
        		errormsg=QMessageBox()
		        errormsg.setWindowTitle("Wrong Time")
		        errormsg.setText("The Selected Time has Lapsed. The Time Has Been Reset to Current Time")
		        errormsg.setIcon(QMessageBox.Critical)
		        errormsg.setStandardButtons(QMessageBox.Ok)
		        x=errormsg.exec_()
		        self.cur_time()
		        return
	        
        stall=self.stalls()
        stall_names=["Mcd1","Mcd2","MiniWok1","MiniWok2"]
        
        cnt=1
        menutext,pricetext="",""

        if hr<12:
            stall_names.pop(1)
        elif hr>=12:
            stall_names.pop(0)

        weekdays=("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
        day = weekdays[self.Calender.selectedDate().dayOfWeek()-1]

        if day=="Saturday" or day=="Sunday":
            stall_names.remove("MiniWok1")
        else:
            stall_names.remove("MiniWok2")

        bol=self.dispinfo("no")
        if bol:
            if store=="McDonalds":
                
                for x in stall[stall_names[0]]: #McD
                    for i in x.split(":"):
                        if cnt%2!=0:
                            menutext=menutext+i+"\n"
                        else:
                        	pricetext=pricetext+i+"\n"
                        cnt+=1
                    self.mcdmenutext.setText(menutext)
                    self.mcdpricetext.setText(pricetext)
            elif store=="MiniWok":
                
                for x in stall[stall_names[1]]: #MiniWok
                    for i in x.split(":"):
                        if cnt%2!=0:
                        	menutext=menutext+i+"\n"

                        else:
                        	pricetext=pricetext+i+"\n"

                        	
                        cnt+=1
                    self.wokmenutext.setText(menutext)
                    self.wokpricetext.setText(pricetext)

            else:
                
                for x in stall[store]: 
                    for i in x.split(":"):
                        if cnt%2!=0:
                        	menutext=menutext+i+"\n"
                        else:
                        	pricetext=pricetext+i+"\n"
                        cnt+=1
                    
                    
                    if store=="Pizza Hut Express":
                        self.pizzamenutext.setText(menutext)
                        self.pizzapricetext.setText(pricetext)
                    elif store=="Bakery Cuisine":
                        self.bakerymenutext.setText(menutext)
                        self.bakerypricetext.setText(pricetext)
                    elif store=="Beverages":
                        self.drinkmenutext.setText(menutext)
                        self.drinkpricetext.setText(pricetext)

        else:
            if store=="Pizza Hut Express":
                self.pizzamenutext.setText("\t Closed \t")
                self.pizzapricetext.setText("           Closed \t")
            elif store=="Bakery Cuisine":
                self.bakerymenutext.setText("\t Closed \t")
                self.bakerypricetext.setText("           Closed \t")
            elif store=="Beverages":
                self.drinkmenutext.setText("\t Closed \t")
                self.drinkpricetext.setText("           Closed \t")
            elif store=="McDonalds":
                self.mcdmenutext.setText("\t Closed \t")
                self.mcdpricetext.setText("           Closed \t")
            elif store=="MiniWok":
                self.wokmenutext.setText("\t Closed \t")
                self.wokpricetext.setText("           Closed \t")

    def dispinfo(self,text):
        hr=self.hourcombobox.currentIndex()
        mint=self.minutecombobox.currentIndex()
        time=hr*100+mint

        store=self.tabWidget.tabText(self.tabWidget.currentIndex())

        f=open("myFile.txt", "r")
        f1=f.readlines()
        f2=f1[f1.index(store+"\n")+1:f1.index(store[0:2]+"\n")]

        weekdays=("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
        weekday=("Monday","Tuesday","Wednesday","Thursday","Friday")

        o_c = eval(open("mf.txt").read())

        day = weekdays[self.Calender.selectedDate().dayOfWeek()-1]
        day1 = weekdays[self.Calender.selectedDate().dayOfWeek()-1]

        weekday_open=o_c[store]["Weekday"][0]
        sat_open=o_c[store]["Saturday"][0]
        sun_open=o_c[store]["Sunday"][0]
            	
        msg=QMessageBox()
        msg.setWindowTitle(store+" store info")

        if day in weekday:
            day="Weekday"

        if o_c[store][day][0]<time<o_c[store][day][1] or o_c[store][day][0]==time:
            msg.setIcon(QMessageBox.Information)
            msg.setText("The store is OPEN for your access")
            msg.setInformativeText("Enjoy your meal! :)")
            self.Waitingtime.setEnabled(True)
            self.Waitingtime.setToolTip("Enter number of people to calculate waiting time")
            bol = True

        else:
            self.Waitingtime.setEnabled(False)
            msg.setIcon(QMessageBox.Warning)
            if day1==datetime.now().strftime("%A") and (int(datetime.now().strftime("%H%M")))>=time :
            	msg.setText("The Store is closed at the moment")
            	self.Waitingtime.setToolTip("The Store is closed at the moment")
           
            else:
            	msg.setText("the store is closed at the given date and time")
            	self.Waitingtime.setToolTip("the store is closed at the given date and time")
            
            if time > o_c[store][day][1]:

                if day1 in weekday:
                    if weekday.index(day1)!=4:     #any weekday other than friday
                        msg.setInformativeText("The store opens on "+str(weekday[weekday.index(day1)+1])+" at "+str(weekday_open)+"Hrs")
                    elif weekday.index(day1)==4:    # friday
                        if sat_open==0:
                            if sun_open==0:
                                msg.setInformativeText("The store opens on Monday at "+str(weekday_open)+"Hrs")
                            else:
                                msg.setInformativeText("The store opens on Sunday at "+str(sun_open)+"Hrs")
                        else:
                            msg.setInformativeText("The store opens on Saturday at "+str(sat_open)+"Hrs")
                elif day == "Saturday":
                    if sun_open==0:
                        msg.setInformativeText("The store opens on Monday at "+str(weekday_open)+"Hrs")
                    else:
                        msg.setInformativeText("The store opens on Sunday at "+str(sun_open)+"Hrs")
                elif day =="Sunday":
                    msg.setInformativeText("The store opens on Monday at "+str(weekday_open)+"Hrs")
            else:
                if day1 in weekday:
                    msg.setInformativeText("The store opens on "+ day1+" at "+str(weekday_open)+"Hrs")
                else:
                    msg.setInformativeText("The store opens on "+ day1+" at "+str(o_c[store][day1][0])+"Hrs")
            bol = False
        
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setDetailedText(" ".join(f2))

        font = QtGui.QFont() #Font of Message box
        font.setFamily("Sylfaen") #Font type
        font.setPointSize(12) #Font size
        msg.setFont(font)

        if text=="display" or not bol:
            y=msg.exec_()
        return bol

    def waiting_time(self):
        store=self.tabWidget.tabText(self.tabWidget.currentIndex())
        try:
        	people=int(self.numberofppltext.text())
        except ValueError:
        	errormsg=QMessageBox()
	        errormsg.setWindowTitle("Error")
	        errormsg.setText("Please Enter Number Of People In Numbers")
	        errormsg.setIcon(QMessageBox.Critical)
	        errormsg.setStandardButtons(QMessageBox.Ok)
	        x=errormsg.exec_()
	        self.numberofppltext.clear()
	        return
        if store=="McDonalds" or store=="Pizza Hut Express" or store=="Bakery Cuisine":
            i=2
        elif store=="MiniWok":
            i=4
        else:
            i=1
        waitingTime=(people*i)+i 

        msg=QMessageBox()

        font = QtGui.QFont() #Font of Message box
        font.setFamily("Sylfaen") #Font type
        font.setPointSize(12) #Font size
        msg.setFont(font)

        msg.setWindowTitle(store+" Waiting time info")
        msg.setText("It will take "+str(waitingTime)+" minutes for you to receive your order ")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)


        y=msg.exec_()
        self.numberofppltext.clear()
     

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())