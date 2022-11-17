from ast import Return
from tkinter.constants import X, Y
from graphics import*
import math
import time
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
#from win32api import GetSystemMetrics


screenWidth = int(1200) 
screenHeight = int(900)
X_Center = screenWidth / 2
Y_Center = screenHeight / 2

ColorBackround = "white"
ColorCartesian = 'black'
ColorFolderJobs = 'blue'
ColorOfArms ='black'
ColorofElbow ='red'
ColorofElbow1 ='green'
ColorIntersection ='blue'
ColorMove = 'red'
ColorOfInternalJobFolder = 'yellow'


#ΣΥΝΑΡΤΗΣΗ ΓΡΑΜΜΗΣ
def DrawLine(x1,y1,x2,y2,window,width,color):
    line = Line(Point(x1, y1), Point(x2, y2))
    line.setWidth(width); line.setFill(color)
    line.draw(window) 

#ΣΥΝΑΡΤΗΣΗ ΚΥΚΛΟΥ
def DrawCircle(x1,y1,radius,window,width,color,fillcolor=''): 
    aCircle = Circle(Point(x1,y1), radius)
    aCircle.setWidth(width);aCircle.setOutline(color)
    if fillcolor !='': aCircle.setFill(fillcolor)
    aCircle.draw(window) 


#AKEΡΑΙΟ ΘΕΤΙΚΟ INPUT
def InputPositiveIntegerFromPopUp(message): 
    while True:
        try:
            ROOT = tk.Tk()
            ROOT.withdraw() # the input dialog
            USER_INP = simpledialog.askstring(title="Είσοδος δεδομένων",prompt=message)
            a = int(USER_INP); 
            if a < 0: 
                messagebox.showerror('Σφαλμα','Πληκτρολογήστε έναν θετικό ακέραιο')
            elif a == 0: 
                messagebox.showerror('Σφαλμα','Πληκτρολογήστε έναν θετικό ακέραιο')
            else :break
        except ValueError:
            messagebox.showerror('Σφαλμα','Πληκτρολογήστε έναν θετικό ακέραιο')
    return int(a)

#ΑΚΕΡΑΙΟ INPUT
def InputIntegerFromPopUp(message): 
    while True:
        try:
            ROOT = tk.Tk()
            ROOT.withdraw() # the input dialog
            USER_INP = simpledialog.askstring(title="Είσοδος δεδομένων",prompt=message) 
            a = float(USER_INP); break
        except ValueError:
             messagebox.showerror('Σφαλμα','Πληκτρολογήστε έναν ακέραιο')
    return int(a)

#ΕΥΡΕΣΗ F
def atn2(x,y):
    if x>0 and (y>0 or y==0):
        F = math.atan(y/x)
    elif x>0 and y<0:
        F = math.atan(y/x) + 2 * math.pi
    elif x<0 and  (y>0 or y==0):
        F = math.atan(y/x) + math.pi
    elif x<0 and y < 0:  
        F = math.atan(y/x) + math.pi
    elif (abs(x)== 0 and y>0):
        F = math.pi/2
    elif (abs(x)== 0 and y<0):
        F = 3 * (math.pi / 2)
    else:
        print ("Πρόβλημα στην γωνία")
    return float(F)


