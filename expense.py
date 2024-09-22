import tkinter as tk
from tkinter import messagebox
import datetime

class ExpenseTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")

        self.expenses = []

        # Add expense frame
        self.add_expense_frame = tk.Frame(root)
        self.add_expense_frame.pack(pady=10)

        self.amount_label = tk.Label(self.add_expense_frame, text="Amount:")
        self.amount_label.grid(row=0, column=0, padx=5, pady=5)
        self.amount_entry = tk.Entry(self.add_expense_frame)
        self.amount_entry.grid(row=0, column=1, padx=5, pady=5)

        self.description_label = tk.Label(self.add_expense_frame, text="Description:")
        self.description_label.grid(row=1, column=0, padx=5, pady=5)
        self.description_entry = tk.Entry(self.add_expense_frame)
        self.description_entry.grid(row=1, column=1, padx=5, pady=5)

        self.add_button = tk.Button(self.add_expense_frame, text="Add Expense", command=self.add_expense)
        self.add_button.grid(row=2, columnspan=2, pady=5)

        # View expenses frame
        self.view_expenses_frame = tk.Frame(root)
        self.view_expenses_frame.pack(pady=10)

        self.view_button = tk.Button(self.view_expenses_frame, text="View Expenses", command=self.view_expenses)
        self.view_button.pack(pady=5)

        # Calculate total expenses frame
        self.calculate_frame = tk.Frame(root)
        self.calculate_frame.pack(pady=10)

        self.calculate_button = tk.Button(self.calculate_frame, text="Calculate Total Expenses", command=self.calculate_total_expenses)
        self.calculate_button.pack(pady=5)

        # Exit button
        self.exit_button = tk.Button(root, text="Exit", command=root.quit)
        self.exit_button.pack(pady=5)

    def add_expense(self):
        try:
            amount = float(self.amount_entry.get())
            description = self.description_entry.get()
            date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            expense = {
                'amount': amount,
                'description': description,
                'date': date
            }
            self.expenses.append(expense)
            messagebox.showinfo("Success", "Expense added successfully!")
            self.amount_entry.delete(0, tk.END)
            self.description_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a valid number for the amount.")

    def view_expenses(self):
        if not self.expenses:
            messagebox.showinfo("Info", "No expenses recorded.")
        else:
            expenses_window = tk.Toplevel(self.root)
            expenses_window.title("View Expenses")

            for idx, expense in enumerate(self.expenses, start=1):
                expense_label = tk.Label(expenses_window, text=f"{idx}. Date: {expense['date']}, Amount: ${expense['amount']:.2f}, Description: {expense['description']}")
                expense_label.pack()

    def calculate_total_expenses(self):
        total = sum(expense['amount'] for expense in self.expenses)
        messagebox.showinfo("Total Expenses", f"Total Expenses: ${total:.2f}")

def main():
    root = tk.Tk()
    app = ExpenseTracker(root)
    root.mainloop()

if __name__ == "__main__":
    main()
