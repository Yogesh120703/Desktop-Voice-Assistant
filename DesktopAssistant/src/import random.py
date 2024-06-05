import tkinter as tk
def store_value():
    val = entry.get()
    print(val)
    entry.delete(0,'end')
    return val
root = tk.Tk()
# Add image file
bg = tk.PhotoImage(file = "pics.png")
# Create Canvas
canvas1 = tk.Canvas( root, width = bg.width(),
                 height = bg.height())
  
canvas1.pack(fill = "both", expand = True)
btn = tk.Button(root,text ="enter command : ",command = lambda: None,compound='right')
circ = tk.PhotoImage(file ="play (1).png")
speak_button = tk.Button(master=root,image=circ,text="speak",command=lambda: None,borderwidth=0)
button2 = tk.Button( root, text = "Reset")
entry = tk.Entry(root)
# Display image
canvas1.create_image( 0, 0, image = bg, 
                     anchor = "nw")
button3_canvas = canvas1.create_window( 190, 100, anchor = "nw",
                                       window = entry)
button1_canvas = canvas1.create_window( 200, 130, 
                                       anchor = "nw",
                                       window = btn)
button2_canvas = canvas1.create_window( 230, 380, 
                                       anchor = "nw",
                                       window = speak_button)

chat_listbox = tk.Listbox(master=canvas1, height=1000, width=50)
scroll_bar = tk.Scrollbar(master=canvas1)
def set_speak_command(command):
    print(command)
    speak_button.configure(command=command)
def set_btn(command):
    btn.configure(command=command)





def speak(text):
    chat_listbox.insert('end', f'Assistant: {text}')


scroll_bar.pack(fill="y",side=tk.RIGHT)
chat_listbox.pack(side=tk.RIGHT,fill="x")
scroll_bar.configure(command=chat_listbox.yview)
chat_listbox.configure(yscrollcommand=scroll_bar.set)
root.geometry('800x750')
root.minsize(700,500)
root.wm_title('Jarvis')
root.resizable(False, True)
mainloop = root.mainloop
mainloop()