#ΓK
def Robot(x2,y2,MyElbowColor):
    
    S1 = (y2**2 + x2**2 + L1**2 - L2**2)/2
    D1 = 4*S1**2 * y2**2 - 4*(y2**2 + x2**2) * (S1**2 - L1**2 * x2**2)
    
    print ("D1",D1)
    
    if D1 > 0 or D1 == 0:
        if x2>0.01 or x2<-0.01:
            y1_1 = (2*S1*y2+math.sqrt(D1))/(2*(x2**2 +y2**2))
            y1_2 = (2*S1*y2-math.sqrt(D1))/(2*(x2**2 +y2**2))
            x1_1 = (S1 - y2 * y1_1)/x2
            x1_2 = (S1 - y2 * y1_2)/x2
        elif x2==0 and y2==0:
            messagebox.showerror('Σφαλμα','Η κίνηση αυτή μπορεί να προκαλέσει την καταστροφή του ρομποτικού βραχίονα!')
        else:
            y1_1 = S1 / y2
            y1_2 = y1_1
            x1_1 = math.sqrt(L1**2-(S1**2)/(y2**2)) 
            x1_2 = 0 - math.sqrt(L1**2-(S1**2)/(y2**2)) 
        print (x1_1 , x1_2 , y1_1 , y1_2 )
    else:
        messagebox.showerror('Σφαλμα','Το άκρο του δεύτερου μέλους του ρομποτικού βραχίονα είναι εκτός χώρου εργασίας.')

    f1_1 = atn2(x1_1,y1_1)
    x2_1 = x2 * math.cos(f1_1) + y2 * math.sin(f1_1)
    y2_1 = -x2 * math.sin(f1_1) + y2 * math.cos(f1_1)

    f1_2 = atn2(x1_2,y1_2)
    x2_2 = x2 * math.cos(f1_2) + y2 * math.sin(f1_2)
    y2_2 = -x2 * math.sin(f1_2) + y2 * math.cos(f1_2)



    if LR == 1:
        f2 = atn2(x2_2,y2_2)
    elif LR == 0:
        f2 = atn2(x2_1,y2_1) 

    #ΕΚΤΕΛΕΣΗ ROBOT
    if f2> 0 and f2  < (math.pi) :
        print(f2)
        DrawLine (X_Center , Y_Center , X_Center + x1_1 ,  Y_Center + y1_1  , win , 6 , MyElbowColor )
        DrawLine (X_Center + x1_1 , Y_Center + y1_1 ,X_Center + x2 , Y_Center + y2  , win , 6 , MyElbowColor )
        DrawCircle (X_Center + x1_1 , Y_Center + y1_1 , 10 , win , 6  , ColorCartesian , ColorBackround )
        DrawCircle (X_Center + x2 ,Y_Center + y2 , 6 , win , 6  , ColorCartesian , ColorBackround ) 
    elif f2 > (math.pi) and f2 < (2 * math.pi):
        print(f2)
        DrawLine (X_Center , Y_Center , X_Center + x1_2 ,  Y_Center + y1_2  , win , 6 , MyElbowColor )
        DrawLine (X_Center + x1_2 , Y_Center + y1_2 ,X_Center + x2 , Y_Center +  y2  , win , 6 , MyElbowColor )
        DrawCircle (X_Center + x1_2 , Y_Center + y1_2 , 10 , win , 6  , ColorCartesian , ColorBackround )
        DrawCircle ( X_Center + x2 ,Y_Center + y2 , 6 , win , 6  , ColorCartesian , ColorBackround )

