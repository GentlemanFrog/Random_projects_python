import pickle
from tkinter import *
from tkinter import messagebox

SAVING_PATH = r"C:\Users\alekl\OneDrive\Pulpit\Random_projects\counter_cough.pickle"

try:
    with open(SAVING_PATH, "rb+") as fh:
        COUGH_COUNTER = pickle.load(fh)
except Exception:
    COUGH_COUNTER = 0


def cough_counter_click():
    global COUGH_COUNTER
    COUGH_COUNTER += 1
    # print(cought_counter)
    counter_label.config(text=COUGH_COUNTER)


def cough_counter_decrement():
    global COUGH_COUNTER
    COUGH_COUNTER -= 1
    # print(cought_counter)
    counter_label.config(text=COUGH_COUNTER)


def cough_counter_reset(label: Label):
    global COUGH_COUNTER
    COUGH_COUNTER = 0
    messagebox.showinfo("Hello", "Counter was set to 0.")
    label.config(text=COUGH_COUNTER)


# Creating instance of window
window = Tk()
# Window.geometry("200x100")
window.title('Cought_counter')

plus_one_button = Button(window, text='+1')
# Wykonuje callback funkcji
plus_one_button.config(command=cough_counter_click)
plus_one_button.config(font=('Monospace', 25, 'bold'))
plus_one_button.config(activebackground='#FF0000')

minus_one_button = Button(window, text='-1')
# Wykonuje callback funkcji
minus_one_button.config(command=cough_counter_decrement)
minus_one_button.config(font=('Monospace', 25, 'bold'))
minus_one_button.config(activebackground='#FF0000')

# Creating label for displaying number:
counter_label = Label(window, text=COUGH_COUNTER)
counter_label.config(font=('Monospace', 25))

reset_button = Button(window, text='Reset')
reset_button.config(command=lambda: cough_counter_reset(counter_label))
reset_button.config(font=('Monospace', 25, 'bold'))
reset_button.config(activebackground='#FF0000')
reset_button.config(compound='top')

plus_one_button.pack()
minus_one_button.pack()
counter_label.pack()
reset_button.pack()

window.mainloop()

with open(SAVING_PATH, "wb+") as fh:
    pickle.dump(COUGH_COUNTER, fh)
