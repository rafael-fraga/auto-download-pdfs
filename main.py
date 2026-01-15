print('Iniciando aplicação...')


from views.gui import GUI
import tkinter as tk


if __name__ == "__main__":
    root = tk.Tk()
    app = GUI(root)
    root.mainloop()