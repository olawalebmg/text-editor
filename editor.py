# from tkinter import *
from tkinter import ttk, font
from ttkthemes import ThemedTk
import tkinter as tk

# creating window
app = ThemedTk(theme="radiance")
app.geometry("1200x700")
app.title("BMG Words")

# main menu that holds other menu
app_menu = tk.Menu()

# file menu
filemenu = tk.Menu(app_menu, tearoff=False)

filemenu.add_command(label="New")
filemenu.add_command(label="Open")
filemenu.add_separator()
filemenu.add_command(label="Save")
filemenu.add_command(label="Save as")
filemenu.add_command(label="Close")

# file menu functions
file_name= None

def new_file(event=None):
    app.title("Untitled")
    global file_name
    file_name = None
    content_text.delete(1.0, END)

# edit menu
editmenu = tk.Menu(app_menu, tearoff=False)

editmenu.add_command(label="Undo")
editmenu.add_command(label="Redo")
editmenu.add_separator()
editmenu.add_command(label="Cut")
editmenu.add_command(label="Copy")
editmenu.add_command(label="Paste")
editmenu.add_command(label="Delete")
editmenu.add_separator()
editmenu.add_command(label="Clear")
editmenu.add_command(label="Select All")

# view menu
viewmenu = tk.Menu(app_menu, tearoff=False)
viewmenu.add_command(label="Undo")

# help menu
helpmenu = tk.Menu(app_menu, tearoff=0)
helpmenu.add_command(label="Help Index")
helpmenu.add_command(label="About...")

# button's image
bold = tk.PhotoImage(file="icons/bold.png")
underline = tk.PhotoImage(file="icons/underline.png")
italic = tk.PhotoImage(file="icons/italic.png")
left = tk.PhotoImage(file="icons/left.png")
right = tk.PhotoImage(file="icons/right.png")
center = tk.PhotoImage(file="icons/center.png")
font_color = tk.PhotoImage(file="icons/font_color.png")

# toolbar
tool_bar = ttk.Label(app)
tool_bar.pack(side=tk.TOP, fill=tk.X)

# statusbar
statusbar = ttk.Label(app, text="Words")
statusbar.pack(side=tk.BOTTOM, fill=tk.X)

# font's drop down box
font_tuple = font.families()
font_family = tk.StringVar()
font_box = ttk.Combobox(tool_bar, width=21, textvariable=font_family, state="readonly")  # combobox
font_box["values"] = font_tuple
font_box.current(font_tuple.index("Arial"))
font_box.grid(row=0, column=0, padx=5)

# font size box
font_size = tk.IntVar()
font_size_box = ttk.Combobox(tool_bar, width=14, textvariable=font_size, state="readonly")
font_size_box["values"] = tuple(range(5, 72, 1))
font_size_box.current(7)
font_size_box.grid(row=0, column=1, padx=5)

# adding button to the editor
# bold button
bold_button = ttk.Button(tool_bar, image=bold)
bold_button.grid(row=0, column=2, padx=2)

# italic button
italic_button = ttk.Button(tool_bar, image=italic)
italic_button.grid(row=0, column=3, padx=2)

# underline button
underline_button = ttk.Button(tool_bar, image=underline)
underline_button.grid(row=0, column=4, padx=2, )

# font-color button
font_btn = ttk.Button(tool_bar, image=font_color, text="font")
font_btn.grid(row=0, column=5, padx=10)

# left align button
left_button = ttk.Button(tool_bar, image=left)
left_button.grid(row=0, column=6, padx=2)

# center align button
center_button = ttk.Button(tool_bar, image=center)
center_button.grid(row=0, column=7, padx=2)

# right align button
right_button = ttk.Button(tool_bar, image=right)
right_button.grid(row=0, column=8, padx=2)

# cascading/adding it to main menu
app_menu.add_cascade(label="File", menu=filemenu)
app_menu.add_cascade(label="Edit", menu=editmenu)
app_menu.add_cascade(label="View", menu=viewmenu)
app_menu.add_cascade(label="Help", menu=helpmenu)

# adding the main context Text widget and Scrollbar Widget
content_text = tk.Text(app, wrap='word', highlightbackground="black")
content_text.pack(expand='no', fill='both')
content_text.place(relx=0.75, rely=0.075, relheight=0.88, relwidth=0.5, anchor='ne')

scroll_bar = tk.Scrollbar(content_text)
content_text.configure(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=content_text.yview)
scroll_bar.pack(side='right', fill='y')

app.config(menu=app_menu)
app.mainloop()
