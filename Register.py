from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1800x1000+0+0")

        # ================ Variables =====================
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_SecurityQ = StringVar()
        self.var_SecurityA = StringVar()
        self.var_pass = StringVar()
        self.var_conpass = StringVar()
        self.var_check = IntVar()

        # ================ Background Image ===============
        bg_img = Image.open(r"C:\Users\ABC\Desktop\new project\images\m_k-photography-ZsjlxSAK6vE-unsplash.jpg")
        bg_img = bg_img.resize((1800, 1000), Image.LANCZOS)
        self.bg = ImageTk.PhotoImage(bg_img)

        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        # ================ Left Image ======================
        left_img = Image.open(r"C:\Users\ABC\Desktop\new project\images\coffee.jpg")
        left_img = left_img.resize((400, 500), Image.LANCZOS)
        self.bg1 = ImageTk.PhotoImage(left_img)

        left_lbl = Label(self.root, image=self.bg1)
        left_lbl.place(x=150, y=100, width=400, height=500)

        # ================ Frame ===========================
        frame = Frame(self.root, bg="white")
        frame.place(x=530, y=100, width=700, height=500)

        register_lbl = Label(frame, text="REGISTER HERE",
                             font=("times new roman", 20, "bold"),
                             fg="green", bg="white")
        register_lbl.place(x=20, y=20)

        # ================ Row 1 ===========================
        fname = Label(frame, text="First Name", font=("times new roman", 15, "bold"), bg="white")
        fname.place(x=50, y=100)
        self.fname_entry = ttk.Entry(frame, textvariable=self.var_fname, font=("times new roman", 15))
        self.fname_entry.place(x=50, y=130, width=250)

        l_name = Label(frame, text="Last Name", font=("times new roman", 15, "bold"), bg="white")
        l_name.place(x=370, y=100)
        self.text_lname = ttk.Entry(frame, textvariable=self.var_lname, font=("times new roman", 15))
        self.text_lname.place(x=370, y=130, width=250)

        # ================ Row 2 ===========================
        contact = Label(frame, text="Contact No", font=("times new roman", 15, "bold"), bg="white")
        contact.place(x=50, y=170)
        self.text_contact = ttk.Entry(frame, textvariable=self.var_contact, font=("times new roman", 15))
        self.text_contact.place(x=50, y=200, width=250)

        email = Label(frame, text="Email", font=("times new roman", 15, "bold"), bg="white")
        email.place(x=370, y=170)
        self.text_email = ttk.Entry(frame, textvariable=self.var_email, font=("times new roman", 15))
        self.text_email.place(x=370, y=200, width=250)

        # ================ Row 3 ===========================
        security = Label(frame, text="Select Security Question",
                         font=("times new roman", 15, "bold"),
                         bg="white")
        security.place(x=50, y=240)

        self.combo_security_q = ttk.Combobox(frame, textvariable=self.var_SecurityQ,
                                             font=("times new roman", 15), state="readonly")
        self.combo_security_q["value"] = ("Select", "Your birth place", "Your girlfriend name", "Your pet name")
        self.combo_security_q.current(0)
        self.combo_security_q.place(x=50, y=270, width=250)

        security_A = Label(frame, text="Security Answer", font=("times new roman", 15, "bold"), bg="white")
        security_A.place(x=370, y=240)
        self.text_security = ttk.Entry(frame, textvariable=self.var_SecurityA, font=("times new roman", 15))
        self.text_security.place(x=370, y=270, width=250)

        # ================ Row 4 ===========================
        password = Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="white")
        password.place(x=50, y=310)
        self.text_password = ttk.Entry(frame, textvariable=self.var_pass, font=("times new roman", 15), show="*")
        self.text_password.place(x=50, y=340, width=250)

        confirm_pswd = Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white")
        confirm_pswd.place(x=370, y=310)
        self.text_confirm = ttk.Entry(frame, textvariable=self.var_conpass, font=("times new roman", 15), show="*")
        self.text_confirm.place(x=370, y=340, width=250)

        # ================ Check Button ====================
        agree = Checkbutton(frame, variable=self.var_check,
                            text="I Agree to the Terms & Conditions",
                            font=("times new roman", 12, "bold"),
                            onvalue=1, offvalue=0, bg="white")
        agree.place(x=50, y=380)

        # ================ Register Button =================
        reg_img = Image.open(r"C:\Users\ABC\Desktop\new project\images\imag.jpg")
        reg_img = reg_img.resize((230, 60), Image.LANCZOS)
        self.photoimage = ImageTk.PhotoImage(reg_img)

        b1 = Button(frame, image=self.photoimage, command=self.register_data,
                    borderwidth=0, cursor="hand2")
        b1.place(x=10, y=420, width=300)

        # ================ Login Button ====================
        login_img = Image.open(r"C:\Users\ABC\Desktop\new project\images\sfh.jpg")
        login_img = login_img.resize((230, 60), Image.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(login_img)

        b2 = Button(frame, image=self.photoimage1, borderwidth=0, cursor="hand2")
        b2.place(x=330, y=420, width=300)

    # ================ Database Function ==================
    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_SecurityQ.get() == "Select":
            messagebox.showerror("Error", "All fields are required!")
        elif self.var_pass.get() != self.var_conpass.get():
            messagebox.showerror("Error", "Password & Confirm Password must be same!")
        elif self.var_check.get() == 0:
            messagebox.showerror("Error", "Please agree to our Terms & Conditions!")
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="python",
                    database="mydata"
                )
                my_cursor = conn.cursor()
                

                # Check Email Already Exists
              
                my_cursor.execute("SELECT * FROM regisetion WHERE email=%s", (self.var_email.get(),))
                row = my_cursor.fetchone()

                if row is not None:
                    messagebox.showerror("Error", "User already exists. Try another email!")
                else:
                    my_cursor.execute("""
                        INSERT INTO regisetion(fname, lname, contact, email, security_Q, security_A, password)
                        VALUES (%s,%s,%s,%s,%s,%s,%s)
                    """, (
                        self.var_fname.get(),
                        self.var_lname.get(),
                        self.var_contact.get(),
                        self.var_email.get(),
                        self.var_SecurityQ.get(),
                        self.var_SecurityA.get(),
                        self.var_pass.get()
                    ))

                    conn.commit()
                    messagebox.showinfo("Success", "Registered Successfully!")
                    conn.close()

            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}")


if __name__ == "__main__":
    root = Tk()
    app = Register(root)
    root.mainloop()
