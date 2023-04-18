import tkinter as tk
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['College']
student_col = db['Students']

# PRN : 2020BTECS00092
# Name : Vishal Shrirang Madle
# LAB  : ADS LAB : ASSIGNMENT 09

def create():
    prn = prn_entry.get()
    name = name_entry.get()
    branch = branch_entry.get()
    student = {"PRN": prn, "name": name, "branch": branch}
    result = student_col.insert_one(student)
    result_box.insert(tk.END, f"Record with PRN {prn} created successfully.")

def read():
    result_box.delete(0, tk.END)
    for student in student_col.find():
        result_box.insert(tk.END, f"PRN: {student['PRN']} Name: {student['name']} Branch: {student['branch']}")

def update():
    old_prn = old_prn_entry.get()
    new_prn = new_prn_entry.get()
    new_name = new_name_entry.get()
    new_branch = new_branch_entry.get()
    student_col.update_one({"PRN": old_prn}, {"$set": {"PRN": new_prn, "name": new_name, "branch": new_branch}})
    result_box.insert(tk.END, f"Record with PRN {old_prn} updated successfully.")

def delete():
    prn = prn_entry.get()
    student_col.delete_one({"PRN": prn})
    result_box.insert(tk.END, f"Record with PRN {prn} deleted successfully.")

window = tk.Tk()
window.title("Student Data Management")

create_frame = tk.LabelFrame(window, text="Create")
create_frame.grid(row=0, column=0, padx=10, pady=10)

prn_label = tk.Label(create_frame, text="PRN:")
prn_label.grid(row=0, column=0, padx=5, pady=5)

prn_entry = tk.Entry(create_frame, width=30)
prn_entry.grid(row=0, column=1, padx=5, pady=5)

name_label = tk.Label(create_frame, text="Name:")
name_label.grid(row=1, column=0, padx=5, pady=5)

name_entry = tk.Entry(create_frame, width=30)
name_entry.grid(row=1, column=1, padx=5, pady=5)

branch_label = tk.Label(create_frame, text="Branch:")
branch_label.grid(row=2, column=0, padx=5, pady=5)

branch_entry = tk.Entry(create_frame, width=30)
branch_entry.grid(row=2, column=1, padx=5, pady=5)

create_button = tk.Button(create_frame, text="Create", command=create, width=10)
create_button.grid(row=3, column=0, columnspan=2, pady=10)

read_frame = tk.LabelFrame(window, text="Read")
read_frame.grid(row=0, column=1, padx=10, pady=10)

result_box = tk.Listbox(read_frame, width=50)
result_box.grid(row=0, column=0, padx=5, pady=5)

scrollbar = tk.Scrollbar(read_frame)
scrollbar.grid(row=0, column=1, sticky="NS")

result_box.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=result_box.yview)

read_button = tk.Button(read_frame, text="Read", command=read, width=10)
read_button.grid(row=1, column=0, columnspan=2, pady=10)








update_frame = tk.LabelFrame(window, text="Update")
update_frame.grid(row=0, column=2, padx=10, pady=10)

old_prn_label = tk.Label(update_frame, text="Old PRN:")
old_prn_label.grid(row=0, column=0, padx=5, pady=5)

old_prn_entry = tk.Entry(update_frame, width=30)
old_prn_entry.grid(row=0, column=1, padx=5, pady=5)

new_prn_label = tk.Label(update_frame, text="New PRN:")
new_prn_label.grid(row=1, column=0, padx=5, pady=5)

new_prn_entry = tk.Entry(update_frame, width=30)
new_prn_entry.grid(row=1, column=1, padx=5, pady=5)

new_name_label = tk.Label(update_frame, text="New Name:")
new_name_label.grid(row=2, column=0, padx=5, pady=5)

new_name_entry = tk.Entry(update_frame, width=30)
new_name_entry.grid(row=2, column=1, padx=5, pady=5)

new_branch_label = tk.Label(update_frame, text="New Branch:")
new_branch_label.grid(row=3, column=0, padx=5, pady=5)

new_branch_entry = tk.Entry(update_frame, width=30)
new_branch_entry.grid(row=3, column=1, padx=5, pady=5)

update_button = tk.Button(update_frame, text="Update", command=update, width=10)
update_button.grid(row=4, column=0, columnspan=2, pady=10)

delete_frame = tk.LabelFrame(window, text="Delete")
delete_frame.grid(row=1, column=0, padx=10, pady=10)

prn_label = tk.Label(delete_frame, text="PRN:")
prn_label.grid(row=0, column=0, padx=5, pady=5)

prn_entry = tk.Entry(delete_frame, width=30)
prn_entry.grid(row=0, column=1, padx=5, pady=5)

delete_button = tk.Button(delete_frame, text="Delete", command=delete, width=10)
delete_button.grid(row=1, column=0, columnspan=2, pady=10)

window.mainloop()


