import cv2
import math
import time

current_time = time.process_time()

face = time.process_time()

face = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalcatface.xml')
eye_glasses = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye_tree_eyeglasses.xml')
eye = cv2.CascadeClassifier(cv2.data.haarcascades+ 'haarcascade_eye.xml')

WHITE = [255, 255, 255]

def File_Read():
    names_open = open("Variable_Names.txt", "r")
    names = []
    while(True):
        Line = names_open.readline()
        if Line == '':
            break
        names.append(Line.split(", ")[1].rstrip())
    
    return names

name_read = File_Read()

"""Function to Find Name"""

def ID_Name(ID, conf):
    if ID > 0:
        Name_String = "Name: " + name_read[ID-1] + "Distance : " + (str(round(conf)))
    
    else: 
        Name_String = " Face Not Recognized "

    return Name_String

"""ReadFile, Add name in the end of the file"""

def Add_Name():
    Name = input('Enter Your Name: ')
    Info = open('Variable_Names.txt', 'r+')
    ID = ((sum(1 for line in Info))+1)
    Info.write(str(ID) + ", " + Name + "\n")
    Info.close()
    return ID

def Display_ID(x, y, w, h, names, Image):
    Name_y_pos = y - 10
    Name_X_pos = x + w/2 - (len(names)*7/2)

    if Name_X_pos < 0 :
        Name_X_pos = 0
    elif (Name_X_pos + 10 + (len(names) * 7) > Image.shape[1]):
        Name_X_pos= Name_X_pos - (Name_X_pos +10 + (len(names) * 7) - (Image.shape[1]))
    if Name_y_pos < 0 :
        Name_y_pos = Name_y_pos = y + h + 10

    draw_box(Image, x, y, w, h)

    cv2.rectangle(Image, (Name_X_pos-10, Name_y_pos-25), (Name_X_pos +10 + (len(names) * 7), Name_y_pos-1), (0,0,0), -2)         
    cv2.rectangle(Image, (Name_X_pos-10, Name_y_pos-25), (Name_X_pos +10 + (len(names) * 7), Name_y_pos-1), WHITE, 1) 
    cv2.putText(Image, names, (Name_X_pos, Name_y_pos - 10), cv2.FONT_HERSHEY_DUPLEX, .4, WHITE)                         

def draw_box(Image, x, y, w, h):
    cv2.line(Image, (x, y), (x + (w/5) ,y), WHITE, 2)
    cv2.line(Image, (x+((w/5)*4), y), (x+w, y), WHITE, 2)
    cv2.line(Image, (x, y), (x, y+(h/5)), WHITE, 2)
    cv2.line(Image, (x+w, y), (x+w, y+(h/5)), WHITE, 2)
    cv2.line(Image, (x, (y+(h/5*4))), (x, y+h), WHITE, 2)
    cv2.line(Image, (x, (y+h)), (x + (w/5) ,y+h), WHITE, 2)
    cv2.line(Image, (x+((w/5)*4), y+h), (x + w, y + h), WHITE, 2)
    cv2.line(Image, (x+w, (y+(h/5*4))), (x+w, y+h), WHITE, 2)

def DispID2(x, y, w, h, names, Image):
    Name_y_pos = y - 40
    Name_X_pos = x + w/2 - (len(names)*7/2)

    if Name_X_pos < 0:
        Name_X_pos = 0
    elif (Name_X_pos +10 + (len(names) * 7) > Image.shape[1]):
          Name_X_pos= Name_X_pos - (Name_X_pos +10 + (len(names) * 7) - (Image.shape[1]))
    if Name_y_pos < 0:
        Name_y_pos = Name_y_pos = y + h + 10
    
    cv2.rectangle(Image, (Name_X_pos-10, Name_y_pos-25), (Name_X_pos +10 + (len(names) * 7), Name_y_pos-1), (0,0,0), -2)         
    cv2.rectangle(Image, (Name_X_pos-10, Name_y_pos-25), (Name_X_pos +10 + (len(names) * 7), Name_y_pos-1), WHITE, 1) 
    cv2.putText(Image, names, (Name_X_pos, Name_y_pos - 10), cv2.FONT_HERSHEY_DUPLEX, .4, WHITE)

def DispID3(x, y, w, h, names, Image):
    Name_y_pos = y - 70
    Name_X_pos = x + w/2 - (len(names)*7/2)

    if Name_X_pos < 0:
        Name_X_pos = 0
    elif (Name_X_pos +10 + (len(names) * 7) > Image.shape[1]):
          Name_X_pos= Name_X_pos - (Name_X_pos +10 + (len(names) * 7) - (Image.shape[1]))
    if Name_y_pos < 0:
        Name_y_pos = Name_y_pos = y + h + 10

    cv2.rectangle(Image, (Name_X_pos-10, Name_y_pos-25), (Name_X_pos +10 + (len(names) * 7), Name_y_pos-1), (0,0,0), -2)          
    cv2.rectangle(Image, (Name_X_pos-10, Name_y_pos-25), (Name_X_pos +10 + (len(names) * 7), Name_y_pos-1), WHITE, 1) 
    cv2.putText(Image, names, (Name_X_pos, Name_y_pos - 10), cv2.FONT_HERSHEY_DUPLEX, .4, WHITE) 

def DrawBox(Image, x, y, w, h):
    cv2.rectangle(Image, (x, y), (x + w, y + h), (255, 255, 255), 1)




def tell_time_passed():
    print ('TIME PASSED ' + str(round(((time.process_time) - current_time)/60), 2) + ' MINS')
    