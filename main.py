import tkinter as tk
from tkinter import messagebox
from tkinter import Scrollbar
import brain

WHITE = '#F0EEED'
BLACK = '#332C39'
RED = '#C92C6D'

pass_handel = brain.SavePass()


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def genpass():
    pass_entry.delete(0,tk.END)
    pass_entry.clipboard_clear()
    if user_pass_option.get() == "complex":
        generated_password = pass_handel.generate_pass_complex()
        pass_entry.clipboard_append(generated_password)
        pass_entry.insert(0,generated_password)
    elif user_pass_option.get() == 'numbers':
        generated_password = pass_handel.generate_pass_numbers()
        pass_entry.clipboard_append(generated_password)
        pass_entry.insert(0,generated_password)
    elif user_pass_option.get() == 'letters':
        generated_password = pass_handel.generate_pass_letters()
        pass_entry.clipboard_append(generated_password)
        pass_entry.insert(0,generated_password)
    else:
        messagebox.showerror(title='Hey!',message='please set an option for you password :)')



# ---------------------------- SAVE PASSWORD ------------------------------- #




def add_pass():
    web = web_entry.get()
    user = user_entry.get()
    pasw = pass_entry.get()

    if len(web) > 1 and len(pasw) > 1:
        is_ok = messagebox.askokcancel(title=web,message=f"these are details you enter:\nweb: {web} \nemial: {user} \npassword: {pasw} \nis it ok to save?")
        if is_ok:
            pass_handel.savepassword(web,user,pasw)
            web_entry.delete(0,tk.END)
            pass_entry.delete(0,tk.END)
            web_entry.focus()
            
    else:
        messagebox.showerror(title='Error',message='web/email-username/password is empty please try again')

def show_passwords():
    pass_text = pass_handel.readpassword()

    saved_pass_window = tk.Toplevel()
    saved_pass_window.resizable(False,False)

    

    saved_pass_window_text = tk.Text(saved_pass_window,bg=WHITE,fg=BLACK)
    saved_pass_window_text.insert(tk.END,pass_text)
    saved_pass_window_text.config(state=tk.DISABLED)
    saved_pass_window_text.grid(column=0,row=0,sticky=tk.EW)

    text_scrollbar= Scrollbar(saved_pass_window,orient='vertical',command=saved_pass_window_text.yview,width=15,relief='flat')
    text_scrollbar.grid(column=1,row=0,sticky=tk.NS)

    saved_pass_window_text.config(xscrollcommand=text_scrollbar.set)

def show_emailadress_entry():
    latest_email = pass_handel.get_last_email()

    if latest_email == False:
        user_entry.insert(0,'dummy@example.com')
    else:
        user_entry.insert(0,latest_email)
        
# ---------------------------- UI SETUP ------------------------------- #

#window

window = tk.Tk()
window.resizable(False,False)
window.title('Passminator')


window.config(bg=WHITE,padx=50,pady=50)

#variables
passgen_options = ['complex','numbers','letters']
user_pass_option = tk.StringVar()
user_pass_option.set('Options')



#canvas

image = tk.PhotoImage(file='logo2.png')
canvas = tk.Canvas(window,bg=WHITE,highlightthickness=0,height=210,width=210)
canvas.create_image(104,105,image=image)
canvas.grid(column=1,row=0,padx=(80,0))

#label
web_label = tk.Label(text='Website:',foreground=BLACK,background=WHITE)
web_label.grid(column=0,row=1)

user_label = tk.Label(text='Email/username:',foreground=BLACK,background=WHITE)
user_label.grid(column=0,row=2)

pass_label = tk.Label(text='Password:',foreground=BLACK,background=WHITE)
pass_label.grid(column=0,row=3)


#Entry

web_entry = tk.Entry(width=35)
web_entry.focus()
web_entry.grid(column=1,row=1,columnspan=2)

user_entry = tk.Entry(width=35)
#user_entry.insert(0,'dummy@example.com')
user_entry.grid(column=1,row=2,columnspan=2)
show_emailadress_entry()

pass_entry = tk.Entry(width=18)
pass_entry.grid(column=1,row=3,padx=(44,0))


#Button

genpas_button = tk.Button(text='Generate Password',width=18,fg=RED,command=genpass)
genpas_button.grid(column=2,row=4,padx=(0,20))

add_button = tk.Button(text='Add',fg=RED,width=16,command=add_pass)
add_button.grid(column=1,row=4,columnspan=1,padx=(40,0))

show_pass_button = tk.Button(text='show saved passwords',width=36,fg=RED,command=show_passwords)
show_pass_button.grid(column=1,row=5,columnspan=2)

#optionmenu

options = tk.OptionMenu(window,user_pass_option,*passgen_options)
options.config(fg=RED)
options.grid(column=2,row=3,padx=(0,100))



window.mainloop()
