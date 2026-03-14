import customtkinter as ctk
import random
import pyperclip # Run 'pip install pyperclip' to make the copy button work

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue") 

def password_generator():
    # Fixed the lowercase letters in the 4th list
    list_of_lists = [
        ['!','@','#','$','%','^','&','*','(',')','-','+','=','{','}','[',']','|',':',';','<','>','.','?','/'],
        [0,1,2,3,4,5,6,7,8,9],
        ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'],
        ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    ]

    password = "".join(str(random.choice(random.choice(list_of_lists))) for _ in range(16))

    entry.delete(0, 'end')
    entry.insert(0, password)

def copy_password():
    password = entry.get()
    if password and password != "Your Password Will Appear Here":
        pyperclip.copy(password)
        # Optional: Change button text temporarily to show it worked
        copy_btn.configure(text="Copied!", fg_color="#187904")
        root.after(1500, lambda: copy_btn.configure(text="Copy", fg_color="#333333"))

root = ctk.CTk()
root.title("Password Generator")
root.geometry("500x400")

# Icon for the title bar
try:
    icon = tk.PhotoImage(file='icon.png')
    root.wm_iconphoto(False, icon)
except:
    pass # Prevents crash if icon.png is missing

center_frame = ctk.CTkFrame(root, width=400, height=300, corner_radius=20)
center_frame.place(relx=0.5, rely=0.5, anchor="center")

entry = ctk.CTkEntry(
    center_frame, 
    font=("Arial", 16), 
    width=320, 
    height=45,
    placeholder_text="Your Password Will Appear Here",
    justify='center',
    corner_radius=10,
    border_color="#555555"
)
entry.pack(pady=(40, 10), padx=20)

# Added a Copy Button
copy_btn = ctk.CTkButton(
    center_frame,
    text="Copy to Clipboard",
    command=copy_password,
    width=150,
    height=30,
    fg_color="#333333",
    hover_color="#444444",
    corner_radius=8
)
copy_btn.pack(pady=(0, 20))

button = ctk.CTkButton(
    center_frame,
    text="Generate Password",
    command=password_generator,
    font=("Arial", 15, "bold"),
    width=220,
    height=45,
    corner_radius=30,
    fg_color="#d32f2f",
    hover_color="#187904", # Nice green hover!
    text_color="white"
)
button.pack(pady=(0, 40))

root.mainloop()