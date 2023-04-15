import tkinter

for i in range(1000000000000000000000):
    i = input("蔡徐坤是？")
    if i == ("鸡"):
        print("蔡徐坤是鸡")
        tk = tkinter.Tk()
        tk.title("鸡你太美~")
        tk.geometry("300x200")
        tki = tkinter.Label(tk, bd=14, fg="red", text="鸡你太美~")
        tki.place(relx=0.2, rely=0.2)
        tk.mainloop()
        break
    else:
        print("再想一想")
        tk = tkinter.Tk()
        tk.title("你干嘛~")
        tk.geometry("300x200")
        tki = tkinter.Label(tk, bd=14, fg="red", text="你干嘛~")
        tki.place(relx=0.2, rely=0.2)
        tk.mainloop()
        i = input("蔡徐坤是？")
        if i == ("鸡"):
            print("蔡徐坤是鸡")

            tk = tkinter.Tk()
            tk.title("鸡你太美~")
            tk.geometry("300x200")
            tki = tkinter.Label(tk, bd=14, fg="red", text="鸡你太美~")
            tki.place(relx=0.2, rely=0.2)
            tk.mainloop()
            break
        else:
            print("再想一想")
            tk = tkinter.Tk()
            tk.title("你干嘛~")
            tk.geometry("300x200")
            tki = tkinter.Label(tk, bd=14, fg="red", text="你干嘛~")
            tki.place(relx=0.2, rely=0.2)
            tk.mainloop()
