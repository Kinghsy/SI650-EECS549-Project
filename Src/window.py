import tkinter as tk
import tkinter.scrolledtext as scrolledtext
import tkinter.ttk as ttk

#from main import load_label

total_label_list = []
label_pos_s = 0
label_pos_e = 9

def load_label(s, e):
    l3 = label1[:]
    l3.extend(label2[:])
    return l3

def search_click():
    print(query_entry.get())

def pre_page():
    label_pos_s = label_pos_s + 10
    label_pos_e = label_pos_e + 10
    list = load_label()
    return 0

def next_page():
    return 0


if __name__ == "__main__":

    # the whole frame
    gui = tk.Tk()
    gui.geometry("1000x600")
    gui.title("Legal Case Report Selection System")

    # the gui title
    label = tk.Label(gui)
    label['text'] = 'Legal Case Report Selection System'
    label.config(font = ("Courier", 20))
    label.pack()

    # the query label frame
    query_frame = tk.LabelFrame(gui, text="query", padx=20, pady=20)
    query_frame.config(font = ("Courier", 16))
    query_frame.place(x=20, y=40)
    # the content and its block
    query_entry = tk.StringVar()
    query_sentence = ttk.Entry(query_frame, width=82, textvariable = query_entry)
    query_sentence.config(font = ("Courier", 14))
    query_sentence.grid()
    # the button itself
    tk.Button(query_frame, text ="Search", command = search_click).grid(pady = 5, sticky = tk.E)

    # labels using
    # labelframe = tk.LabelFrame(gui, text="labels", padx=20, pady=120)
    # labelframe.config(font = ("Courier", 16))
    # labelframe.place(x=20, y=120)
    label1 = ["11111111", "22222222", "33333333", "44444444", "55555555"]
    label2 = ["66666666", "77777777", "88888888", "99999999", "00000000"]
    check_var1 = [tk.IntVar() for w in range(0, 5)]
    check_var2 = [tk.IntVar() for w in range(0, 5)]
    for i in range(0, 5):
        c = tk.Checkbutton(gui, text=label1[i], variable=check_var1[i], onvalue=1, offvalue=0, height=0, width=0)
        c.config(font = ("Courier", 12))
        c.place(x = 50 + 150*i, y = 180)
    for i in range(0, 5):
        c = tk.Checkbutton(gui, text=label2[i], variable=check_var2[i], onvalue=1, offvalue=0, height=0, width=0)
        c.config(font = ("Courier", 12))
        c.place(x = 50 + 150*i, y = 200)
    pre_page_but = tk.Button(gui, text = "previous set", command = pre_page)
    pre_page_but.config(font = ("Courier", 12))
    pre_page_but.place(x = 800, y = 180)
    next_page_but = tk.Button(gui, text = "next set", command = next_page)
    next_page_but.config(font = ("Courier", 12))
    next_page_but.place(x = 800, y = 220)





    # send = tk.LabelFrame(gui, text = "text", padx = 20, pady = 10)
    # send.place(x = 720, y = 240)



    # button = tk.Button(gui)
    # button['text'] = 'change it'
    # button['command'] = on_click
    # button.pack()






    gui.mainloop()
