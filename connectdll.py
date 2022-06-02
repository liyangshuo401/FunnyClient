from getdll import *
from tkinter import messagebox
import pymysql
def connect_mysql_server():
    try:
        come_server = pymysql.connect(
            host=(get_input3.get()),
            port=get_input4.get(),
            user=str(get_input1.get()),
            passwd=str(get_input2.get()),
            db=str(get_input5.get()),
            charset=str(get_input6.get())
            )
    except:
        messagebox.showerror('Error','Can not connect to MySQL server.')
    return ()