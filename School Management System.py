# import modules

from tkinter import *
import os


# Designing window for registration

def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(register_screen, text="Please enter details below", bg="cyan",font=("Arial", 13)).pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="black",fg="white", command=register_user).pack()


# Designing window for login

def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("358x250")
    Label(login_screen, text="Please enter details below to login",bg="cyan",height="2",font=("Arial", 13)).pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command=login_verify, bg="black", fg="white").pack()


# Implementing event on register button

def register_user():
    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()


# Implementing event on login button

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            menu_page()

        else:
            password_not_recognised()

    else:
        user_not_found()


def teadetail():
    print("Name ", tn.get())
    print("Specialization ", spec.get())
    print("Salary ", sal.get())
    print("Grade ", gr.get())
    print("Subject Assigned", subas.get())


def teacher():
    global tc
    global tn
    tn = StringVar()
    global spec
    spec = StringVar()
    global sal
    sal = StringVar()
    global gr
    gr = StringVar()
    global subas
    subas= StringVar()

    tc = Toplevel(login_success_screen)
    tc.title("Teacher Module")
    tc.geometry("250x320")
    Label(tc, text="Welcome to the Teacher page", bg="cyan", font=("Arial", 13)).pack()
    Label(tc, text="Name:", bg="black", fg="white", font=("Arial", 13)).pack()
    t1 = Entry(tc, textvariable=tn, borderwidth=5).pack()
    Label(tc, text="Specialization", bg="black", fg="white", font=("Arial", 13)).pack()
    t2 = Entry(tc, textvariable=spec, borderwidth=5).pack()
    Label(tc, text="Salary:", bg="black", fg="white", font=("Arial", 13)).pack()
    t3 = Entry(tc, textvariable=sal, borderwidth=5).pack()
    Label(tc, text="Grade:", bg="black", fg="white", font=("Arial", 13)).pack()
    t4 = Entry(tc, textvariable=gr, borderwidth=5).pack()
    Label(tc, text="Subject Assigned:", bg="black", fg="white", font=("Arial", 13)).pack()
    t5 = Entry(tc, textvariable=subas, borderwidth=5).pack()

    Button(tc, text="Submit", bg="black", fg="white", command=teadetail).pack()



def studetail():
    print("Name ", sn.get())
    print(" FatherName ", fn.get())
    print("Age ", age.get())
    print("Gender ", g.get())
    print("Previous class ", pc.get())
    print("Present class ", prc.get())
    print("Address ", add.get())
    print("Contact ", c.get())
    print("father Contact ", fc.get())
    print("Previous Grade ", pg.get())


def student():
    global sc

    global sn
    sn=StringVar()
    global fn
    fn = StringVar()
    global age
    age = StringVar()
    global g
    g = StringVar()
    global pc
    pc = StringVar()
    global prc
    prc = StringVar()
    global add
    add = StringVar()
    global c
    c = StringVar()
    global fc
    fc = StringVar()
    global pg
    pg = StringVar()
    global E1
    global E2
    global E3
    global E4
    global E5
    global E6
    global E7
    global E8
    global E9
    global E10

    sc = Toplevel(login_success_screen)
    sc.title("STUDENT PAGE")
    sc.geometry("300x600")
    Label(sc, text="Welcome to The Student Page", bg="cyan", font=("Arial", 13)).pack()
    Label(sc, text="").pack()
    Label(sc, text="Name:", bg="black", fg="white", font=("Arial", 13)).pack()
    E1 = Entry(sc,textvariable=sn, borderwidth=5 ).pack()
    Label(sc, text=" Father Name:", bg="black", fg="white", font=("Arial", 13)).pack()
    E2 = Entry(sc, textvariable=fn, borderwidth=5 ).pack()
    Label(sc, text="Age:", bg="black", fg="white", font=("Arial", 13)).pack()
    E3 = Entry(sc, textvariable=age, borderwidth=5 ).pack()
    Label(sc, text="Gender:", bg="black", fg="white", font=("Arial", 13)).pack()
    E4 = Entry(sc, textvariable=g, borderwidth=5 ).pack()
    Label(sc, text="Previous Class:", bg="black", fg="white", font=("Arial", 13)).pack()
    E5 = Entry(sc, textvariable=pc, borderwidth=5 ).pack()
    Label(sc, text="Present Class:", bg="black", fg="white", font=("Arial", 13)).pack()
    E6 = Entry(sc, textvariable=prc, borderwidth=5 ).pack()
    Label(sc, text="Address:", bg="black", fg="white", font=("Arial", 13)).pack()
    E7 = Entry(sc, textvariable=add, borderwidth=5 ).pack()
    Label(sc, text="Contact:", bg="black", fg="white", font=("Arial", 13)).pack()
    E8 = Entry(sc, textvariable=c, borderwidth=5 ).pack()
    Label(sc, text="Father Contact:", bg="black", fg="white", font=("Arial", 13)).pack()
    E9 = Entry(sc, textvariable=fc, borderwidth=5 ).pack()
    Label(sc, text="previous Grade:", bg="black", fg="white", font=("Arial", 13)).pack()
    E10 = Entry(sc, textvariable=pg, borderwidth=5 ).pack()


    Button(sc, text="Submit", bg="black", fg="white",command=studetail).pack()





# Designing popup for Menu Page
def menu_page():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("School management")
    login_success_screen.geometry("250x150")
    Label(login_success_screen, text="Welcome to the Menu Page",bg="cyan",font=("Arial", 13)).pack()
    Label(login_success_screen, text="").pack()
    Button(login_success_screen, text="TEACHER MODULE",bg="black", fg="white", command=teacher).pack()
    Label(login_success_screen, text="").pack()
    Button(login_success_screen, text="STUDENT MODULE",bg="black", fg="white", command=student).pack()




# Designing popup for login invalid password

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()


# Designing popup for user not found

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()


# Deleting popups

def delete_login_success():
    login_success_screen.destroy()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()


# Designing Main(first) window

def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Account Login")
    Label(text="Select Your Choice", bg="Cyan", width="300", height="2", font=("Arial", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command=login, bg="black", fg="white").pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register, bg="black", fg="white").pack()

    main_screen.mainloop()


main_account_screen()
