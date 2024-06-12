from tkinter import *
from PIL import ImageTk,Image
import pymysql
from tkinter import messagebox
from AddBook import *
from DeleteBook import *
from ViewBooks import *
from IssueBook import *
from ReturnBook import *
# Add your own database name and password here to reflect in the code
mypass = "climin"
mydatabase ="librarydb"

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

root = Tk()
root.title("Library")
root.minsize(width=400,height=400)
root.geometry("600x500")

# Function to resize the background image to fill the window
def resize_image(event):
    new_width = event.width
    new_height = event.height
    image = bg_image.resize((new_width, new_height), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(image)
    Canvas1.create_image(0, 0, anchor=NW, image=img)
    Canvas1.image = img  # Keep a reference to avoid garbage collection
    Canvas1.config(width=new_width, height=new_height)  # Update canvas size

# Adding a background image
bg_image = Image.open("lib.jpg")
img = ImageTk.PhotoImage(bg_image)

Canvas1 = Canvas(root)
Canvas1.pack(expand=True, fill=BOTH)
Canvas1.create_image(0, 0, anchor=NW, image=img)
Canvas1.image = img  # Keep a reference to avoid garbage collection

root.bind("<Configure>", resize_image)  # Bind the resize event to the function

headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

headingLabel = Label(headingFrame1, text="Welcome to \n SLit Library", bg='black', fg='white', font=('Courier',15))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

btn1 = Button(root,text="Add Book Details",bg='black', fg='white', command=addBook)
btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
    
btn2 = Button(root,text="Delete Book",bg='black', fg='white', command=delete)
btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
    
btn3 = Button(root,text="View Book List",bg='black', fg='white', command=View)
btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)
    
btn4 = Button(root,text="Issue Book to Student",bg='black', fg='white', command = issueBook)
btn4.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)
    
btn5 = Button(root,text="Return Book",bg='black', fg='white', command = returnBook)
btn5.place(relx=0.28,rely=0.8, relwidth=0.45,relheight=0.1)

root.mainloop()
