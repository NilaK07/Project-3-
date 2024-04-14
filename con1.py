import tkinter as tk
from tkinter import messagebox

class ContactManagerGUI:
    def __init__(self, master):
        self.master = master
        master.title("Contact Management System")
        master.configure(bg="#f0f0f0")  
        self.name_label = tk.Label(master, text="Name:", bg="#f0f0f0") 
        self.name_label.grid(row=0, column=0, sticky="e")
        self.name_entry = tk.Entry(master)
        self.name_entry.grid(row=0, column=1)

        self.phone_label = tk.Label(master, text="Phone Number:", bg="#f0f0f0") 
        self.phone_label.grid(row=1, column=0, sticky="e")
        self.phone_entry = tk.Entry(master)
        self.phone_entry.grid(row=1, column=1)

        self.email_label = tk.Label(master, text="Email:", bg="#f0f0f0") 
        self.email_label.grid(row=2, column=0, sticky="e")
        self.email_entry = tk.Entry(master)
        self.email_entry.grid(row=2, column=1)

        self.address_label = tk.Label(master, text="Address:", bg="#f0f0f0") 
        self.address_label.grid(row=3, column=0, sticky="e")
        self.address_entry = tk.Entry(master)
        self.address_entry.grid(row=3, column=1)
        self.add_button = tk.Button(master, text="Add Contact", command=self.add_contact, bg="#007bff", fg="white") 
        self.add_button.grid(row=4, column=0, columnspan=2, pady=5)
        self.view_button = tk.Button(master, text="View Contacts", command=self.view_contacts, bg="#007bff", fg="white")  
        self.view_button.grid(row=5, column=0, columnspan=2, pady=5)

        self.search_label = tk.Label(master, text="Search:", bg="#f0f0f0")  
        self.search_entry = tk.Entry(master)
        self.search_entry.grid(row=6, column=1)

        self.search_button = tk.Button(master, text="Search", command=self.search_contact, bg="#007bff", fg="white")
        self.search_button.grid(row=6, column=2)

        self.update_button = tk.Button(master, text="Update Contact", command=self.update_contact, bg="#007bff", fg="white") 
        self.update_button.grid(row=7, column=0, columnspan=2, pady=5)

        self.delete_button = tk.Button(master, text="Delete Contact", command=self.delete_contact, bg="#007bff", fg="white")
        self.delete_button.grid(row=8, column=0, columnspan=2, pady=5)

        self.output_text = tk.Text(master, height=10, width=40, bg="#d9d9d9")
        self.output_text.grid(row=9, column=0, columnspan=3, padx=5, pady=5)
        self.contact_manager = ContactManager()

    def add_contact(self):
        name = self.name_entry.get()
        phone_number = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()
        self.contact_manager.add_contact(name, phone_number, email, address)
        messagebox.showinfo("Success", "Contact added successfully.")

    def view_contacts(self):
        self.output_text.delete('1.0', tk.END)
        contacts = self.contact_manager.view_contacts()
        for contact in contacts:
            self.output_text.insert(tk.END, contact + '\n')

    def search_contact(self):
        query = self.search_entry.get()
        results = self.contact_manager.search_contact(query)
        self.output_text.delete('1.0', tk.END)
        if results:
            for contact in results:
                self.output_text.insert(tk.END, contact + '\n')
        else:
            self.output_text.insert(tk.END, "No matching contacts found.")

    def update_contact(self):
        name = self.name_entry.get()
        phone_number = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()
        self.contact_manager.update_contact(name, phone_number, email, address)
        messagebox.showinfo("Success", "Contact updated successfully.")

    def delete_contact(self):
        name = self.name_entry.get()
        self.contact_manager.delete_contact(name)
        messagebox.showinfo("Success", "Contact deleted successfully.")

class ContactManager:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone_number, email, address):
        self.contacts[name] = f"Phone: {phone_number}, Email: {email}, Address: {address}"

    def view_contacts(self):
        return self.contacts.values()

    def search_contact(self, query):
        results = []
        for name, details in self.contacts.items():
            if query.lower() in name.lower() or query in details:
                results.append(name + ": " + details)
        return results

    def update_contact(self, name, phone_number, email, address):
        if name in self.contacts:
            self.contacts[name] = f"Phone: {phone_number}, Email: {email}, Address: {address}"
        else:
            messagebox.showerror("Error", "Contact not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
        else:
            messagebox.showerror("Error", "Contact not found.")

def main():
    root = tk.Tk()
    app = ContactManagerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