#EΛΕΓΧΟΣ ΕΠΟΜΕΝΟΥ ΣΗΜΕΙΟΥ
def nextpointcheck(x,y,x2,y2,L1,L2):
    
        
    dx , dy = (x - x2) , (y - y2)
    if dx==0:
        dx=0.0000001
    a = dy/dx 
    b = y2 - (a * x2)
    dr = (dx**2 + dy**2)**.5
    big_d = x2 * y - x * y2
    discriminant = 4*(a**2)*(b**2)-(4*(a**2+1))*(b**2-((L1-L2)**2))
        
    
    if discriminant < 0 :
        DrawLine (X_Center + x2 , Y_Center + y2 , X_Center + x ,  Y_Center + y , win , 3 , ColorofElbow1 )
        print("discriminant",discriminant)
        return True

        
    elif discriminant > 0:
        xs1 = ((-2*a*b) + math.sqrt(discriminant)) / (2*((a**2)+1))
        xs2 = ((-2*a*b) - math.sqrt(discriminant)) / (2*((a**2)+1))

        ys1 = a*xs1 + b 
        ys2 = a*xs2 + b 
            
        Dp0p1 = math.sqrt(((y- y2)**2) + ((x-x2)**2))
        Dp0s1 = math.sqrt(((ys1- y2)**2) + ((xs1-x2)**2))
        Dp0s2 = math.sqrt(((ys2- y2)**2) + ((xs2-x2)**2))
        Dp1s1 = math.sqrt(((ys1- y)**2) + ((xs1-x)**2))
        Dp1s2 = math.sqrt(((ys2- y)**2) + ((xs2-x)**2))

        Dmin0 = min(Dp0s1,Dp0s2)
        Dmin1 = min(Dp1s1,Dp1s2)
        Dmax = max(Dmin0,Dmin1)
            
        if Dmax > Dp0p1:
            DrawLine (X_Center + x2 , Y_Center + y2 , X_Center + x ,  Y_Center + y , win , 3 , ColorofElbow1 )
            print ("Dmax=",Dmax)
            print ("Dp0p1=",Dp0p1)
            print("discriminant",discriminant)
            return True

                
            
        elif Dmax < Dp0p1 or Dmax==Dp0p1:
            DrawLine (X_Center + x2 , Y_Center + y2 , X_Center + x ,  Y_Center + y  , win , 3 , ColorofElbow1 )
            messagebox.showerror('Σφαλμα','Η κίνηση αυτή δεν είναι εφικτή όπως φαίνεται!')
            print ("Dmax=",Dmax)
            print ("Dp0p1=",Dp0p1)
            return False
    
    elif discriminant==0:
        if abs(x2)>abs(L1-L2): #or abs(x2)==abs(L1-L2):
            DrawLine (X_Center + x2 , Y_Center + y2 , X_Center + x ,  Y_Center + y , win , 3 , ColorofElbow1 )
            print("discriminant",discriminant)
            return True
        else:
            xs1 = ((-2*a*b) + math.sqrt(discriminant)) / (2*((a**2)+1))
            xs2 = ((-2*a*b) - math.sqrt(discriminant)) / (2*((a**2)+1))

            ys1 = math.sqrt(((L1-L2)**2)-(xs1**2))
            ys2 = -math.sqrt(((L1-L2)**2)-(xs2**2))
            
            Dp0p1 = math.sqrt(((y- y2)**2) + ((x-x2)**2))
            Dp0s1 = math.sqrt(((ys1- y2)**2) + ((xs1-x2)**2))
            Dp0s2 = math.sqrt(((ys2- y2)**2) + ((xs2-x2)**2))
            Dp1s1 = math.sqrt(((ys1- y)**2) + ((xs1-x)**2))
            Dp1s2 = math.sqrt(((ys2- y)**2) + ((xs2-x)**2))

            Dmin0 = min(Dp0s1,Dp0s2)
            Dmin1 = min(Dp1s1,Dp1s2)
            Dmax = max(Dmin0,Dmin1)

            if Dmax > Dp0p1:
                DrawLine (X_Center + x2 , Y_Center + y2 , X_Center + x ,  Y_Center + y , win , 3 , ColorofElbow1 )
                print ("Dmax=",Dmax)
                print ("Dp0p1=",Dp0p1)
                print("discriminant",discriminant)
                return True

                
            
            elif Dmax < Dp0p1 or Dmax==Dp0p1:
                DrawLine (X_Center + x2 , Y_Center + y2 , X_Center + x ,  Y_Center + y  , win , 3 , ColorofElbow1 )
                messagebox.showerror('Σφαλμα','Η κίνηση αυτή δεν είναι εφικτή όπως φαίνεται!')
                print ("Dmax=",Dmax)
                print ("Dp0p1=",Dp0p1)
                return False


#BACKGROUND
def DesignAxes(MyColor, MyColor1):
    DrawCircle (screenWidth / 2, screenHeight / 2,  L1+L2 , win ,2 , MyColor, ColorBackround)
    DrawLine (0, screenHeight / 2, screenWidth, screenHeight / 2, win, 2, MyColor) 
    DrawLine (screenWidth / 2, 0, screenWidth / 2, screenHeight, win, 2, MyColor) 
    DrawCircle (screenWidth / 2 ,screenHeight / 2 , abs(L1-L2) , win, 2, MyColor1 ,ColorOfInternalJobFolder)

#KINHMATIKO
def Anime(xt, yt):
    Duration = 1.5 
    Rate = 10
    Points = int(Duration * Rate) 
    DelaySec = 1 / Rate 
    
    for i in range(0, Points + 1):
        xp = float((xt - x2) * i / Points + x2)
        yp = float((yt - y2) * i / Points + y2)
        Robot(xp,yp,ColorofElbow)
        time.sleep(DelaySec)
        Robot(xp,yp,ColorBackround)
        DesignAxes(ColorCartesian , ColorofElbow)
        DrawLine (X_Center + x2 , Y_Center + y2 , X_Center + xt ,  Y_Center + yt , win , 3 , ColorofElbow1 )

    
    DesignAxes(ColorCartesian, ColorofElbow)
    DrawLine (X_Center + x2 , Y_Center + y2 , X_Center + xt ,  Y_Center + yt , win , 3 , ColorofElbow1 )
    Robot(xp, yp, ColorofElbow)

                                ###ΑΡΧΗ ΠΡΟΓΡΑΜΜΑΤΟΣ###
