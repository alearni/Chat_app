import tkinter as tk

def display_text():
    text = entry.get()
    entry.delete(0, tk.END)  # Clear the entry
    frame = tk.Frame(history_frame)
    frame.pack(fill=tk.X)
    label = tk.Label(frame, text=text,fg="white",bg="black",font=('Arial',15),borderwidth=0)
    label.pack(side=tk.LEFT, padx=5)

root = tk.Tk()
root.title("Entry and Button Demo")


history_frame = tk.Frame(root,bg="black",)
history_frame.pack(padx=10, pady=10, fill=tk.X)
entry = tk.Entry(root, width=20,font=('Arial',15))
entry.pack(padx=10, pady=5, fill=tk.X)

button = tk.Button(root, text="Display Text", command=display_text)
button.pack(pady=5)

root.mainloop()
