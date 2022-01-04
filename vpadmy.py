import tkinter as tk
from tkinter import Menu, ttk 
from tkinter import font, colorchooser, filedialog,messagebox
import os
from typing import Counter

main_application = tk.Tk()
main_application.geometry('1200x800')
main_application.title('Vpad Text Editor')

########################### Main Menu ##########################
#........................... Ending .....................
main_menu = tk.Menu()
#file icons
new_icon =tk.PhotoImage(file="icons2/new.png")
open_icon =tk.PhotoImage(file="icons2/open.png")
save_icon =tk.PhotoImage(file="icons2/save.png")
save_as_icon =tk.PhotoImage(file="icons2/save_as.png")
exit_icon =tk.PhotoImage(file="icons2/exit.png")

file = tk.Menu(main_menu, tearoff=False) 


file.add_command(label='New',image=new_icon,compound=tk.LEFT, accelerator='Ctrl + N',)
file.add_command(label='Open',image=open_icon ,compound=tk.LEFT, accelerator='Ctrl + O')
file.add_command(label='Save',image=save_icon,compound=tk.LEFT, accelerator='Ctrl + S')
file.add_command(label='Save as',image=save_as_icon,compound=tk.LEFT, accelerator='Ctrl + Alt + S')
file.add_command(label='Exit',image=exit_icon,compound=tk.LEFT, accelerator='Ctrl + Q')

edit= tk.Menu(main_menu, tearoff=False)
#edit icons
copy_icon =tk.PhotoImage(file= "icons2/copy.png")
cut_icon =tk.PhotoImage(file= "icons2/cut.png")
paste_icon =tk.PhotoImage(file= "icons2/paste.png")
clear_all_icon =tk.PhotoImage(file= "icons2/clear_all.png")
find_icon =tk.PhotoImage(file= "icons2/find.png")

edit.add_command(label='Copy', accelerator='Ctrl + C', image=copy_icon,compound=tk.LEFT)
edit.add_command(label='Cut', accelerator='Ctrl + X', image=cut_icon,compound=tk.LEFT)
edit.add_command(label='Paste', accelerator='Ctrl + V', image=paste_icon, compound=tk.LEFT)
edit.add_command(label='Clear All', accelerator='Ctrl + Alt + X', image=clear_all_icon, compound=tk.LEFT)
edit.add_command(label='Find', accelerator='Ctrl + F', image=find_icon, compound=tk.LEFT)


view = tk.Menu(main_menu, tearoff=False)
#view icons
tool_bar_icon= tk.PhotoImage(file= "icons2/tool_bar.png")
status_bar_icon = tk.PhotoImage(file="icons2/status_bar.png")

view.add_checkbutton(label='Tool Bar',image=tool_bar_icon, compound=tk.LEFT)
view.add_checkbutton(label='Task Bar', image=status_bar_icon, compound=tk.LEFT)

color_theme = tk.Menu(main_menu, tearoff=False)
#color_theme icons
light_default_icon= tk.PhotoImage(file="icons2/ligth_default.png")
ligth_plus_icon= tk.PhotoImage(file="icons2/ligth_plus.png")
dark_icon= tk.PhotoImage(file="icons2/dark.png")
red_icon= tk.PhotoImage(file="icons2/red.png")
monokai_icon= tk.PhotoImage(file="icons2/monokai.png")
night_blue_icon= tk.PhotoImage(file="icons2/night_blue.png")

theme_choice= tk.StringVar()
color_icons =(light_default_icon,ligth_plus_icon, dark_icon, red_icon, monokai_icon, night_blue_icon)

color_dict = {
    'Ligth Default' : ('#000000','#ffffff'),
    'Ligth Plus' : ('#474747', '#e0e0e0'),
    'Dark' : ('#c4c4c4','#2d2d2d'),
    'Red':('#2d2d2d','#ffe8e8'),
    'Monokai':('#d3b774','#474747'),
    'Night Blue' : ('#ededed', '#6b9dc2')
}
Count=0
for i in color_dict:
    color_theme.add_radiobutton(label=i , image=color_icons, variable=theme_choice,compound=tk.LEFT)
    Count+=1

#Cascade
main_menu.add_cascade(label='File', menu=file)
main_menu.add_cascade(label='Edit', menu=edit)
main_menu.add_cascade(label='View', menu=view)
main_menu.add_cascade(label='Color Theme', menu=color_theme)

########################### Toolbar ##########################
#........................... Ending .....................


###########################Text Editor ##########################
#........................... Ending .....................



########################### Main Status Bar ##########################
#........................... Ending .....................


########################### Main menu fUNCTIONALITY ##########################
#........................... Ending .....................




main_application.config(menu=main_menu)
main_application.mainloop()