#USERINPUT
L1 = InputPositiveIntegerFromPopUp("Δώσε το μήκος L1 του 1ου μέλους του ρομποτικού βραχίονα:")
L2 = InputPositiveIntegerFromPopUp("Δώσε το μήκος L2 του 2ου μέλους του ρομποτικού βραχίονα:")
x2 = InputIntegerFromPopUp("Δώσε τη x συντεταγμένη του άκρου του δεύτερου μέλους.")
y2 = InputIntegerFromPopUp("Δώσε τη y συντεταγμένη του άκρου του δεύτερου μέλους.")

#ΕΛΕΓΧΟΣ ΟΡΙΟΥ ΦΑΚΕΛΩΝ
while True:
        ROOT = tk.Tk()
        ROOT.withdraw()
        c=math.sqrt(x2**2+y2**2)

        if c>=(L1+L2):
            messagebox.showerror('Σφαλμα','Οι συντεταγμένες που δόθηκαν είναι εκτός του εξωτερικού φακέλου')
            x2 = InputIntegerFromPopUp("Δώσε τη x συντεταγμένη του άκρου του δεύτερου μέλους.")
            y2 = InputIntegerFromPopUp("Δώσε τη y συντεταγμένη του άκρου του δεύτερου μέλους.")
        elif c<=(abs(L1-L2)):
            messagebox.showerror('Σφαλμα', 'Οι συντεταγμένες που δόθηκαν είναι εντός του εσωτερικού φακέλου')
            x2 = InputIntegerFromPopUp("Δώσε τη x συντεταγμένη του άκρου του δεύτερου μέλους.")
            y2 = InputIntegerFromPopUp("Δώσε τη y συντεταγμένη του άκρου του δεύτερου μέλους.")
        else: break 

#WINDOW INFO
win = GraphWin(width = screenWidth, height = screenHeight) 
win.setCoords(0, 0, screenWidth, screenHeight) 
win.setBackground(ColorBackround)
instructions = Text(Point(60,screenHeight-10),"Reverse Model") 
instructions.draw(win) 

#EKTEΛΕΣΗ ΓΡΑΜΜΩΝ ΚΑΡΤΕΣΙΑΝΟΥ ΚΑΙ ΧΩΡΟΥ ΕΡΓΑΣΙΑΣ
DesignAxes (ColorCartesian, ColorofElbow)

#ΑΡΙΣΤΕΡΟ/ΔΕΞΙΟ ΤΣΕΚ
while True:
    try:
        result = messagebox.askyesno("Προσοχή", "Θα επιθυμούσατε αριστερόστροφη λύση; (Αν επιθυμείτε δεξιόστροφη πατήστε ΟΧΙ)") 
        if result == True:
            LR=0
        else:
            LR=1
    except ValueError as val_err:
        print("An error occurred:\n{}".format(val_err))
    if (LR == 0 or LR == 1) == True: break


#ΕΥΡΕΣΗ f1_1, f1_2, f2_1, f2_2

Robot(x2,y2,ColorofElbow)

while True:
    x3=InputIntegerFromPopUp("δωσε την συντεταγμενη Χ για ευθυγραμμη κινηση") #'1' for negatives numbers 
    y3=InputIntegerFromPopUp("Δωσε την συντεταγμενη Υ για ευθυγραμμη κινηση")      
    while True:
        ROOT = tk.Tk()
        ROOT.withdraw()
        c=math.sqrt(x3**2+y3**2)

        if c>=(L1+L2):
            messagebox.showerror('Σφαλμα','Οι συντεταγμένες που δόθηκαν είναι εκτός του εξωτερικού φακέλου')
            x3 = InputIntegerFromPopUp("Δώσε τη x συντεταγμένη του άκρου του δεύτερου μέλους.")
            y3 = InputIntegerFromPopUp("Δώσε τη y συντεταγμένη του άκρου του δεύτερου μέλους.")
        elif c<=(abs(L1-L2)):
            messagebox.showerror('Σφαλμα', 'Οι συντεταγμένες που δόθηκαν είναι εντός του εσωτερικού φακέλου')
            x3 = InputIntegerFromPopUp("Δώσε τη x συντεταγμένη του άκρου του δεύτερου μέλους.")
            y3 = InputIntegerFromPopUp("Δώσε τη y συντεταγμένη του άκρου του δεύτερου μέλους.")
        else: break 
    check=nextpointcheck(x3,y3,x2,y2,L1,L2)
    print(check)
    if check==False:
        messagebox.showerror('Σφαλμα','Η κίνηση αυτή δεν είναι εφικτή όπως φαίνεται!')
        #Nextpointcheck
    if check==True:
        break


Anime (x3,y3)



win.getMouse() 
win.close()