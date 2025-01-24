import tkinter as tk

def cut(event=None):
    text_field.event_generate("<<Cut>>")
    return "break"

def copy(event=None):
    text_field.event_generate("<<Copy>>")
    return "break"

def paste(event=None):
    text_field.event_generate("<<Paste>>")
    return "break"

root = tk.Tk()
root.title("Контекстное меню")

text_field = tk.Text(root, wrap="word", height=10, width=40)
text_field.pack(padx=10, pady=10)

context_menu = tk.Menu(root, tearoff=0)
context_menu.add_command(label="Вырезать", command=cut)
context_menu.add_command(label="Копировать", command=copy)
context_menu.add_command(label="Вставить", command=paste)

def show_context_menu(event):
    context_menu.tk_popup(event.x_root, event.y_root)


text_field.bind("<Button-3>", show_context_menu)

# сделала так а не через:
# text_field.bind("<Control-x>", cut)
# чтобы работало и на русской раскладке

def universal_hotkeys(event):
    if event.state & 0x4: # CTRL
        if event.keycode == 88:  # X
            return cut()
        elif event.keycode == 67:  # C
            return copy()
        elif event.keycode == 86:  # V
            return paste()


text_field.bind("<KeyPress>", universal_hotkeys)
root.mainloop()