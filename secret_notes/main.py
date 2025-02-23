import tkinter
from tkinter import messagebox
import base64



def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)
def save_and_encrypt() :
    title = title_entry.get()
    message = text_entry.get("1.0",tkinter.END)
    master_key = master_key_entry.get()

    if len(title) == 0 or len(message)==0 or len(master_key)==0:
        messagebox.showwarning(title="Warning!",message="Please enter all info!")
    else:
        message_encrypted = encode(master_key,message)
        try:
            with open("mysecret.txt", "a") as data_file:
                data_file.write(f"\n{title}\n{message_encrypted}")
        except FileNotFoundError:
            with open("mysecret.txt","w") as data_file:
                data_file.write(f"\n{title}\n{message_encrypted}")
        finally:
            title_entry.delete(0,tkinter.END)
            master_key_entry.delete(0,tkinter.END)
            text_entry.delete("1.0",tkinter.END)


def decrypt():
    message_encrypted = text_entry.get("1.0",tkinter.END)
    master_key=master_key_entry.get()

    if len(message_encrypted) == 0 or len(master_key) == 0:
        messagebox.showwarning(title="Warning!", message="Please enter all info!")
    else:
        try:
            decrypted_message = decode(master_key, message_encrypted)
            text_entry.delete("1.0", tkinter.END)
            text_entry.insert(1.0, decrypted_message)
        except:
            messagebox.showerror(title="Warning!",message="Please enter encrpyted text!")






#Arayüz
FONT = {"Verdana",20,"normal"}
window = tkinter.Tk()
window.title("Secret Notes")
window.config(width=400,height=650,pady=30,padx=30)


top_secret_photo = tkinter.PhotoImage(file="topsecret1.png")
photo_label = tkinter.Label(image=top_secret_photo)
photo_label.pack()


title_info_label=tkinter.Label(text="Entry Your Title",font=FONT)
title_info_label.pack()

title_entry=tkinter.Entry(width=30)
title_entry.pack()

text_label = tkinter.Label(text="Entry Your Secret",font=FONT)
text_label.pack()

text_entry = tkinter.Text(width=50)
text_entry.pack()

master_key_label = tkinter.Label(text="Enter Master Key",font=FONT)
master_key_label.pack()

master_key_entry = tkinter.Entry(width=30)
master_key_entry.pack()

encrypt_button = tkinter.Button(text="Save & Encrypt",command=save_and_encrypt)
encrypt_button.pack()

decrypt_button = tkinter.Button(text="Decrypt",command=decrypt)
decrypt_button.pack()




tkinter.mainloop()