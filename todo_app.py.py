#!/usr/bin/env python
# coding: utf-8

# In[2]:


import tkinter as tk
from tkinter import messagebox

TASKS_FILE = 'tasks.txt'

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("400x450")
        self.root.configure(bg="white")

        self.tasks = []

        # Heading
        tk.Label(root, text="My To-Do List", font=("Helvetica", 18, "bold"), bg="white").pack(pady=10)

        # Entry field
        self.task_entry = tk.Entry(root, font=("Helvetica", 14))
        self.task_entry.pack(pady=10, padx=20, fill="x")

        # Add button
        tk.Button(root, text="Add Task", font=("Helvetica", 12), command=self.add_task).pack(pady=5)

        # Task listbox
        self.task_listbox = tk.Listbox(root, font=("Helvetica", 12), selectbackground="#ddd", selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10, padx=20, fill="both", expand=True)

        # Buttons for operations
        tk.Button(root, text="Delete Selected", font=("Helvetica", 12), command=self.delete_task).pack(pady=5)
        tk.Button(root, text="Mark as Done", font=("Helvetica", 12), command=self.mark_done).pack(pady=5)

        self.load_tasks()

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append(task)
            self.update_listbox()
            self.task_entry.delete(0, tk.END)
            self.save_tasks()

    def delete_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            self.tasks.pop(index)
            self.update_listbox()
            self.save_tasks()

    def mark_done(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            task = self.tasks[index]
            if not task.startswith("✓ "):
                self.tasks[index] = "✓ " + task
            else:
                self.tasks[index] = task.replace("✓ ", "")
            self.update_listbox()
            self.save_tasks()

    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

    def load_tasks(self):
        try:
            with open(TASKS_FILE, 'r',  encoding='utf-8') as f:
                self.tasks = [line.strip() for line in f.readlines()]
                self.update_listbox()
        except FileNotFoundError:
            pass

    def save_tasks(self):
        with open(TASKS_FILE, 'w',  encoding='utf-8') as f:
            for task in self.tasks:
                f.write(task + '\n')

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()


# In[ ]:





# In[ ]:




