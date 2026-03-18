import os, ctypes, sys, tkinter
#I модуль запуска
def main_window():
    root = tkinter.Tk()
    root.title('Scarecrow.alpha')
    root.geometry('500x250')
    label = tkinter.Label(root, text='scarecrow.alpha')
    label.pack(pady=20)
    bat = tkinter.Button(root, text='запустить')
    root.mainloop()
def admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
if not admin():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    sys.exit()
else: main_window()

    


