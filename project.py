from tkinter import *

window = Tk()
window.title("Product Calculator")
window.geometry("600x600")
window.configure(background="lightblue")
window.title("here's the product")

def calculate_product():
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        product = num1 * num2
        result_label.config(text=f"Product: {product}")
    

Label(window, text="Enter first number:", bg="lightblue").pack(pady=5)
entry_num1 = Entry(window)
entry_num1.pack(pady=5)

Label(window, text="Enter second number:", bg="lightblue").pack(pady=5)
entry_num2 = Entry(window)
entry_num2.pack(pady=5)

Button(window, text="Calculate Product", command=calculate_product).pack(pady=10)

result_label = Label(window, text="", bg="lightblue", font=("Arial", 12))
result_label.pack(pady=5)

window.mainloop()