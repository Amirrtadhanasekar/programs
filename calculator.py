import tkinter as tk
from tkinter import messagebox
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Multi-Purpose Calculator")

        self.main_menu()

    def main_menu(self):
        self.clear_frame()

        self.menu_label = tk.Label(self.root, text="Main Menu", font=("Arial", 16))
        self.menu_label.pack(pady=10)

        self.arithmetic_button = tk.Button(self.root, text="Arithmetic Operations", command=self.arithmetic_operations)
        self.arithmetic_button.pack(pady=5)

        self.geometric_button = tk.Button(self.root, text="Geometric Computations", command=self.geometric_computations)
        self.geometric_button.pack(pady=5)

        self.string_button = tk.Button(self.root, text="String Formatting", command=self.string_formatting)
        self.string_button.pack(pady=5)

        self.swap_button = tk.Button(self.root, text="Value Swapping Demo", command=self.value_swapping)
        self.swap_button.pack(pady=5)

        self.operator_button = tk.Button(self.root, text="Operator Demonstrations", command=self.operator_demonstrations)
        self.operator_button.pack(pady=5)

        self.exit_button = tk.Button(self.root, text="Exit", command=self.root.quit)
        self.exit_button.pack(pady=5)

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def arithmetic_operations(self):
        self.clear_frame()

        self.label = tk.Label(self.root, text="Arithmetic Operations", font=("Arial", 16))
        self.label.pack(pady=10)

        self.num1_label = tk.Label(self.root, text="Enter the first number:")
        self.num1_label.pack()
        self.num1_entry = tk.Entry(self.root)
        self.num1_entry.pack()

        self.num2_label = tk.Label(self.root, text="Enter the second number:")
        self.num2_label.pack()
        self.num2_entry = tk.Entry(self.root)
        self.num2_entry.pack()

        self.add_button = tk.Button(self.root, text="Addition", command=lambda: self.perform_arithmetic_operation('1'))
        self.add_button.pack(pady=5)

        self.sub_button = tk.Button(self.root, text="Subtraction", command=lambda: self.perform_arithmetic_operation('2'))
        self.sub_button.pack(pady=5)

        self.mul_button = tk.Button(self.root, text="Multiplication", command=lambda: self.perform_arithmetic_operation('3'))
        self.mul_button.pack(pady=5)

        self.div_button = tk.Button(self.root, text="Division", command=lambda: self.perform_arithmetic_operation('4'))
        self.div_button.pack(pady=5)

        self.back_button = tk.Button(self.root, text="Back to Main Menu", command=self.main_menu)
        self.back_button.pack(pady=10)

    def perform_arithmetic_operation(self, choice):
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            if choice == '1':
                result = num1 + num2
                operation = "+"
            elif choice == '2':
                result = num1 - num2
                operation = "-"
            elif choice == '3':
                result = num1 * num2
                operation = "*"
            elif choice == '4':
                if num2 == 0:
                    messagebox.showerror("Error", "Division by zero!")
                    return
                result = num1 / num2
                operation = "/"
            messagebox.showinfo("Result", f"Result: {num1} {operation} {num2} = {result}")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")

    def geometric_computations(self):
        self.clear_frame()

        self.label = tk.Label(self.root, text="Geometric Computations", font=("Arial", 16))
        self.label.pack(pady=10)

        self.circle_button = tk.Button(self.root, text="Calculate Area of Circle", command=lambda: self.perform_geometric_computation('1'))
        self.circle_button.pack(pady=5)

        self.rectangle_button = tk.Button(self.root, text="Calculate Area of Rectangle", command=lambda: self.perform_geometric_computation('2'))
        self.rectangle_button.pack(pady=5)

        self.triangle_button = tk.Button(self.root, text="Calculate Area of Triangle", command=lambda: self.perform_geometric_computation('3'))
        self.triangle_button.pack(pady=5)

        self.back_button = tk.Button(self.root, text="Back to Main Menu", command=self.main_menu)
        self.back_button.pack(pady=10)

    def perform_geometric_computation(self, choice):
        if choice == '1':
            self.clear_frame()
            self.radius_label = tk.Label(self.root, text="Enter the radius of the circle:")
            self.radius_label.pack()
            self.radius_entry = tk.Entry(self.root)
            self.radius_entry.pack()
            self.calculate_circle_button = tk.Button(self.root, text="Calculate", command=lambda: self.calculate_area('circle'))
            self.calculate_circle_button.pack(pady=5)
        elif choice == '2':
            self.clear_frame()
            self.length_label = tk.Label(self.root, text="Enter the length of the rectangle:")
            self.length_label.pack()
            self.length_entry = tk.Entry(self.root)
            self.length_entry.pack()
            self.width_label = tk.Label(self.root, text="Enter the width of the rectangle:")
            self.width_label.pack()
            self.width_entry = tk.Entry(self.root)
            self.width_entry.pack()
            self.calculate_rectangle_button = tk.Button(self.root, text="Calculate", command=lambda: self.calculate_area('rectangle'))
            self.calculate_rectangle_button.pack(pady=5)
        elif choice == '3':
            self.clear_frame()
            self.base_label = tk.Label(self.root, text="Enter the base of the triangle:")
            self.base_label.pack()
            self.base_entry = tk.Entry(self.root)
            self.base_entry.pack()
            self.height_label = tk.Label(self.root, text="Enter the height of the triangle:")
            self.height_label.pack()
            self.height_entry = tk.Entry(self.root)
            self.height_entry.pack()
            self.calculate_triangle_button = tk.Button(self.root, text="Calculate", command=lambda: self.calculate_area('triangle'))
            self.calculate_triangle_button.pack(pady=5)

        self.back_button = tk.Button(self.root, text="Back to Main Menu", command=self.main_menu)
        self.back_button.pack(pady=10)

    def calculate_area(self, shape):
        try:
            if shape == 'circle':
                radius = float(self.radius_entry.get())
                area = math.pi * radius ** 2
                messagebox.showinfo("Result", f"Area of the circle with radius {radius}: {area:.2f}")
            elif shape == 'rectangle':
                length = float(self.length_entry.get())
                width = float(self.width_entry.get())
                area = length * width
                messagebox.showinfo("Result", f"Area of the rectangle with length {length} and width {width}: {area:.2f}")
            elif shape == 'triangle':
                base = float(self.base_entry.get())
                height = float(self.height_entry.get())
                area = 0.5 * base * height
                messagebox.showinfo("Result", f"Area of the triangle with base {base} and height {height}: {area:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")

    def string_formatting(self):
        self.clear_frame()

        self.label = tk.Label(self.root, text="String Formatting", font=("Arial", 16))
        self.label.pack(pady=10)

        self.string_label = tk.Label(self.root, text="Enter a sentence or phrase:")
        self.string_label.pack()
        self.string_entry = tk.Entry(self.root)
        self.string_entry.pack()

        self.format_button = tk.Button(self.root, text="Format String", command=self.perform_string_formatting)
        self.format_button.pack(pady=5)

        self.back_button = tk.Button(self.root, text="Back to Main Menu", command=self.main_menu)
        self.back_button.pack(pady=10)

    def perform_string_formatting(self):
        string_input = self.string_entry.get()
        if string_input:
            formatted_strings = (
                f"Original String: {string_input}\n"
                f"Uppercase: {string_input.upper()}\n"
                f"Lowercase: {string_input.lower()}\n"
                f"Title Case: {string_input.title()}\n"
                f"Reversed: {string_input[::-1]}"
            )
            messagebox.showinfo("Formatted Strings", formatted_strings)
        else:
            messagebox.showerror("Error", "Please enter a valid string.")

    def value_swapping(self):
        self.clear_frame()

        self.label = tk.Label(self.root, text="Value Swapping Demo", font=("Arial", 16))
        self.label.pack(pady=10)

        self.value1_label = tk.Label(self.root, text="Enter the first value:")
        self.value1_label.pack()
        self.value1_entry = tk.Entry(self.root)
        self.value1_entry.pack()

        self.value2_label = tk.Label(self.root, text="Enter the second value:")
        self.value2_label.pack()
        self.value2_entry = tk.Entry(self.root)
        self.value2_entry.pack()

        self.swap_button = tk.Button(self.root, text="Swap Values", command=self.perform_value_swapping)
        self.swap_button.pack(pady=5)

        self.back_button = tk.Button(self.root, text="Back to Main Menu", command=self.main_menu)
        self.back_button.pack(pady=10)

    def perform_value_swapping(self):
        value1 = self.value1_entry.get()
        value2 = self.value2_entry.get()
        messagebox.showinfo("Before Swapping", f"Before swapping: value1 = {value1}, value2 = {value2}")
        value1, value2 = value2, value1
        messagebox.showinfo("After Swapping", f"After swapping: value1 = {value1}, value2 = {value2}")

    def operator_demonstrations(self):
        self.clear_frame()

        self.label = tk.Label(self.root, text="Operator Demonstrations", font=("Arial", 16))
        self.label.pack(pady=10)

        self.a_label = tk.Label(self.root, text="Enter a number (integer):")
        self.a_label.pack()
        self.a_entry = tk.Entry(self.root)
        self.a_entry.pack()

        self.b_label = tk.Label(self.root, text="Enter another number (integer):")
        self.b_label.pack()
        self.b_entry = tk.Entry(self.root)
        self.b_entry.pack()

        self.demo_button = tk.Button(self.root, text="Show Operations", command=self.perform_operator_demonstrations)
        self.demo_button.pack(pady=5)

        self.back_button = tk.Button(self.root, text="Back to Main Menu", command=self.main_menu)
        self.back_button.pack(pady=10)

    def perform_operator_demonstrations(self):
        try:
            a = int(self.a_entry.get())
            b = int(self.b_entry.get())
            operations = (
                f"Addition: {a} + {b} = {a + b}\n"
                f"Subtraction: {a} - {b} = {a - b}\n"
                f"Multiplication: {a} * {b} = {a * b}\n"
                f"Division: {a} / {b} = {a / b}\n"
                f"Floor Division: {a} // {b} = {a // b}\n"
                f"Modulus: {a} % {b} = {a % b}\n"
                f"Exponentiation: {a} ** {b} = {a ** b}"
            )
            messagebox.showinfo("Operations", operations)
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter valid integers.")

def main():
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
