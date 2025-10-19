import tkinter as tk
from tkinter import messagebox

# Function to calculate BMI
def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        # Validate input
        if weight <= 0 or height <= 0:
            messagebox.showerror("Invalid Input", "Weight and height must be positive numbers.")
            return

        bmi = weight / (height ** 2)

        # Determine category
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 25:
            category = "Normal weight"
        elif 25 <= bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        result_label.config(text=f"BMI: {bmi:.2f}\nCategory: {category}")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric values.")

# Create main window
window = tk.Tk()
window.title("BMI Calculator")
window.geometry("300x300")

# Labels and Entry Fields
tk.Label(window, text="Enter Weight (kg):").pack(pady=5)
weight_entry = tk.Entry(window)
weight_entry.pack(pady=5)

tk.Label(window, text="Enter Height (m):").pack(pady=5)
height_entry = tk.Entry(window)
height_entry.pack(pady=5)

# Button to Calculate
tk.Button(window, text="Calculate BMI", command=calculate_bmi).pack(pady=10)

# Label to show the result
result_label = tk.Label(window, text="", font=("Arial", 12))
result_label.pack(pady=10)

# Start the GUI loop
window.mainloop()
