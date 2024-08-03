from tkinter import *
from tkinter import messagebox
import tkinter as tk

# Initialize window
root = Tk()
root.geometry('700x650')
root.config(bg='#d3f3f5')
root.title('Python Contact Book')
root.resizable(0, 0)

contactlist = [
    ['Siddharth Nigam', '369854712', 'siddharth@example.com'],
    ['Gaurav Bansal', '521155222', 'gaurav@example.com'],
    ['Abhishek Nikam', '78945614', 'abhishek@example.com'],
    ['Sashi Raghuvanshi', '58745246', 'sashi@example.com'],
    ['Mohit Paul', '5846975', 'mohit@example.com'],
    ['Karan Patel', '5647892', 'karan@example.com'],
    ['Rahul Sharma', '89685320', 'rahul@example.com'],
    ['Sumit Mishra', '98564785', 'sumit@example.com'],
    ['Tarun Parmar', '85967412', 'tarun@example.com']
]

Name = StringVar()
Number = StringVar()
Email = StringVar()
Search = StringVar()

# Create frame
frame = Frame(root)
frame.pack(side=RIGHT)

scroll = Scrollbar(frame, orient=VERTICAL)
select = Listbox(frame, yscrollcommand=scroll.set, font=('Times New Roman', 16), bg="#f0fffc", width=20, height=20, borderwidth=3, relief="groove")
scroll.config(command=select.yview)
scroll.pack(side=RIGHT, fill=Y)
select.pack(side=LEFT, fill=BOTH, expand=1)

# Function to get selected value
def Selected():
    if len(select.curselection()) == 0:
        messagebox.showerror("Error", "Please Select the Name")
        return None
    return int(select.curselection()[0])

# Function to add new contact
def AddContact():
    if Name.get() and Number.get() and Email.get():
        contactlist.append([Name.get(), Number.get(), Email.get()])
        Select_set()
        EntryReset()
        messagebox.showinfo("Confirmation", "Successfully Added New Contact")
    else:
        messagebox.showerror("Error", "Please fill in all the information")

# Function to update existing contact
def UpdateDetail():
    if Selected() is not None and Name.get() and Number.get() and Email.get():
        contactlist[Selected()] = [Name.get(), Number.get(), Email.get()]
        Select_set()
        EntryReset()
        messagebox.showinfo("Confirmation", "Successfully Updated Contact")
    else:
        messagebox.showerror("Error", "Please fill in all the information")

# Function to reset entry fields
def EntryReset():
    Name.set('')
    Number.set('')
    Email.set('')

# Function to delete selected contact
def Delete_Entry():
    if Selected() is not None:
        result = messagebox.askyesno('Confirmation', 'Do you want to delete the selected contact?')
        if result:
            del contactlist[Selected()]
            Select_set()
    else:
        messagebox.showerror("Error", 'Please select a contact')

# Function to view selected contact
def VIEW():
    if Selected() is not None:
        NAME, PHONE, EMAIL = contactlist[Selected()]
        Name.set(NAME)
        Number.set(PHONE)
        Email.set(EMAIL)

# Function to exit application
def EXIT():
    root.destroy()

# Function to set contact list in Listbox
def Select_set():
    contactlist.sort()
    select.delete(0, END)
    for name, phone, email in contactlist:
        select.insert(END, name)

Select_set()

# Function to search contacts
def SearchContact():
    search_query = Search.get().lower()
    select.delete(0, END)
    for name, phone, email in contactlist:
        if search_query in name.lower() or search_query in phone.lower() or search_query in email.lower():
            select.insert(END, name)

# Define labels, entry widgets, and buttons
Label(root, text='Name', font=("Times New Roman", 25, "bold"), bg='SlateGray3').place(x=30, y=20)
Entry(root, textvariable=Name, width=30).place(x=200, y=30)
Label(root, text='Contact No.', font=("Times New Roman", 22, "bold"), bg='SlateGray3').place(x=30, y=70)
Entry(root, textvariable=Number, width=30).place(x=200, y=80)
Label(root, text='Email', font=("Times New Roman", 22, "bold"), bg='SlateGray3').place(x=30, y=120)
Entry(root, textvariable=Email, width=30).place(x=200, y=130)

Button(root, text="ADD", font='Helvetica 18 bold', bg='#e8c1c7', command=AddContact, padx=20).place(x=50, y=180)
Button(root, text="EDIT", font='Helvetica 18 bold', bg='#e8c1c7', command=UpdateDetail, padx=20).place(x=50, y=240)
Button(root, text="DELETE", font='Helvetica 18 bold', bg='#e8c1c7', command=Delete_Entry, padx=20).place(x=50, y=300)
Button(root, text="VIEW", font='Helvetica 18 bold', bg='#e8c1c7', command=VIEW).place(x=50, y=360)
Button(root, text="RESET", font='Helvetica 18 bold', bg='#e8c1c7', command=EntryReset).place(x=50, y=420)
Button(root, text="EXIT", font='Helvetica 24 bold', bg='tomato', command=EXIT).place(x=250, y=470)

# Add search functionality
Label(root, text='Search', font=("Times New Roman", 22, "bold"), bg='SlateGray3').place(x=30, y=520)
Entry(root, textvariable=Search, width=30).place(x=200, y=530)
Button(root, text="SEARCH", font='Helvetica 18 bold', bg='#e8c1c7', command=SearchContact).place(x=50, y=570)

root.mainloop()
