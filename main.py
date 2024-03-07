import tkinter as tk
import webbrowser


def on_click_btn_clickme():
  label["text"] = "Button clicked"

def on_click_btn_exit():
  label["text"] = "Exiting"
  
def on_click_btn_open_google():
  webbrowser.open('Google' , "https://www.google.com/")

 
  
window = tk.Tk()
window.title("Simple windows app")
window.geometry("600x300")
window.attributes('-fullscreen', True) #for full screen
width  = window.winfo_screenwidth()
height  = window.winfo_screenheight()
window.geometry("%dx%d" % (width, height))


hello = tk.Label(text="Hello world!")
hello.pack()

#label for displaying click button
label = tk.Label(window, text="Click the button to display the text",
font=("Arial 20 bold"))
label.pack(pady=20)
btn_ClickME = tk.Button(text="Click me!", command=on_click_btn_clickme)
btn_ClickME .pack()

btn_Exit = tk.Button(text="Exit", command=on_click_btn_exit)
btn_Exit.pack() # pack on window (appear o window)

btn_Open_google = tk.Button(text="Click to open Google", command=on_click_btn_open_google)
btn_Open_google.pack()

tk.mainloop()


