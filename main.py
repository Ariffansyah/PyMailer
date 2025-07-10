import configparser
import re
import smtplib
from email.mime.text import MIMEText

import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

status_label = None

def show_status(tab, text, color):
    global status_label
    if status_label is not None:
        status_label.destroy()
        status_label = None
    status_label = ctk.CTkLabel(
        tab, text=text, text_color=color, font=ctk.CTkFont(size=14, weight="bold")
    )
    status_label.pack(pady=(10, 5), padx=10)

def is_html(body):
    if re.search(r"<[^>]+>", body):
        return True
    return False

def send_email(sender_email, mailtrap_token, recipient_email, subject, body):
    if not sender_email or not mailtrap_token or not recipient_email:
        show_status(home_tab, "Please fill in all fields.", "red")
        return
    try:
        smtp_server = "live.smtp.mailtrap.io"
        smtp_port = 587
        smtp_user = "api"
        smtp_password = mailtrap_token

        subtype = "html" if is_html(body) else "plain"

        msg = MIMEText(body, subtype)
        msg["From"] = sender_email
        msg["To"] = ", ".join(recipient_email)
        msg["Subject"] = subject

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_user, smtp_password)
            server.sendmail(sender_email, recipient_email, msg.as_string())

        show_status(home_tab, "Email sent successfully!", "green")
    except Exception as e:
        show_status(home_tab, f"Failed to send email: {e}", "red")

def save_settings(sender_email, mailtrap_token):
    config = configparser.ConfigParser()
    config["Settings"] = {
        "sender_email": sender_email,
        "mailtrap_token": mailtrap_token,
    }
    with open("settings.ini", "w") as configfile:
        config.write(configfile)
    show_status(settings_tab, "Settings saved successfully!", "green")

def load_settings():
    config = configparser.ConfigParser()
    config.read("settings.ini")
    if "Settings" in config:
        sender_email = config["Settings"].get("sender_email", "")
        mailtrap_token = config["Settings"].get("mailtrap_token", "")
        return sender_email, mailtrap_token
    return "", ""

def center_window(win, width, height):
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x = int((screen_width / 2) - (width / 2))
    y = int((screen_height / 2) - (height / 2))
    win.geometry(f"{width}x{height}+{x}+{y}")

def select_all(event):
    widget = event.widget
    try:
        widget.tag_add("sel", "1.0", "end")
        return "break"
    except Exception:
        try:
            widget.select_range(0, 'end')
            widget.icursor('end')
            return "break"
        except Exception:
            return

app = ctk.CTk()
app.title("PyMailer — Mailtrap Email Sender")
window_width = 1024
window_height = 768
center_window(app, window_width, window_height)
app.resizable(True, True)

tabview = ctk.CTkTabview(app)
tabview.pack(pady=30, padx=30, fill="both", expand=True)
tabview.add("Home")
tabview.add("Settings")

home_tab = tabview.tab("Home")
settings_tab = tabview.tab("Settings")

# ======== Settings Tab Layout ========
settings_frame = ctk.CTkFrame(settings_tab, fg_color="#181F2A", corner_radius=18)
settings_frame.pack(pady=30, padx=60, fill="both", expand=True)

ctk.CTkLabel(
    settings_frame, text="Settings", font=ctk.CTkFont(size=28, weight="bold"), text_color="#4CFFB3"
).pack(pady=(30, 18))

sender_email_label = ctk.CTkLabel(
    settings_frame, text="Sender Email:", anchor="w", font=ctk.CTkFont(size=17, weight="bold"), text_color="#9ED9C7"
)
sender_email_label.pack(pady=(12, 2), padx=10, anchor="w")
sender_email_entry = ctk.CTkEntry(settings_frame, width=400, font=ctk.CTkFont(size=16))
sender_email_entry.pack(pady=(0, 18), padx=10)

mailtrap_token_label = ctk.CTkLabel(
    settings_frame, text="Mailtrap Token:", anchor="w", font=ctk.CTkFont(size=17, weight="bold"), text_color="#9ED9C7"
)
mailtrap_token_label.pack(pady=(12, 2), padx=10, anchor="w")
mailtrap_token_entry = ctk.CTkEntry(settings_frame, width=400, show="*", font=ctk.CTkFont(size=16))
mailtrap_token_entry.pack(pady=(0, 18), padx=10)

