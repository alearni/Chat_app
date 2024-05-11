from customtkinter import *
from PIL import Image

app = CTk()
app.geometry("500x400")
app.title("Entry and Button Demo")
set_appearance_mode("dark")

history_frame = CTkFrame(app, bg_color="black", border_color="#0098DB")
history_frame.pack(padx=10, pady=10, fill="x")

history_frame.pack_propagate(False)
img = Image.open("send.png")



def display_text():
    text = entry.get()
    if not text:
        return
    entry.delete(0, END)
    width = max(100, min(500, len(text) * 10))
    frame = CTkFrame(history_frame, width=width, corner_radius=15)
    frame.pack(fill="x")
    # Add padding to the label
    label = CTkLabel(master=frame, text=text, fg_color="#0098DB", bg_color="#000000", font=('Arial', 15), padx=5, pady=5)
    label.pack(side="left", padx=5)


entry = CTkEntry(app, width=450, font=("Arial", 15))
entry.pack(side="left", pady=5, fill="x")

button = CTkButton(app,text="", image=CTkImage(img), command=display_text,width=20)
button.pack(side="left")

app.mainloop()
