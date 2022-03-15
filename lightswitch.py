import tkinter as tk
window = tk.Tk()

button = tk.Button(text='Lichtknop', bg="white", fg="black")
button.pack(pady = 20, padx = 20)

# schijf hier tussen je code
knop = 1

def click(event):
    global knop
    if knop == 1:
        window.configure(bg = "yellow")
        button['text'] = 'Switch light on'
        print("Switch light on")
        knop = 2
    elif knop == 2:
        
        window.configure(bg = "black")
        button['text'] = 'Switch light off'
        print("Switch light off")
        knop = 1

#-----------------------------

button.bind('<Button-1>', click)   
        
# schijf hier tussen je code

window.mainloop()