import tkinter
import tkinter.ttk

root = tkinter.Tk()
root.title("Sandbox")

mainframe = tkinter.ttk.Frame(root)
mainframe.pack()

normal_tree = tkinter.ttk.Treeview(mainframe)
normal_tree.pack()

root.mainloop()
