'''import tkinter as tk
from tkinter import simpledialog

class GetUserNamePassword(simpledialog.Dialog):

    def body(self, master):

        tk.Label(master, text="Username:").grid(row=0)
        tk.Label(master, text="Password:").grid(row=1)

        self.e1 = tk.Entry(master)
        self.e2 = tk.Entry(master, show='*')

        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)
        return self.e1 # initial focus

    def apply(self):
        first = str(self.e1.get())
        second = str(self.e2.get())
        self.result = (first, second) # or something

root = tk.Tk()
root.withdraw()
d = GetUserNamePassword(root)
print(d.result)'''


'''import tkinter as tk
import smtplib

class EmailGUI:
    def __init__(self, master):
        self.master = master
        master.title("Email Login and SMTP Configuration")

        # Email login frame
        self.login_frame = tk.LabelFrame(master, text="Email Login")
        self.login_frame.pack(pady=10)

        self.email_label = tk.Label(self.login_frame, text="Email:")
        self.email_label.grid(row=0, column=0, padx=5, pady=5)

        self.email_entry = tk.Entry(self.login_frame)
        self.email_entry.grid(row=0, column=1, padx=5, pady=5)

        self.password_label = tk.Label(self.login_frame, text="Password:")
        self.password_label.grid(row=1, column=0, padx=5, pady=5)

        self.password_entry = tk.Entry(self.login_frame, show="*")
        self.password_entry.grid(row=1, column=1, padx=5, pady=5)

        # SMTP configuration frame
        self.smtp_frame = tk.LabelFrame(master, text="SMTP Configuration")
        self.smtp_frame.pack(pady=10)

        self.smtp_server_label = tk.Label(self.smtp_frame, text="SMTP Server:")
        self.smtp_server_label.grid(row=0, column=0, padx=5, pady=5)

        self.smtp_server_entry = tk.Entry(self.smtp_frame)
        self.smtp_server_entry.grid(row=0, column=1, padx=5, pady=5)

        self.smtp_port_label = tk.Label(self.smtp_frame, text="SMTP Port:")
        self.smtp_port_label.grid(row=1, column=0, padx=5, pady=5)

        self.smtp_port_entry = tk.Entry(self.smtp_frame)
        self.smtp_port_entry.grid(row=1, column=1, padx=5, pady=5)

        self.submit_button = tk.Button(master, text="Submit", command=self.submit)
        self.submit_button.pack(pady=10)

    def submit(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        smtp_server = self.smtp_server_entry.get()
        smtp_port = int(self.smtp_port_entry.get())

        try:
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(email, password)
            print("Login successful!")
            server.quit()
        except Exception as e:
            print(f"Error: {e}")

root = tk.Tk()
email_gui = EmailGUI(root)
root.mainloop()'''



import tkinter as tk
import smtplib
from email.mime.text import MIMEText
from PIL import ImageTk, Image


class EmailGUI:
    def __init__(self, master):
        self.master = master
        master.title("Email Login and SMTP Configuration")
       
        #inserting image
        self.bg = ImageTk.PhotoImage(file=r"C:\Users\YUVA\Downloads\gmail1.jpg")
        bg = tk.Label(self.master, image=self.bg,height=180).pack()

        #mail_image = Image.open(r"C:\Users\YUVA\Downloads\th.jpg") 
        #mail_image = mail_image.resize((30, 30), Image.ANTIALIAS)
        #self.mail_photo = ImageTk.PhotoImage(mail_image)

        # Email login frame
        self.login_frame = tk.LabelFrame(master, text="Email Login")
        self.login_frame.pack(pady=10)

        self.email_label = tk.Label(self.login_frame, text="Email:")
        self.email_label.grid(row=0, column=0, padx=5, pady=5)

        self.email_entry = tk.Entry(self.login_frame)
        self.email_entry.grid(row=0, column=1, padx=5, pady=5)

        self.password_label = tk.Label(self.login_frame, text="Password:")
        self.password_label.grid(row=1, column=0, padx=5, pady=5)

        self.password_entry = tk.Entry(self.login_frame, show="*")
        self.password_entry.grid(row=1, column=1, padx=5, pady=5)

        # SMTP configuration frame
        self.smtp_frame = tk.LabelFrame(master, text="SMTP Configuration")
        self.smtp_frame.pack(pady=10)

        self.smtp_server_label = tk.Label(self.smtp_frame, text="SMTP Server:")
        self.smtp_server_label.grid(row=0, column=0, padx=5, pady=5)

        self.smtp_server_entry = tk.Entry(self.smtp_frame)
        self.smtp_server_entry.grid(row=0, column=1, padx=5, pady=5)

        self.smtp_port_label = tk.Label(self.smtp_frame, text="SMTP Port:")
        self.smtp_port_label.grid(row=1, column=0, padx=5, pady=5)

        self.smtp_port_entry = tk.Entry(self.smtp_frame)
        self.smtp_port_entry.grid(row=1, column=1, padx=5, pady=5)

        # Send email frame
        self.send_frame = tk.LabelFrame(master, text="Send Email")
        self.send_frame.pack(pady=10)

        self.recipient_label = tk.Label(self.send_frame, text="Recipient:")
        self.recipient_label.grid(row=0, column=0, padx=5, pady=5)

        self.recipient_entry = tk.Entry(self.send_frame)
        self.recipient_entry.grid(row=0, column=1, padx=5, pady=5)

        self.subject_label = tk.Label(self.send_frame, text="Subject:")
        self.subject_label.grid(row=1, column=0, padx=5, pady=5)

        self.subject_entry = tk.Entry(self.send_frame)
        self.subject_entry.grid(row=1, column=1, padx=5, pady=5)

        self.message_label = tk.Label(self.send_frame, text="Message:")
        self.message_label.grid(row=2, column=0, padx=5, pady=5)

        self.message_text = tk.Text(self.send_frame, height=10, width=30)
        self.message_text.grid(row=2, column=1, padx=5, pady=5)

        self.send_button = tk.Button(master, text="Send Email", command=self.send_email)
        self.send_button.pack(pady=10)

    def send_email(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        smtp_server = self.smtp_server_entry.get()
        smtp_port = int(self.smtp_port_entry.get())
        recipient = self.recipient_entry.get()
        subject = self.subject_entry.get()
        message = self.message_text.get("1.0", "end-1c")

        try:
            msg = MIMEText(message)
            msg['Subject'] = subject
            msg['From'] = email
            msg['To'] = recipient

            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(email, password)
            server.send_message(msg)
            print("Email sent successfully!")
            server.quit()
        except Exception as e:
            print(f"Error: {e}")

root = tk.Tk()
email_gui = EmailGUI(root)
root.mainloop()