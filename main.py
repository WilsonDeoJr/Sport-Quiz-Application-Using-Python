from tkinter import *
import http_request as ht
import importlib
from random import *

root = Tk()
try: 
    score = StringVar()
    points = 0

    def submit():
        choices_reload()
        answer()

    def choices_reload():
        importlib.reload(ht)      
        questionbank.set(ht.questioners())
        choice1.set(ht.choices(0))
        choice2.set(ht.choices(1))
        choice3.set(ht.choices(2)) 
        choice4.set(ht.choices(3))
        
    def correct():
        global points
        points = points + 1
        score.set(str(points))

    def answer():
           
        if user_choice.get() == 4:
            correct()
        elif user_choice.get() != 4:
            pass

    def reset():
        global points
        points = 0
        score.set(str(points))

    questionbank = StringVar()
    questionbank.set(ht.questioners())   
    root.title('Sport Quiz')
   
    root.iconbitmap("sports_icon.ico")
    position = 'w'

    questionLabel = Label(root, textvariable=questionbank, font=("Helvetica", 12)) ## label for questions
    questionLabel.pack(anchor=position)
    
    user_choice = IntVar()
    user_choice.set(0)
    
    choice1 = StringVar()
    choice1.set(ht.choices(0))
    choice2 = StringVar()
    choice2.set(ht.choices(1))
    choice3 = StringVar()
    choice3.set(ht.choices(2))
    choice4 = StringVar()
    choice4.set(ht.choices(3))
    vals = StringVar()
    vals.set(choice)
    # Choices with radio button
    Radiobutton(root, textvariable=choice1, variable=user_choice, value=1, font=("Helvetica", 10)).pack(anchor=position)
    Radiobutton(root, textvariable=choice2, variable=user_choice, value=2, font=("Helvetica", 10)).pack(anchor=position)
    Radiobutton(root, textvariable=choice3, variable=user_choice, value=3, font=("Helvetica", 10)).pack(anchor=position)
    Radiobutton(root, textvariable=choice4, variable=user_choice, value=4, font=("Helvetica", 10)).pack(anchor=position)         
 
       
    Button(root, text='Submit', command=submit).pack(anchor=position) ## button for submit
    Button(root, text='Reset', command=reset).pack() ## button for reset
    Button(root, text='Quit', command=root.quit).pack() 

    score.set(str(points))
    Label(root, text='Score:').pack()
    scoreLabel = Label(root, textvariable=score, font=("Helvetica", 10))
    scoreLabel.pack()   
    
except IndexError:
    root.title('Error in Sport Quiz')
    ErrorMsg = StringVar()
    ErrorMsg.set('Cannot connect to API. Please check your coonection!!')
    questionLabel = Label(root, textvariable=ErrorMsg, font=("Helvetica", 12))
    questionLabel.pack(anchor=W)

root.geometry('600x400')
root.mainloop()
