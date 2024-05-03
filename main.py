from PyQt5 import QtWidgets,QtGui,QtCore
from PyQt5.QtWidgets import QTableWidgetItem
from doctortest import Ui_MainWindow
from IOCAMReg import Ui_Form
import mysql.connector
import sys
import cv2
import os


class DBHelper:
    def __init__(self):
        self.con = mysql.connector.connect(
        # MySQL Server IP Address
        host="localhost",
        # MySQL Username
        user="MySqlUsername",
        # MySQL Server Port
        port = 3306,
        # MySQL Password
        passwd="mySQLPassword",
        # MySQL DB Name
        database = "mySQLDBName",
        auth_plugin = 'root',
        autocommit = True
        )
        query = 'create table if not exists Patients(UserID int, `Pname` varchar(200),phone varchar(20),earning int)'
        cur = self.con.cursor()
        cur.execute(query)
        
        # self.con.commit()
    def insert_user(self,UserID,name,phone,earning):
        query = 'insert into Patients(UserID,`Pname`,`phone`,earning) values(%s,%s,%s,%s)'
        cur = self.con.cursor()
        val = (UserID,name,phone,earning)
        cur.execute(query,val)
        self.con.commit()
    def dbrowcount(self):
        query = 'select *  from Patients'
        cur = self.con.cursor()
        cur.execute(query)
        cur.fetchall()
        return(cur.rowcount)
        
    def fetchall(self):
        query = 'select *  from Patients'
        cur = self.con.cursor()
        cur.execute(query)
        return(cur.fetchall())

class IOWindow(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(IOWindow, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        self.ui.DoneButton.clicked.connect(self.OpenIOCam)
    
    def OpenIOCam(self):
        from datetime import datetime
        cap = cv2.VideoCapture(1)
        IOWindow.destroy(self)
        print (cv2.VideoCapture(1))
        PatientName = self.ui.NameEntry.text()
        

        # Check if the webcam is opened correctly
        if not cap.isOpened():
            raise IOError("Cannot open webcam")

        while True:
            ret, frame = cap.read()
            frame = cv2.resize(frame, None, fx=2, fy=2, interpolation=cv2.INTER_AREA)
            datetime = datetime.today()
            date = datetime.today().strftime("%b-%d-%Y")
            cv2.imshow('Input', frame)

            c = cv2.waitKey(1)
            if c == 27:
                break
            if cv2.getWindowProperty('Input',cv2.WND_PROP_VISIBLE) < 1:        
                break
            x = cv2.waitKey(1)
            if x == 32:
                cv2.imwrite(f"IOCamImages/{PatientName}{date}.png",frame)
                img = cv2.imread(f"IOCamImages/{PatientName}{date}.png",cv2.IMREAD_UNCHANGED)
                cv2.putText(img,f"{PatientName} {datetime}",(10,50),cv2.FONT_HERSHEY_SIMPLEX,1,(209,80,0,255),3)
                cv2.imwrite(f"IOCamImages/{PatientName}{date}.png",img)
                

        cap.release()
        cv2.destroyAllWindows()
        

class window(QtWidgets.QMainWindow):
    def __init__(self):
        super(window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        
        # self.loadpatients()
        self.ui.SButton.clicked.connect(self.onclick)
        self.ui.TButton.clicked.connect(self.CalculateEarning)
        self.ui.RefreshButton.clicked.connect(self.loadpatients)
        self.ui.actionExit.triggered.connect(self.OnExit)
        self.ui.AddImage.clicked.connect(self.OnIOWindowClick)
        self.ui.ViewImage.clicked.connect(self.ViewImages)
    def OnIOWindowClick(self):
        win2 = IOWindow(self)
        win2.show()
    def ViewImages(self):
        currentDIR = os.getcwd()
        os.startfile(currentDIR+"\\IOCamImages", 'open')
        
    def CalculateEarning(self):
        Total = 0
        rowcount = self.ui.Ptable.rowCount()
        for i in range(0,rowcount):
            Total = Total+int(self.ui.Ptable.item(i,2).text())
        self.ui.TotalEarning.setText(str(Total)+"₹")
    def OnExit(self):
        sys.exit()
        
    def onclick(self):
        name1 = self.ui.ninput.text()
        phoneno2 = self.ui.pinput.text()
        earning3 = self.ui.einput.text()
        
        if name1 and phoneno2 and earning3 is not None:
            rowcount = self.ui.Ptable.rowCount()
            self.ui.Ptable.setRowCount(rowcount+1)
            self.ui.Ptable.setItem(rowcount,0,QTableWidgetItem(name1))
            self.ui.Ptable.setItem(rowcount,1,QTableWidgetItem(phoneno2))
            self.ui.Ptable.setItem(rowcount,2,QTableWidgetItem(earning3))
            helper.insert_user(1,name1,phoneno2,int(earning3))
            
            
    
        
    def loadpatients(self):
        print("patients loaded")
        row_count = helper.dbrowcount()
        Patients = helper.fetchall()
        print(row_count)
        print(Patients)
        
        for i in range(0,row_count):
            self.ui.Ptable.setRowCount(row_count)
            self.ui.Ptable.setItem(i,0,QTableWidgetItem(Patients[i][1]))
            self.ui.Ptable.setItem(i,1,QTableWidgetItem(Patients[i][2]))
            self.ui.Ptable.setItem(i,2,QTableWidgetItem(str(Patients[i][3])))
            
            

    
def create_app():
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('dentist.png'))
    win = window()
    win.show()
    sys.exit(app.exec_())
    
    
helper = DBHelper()

create_app()