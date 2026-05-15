import tkinter as tk

ASCII_ART = """XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XX                                                                          XX
XX   MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM   XX
XX   MMMMMMMMMMMMMMMMMMMMMssssssssssssssssssssssssssMMMMMMMMMMMMMMMMMMMMM   XX
XX   MMMMMMMMMMMMMMMMss'''                          '''ssMMMMMMMMMMMMMMMM   XX
XX   MMMMMMMMMMMMyy''                                    ''yyMMMMMMMMMMMM   XX
XX   MMMMMMMMyy''                                            ''yyMMMMMMMM   XX
XX   MMMMMy''                                                    ''yMMMMM   XX
XX   MMMy'                                                          'yMMM   XX
XX   Mh'                                                              'hM   XX
XX   -                                                                  -   XX
XX                                                                          XX
XX   ::                                                                ::   XX
XX   MMhh.        ..hhhhhh..                      ..hhhhhh..        .hhMM   XX
XX   MMMMMh   ..hhMMMMMMMMMMhh.                .hhMMMMMMMMMMhh..   hMMMMM   XX
XX   ---MMM .hMMMMdd:::dMMMMMMMhh..        ..hhMMMMMMMd:::ddMMMMh. MMM---   XX
XX   MMMMMM MMmm''      'mmMMMMMMMMyy.  .yyMMMMMMMMmm'      ''mmMM MMMMMM   XX
XX   ---mMM ''             'mmMMMMMMMM  MMMMMMMMmm'             '' MMm---   XX
XX   yyyym'    .              'mMMMMm'  'mMMMMm'              .    'myyyy   XX
XX   mm''    .y'     ..yyyyy..  ''''      ''''  ..yyyyy..     'y.    ''mm   XX
XX           MN    .sMMMMMMMMMss.   .    .   .ssMMMMMMMMMs.    NM           XX
XX           N`    MMMMMMMMMMMMMN   M    M   NMMMMMMMMMMMMM    `N           XX
XX            +  .sMNNNNNMMMMMN+   `N    N`   +NMMMMMNNNNNMs.  +            XX
XX              o+++     ++++Mo    M      M    oM++++     +++o              XX
XX                                oo      oo                                XX
XX           oM                 oo          oo                 Mo           XX
XX         oMMo                M              M                oMMo         XX
XX       +MMMM                 s              s                 MMMM+       XX
XX      +MMMMM+            +++NNNN+        +NNNN+++            +MMMMM+      XX
XX     +MMMMMMM+       ++NNMMMMMMMMN+    +NMMMMMMMMNN++       +MMMMMMM+     XX
XX     MMMMMMMMMNN+++NNMMMMMMMMMMMMMMNNNNMMMMMMMMMMMMMMNN+++NNMMMMMMMMM     XX
XX     yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy     XX
XX   m  yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy  m   XX
XX   MMm yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy mMM   XX
XX   MMMm .yyMMMMMMMMMMMMMMMM     MMMMMMMMMM     MMMMMMMMMMMMMMMMyy. mMMM   XX
XX   MMMMd   ''''hhhhh       odddo          obbbo        hhhh''''   dMMMM   XX
XX   MMMMMd             'hMMMMMMMMMMddddddMMMMMMMMMMh'             dMMMMM   XX
XX   MMMMMMd              'hMMMMMMMMMMMMMMMMMMMMMMh'              dMMMMMM   XX
XX   MMMMMMM-               ''ddMMMMMMMMMMMMMMdd''               -MMMMMMM   XX
XX   MMMMMMMM                   '::dddddddd::'                   MMMMMMMM   XX
XX   MMMMMMMM-                                                  -MMMMMMMM   XX
XX   MMMMMMMMM                                                  MMMMMMMMM   XX
XX   MMMMMMMMMy                                                yMMMMMMMMM   XX
XX   MMMMMMMMMMy.                                            .yMMMMMMMMMM   XX
XX   MMMMMMMMMMMMy.                                        .yMMMMMMMMMMMM   XX
XX   MMMMMMMMMMMMMMy.                                    .yMMMMMMMMMMMMMM   XX
XX   MMMMMMMMMMMMMMMMs.                                .sMMMMMMMMMMMMMMMM   XX
XX   MMMMMMMMMMMMMMMMMMss.           ....           .ssMMMMMMMMMMMMMMMMMM   XX
XX   MMMMMMMMMMMMMMMMMMMMNo         Flowedka         oNMMMMMMMMMMMMMMMMMMMM   XX
XX                                                                          XX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"""

PASSWORD = "9427"

root = tk.Tk()
root.title("ASCII Art")
root.configure(bg="black")
root.attributes("-fullscreen", True)

root.bind("<q>", lambda e: None)
root.bind("<Q>", lambda e: None)

ascii_frame = tk.Frame(root, bg="black")
ascii_frame.place(relx=0.05, rely=0.5, anchor="w")

ascii_label = tk.Label(
    ascii_frame,
    text=ASCII_ART,
    font=("Courier", 7),
    fg="white",
    bg="black",
    justify="left",
)
ascii_label.pack()

title_label = tk.Label(
    root,
    text="windows,is blocked!!!",
    font=("Courier", 36, "bold"),
    fg="white",
    bg="black",
    justify="left",
)
title_label.place(relx=0.55, rely=0.30, anchor="w")


def check_password():
    typed = password_var.get()
    if typed == PASSWORD:
        password_entry.config(state="disabled")
        submit_btn.config(state="disabled")
        root.after(2000, root.destroy)


def on_key_release(event):
    typed = password_var.get()
    if typed == PASSWORD:
        check_password()
    if len(typed) > len(PASSWORD):
        password_var.set("")


password_var = tk.StringVar()

entry_frame = tk.Frame(root, bg="white", padx=2, pady=2)
entry_frame.place(relx=0.425, rely=0.43, relwidth=0.52, anchor="w")

password_entry = tk.Entry(
    entry_frame,
    textvariable=password_var,
    font=("Courier", 22),
    fg="white",
    bg="black",
    insertbackground="white",
    relief="flat",
    show="*",
)
password_entry.pack(fill="x", ipady=10, ipadx=8)
password_entry.bind("<KeyRelease>", on_key_release)
password_entry.bind("<Return>", lambda e: check_password())
password_entry.focus_set()

btn_frame = tk.Frame(root, bg="white", padx=2, pady=2)
btn_frame.place(relx=0.695, rely=0.505, anchor="n")

submit_btn = tk.Button(
    btn_frame,
    text="Check",
    command=check_password,
    font=("Courier", 13, "bold"),
    fg="white",
    bg="black",
    activebackground="#222222",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
)
submit_btn.pack(ipady=5, ipadx=18)
by_label = tk.Label(
    root,
    text="by flowedka",
    font=("Courier", 11),
    fg="#666666",
    bg="black",
)
by_label.place(relx=0.695, rely=0.650, anchor="n")

total_seconds = 3 * 3600 + 30 * 100

timer_label = tk.Label(
    root,
    text="03:30:00",
    font=("Courier", 48, "bold"),
    fg="white",
    bg="black",
)
timer_label.place(relx=0.695, rely=0.61, anchor="center")


def update_timer():
    global total_seconds
    if total_seconds <= 0:
        timer_label.config(text="00:00:00")
        return
    h = total_seconds // 3600
    m = (total_seconds % 3600) // 60
    s = total_seconds % 60
    timer_label.config(text=f"{h:02d}:{m:02d}:{s:02d}")
    total_seconds -= 1
    root.after(1000, update_timer)


update_timer()

root.mainloop()