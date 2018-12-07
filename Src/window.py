import tkinter as tk
import tkinter.scrolledtext as scrolledtext
import tkinter.ttk as ttk
import Const



label_pos = 0
f = open(Const.path_to_label_file)
total_label_list = f.read().splitlines()
f.close()
print(total_label_list)
label1 = total_label_list[label_pos: label_pos + 5]
label2 = total_label_list[label_pos + 5: label_pos + 10]
selcted_label = []
button_list = []


#def label_plot(button_list, label1, label2, check_var1, check_var2):
def label_plot():
    global button_list
    global label1
    global label2
    global check_var1
    global check_var2
    for ele in button_list:
        ele.place_forget()
    button_list = []
    for i in range(0, 5):
        c = tk.Checkbutton(gui, text=label1[i], variable=check_var1[i], onvalue=1, offvalue=0, height=0, width=0)
        c.config(font=("Courier", 12))
        c.place(x=50 + 150 * i, y=180)
        button_list.append(c)
    for i in range(0, 5):
        c = tk.Checkbutton(gui, text=label2[i], variable=check_var2[i], onvalue=1, offvalue=0, height=0, width=0)
        c.config(font=("Courier", 12))
        c.place(x=50 + 150 * i, y=200)
        button_list.append(c)

def deal_label():
    global check_var1
    global check_var2
    global label1
    global label2
    global selcted_label
    for i in range(0, 5):
        if (check_var1[i].get() == 1) and (not label1[i] in selcted_label):
            selcted_label.append(label1[i])
        if (check_var1[i].get() == 0) and (label1[i] in selcted_label):
            selcted_label.remove(label1[i])
        if (check_var2[i].get() == 1) and (not label2[i] in selcted_label):
            selcted_label.append(label2[i])
        if (check_var2[i].get() == 0) and (label2[i] in selcted_label):
            selcted_label.remove(label2[i])
    return 0

def redeal_label():
    global check_var1
    global check_var2
    global label1
    global label2
    global selcted_label
    for i in range(0, 5):
        if (label1[i] in selcted_label):
            check_var1[i].set(1)
        else:
            check_var1[i].set(0)
        if (label2[i] in selcted_label):
            check_var2[i].set(1)
        else:
            check_var2[i].set(0)
    return 0

def search_click():
    print(query_entry.get())

def pre_set():
    global label_pos
    global total_label_list
    global label1
    global label2
    global selcted_label
    deal_label()
    if (label_pos != 0):
        label_pos = label_pos - 10
    label1 = total_label_list[label_pos: label_pos + 5]
    label2 = total_label_list[label_pos + 5: label_pos + 10]
    redeal_label()
    label_plot()
    print(selcted_label)
    return 0

def next_set():
    global label_pos
    global total_label_list
    global label1
    global label2
    global selcted_label
    deal_label()
    label_pos = label_pos + 10
    label1 = total_label_list[label_pos: label_pos + 5]
    label2 = total_label_list[label_pos + 5: label_pos + 10]
    redeal_label()
    label_plot()
    print(selcted_label)
    return 0



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
check_var1 = [tk.IntVar() for w in range(0, 5)]
check_var2 = [tk.IntVar() for w in range(0, 5)]
label_plot()
pre_page_but = tk.Button(gui, text = "previous set", command = pre_set)
pre_page_but.config(font = ("Courier", 12))
pre_page_but.place(x = 800, y = 180)
next_page_but = tk.Button(gui, text = "next set", command = next_set)
next_page_but.config(font = ("Courier", 12))
next_page_but.place(x = 800, y = 220)





# send = tk.LabelFrame(gui, text = "text", padx = 20, pady = 10)
# send.place(x = 720, y = 240)



# button = tk.Button(gui)
# button['text'] = 'change it'
# button['command'] = on_click
# button.pack()






gui.mainloop()
