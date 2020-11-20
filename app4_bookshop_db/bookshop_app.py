""" The Booshop desktop application
    Allows user to create, view, update and delete book entries
    The book entry consists of
      - Name, Author, Year of Publication and ISBN
"""

from tkinter import *

app_window = Tk()

title_lb = Label(app_window, text="Title")
title_lb.grid(row=0, column=0)
title_txt = StringVar()
title_ent = Entry(app_window, textvariable=title_txt)
title_ent.grid(row=0, column=1)

author_lb = Label(app_window, text="Author")
author_lb.grid(row=0, column=2)
author_txt = StringVar()
author_ent = Entry(app_window, textvariable=author_txt)
author_ent.grid(row=0, column=3)


year_lb = Label(app_window, text="Year")
year_lb.grid(row=1, column=0)
year_txt = StringVar()
year_ent = Entry(app_window, textvariable=year_txt)
year_ent.grid(row=1, column=1)


isbn_lb = Label(app_window, text="ISBN")
isbn_lb.grid(row=1, column=2)
isbn_txt = StringVar()
isbn_ent = Entry(app_window, textvariable=isbn_txt)
isbn_ent.grid(row=1, column=3)

book_lst = Listbox(app_window, height=6, width=35)
book_lst.grid(row=2, column=0, rowspan=6, columnspan=2)
scrl_bar = Scrollbar(app_window)
scrl_bar.grid(row=2, column=2, rowspan=6)
book_lst.configure(yscrollcommand=scrl_bar.set)
scrl_bar.configure(command=book_lst.yview)

vw_all_btn = Button(app_window, text="View All", width=12)
vw_all_btn.grid(row=2, column=3)

srch_btn = Button(app_window, text="Search Entry", width=12)
srch_btn.grid(row=3, column=3)

add_ent_btn = Button(app_window, text="Add Entry", width=12)
add_ent_btn.grid(row=4, column=3)

updt_btn = Button(app_window, text="Update", width=12)
updt_btn.grid(row=5, column=3)

dlt_btn = Button(app_window, text="Delete", width=12)
dlt_btn.grid(row=6, column=3)

cls_btn = Button(app_window, text="Close", width=12)
cls_btn.grid(row=7, column=3)

app_window.mainloop()
