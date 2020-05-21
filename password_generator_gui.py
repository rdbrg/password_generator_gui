import string
import secrets
from tkinter import *
from copypaste import copy


def temp2(word, length_pass):
    if 4 <= length_pass <= 24:
        password = ''.join(secrets.choice(word) for i in range(length_pass))
        label_show_password['text'] = password
    else:
        label_show_password['text'] = 'Out of range (4 - 24)'


def temp(easy_hard_let_num, length_pass, tree):
    if easy_hard_let_num == 'easy':
        word = string.ascii_letters * 100 + string.digits * 100
        temp2(word, length_pass)
    elif easy_hard_let_num == 'hard':
        word = string.ascii_letters * 10 + string.digits * 10 + string.punctuation * 10
        temp2(word, length_pass)
    elif easy_hard_let_num == 'letters':
        word = string.ascii_letters * 10
        temp2(word, length_pass)
    elif easy_hard_let_num == 'numbers':
        word = string.digits * 10
        temp2(word, length_pass)


def getNewPassword():
    if radio_num_var.get() == 4 and (
            radio_easy_hard_let_num.get() == 'easy' or radio_easy_hard_let_num.get() == 'hard' or radio_easy_hard_let_num.get() == 'letters' or radio_easy_hard_let_num.get() == 'numbers'):
        temp(radio_easy_hard_let_num.get(), 4, None)
    elif radio_num_var.get() == 6 and (
            radio_easy_hard_let_num.get() == 'easy' or radio_easy_hard_let_num.get() == 'hard' or radio_easy_hard_let_num.get() == 'letters' or radio_easy_hard_let_num.get() == 'numbers'):
        temp(radio_easy_hard_let_num.get(), 6, None)
    elif radio_num_var.get() == 12 and (
            radio_easy_hard_let_num.get() == 'easy' or radio_easy_hard_let_num.get() == 'hard' or radio_easy_hard_let_num.get() == 'letters' or radio_easy_hard_let_num.get() == 'numbers'):
        temp(radio_easy_hard_let_num.get(), 12, None)
    elif radio_num_var.get() == 24 and (
            radio_easy_hard_let_num.get() == 'easy' or radio_easy_hard_let_num.get() == 'hard' or radio_easy_hard_let_num.get() == 'letters' or radio_easy_hard_let_num.get() == 'numbers'):
        temp(radio_easy_hard_let_num.get(), 24, None)
    elif radio_num_var.get() == 424 and (
            radio_easy_hard_let_num.get() == 'easy' or radio_easy_hard_let_num.get() == 'hard' or radio_easy_hard_let_num.get() == 'letters' or radio_easy_hard_let_num.get() == 'numbers'):
        try:
            temp(radio_easy_hard_let_num.get(), int(entry_num.get()), int(entry_num.get()))
        except:
            if entry_num.get() == '' or entry_num.get() == ' ' or entry_num.get() == '  ' or entry_num.get() == '   ':
                label_show_password['text'] = 'Enter numbers (4 - 24)'
            else:
                label_show_password['text'] = 'Enter only numbers'


check_var = False
paste_password = 'Press create password..'


def copyToClickboard():
    copy(label_show_password['text'])
    global paste_password
    paste_password = label_show_password['text']


def status1(event):
    if paste_password == 'Press create password..':
        copy_var = 'Press copy..'
        global check_var
        check_var = True
        status_bar['text'] = copy_var
    else:
        copy_var = 'Press copy..'
        status_bar['text'] = copy_var
        check_var = True


def status2(event):
    if check_var is True:
        if paste_password == 'Press create password..':
            copys_var = 'Password copied to clipboard..'
            status_bar['text'] = copys_var
        else:
            copys_var = 'Password copied to clipboard..'
            status_bar['text'] = copys_var
    else:
        status_bar['text'] = 'First create a password..'


root = Tk()
root.title('Passwords generator')
root.geometry('+500+300')
root.resizable(False, False)

label_show_password = Label(width=29, font=('Arial', 12))
btn_show_password = Button(text='Create password', height=2, command=getNewPassword)
btn_show_password.bind('<Button-1>', status1)
btn_copy_password = Button(text='Copy', width=8, command=copyToClickboard)
btn_copy_password.bind('<Button-1>', status2)
label_show_password.grid(row=0, column=0, columnspan=3, sticky=W, pady=5, padx=5)
btn_show_password.grid(row=1, columnspan=2, rowspan=2, sticky=W, pady=5, padx=10)
btn_copy_password.grid(row=0, column=3, columnspan=2, pady=5, padx=20)

radio_easy_hard_let_num = StringVar()
radio_easy_hard_let_num.set('letters')
radiobutton_easy = Radiobutton(text='letters + numbers', variable=radio_easy_hard_let_num, value='easy')
radiobutton_hard = Radiobutton(text='letters + numbers + punctuation', variable=radio_easy_hard_let_num, value='hard')
radiobutton_only_letters = Radiobutton(text='only letters', variable=radio_easy_hard_let_num, value='letters')
radiobutton_only_numbers = Radiobutton(text='only numbers', variable=radio_easy_hard_let_num, value='numbers')
radiobutton_easy.grid(row=3, column=2, sticky=W, padx=5)
radiobutton_hard.grid(row=4, column=2, sticky=W, padx=5)
radiobutton_only_letters.grid(row=1, column=2, sticky=W, padx=5)
radiobutton_only_numbers.grid(row=2, column=2, sticky=W, padx=5)

radio_num_var = IntVar()
radio_num_var.set(4)
radiobutton_4 = Radiobutton(text='4-num', variable=radio_num_var, value=4)
radiobutton_6 = Radiobutton(text='6-num', variable=radio_num_var, value=6)
radiobutton_12 = Radiobutton(text='12-num', variable=radio_num_var, value=12)
radiobutton_24 = Radiobutton(text='24-num', variable=radio_num_var, value=24)
radiobutton_you_num = Radiobutton(variable=radio_num_var, value=424)
entry_num = Entry(width=6)

radiobutton_4.grid(row=1, column=3, columnspan=3, sticky=W, padx=20)
radiobutton_6.grid(row=2, column=3, columnspan=2, sticky=W, padx=20)
radiobutton_12.grid(row=3, column=3, columnspan=2, sticky=W, padx=20)
radiobutton_24.grid(row=4, column=3, columnspan=2, sticky=W, padx=20)
radiobutton_you_num.grid(row=5, column=3, sticky=E)
entry_num.grid(row=5, column=4, sticky=W)

status_bar = Label(text=paste_password, fg='gray')
status_bar.grid(row=5, column=0, columnspan=3, sticky=W, padx=10)

root.mainloop()