sender_email, mailtrap_token = load_settings()
if sender_email or mailtrap_token:
    show_status(settings_frame, "Settings loaded from file.", "#aaaaaa")
    sender_email_entry.insert(0, sender_email)
    mailtrap_token_entry.insert(0, mailtrap_token)
else:
    show_status(
        settings_frame, "No settings found. Please enter your details.", "#aaaaaa"
    )

save_button = ctk.CTkButton(
    settings_frame,
    text="💾 Save Settings",
    fg_color="#20B486",
    hover_color="#19A174",
    font=ctk.CTkFont(size=18, weight="bold"),
    corner_radius=10,
    width=180,
    height=45,
    command=lambda: save_settings(sender_email_entry.get(), mailtrap_token_entry.get()),
)
save_button.pack(pady=(30, 10), padx=10)

# ======== Home Tab Layout ========
home_frame = ctk.CTkFrame(home_tab, fg_color="#181F2A", corner_radius=18)
home_frame.pack(pady=30, padx=60, fill="both", expand=True)

ctk.CTkLabel(
    home_frame, text="Send Email", font=ctk.CTkFont(size=28, weight="bold"), text_color="#4CFFB3"
).pack(pady=(30, 18))

recipient_email_label = ctk.CTkLabel(
    home_frame,
    text="Recipient Email(s) (comma separated):",
    anchor="w",
    font=ctk.CTkFont(size=17, weight="bold"),
    text_color="#9ED9C7"
)
recipient_email_label.pack(pady=(12, 2), padx=10, anchor="w")
recipient_email_entry = ctk.CTkEntry(home_frame, width=700, font=ctk.CTkFont(size=16))
recipient_email_entry.pack(pady=(0, 18), padx=10)

subject_label = ctk.CTkLabel(
    home_frame, text="Subject:", anchor="w", font=ctk.CTkFont(size=17, weight="bold"), text_color="#9ED9C7"
)
subject_label.pack(pady=(12, 2), padx=10, anchor="w")
subject_entry = ctk.CTkEntry(home_frame, width=700, font=ctk.CTkFont(size=16))
subject_entry.pack(pady=(0, 18), padx=10)

body_label = ctk.CTkLabel(
    home_frame, text="Body:", anchor="w", font=ctk.CTkFont(size=17, weight="bold"), text_color="#9ED9C7"
)
body_label.pack(pady=(12, 2), padx=10, anchor="w")
body_textbox = ctk.CTkTextbox(home_frame, width=900, height=200, font=ctk.CTkFont(size=15))
body_textbox.pack(pady=(0, 25), padx=10, fill="both", expand=True)

body_textbox.bind("<Control-a>", select_all)
body_textbox.bind("<Command-a>", select_all) # for mac
recipient_email_entry.bind("<Control-a>", select_all)
recipient_email_entry.bind("<Command-a>", select_all)
subject_entry.bind("<Control-a>", select_all)
subject_entry.bind("<Command-a>", select_all)
sender_email_entry.bind("<Control-a>", select_all)
sender_email_entry.bind("<Command-a>", select_all)
mailtrap_token_entry.bind("<Control-a>", select_all)
mailtrap_token_entry.bind("<Command-a>", select_all)

send_button = ctk.CTkButton(
    home_frame,
    text="📧 Send Email",
    fg_color="#20B486",
    hover_color="#19A174",
    font=ctk.CTkFont(size=18, weight="bold"),
    corner_radius=10,
    width=200,
    height=50,
    command=lambda: send_email(
        sender_email_entry.get(),
        mailtrap_token_entry.get(),
        [
            email.strip()
            for email in recipient_email_entry.get().split(",")
            if email.strip()
        ],
        subject_entry.get(),
        body_textbox.get("1.0", "end-1c"),
    ),
)
send_button.pack(pady=(18, 18), padx=10, side="bottom")

app.mainloop()
