import PySimpleGUI as sg
from gtts import gTTS
import os
import time
import speech_recognition as sr

from PIL import Image,ImageTk
import tkinter as tk
from tkinter import *
from tkinter import ttk

sg.theme('DarkAmber')
layout_column= [[sg.Text("\n  Hello User Please choose one of the options", size=(50,5), font=("Stencil", 24), text_color='white')], [sg.Button("Text-To-Speech",size= 
(20, 2),button_color=("white", "grey"))], [sg.Button("Speech-To-Text",size= 
(20, 2),button_color=("white", "grey"))],[sg.Button("Speech-To-Sign Gestures",size= 
(20, 2),button_color=("white", "grey"))]]

layout = [[sg.Column(layout_column, element_justification='center')]]

# Create the window
window = sg.Window("Communication Aid Application", layout, size=(840,600),grab_anywhere=True)

def speecht():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        text = r.recognize_google(audio)
        layout4=[[sg.Text("You said: "+text ,size=(50,5))],[sg.Button("Close")]]
        window4=sg.Window("Speech-To-Text",layout4)
        event4,values4=window4.read()
        if event4=="Close" or event4==sg.WIN_CLOSED:
            window4.close()
            return False
        return True
            
# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "Text-To-Speech":
        layout2 = [
    [sg.Text('Please enter your text')],
    [sg.Text('Text :', size =(5, 1)), sg.InputText()],
    [sg.Submit(), sg.Cancel()]
        ]
        window2 = sg.Window("Text-To-Speech", layout2,grab_anywhere=True)
        while True:
            event2, values2 = window2.read()
            if event2 == "Submit":
                language='en'
                audio=gTTS(text=values2[0],lang=language,slow=False)

                audio.save("1.wav")
                os.system("1.wav")
            if event2 == "Cancel" or event2==sg.WIN_CLOSED :
                window2.close()
                break
    if event == "Speech-To-Text":
        layout3=[[sg.Text("Click on the OK button and Speak",size =(35,1 ))],[sg.Button("OK"), sg.Cancel()]]
        window3=sg.Window("Speech-To-Text",layout3)
        while True:
            event3,values3=window3.read()
            if event3 == "Cancel" or event3==sg.WIN_CLOSED:
                    window3.close()
                    break
                    
            if event3=="OK":
                
                    re=speecht()
                    

    if event == "Speech-To-Sign Gestures":
        layout5=[[sg.Text("Click on the OK button and Speak",size =(35,1 ))],[sg.Button("OK"), sg.Cancel()]]
        window5=sg.Window("Speech-To-Sign Gestures",layout5)
        while True:
            event5, values5 = window5.read()
            if event5 == "Cancel" or event5==sg.WIN_CLOSED:
                window5.close()
                break
            if event5 =="OK":
                
                def split_str(s):
                    return [ch for ch in s]

                r = sr.Recognizer()
                root = Tk()
                root.title('Translation')
                root.state('zoomed')
                main_frame = Frame(root)
                main_frame.pack(fill=BOTH, expand=1)

                my_canvas = Canvas(main_frame)
                my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

                my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
                my_scrollbar.pack(side=RIGHT, fill=Y)

                my_canvas.configure(yscrollcommand=my_scrollbar.set)
                my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

                second_frame = Frame(my_canvas)
                my_canvas.create_window((0,0), window=second_frame, anchor="nw")

                photoimage_list = []

                with sr.Microphone() as source:
                    
                    audio = r.listen(source)
                    
                 
                try:
                    text = r.recognize_google(audio)
                    
                    c=split_str(text)
                    i=0
                    j=0
                    for r in c:
                            
                        if r == 'a' or r=='A':
                            ph_a = PhotoImage(master=root,file='C:\\Users\\Tarun\\Desktop\\american language\\a.PNG')
                            photoimage_list.append(ph_a)
                            lab_a = Label(second_frame,image=ph_a)
                            lab_a.grid(row = j,column = i)
                            i=i+1;

                        if r == 'b' or r=='B':
                            ph_b = PhotoImage(master=root,file='C:\\Users\\Tarun\\Desktop\\american language\\b.png')
                            photoimage_list.append(ph_b)
                            lab_b = Label(second_frame,image=ph_b)
                            lab_b.grid(row = j,column = i)
                            i=i+1;

                            
                        if r == 'c' or r=='C':
                            ph_c = PhotoImage(master=root,file='C:\\Users\\Tarun\\Desktop\\american language\\c.png')
                            photoimage_list.append(ph_c)
                            lab_c = Label(second_frame,image=ph_c)
                            lab_c.grid(row = j,column = i)
                            i=i+1;

                            
                        if r == 'd' or r=='D':
                            ph_d = PhotoImage(master=root,file="C:\\Users\\Tarun\\Desktop\\american language\\d.png")
                            photoimage_list.append(ph_d)
                            lab_d = Label(second_frame,image=ph_d)
                            lab_d.grid(row = j,column = i)
                            i=i+1;


                        if r == 'e' or r=='E':
                            ph_e = PhotoImage(master=root,file="C:\\Users\\Tarun\\Desktop\\american language\\e.png")
                            photoimage_list.append(ph_e)
                            lab_e = Label(second_frame,image=ph_e)
                            lab_e.grid(row = j,column = i)
                            i=i+1;


                        if r == 'f' or r=='F':
                            ph_f = PhotoImage(master=root,file="C:\\Users\\Tarun\\Desktop\\american language\\f.png")
                            photoimage_list.append(ph_f)
                            lab_f = Label(second_frame,image=ph_f)
                            lab_f.grid(row = j,column = i)
                            i=i+1;


                        if r == 'g' or r=='G':
                            ph_g = PhotoImage(master=root,file="C:\\Users\\Tarun\\Desktop\\american language\\g.png")
                            photoimage_list.append(ph_g)
                            lab_g = Label(second_frame,image=ph_g)
                            lab_g.grid(row = j,column = i)
                            i=i+1;


                        if r == 'h' or r=='H':
                            ph_h = PhotoImage(master=root,file="C:\\Users\\Tarun\\Desktop\\american language\\h.png")
                            photoimage_list.append(ph_h)
                            lab_h = Label(second_frame,image=ph_h)
                            lab_h.grid(row = j,column = i)
                            i=i+1;


                        if r == 'i' or r=='I':
                            ph_i = PhotoImage(master=root,file="C:\\Users\\Tarun\\Desktop\\american language\\i.png")
                            photoimage_list.append(ph_i)
                            lab_i = Label(second_frame,image=ph_i)
                            lab_i.grid(row = j,column = i)
                            i=i+1;


                        if r == 'j' or r=='J':
                            ph_j = PhotoImage(master=root,file="C:\\Users\\Tarun\\Desktop\\american language\\j.png")
                            photoimage_list.append(ph_j)
                            lab_j = Label(second_frame,image=ph_j)
                            lab_j.grid(row = j,column = i)
                            i=i+1;

                        if r == 'k' or r=='K':
                            ph_k = PhotoImage(master=root,file="C:\\Users\\Tarun\\Desktop\\american language\\k.png")
                            photoimage_list.append(ph_k)
                            lab_k = Label(second_frame,image=ph_k)
                            lab_k.grid(row = j,column = i)
                            i=i+1;

                        if r == 'l' or r=='L':
                            ph_l = PhotoImage(master=root,file="C:\\Users\\Tarun\\Desktop\\american language\\l.png")
                            photoimage_list.append(ph_l)
                            lab_l = Label(second_frame,image=ph_l)
                            lab_l.grid(row = j,column = i)
                            i=i+1;

                        if r == 'm' or r=='M':
                            ph_m = PhotoImage(master=root,file="C:\\Users\\Tarun\\Desktop\\american language\\m.png")
                            photoimage_list.append(ph_m)
                            lab_m = Label(second_frame,image=ph_m)
                            lab_m.grid(row = j,column = i)
                            i=i+1;

                        if r == 'n' or r=='n':
                            ph_n = PhotoImage(master=root,file="C:\\Users\\Tarun\\Desktop\\american language\\n.png")
                            photoimage_list.append(ph_n)
                            lab_n = Label(second_frame,image=ph_n)
                            lab_n.grid(row = j,column = i)
                            i=i+1;

                        if r == 'o' or r=='O':
                            ph_o = PhotoImage(master=root,file="C:\\Users\\Tarun\\Desktop\\american language\\o.png")
                            photoimage_list.append(ph_o)
                            lab_o = Label(second_frame,image=ph_o)
                            lab_o.grid(row = j,column = i)
                            i=i+1;

                        if r == 'p' or r=='P':
                            ph_p = PhotoImage(master=root,file="C:\\Users\\Tarun\\Desktop\\american language\\p.png")
                            photoimage_list.append(ph_p)
                            lab_p = Label(second_frame,image=ph_p)
                            lab_p.grid(row = j,column = i)
                            i=i+1;

                        if r == 'q' or r=='Q':
                            ph_q = PhotoImage(master=root,file="C:\\Users\\Tarun\\Desktop\\american language\\q.png")
                            photoimage_list.append(ph_q)
                            lab_q = Label(second_frame,image=ph_q)
                            lab_q.grid(row = j,column = i)
                            i=i+1;

                        if r == 'r' or r=='R':
                            ph_r = PhotoImage(master=root,file="C:\\Users\\Tarun\\Desktop\\american language\\r.png")
                            photoimage_list.append(ph_r)
                            lab_r = Label(second_frame,image=ph_r)
                            lab_r.grid(row = j,column = i)
                            i=i+1;

                        if r == 's' or r=='S':
                            ph_s = PhotoImage(master=root,file="C:\\Users\\Tarun\\Desktop\\american language\\s.png")
                            photoimage_list.append(ph_s)
                            lab_s = Label(second_frame,image=ph_s)
                            lab_s.grid(row = j,column = i)
                            i=i+1;

                        if r == 't' or r=='T':
                            ph_t = PhotoImage(master=root,file="C:\\Users\\Tarun\\Desktop\\american language\\t.png")
                            photoimage_list.append(ph_t)
                            lab_t = Label(second_frame,image=ph_t)
                            lab_t.grid(row = j,column = i)
                            i=i+1;
                            


                        if r == 'u' or r=='U':
                            ph_u = PhotoImage(master=root,file="C:\\Users\\Tarun\\Desktop\\american language\\u.png")
                            photoimage_list.append(ph_u)
                            lab_u = Label(second_frame,image=ph_u)
                            lab_u.grid(row = j,column = i)
                            i=i+1;

                        if r == 'v' or r=='V':
                            ph_v = PhotoImage(file="C:\\Users\\Tarun\\Desktop\\american language\\v.png")
                            photoimage_list.append(ph_v)
                            lab_v = Label(second_frame,image=ph_v)
                            lab_v.grid(row = j,column = i)
                            i=i+1;

                        if r == 'w' or r==' W':
                            ph_w = PhotoImage(master=root,file="C:\\Users\\Tarun\\Desktop\\american language\\w.png")
                            photoimage_list.append(ph_w)
                            lab_w = Label(second_frame,image=ph_w)
                            lab_w.grid(row = j,column = i)
                            i=i+1;

                        if r == 'x' or r=='X':
                            ph_x = PhotoImage(master=root,file="C:\\Users\\Tarun\\Desktop\\american language\\x.png")
                            photoimage_list.append(ph_x)
                            lab_x = Label(second_frame,image=ph_x)
                            lab_x.grid(row = j,column = i)
                            i=i+1;

                        if r == 'y' or r=='Y':
                            ph_y = PhotoImage(master=root,file="C:\\Users\\Tarun\\Desktop\\american language\\y.png")
                            photoimage_list.append(ph_y)
                            lab_y = Label(second_frame,image=ph_y)
                            lab_y.grid(row = j,column = i)
                            i=i+1;

                        if r == 'z' or r=='Z':
                            ph_z = PhotoImage(master=root,file="C:\\Users\\Tarun\\Desktop\\american language\\z.png")
                            photoimage_list.append(ph_z)
                            lab_z = Label(second_frame,image=ph_z)
                            lab_z.grid(row = j,column = i)
                            i=i+1;


                        if r == ' ':
                            j=j+1
                            i=0
                except Exception as e:
                    print (e)

        
    if event == sg.WIN_CLOSED:
        break

window.close()
