from tkinter import*
import pbbackend

#Button logic
def get_selected_row(event): #event handler for selecting an entry
    global selected_tuple
    index=list1.curselection()[0]
    selected_tuple=list1.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])
    e2.delete(0,END)
    e2.insert(END,selected_tuple[2])
    e3.delete(0,END)
    e3.insert(END,selected_tuple[3])
    e4.delete(0,END)
    e4.insert(END,selected_tuple[4])
def view_command():  
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)
def search_command():
    list1.delete(0,END)
    for row in backend.search(firstName_text.get(),lastName_text.get(),location_text.get(),number_text.get()):
        list1.insert(END,row)

def add_command():
    backend.insert(firstName_text.get(),lastName_text.get(),location_text.get(),number_text.get())
    list1.delete(0,END)
    list1.insert(END,(firstName_text.get(),lastName_text.get(),location_text.get(),number_text.get()))

def delete_command(): 
    backend.delete(selected_tuple[0])
    view_command()

def update_command():
    backend.update(selected_tuple[0],firstName_text.get(),lastName_text.get(),location_text.get(),number_text.get())
    view_command()


    
#Start gui   
window = Tk()
window.wm_title("Phone Book")

#Entry labels
l1 = Label(window,text="First Name")
l1.grid(row=0,column=0)

l2 = Label(window,text="Last Name")
l2.grid(row=0,column=2)

l3 = Label(window,text="City")
l3.grid(row=1,column=0)

l4 = Label(window,text="Number")
l4.grid(row=1,column=2)

#Entry Boxes
firstName_text=StringVar()
e1=Entry(window,textvariable=firstName_text)
e1.grid(row=0,column=1)

lastName_text=StringVar()
e2=Entry(window,textvariable=lastName_text)
e2.grid(row=0,column=3)

location_text=StringVar()
e3=Entry(window,textvariable=location_text)
e3.grid(row=1,column=1)

number_text=StringVar()
e4=Entry(window,textvariable=number_text)
e4.grid(row=1,column=3)

#Listbox logic
list1=Listbox(window, height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

#Scrollbar logic
sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

#list logic
list1.configure(yscrollcommand=sb1.set)  #define scrollbar action
sb1.configure(command=list1.yview)
list1.bind('<<ListboxSelect>>', get_selected_row) #bind selection event to handler function

#Buttons
b1=Button(window,text="View all", width=12,command=view_command)
b1.grid(row=2,column=3)

b2=Button(window,text="Search Entry", width=12,command=search_command)
b2.grid(row=3,column=3)

b3=Button(window,text="Add Entry", width=12, command=add_command)
b3.grid(row=4,column=3)

b4=Button(window,text="Update selected", width=12, command = update_command)
b4.grid(row=5,column=3)

b5=Button(window,text="Delete Selected", width=12, command = delete_command)
b5.grid(row=6,column=3)

b6=Button(window,text="close", width=12,command=window.destroy)
b6.grid(row=7,column=3)




window.mainloop()
