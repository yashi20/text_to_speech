# import libraries

from tkinter import *
from gtts import gTTS
from playsound import playsound

# Initialized window

root = Tk()
root.geometry('350x300')
root.resizable(0, 0)
root.config(bg='ghost white')
root.title('DataFlair - TEXT_TO_SPEECH')

# heading
Label(root, text='TEXT_TO_SPEECH', font='arial 20 bold', bg='white smoke').pack()
Label(root, text='DataFlair', font='arial 15 bold', bg='white smoke').pack(side=BOTTOM)

# label
Label(root, text='Enter Text', font='arial 15 bold', bg='white smoke').place(x=20, y=60)

# text variable
Msg = StringVar()

# Entry
entry_field = Entry(root, textvariable=Msg, width='50')
entry_field.place(x=20, y=100)


# define function

def text_to_speech():
    message = entry_field.get()
    speech = gTTS(text=message)
    speech.save('yashi.mp3')
    playsound('yashi.mp3')


def stop():
    root.destroy()


def reset():
    Msg.set("")


# Button
Button(root, text="PLAY", font='arial 15 bold', command=text_to_speech, width=4).place(x=25, y=140)
Button(root, text='EXIT', font='arial 15 bold', command=stop, bg='OrangeRed1').place(x=100, y=140)
Button(root, text='RESET', font='arial 15 bold', command=reset).place(x=175, y=140)

# infinite loop to run program
root.mainloop()
