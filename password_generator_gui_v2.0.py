import tkinter as tk
import tkinter.ttk as ttk
from variables import *
import secrets
import string
import copypaste


class MainWindow(tk.Tk):

    def __init__(self, *arg, **kwargs):
        tk.Tk.__init__(self, *arg, **kwargs)

        tk.Tk.title(self, "Password generator")
        width = 400
        height = 300
        w = self.winfo_screenwidth() // 2
        h = self.winfo_screenheight() // 2

        # tk.Tk.wm_iconbitmap(self, default='D:\YandexDisk\password_generator_gui\icon.ico')
        tk.Tk.geometry(self, f"{width}x{height}+{w - width // 2}+{h - height // 2}")
        tk.Tk.resizable(self, False, False)

        self.stl = ttk.Style()
        self.init_widget()

    def init_widget(self):
        self.stl.configure('OutputWindow.TFrame', background=WHITE)
        main_frame = ttk.Frame(self, style='OutputWindow.TFrame')
        main_frame.pack(expand=True, fill=tk.BOTH)

        self.stl.configure('OutputText.TLabel', background=WHITE, font=20, foreground=RED)
        self.label_output = ttk.Label(main_frame, text="Press Generate", style='OutputText.TLabel')
        self.label_output.pack(expand=True)

        second_frame = ttk.Frame(self)
        second_frame.pack(anchor=tk.W)

        """Display password length"""
        rb_frame = ttk.Labelframe(second_frame, text="Length")
        rb_frame.pack(padx=X, pady=Y, side=tk.LEFT)
        self.rb_length = tk.IntVar()
        self.rb_length.set(12)
        self.name_rb_list = ["4", "6", "12", "24"]
        self.radiobutton_lenght_list = []
        i = 0
        for rb_num in range(4):
            rb = ttk.Radiobutton(rb_frame, text=self.name_rb_list[i], variable=self.rb_length,
                                 value=self.name_rb_list[int(i)])
            rb.pack(side=tk.TOP, padx=X, pady=Y // 3, anchor=tk.W)
            i += 1
            self.radiobutton_lenght_list.append(rb)

        """Display types password"""
        rb_frame_2 = ttk.Labelframe(second_frame, text="Type")
        rb_frame_2.pack(side=tk.LEFT)
        self.rb_type = tk.StringVar()
        self.charset_variation_list = [string.digits,
                                       string.ascii_letters,
                                       string.digits + string.ascii_letters,
                                       string.digits + string.ascii_letters + string.punctuation]
        self.name_rb_type_list = ["numbers", "letters", "numbers + letters", "numbers + letters + punctuation"]
        self.rb_type.set(self.charset_variation_list[3])
        self.radiobutton_type_list = []
        j = 0
        for rb_type in range(4):
            rb = ttk.Radiobutton(rb_frame_2,
                                 text=self.name_rb_type_list[j],
                                 variable=self.rb_type,
                                 value=self.charset_variation_list[j])
            rb.pack(side=tk.TOP, padx=X, pady=Y // 3, anchor=tk.W)
            j += 1
            self.radiobutton_type_list.append(rb)

        """Display buttons"""
        buttons_frame = ttk.Frame(second_frame)
        buttons_frame.pack(padx=X, pady=Y)

        name_buttons = ["Generate", "Copy"]
        buttons_command = [lambda: self.generate_password(self.rb_length.get(), self.rb_type.get()),
                           lambda: self.copy_function(self.label_output['text'])]
        self.button_list = []
        k = 0
        for btn in range(2):
            self.stl.configure('ButtonGenerate.TButton', relief='flat', width=30)
            btn = ttk.Button(buttons_frame,
                             text=name_buttons[k],
                             style='ButtonGenerate.TButton',
                             command=buttons_command[k])
            btn.pack(pady=Y // 3, anchor=tk.S)
            k += 1
            self.button_list.append(btn)

        """Status bar"""
        self.status_bar_text_list = ["Press Generate..",
                                     "Password generated! Press Copy..",
                                     "Password copied to clipboard"]
        self.stl.configure('StatusBar.TLabel', foreground=GRAY)
        self.label_status_bar = ttk.Label(self,
                                          text=self.status_bar_text_list[0],
                                          relief=tk.GROOVE,
                                          anchor=tk.CENTER,
                                          style='StatusBar.TLabel')
        self.label_status_bar.pack(fill=tk.X)

    def generate_password(self, length, types):
        self.label_output.configure(text=''.join(secrets.choice(types) for i in range(length)))
        self.label_status_bar.configure(text=self.status_bar_text_list[1])

    def copy_function(self, text_password):
        copypaste.copy(text_password)
        self.label_status_bar.configure(text=self.status_bar_text_list[2])


if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()
