# importing tkinter
import tkinter
# importing messagebox
from tkinter import messagebox


# create a class
class LoginForm:
    def __init__(self, window):
        self.window = window
        self.window.title('Login form')
        self.window.iconbitmap('images.ico')
        self.window.geometry('500x600')
        self.window.configure(bg='#2E5D76')

        frame = tkinter.Frame(bg='#2E5D76')

        # create the widgets for the login form
        login_label = tkinter.Label(frame, text="Login", bg='#2E5D76', fg="#FFFFFF", font=("Arial", 30))
        username_label = tkinter.Label(frame, text="Username", bg='#2E5D76', fg="#FFFFFF", font=("Arial", 18))
        self.username_entry = tkinter.Entry(frame, font=("Arial", 18))
        self.password_entry = tkinter.Entry(frame, show="*", font=("Arial", 18))
        password_label = tkinter.Label(frame, text="Password", bg='#2E5D76', fg="#FFFFFF", font=("Arial", 18))
        btn = tkinter.Button(frame, text="Login", background="#2E5D76", fg="#FFFFFF", font=("Arial", 18),
                             command=self.login)

        # layout the widgets using the grid layout manager
        username_label.grid(row=1, column=0)
        self.username_entry.grid(row=1, column=1, pady=20)
        password_label.grid(row=2, column=0)
        self.password_entry.grid(row=2, column=1, pady=20)
        btn.grid(row=3, column=0, columnspan=2, pady=30)
        login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)

        frame.pack()
# create the login button function

    def login(self):
        username = 'admin'
        password = 'password'
        if self.username_entry.get() == username and self.password_entry.get() == password:
            # login successful, do something here
            messagebox.showinfo(title="Login Success", message="You successfully logged in.")
        else:
            # login failed, show an error message
            messagebox.showerror(title="Error", message="Invalid login.")


window = tkinter.Tk()
login_form = LoginForm(window)
window.mainloop()
