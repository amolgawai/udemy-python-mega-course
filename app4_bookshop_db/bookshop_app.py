""" The Booshop desktop application
    Allows user to create, view, update and delete book entries
    The book entry consists of
      - Name, Author, Year of Publication and ISBN
"""

from tkinter import *
import bookshop_db

bookshop_db.create_book_db_table()
app_window = Tk()
app_window.wm_title("Book Shop")

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

def row_selected():
    """ Function bound to Listbox row selection event

    Returns
    -------
    tuple : selected row

    """
    cur_sel = book_lst.curselection()
    if not cur_sel:
        return
    index = book_lst.curselection()[0]
    seleced_row = book_lst.get(index)
    return seleced_row


def on_row_selected(event):
    """ Callback for row selection

    Parameters
    ---------
    event: The event object

    """
    selection = row_selected()
    if not selection:
        return
    title_ent.delete(0, END)
    title_ent.insert(END, selection[1])
    author_ent.delete(0, END)
    author_ent.insert(END, selection[2])
    year_ent.delete(0, END)
    year_ent.insert(END, selection[3])
    isbn_ent.delete(0, END)
    isbn_ent.insert(END, selection[4])


book_lst = Listbox(app_window, height=6, width=35)
book_lst.grid(row=2, column=0, rowspan=6, columnspan=2)
book_lst.bind('<<ListboxSelect>>', on_row_selected)
scrl_bar = Scrollbar(app_window)
scrl_bar.grid(row=2, column=2, rowspan=6)
book_lst.configure(yscrollcommand=scrl_bar.set)
scrl_bar.configure(command=book_lst.yview)

def cmd_view():
    """ The command for View All button """
    book_lst.delete(0, END)
    for row in bookshop_db.get_db_rows():
        book_lst.insert(END, row)



vw_all_btn = Button(app_window, text="View All", width=12, command=cmd_view)
vw_all_btn.grid(row=2, column=3)

def cmd_search():
    """ Searches for author """
    book_lst.delete(0, END)
    for row in bookshop_db.search_book(title_txt.get(),
                                       author_txt.get(),
                                       year_txt.get(),
                                       isbn_txt.get()):
        book_lst.insert(END, row)


srch_btn = Button(app_window, text="Search Entry", width=12, command=cmd_search)
srch_btn.grid(row=3, column=3)

def cmd_add():
    """ Adds entry to database """
    bookshop_db.insert_book(title_txt.get(),
                            author_txt.get(),
                            year_txt.get(),
                            isbn_txt.get())
    cmd_search()


add_ent_btn = Button(app_window, text="Add Entry", width=12, command=cmd_add)
add_ent_btn.grid(row=4, column=3)

def cmd_update():
    """ Udate command callback """
    selection = row_selected()
    bookshop_db.update_db_entry(selection[0],
                                title_txt.get(),
                                author_txt.get(),
                                year_txt.get(),
                                isbn_txt.get())
    cmd_search()


updt_btn = Button(app_window, text="Update", width=12, command=cmd_update)
updt_btn.grid(row=5, column=3)

def cmd_delete():
    """ Deletes the selected item """
    bookshop_db.delete_db_entry(row_selected()[0])
    cmd_view()



dlt_btn = Button(app_window, text="Delete", width=12, command=cmd_delete)
dlt_btn.grid(row=6, column=3)

cls_btn = Button(app_window, text="Close", width=12, command=app_window.destroy)
cls_btn.grid(row=7, column=3)

app_window.mainloop()
