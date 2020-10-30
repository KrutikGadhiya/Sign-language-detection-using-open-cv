#import module needed
import tkinter as tk
#write the new window function which
#will be called when button pressed
def new_window():
    window = tk.Toplevel(root)
    canvas = tk.Canvas(window, height=HEIGHT, width=WIDTH)
    canvas.pack()

HEIGHT = 400
WIDTH = 300
#create original window (title not need but why not?)
root = tk.Tk()
root.title("new window making machine: ")
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()
#create button that will be placed
button = tk.Button(root, text="new window", bg='black', fg='#469A00',
                              command=lambda: new_window())
#can use .grid() or .place() instead of pack .place()
#is the best according to me if you want the most control of positions
button.pack()
root.mainloop()