from connectdll import *
from getdll import *
def client_main():
    reg_window.destroy()
    client_window = tk.Tk()
    client_window.geometry('1024x512')
    client_window['background'] = '#1E90FF'
    client_window.title('客户端')
    come_mysql = tk.Button(client_window,text='连接数据库',bg='yellow',command=connect_mysql_server)
    come_mysql.grid(row=3, column=0, sticky="w", padx=10, pady=5)
    client_window.mainloop()
    return ()
if __name__ == '__main__':
    client_main()