# PyMailer

**PyMailer** is a modern, customizable desktop email sender application built with [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) for a stylish UI. It allows you to send plain text or HTML emails easily via [Mailtrap](https://mailtrap.io/) SMTP, with multi-recipient support and settings storage.

![PyMailer Screenshot](./Screenshots/homepage.png)
---

## Features

- **Modern, Responsive Interface:** Uses CustomTkinter with a dark theme and accent colors.
- **Send Emails:** Easily send to one or multiple recipients (comma-separated).
- **HTML & Plain Text Supported:** Auto-detects HTML and sends accordingly.
- **Mailtrap SMTP Integration:** Secure, reliable testing with Mailtrap's API token.
- **Save & Load Settings:** Email and Mailtrap token are stored locally.
- **Large Editable Body:** Compose and review emails comfortably.
- **Keyboard Shortcuts:** `Ctrl+A`/`Cmd+A` to select all in any field.
- **Resizable Window:** Maximize, minimize, or resize as you wish.

---

## Installation

1. **Clone this repository:**
   ```sh
   git clone https://github.com/yourusername/pymailer.git
   cd pymailer
   ```

2. **Install dependencies:**
   ```
   pip install customtkinter
   ```

3. **(Optional) Install Mailtrap:**
   - Sign up at [Mailtrap.io](https://mailtrap.io/)
   - Get your API token from your Inbox's SMTP settings.

---

## Usage

1. **Run the application:**
   ```
   python main.py
   ```

2. **Settings:**
   - Go to the "Settings" tab.
   - Enter your sender email and Mailtrap API token.
   - Click "Save Settings".

3. **Send Email:**
   - Go to the "Home" tab.
   - Enter recipient emails (comma-separated for multiple).
   - Enter subject and body (supports HTML).
   - Click "Send Email".

---

## Notes

- **Mailtrap only delivers to its sandbox inboxes by default.** Use for testing, not for actual delivery.
- The app auto-detects HTML content. Paste HTML or plain text; your recipient will see the styled result.
- Your settings (sender email & token) are saved to `settings.ini` in the app directory.

---

## Screenshot
![PyMailer Screenshot](./Screenshots/homepage.png)
![PyMailer Settings](./Screenshots/settingspage.png)
---

## License

MIT License - see [LICENSE](LICENSE) for details.

---

## Credits

- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)
- [Mailtrap](https://mailtrap.io/)

---
