import ttkbootstrap as btk
import tkinter as tk
import customtkinter as ctk
def repayment_page():
    if repayment_page==True:
        repayment_page=False
        payment_var=payment.get()
        return payment_var
    
def load_repayment_page (main_frame1, total_price,clear_page,load_page5):
    global repayment_page
    global payment
    repayment_page=True
    #Clearing the previous page
    clear_page(main_frame1)

    #Creating a new frame to show the process of the payment
    repayment_frame=btk.Frame(main_frame1)
    repayment_frame.pack(expand=True, fill='both')

    #Creating a label to show the error message
    error_label=btk.Label(repayment_frame, text='Payment is not enough', font=('Chalet Bold', 15), bootstyle='light' )
    error_label.place(relx=0.5, rely=0.4, anchor='center')

    #Creating a label to show the total price
    total_price_label=btk.Label(repayment_frame, text='Total price\t: ', font=('Chalet Bold', 15), bootstyle='light' )
    total_price_label.place(relx=0.3, rely=0.5, anchor='w')

    #Creating a label to show the total price that the customers have to pay
    total_price_selected=btk.Label(repayment_frame, text='RM'+str(total_price), font=('Chalet Bold', 15), bootstyle='light' )
    total_price_selected.place(relx=0.6, rely=0.5, anchor='w')

    #Creating a label to show the payment
    payment_menu=btk.Label(repayment_frame, text='Payment\t\t:', font=('Chalet Bold', 15), bootstyle='light' )
    payment_menu.place(relx=0.3, rely=0.6, anchor='w')
    payment_var=tk.IntVar()
    payment=btk.Entry(repayment_frame, font=('Chalet Bold', 15), bootstyle='light', textvariable=payment_var )
    payment.place(relx=0.53, rely=0.6, anchor='w')

    #Making sure that the customers can only enter numbers in the payment entry
    def only_numbers(char):
        return char.isdigit()
    validation = repayment_frame.register(only_numbers)
    payment.config(validate="key", validatecommand=(validation, "%S"))

    #Creating a button to confirm the payment
    confirm_button=ctk.CTkButton(repayment_frame, text='Confirm', corner_radius=0, command=lambda:load_page5()) 
    confirm_button.place(relx=0.9, rely=0.6, anchor='center')  

def payment_var():
    payment_var=tk.IntVar()
    payment_var=payment.get()
    return payment_var


def thank_you_page(main_frame1, load_page2):
    thank_you_frame=btk.Frame(main_frame1)
    thank_you_frame.pack(expand=True, fill='both')
    thank_you_label=btk.Label(thank_you_frame, text='Thank you for your purchase', font=('Chalet Bold', 15), bootstyle='light' )
    thank_you_label.place(relx=0.5, rely=0.5, anchor='center')
    #Creating a button to allow the customer to go back to the first page
    back_button=ctk.CTkButton(thank_you_frame, text='Book again', corner_radius=0, command=lambda:load_page2())
    back_button.place(relx=0.5, rely=0.7, anchor='center')

def change_page(main_frame1, total_price, payment_data, load_page2):
     #If the payment is enough, a new frame will be created to show the change
    change_frame=btk.Frame(main_frame1)
    change_frame.pack(expand=True, fill='both')
    #Allow the customer to see the change
    change_label=btk.Label(change_frame, text='Change: RM'+str(int(payment_data)-total_price), font=('Chalet Bold', 15), bootstyle='light' )
    change_label.place(relx=0.5, rely=0.5, anchor='center')
    thank_you=btk.Label(change_frame, text='Thank you for your purchase', font=('Chalet Bold', 15), bootstyle='light' )
    thank_you.place(relx=0.5, rely=0.6, anchor='center')
    #Creating a button to allow the customer to go back to the first page
    back_button=ctk.CTkButton(change_frame, text='Book again', corner_radius=0, command=lambda:load_page2())
    back_button.place(relx=0.5, rely=0.7, anchor='center')
