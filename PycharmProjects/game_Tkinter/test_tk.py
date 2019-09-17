import tkinter as tk

win = tk.Tk()
canvas = tk.Canvas(win, height=600, width=1000)
canvas.create_line(70,200,150,50,250,200,width=3.0,fill='red')
canvas.create_oval(600,400,900,500,fill='blue')
canvas.create_rectangle(400,200,600,300,fill='green')
canvas.create_text(400,50,text='色々な図形',font=('Times',50))
canvas.pack()
win.mainloop()