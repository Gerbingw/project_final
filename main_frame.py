import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import ttkbootstrap as btk
from PIL import ImageTk,Image
import calculation2 as cal
import summary as sum
from datatabulation import create_tables, create_connection, insert_ticket_data
#main window
window=btk.Window(themename='darkly')
window.title('Raja Amusement Park')
window.geometry('1200x700')
window.minsize(600,500)

#layout of window
window.rowconfigure([0,1,2,3], weight=1, uniform='a')
window.columnconfigure([0,1,2], weight=1, uniform='a')
main_frame1=ttk.Frame(window)
main_frame1.grid(row=0, rowspan=5, column=0, columnspan=5, sticky='news')

def clear_page(frame):
    for widget in frame.winfo_children():
        widget.destroy()


ride_pass_page=False
package_pass_page=False
ticket_pass_page=False
finish_page=False
parent_page=False

#logo
logo_img= Image.open(r'Picture/Logo4.png').resize((190,190))
image_tk=ImageTk.PhotoImage(logo_img)
logo_widget=btk.Label(main_frame1, image=image_tk)
logo_widget.image=logo_img
logo_widget.pack(side='top',anchor='nw', padx=10, pady=10)

#Page 1
def load_page1():
    if finish_page==True:
        clear_page(main_frame1)
    
    
    #Creating title frame
    title_frm=btk.Frame(main_frame1)
    title_frm.place(relx=0.5, rely=0.1, anchor='n')
    
    title=btk.Label(title_frm, text='Welcome to Raja Amusement Park', bootstyle='light', font=('Proxima Nova',25))
    #Make title same row as image
    title_frm.columnconfigure(0, weight=1)
    title_frm.rowconfigure(0, weight=1)
    title.pack()



    #Creating frames in first page
    frame1=btk.Frame(main_frame1)
    frame2=btk.Frame(main_frame1)
    frame3=btk.Frame(main_frame1)
    #Layout
    frame1.pack(fill='both')
    frame2.pack(fill='both')
    frame3.pack(fill='both')

    #Widgets in the frames
    desc1=ttk.Label(
        frame1,
        text='''
        Ticket types that are available for booking:
        1. Adult\t\t(RM 20.00)
        2. Children\t\t(RM 12.00)
        3. Senior citizen\t(RM 16.00)
        ''',  
        bootstyle='light',
        justify='left',
        font=('Chalet Bold', 15)
        )

    desc2=ttk.Label(
        frame2,
        text='''
        Packages that are offered for booking:
        1. Group of 5 individuals\t\t(RM 70.00)
        2. Family(min 5 family members)\t(RM 50.00)
        ''',
        bootstyle='light',
        justify='left',
        font=('Chalet Bold', 15)
    )

    desc3=ttk.Label(
        frame3,
        text='''
        Pass that are available for add on:
        1. Roller coaster ride\t(RM 12.00)
        2. Ghost house\t(RM 10.00)
        3. Pirate ship ride\t(RM 11.00)
        ''',
        bootstyle='light',
        justify='left',
        font=('Chalet Bold', 15)
    )
    #Creating next button to go to next page
    continue_btn=btk.Button(main_frame1, text='Continue to next page', command=lambda:load_page2())
    #Layout
    desc3.pack(fill='both', side='left')
    desc2.pack(fill='both', side='left')
    desc1.pack(fill='both', side='left')
    continue_btn.place(relx=0.6, rely=0.6)

def load_page3_close_slidebar():
    #When this function is called, the sliderbar will move downwards and the page 3 will be loaded
    global ticket_pass_page
    global package_pass_page
    package_pass_page=True
    ticket_pass_page=False
    load_page3()
    menu.animate()

def load_pass_page_close_slidebar():
    #When this function is called, the sliderbar will move downwards and the ride pass page will be loaded 
    global ride_pass_page
    ride_pass_page=True
    load_ride_pass()
    menu.animate()


def load_page2():
    global ticket_pass_page
    global main_frame1
    global menu
    global ticket_booking
    global ticket_amount
    global ticket_type
    ticket_pass_page=True
    
    #Clearing the previous page
    clear_page(main_frame1)

    #Naming page 2 as 'Booking page' in main_frame1
    title=btk.Label(main_frame1, text='Booking page', font=('Proxima Nova',25), bootstyle='light')
    title.place(relx=0.5, rely=0.1, anchor='n')

    #Creating a place for the customers to book their tickets
    ticket_booking=btk.Frame(main_frame1)
    ticket_booking.place(relx=0.5, rely=0.3, anchor='center')

    # There will be a title for the ticket booking frame
    ticket_booking_title=btk.Label(ticket_booking, text='Ticket booking', font=('Chalet Bold', 20), bootstyle='light' )
    ticket_booking_title.pack(side='top', padx=10, pady=10)

    # In the ticket booking frame, a dropdown menu will be placed to allow the customers to choose the type of ticket they want to book
    ticket_type=ctk.CTkComboBox(ticket_booking, values=['Adult', 'Children', 'Senior citizen'], state='readonly')
    ticket_type.pack(side='left', padx=10, pady=10)

    # In the ticket booking frame, a spinbox will be placed to allow the customers to choose the amount of ticket they want to book
    ticket_amount=btk.Spinbox(ticket_booking,text='Amount', from_=0, to=1000, textvariable=ticket_amount_var)
    ticket_amount.pack(side='left', padx=10, pady=10)

    #placing slidebar
    menu=cal.slidebar(main_frame1, 1.0, 0.8 )

    #Creating buttons to show packages and add ride pass in another frame in the slidebar
    package_btn=ctk.CTkButton(menu, text='Packages', corner_radius=0, command=lambda:load_page3_close_slidebar())
    package_btn.pack(side='top', padx=10, pady=10)
    ride_pass_btn=ctk.CTkButton(menu, text='Add ride pass', corner_radius=0, command=lambda:load_pass_page_close_slidebar())
    ride_pass_btn.pack(side='top', padx=10, pady=10)
    
    #Placing a button to show the menu
    animate_button=ctk.CTkButton(main_frame1, text='Other options', corner_radius=0, command=lambda:menu.animate())
    animate_button.place(relx=0.5, rely=0.7, anchor='center')

    #Creating a button to go to payment page
    payment_button=ctk.CTkButton(main_frame1, text='Payment', corner_radius=0, command=lambda:load_page4())
    payment_button.place(relx=0.7, rely=0.7, anchor='center')



#Creating a new frame in second page for ride when the button 'Add ride pass' is clicked
def load_ride_pass():
    global ride_pass_type
    global ride_pass_amount
    #Creating a new frame for ride pass
    ride_pass=btk.Frame(main_frame1)
    ride_pass.place(relx=0.5 , rely=0.55, anchor='center')

    #Creating a tittle for the ride pass frame
    ride_pass_title=btk.Label(ride_pass, text='Ride pass', font=('Chalet Bold', 20), bootstyle='light' )
    ride_pass_title.pack(side='top', padx=10, pady=10)

    #Creating a dropdown menu for the customers to choose the type of ride pass they want to add
    ride_pass_type=ctk.CTkComboBox(ride_pass, values=['Roller coaster ride', 'Ghost house', 'Pirate ship ride'], state='readonly' )
    ride_pass_type.pack(side='left', padx=10, pady=10)

    #Creating a spinbox for the customers to choose the amount of ride pass they want to add
    ride_pass_amount=btk.Spinbox(ride_pass,text='Amount', from_=0, to=1000, textvariable=ride_pass_amount_var)
    ride_pass_amount.pack(side='left', padx=10, pady=10)


#creating a new page for packages
def load_page3():
    global package_amount
    global package_type
    #clearing the previous page
    clear_page(ticket_booking)

    #Naming next section as 'Package page' in main_frame1
    title=btk.Label(main_frame1, text='Package page', font=('Proxima Nova',25), bootstyle='light')
    title.place(relx=0.5, rely=0.1, anchor='n')

    #creating a place for the customers to book their packages
    package_booking=btk.Frame(main_frame1)
    package_booking.place(relx=0.5, rely=0.3, anchor='center')

    # There will be a title for the package booking frame
    package_booking_title=btk.Label(package_booking, text='Package booking', font=('Chalet Bold', 20), bootstyle='light' )
    package_booking_title.pack(side='top', padx=10, pady=10)

    # In the package booking frame, a dropdown menu will be placed to allow the customers to choose the type of package they want to book
    package_type=ctk.CTkComboBox(package_booking, values=['Group of 5 individuals', 'Family'], state='readonly')
    package_type.pack(side='left', padx=10, pady=10)

    # In the package booking frame, a spinbox will be placed to allow the
    # customers to choose the amount of package they want to book
    package_amount=btk.Spinbox(package_booking,text='Amount', from_=0, to=1000, textvariable=package_amount_var)
    package_amount.pack(side='left', padx=10, pady=10)

    #creating a button to go back to the ticket booking page
    back_button=ctk.CTkButton(main_frame1, text='Back', corner_radius=0, command=lambda:load_page2())
    back_button.place(relx=0.3, rely=0.7, anchor='center')


#Creating a new page to show the final booking details
def load_page4():
    global ticket_pass_page
    global package_pass_page
    global ride_pass_page
    global selected_ticket_type
    global pass_price
    global total_price
    global selected_children_ticket_amount
    global selected_children_ticket
    global selected_ticket_amount
    global selected_package_type
    global selected_package_amount
    global selected_ride_pass_type
    global selected_ride_pass_amount
    global parent_page
 

    
    #Creating variables to store the data that the customers have chosen
    selected_ticket_type='None'  
    selected_ticket_amount=0
    selected_package_type='None'
    selected_package_amount=0
    selected_ride_pass_type='None'
    selected_ride_pass_amount=0
    total_price=0

    
    #Determine whenever which page is loaded, the data from customer will be stored in the correct variable
    if ticket_pass_page==True:
        if ride_pass_page==True:

            selected_ticket_type=tk.StringVar()
            selected_ticket_amount=tk.IntVar()
            
            selected_ride_pass_type=tk.StringVar()
            selected_ride_pass_amount=tk.IntVar()

            selected_ticket_type=ticket_type.get()
            selected_ticket_amount=ticket_amount.get()

            selected_ride_pass_type=ride_pass_type.get()
            selected_ride_pass_amount=ride_pass_amount.get()
            create_tables(), create_connection(), insert_ticket_data(selected_ticket_type,selected_ticket_amount,selected_package_type,selected_package_amount,selected_ride_pass_type,selected_ride_pass_amount,total_price)

            ticket_price=cal.price_calculation_ticket(selected_ticket_type, selected_ticket_amount)
            pass_price=cal.price_calculation_pass(selected_ride_pass_type, selected_ride_pass_amount)
            total_price=ticket_price+pass_price
            ticket_payment_page_summary()
            
            

            #When the customers choose the ticket type as 'Children'
            if selected_ticket_type=='Children':
                selected_children_ticket_amount=selected_ticket_amount
                selected_children_ticket_amount=selected_ticket_amount
                pass_price=cal.price_calculation_pass(selected_ride_pass_type, selected_ride_pass_amount)
                #This will active the parenting page
                load_parenting_page()
        else:
            selected_ticket_type=tk.StringVar()
            selected_ticket_amount=tk.IntVar()
            
            selected_ticket_type=ticket_type.get()
            selected_ticket_amount=ticket_amount.get()

            ticket_price=cal.price_calculation_ticket(selected_ticket_type, selected_ticket_amount)
            total_price=ticket_price
            ticket_payment_page_summary()
            

            if selected_ticket_type=='Children':
                selected_children_ticket=selected_ticket_type
                selected_children_ticket_amount=selected_ticket_amount
                #This will active the parent page
                load_parenting_page()
            
    elif package_pass_page==True:
        if ride_pass_page==True:
            selected_package_type=tk.StringVar()
            selected_package_amount=tk.IntVar()
            
            selected_ride_pass_type=tk.StringVar()
            selected_ride_pass_amount=tk.IntVar()

            selected_package_type=package_type.get()
            selected_package_amount=package_amount.get()
            selected_ride_pass_type=ride_pass_type.get()
            selected_ride_pass_amount=ride_pass_amount.get()

            package_price=cal.price_calculation_package(selected_package_type, selected_package_amount)
            pass_price=cal.price_calculation_pass(selected_ride_pass_type, selected_ride_pass_amount)
            total_price=package_price+pass_price
            package_payment_page_summary()
            
        else:
            selected_package_type=tk.StringVar()
            selected_package_amount=tk.IntVar()

            selected_package_type=package_type.get()
            selected_package_amount=package_amount.get()

            package_price=cal.price_calculation_package(selected_package_type, selected_package_amount)
            total_price=package_price
            package_payment_page_summary()


def children_others_details():
    global total_price
    global selected_ticket_type2
    global selected_ticket_amount2
    if ride_pass_page==True:
        
        selected_ticket_type2=tk.StringVar()
        selected_ticket_amount2=tk.IntVar()
        selected_ticket_type2=ticket_type2.get()
        selected_ticket_amount2=ticket_amount2.get()

        ticket_price=cal.price_calculation_ticket(selected_ticket_type2, selected_ticket_amount2)
        children_price=cal.price_calculation_ticket(selected_children_ticket,selected_children_ticket_amount)
        total_price=ticket_price+children_price+pass_price
        children_and_adult_or_senior_ticket_summary()

    else:
        selected_ticket_type2=tk.StringVar()
        selected_ticket_amount2=tk.IntVar()
        selected_ticket_type2=ticket_type2.get()
        selected_ticket_amount2=ticket_amount2.get()

        ticket_price=cal.price_calculation_ticket(selected_ticket_type2, selected_ticket_amount2)
        children_price=cal.price_calculation_ticket(selected_children_ticket,selected_children_ticket_amount)
        total_price=ticket_price+children_price
        children_and_adult_or_senior_ticket_summary()

       

def package_payment_page_summary():
    global payment
   
    #Creating a new frame to show the booking details
    package_details=btk.Frame(main_frame1)
    package_details.pack(expand=True, fill='both')
     #Creating a title for the booking details
    booking_details_title=btk.Label(package_details, text='Booking details', font=('Chalet Bold', 20), bootstyle='light' )
    booking_details_title.pack(side='top', padx=10, pady=10)
    #Creating a label to show the package type
    package_type_label=btk.Label(package_details, text='Package type\t: ', font=('Chalet Bold', 15), bootstyle='light' )
    package_type_label.place(relx=0.3, rely=0.3, anchor='w')

    #Creating a label to show the package amount
    package_amount_label=btk.Label(package_details, text='Package amount\t: ', font=('Chalet Bold', 15), bootstyle='light' )
    package_amount_label.place(relx=0.3, rely=0.4, anchor='w')

    #Creating a label to show the ride pass type
    ride_pass_type_label=btk.Label(package_details, text='Ride pass type\t: ', font=('Chalet Bold', 15), bootstyle='light' )
    ride_pass_type_label.place(relx=0.3, rely=0.5, anchor='w')

    #Creating a label to show the ride pass amount
    ride_pass_amount_label=btk.Label(package_details, text='Ride pass amount\t: ', font=('Chalet Bold', 15), bootstyle='light' )
    ride_pass_amount_label.place(relx=0.3, rely=0.6, anchor='w')

    #Creating a label to show the package type that the customers have chosen
    package_type_selected=btk.Label(package_details, text=selected_package_type, font=('Chalet Bold', 15), bootstyle='light' )
    package_type_selected.place(relx=0.6, rely=0.3, anchor='w')

    #Creating a label to show the package amount that the customers have chosen
    package_amount_selected=btk.Label(package_details, text=selected_package_amount, font=('Chalet Bold', 15), bootstyle='light' )
    package_amount_selected.place(relx=0.6, rely=0.4, anchor='w')

    #Creating a label to show the ride pass type that the customers have chosen
    ride_pass_type_selected=btk.Label(package_details, text=selected_ride_pass_type, font=('Chalet Bold', 15), bootstyle='light' )
    ride_pass_type_selected.place(relx=0.6, rely=0.5, anchor='w')

    #Creating a label to show the ride pass amount that the customers have chosen
    ride_pass_amount_selected=btk.Label(package_details, text=selected_ride_pass_amount, font=('Chalet Bold', 15), bootstyle='light' )
    ride_pass_amount_selected.place(relx=0.6, rely=0.6, anchor='w')

    #Creating a label to show the total price
    total_price_label=btk.Label(package_details, text='Total price\t: ', font=('Chalet Bold', 15), bootstyle='light' )
    total_price_label.place(relx=0.3, rely=0.7, anchor='w')

    #Creating a label to show the total price that the customers have to pay
    total_price_selected=btk.Label(package_details, text='RM'+str(total_price), font=('Chalet Bold', 15), bootstyle='light' )
    total_price_selected.place(relx=0.6, rely=0.7, anchor='w')

    #Creating a place for the customers to pay
    payment_menu=btk.Label(package_details, text='Payment\t\t:', font=('Chalet Bold', 15), bootstyle='light' )
    payment_menu.place(relx=0.3, rely=0.9, anchor='w')
    payment_var=tk.IntVar()
    payment=btk.Entry(package_details, font=('Chalet Bold', 15), bootstyle='light', textvariable=payment_var )
    payment.place(relx=0.53, rely=0.9, anchor='w')

    #Making sure that the customers can only enter numbers in the payment entry
    def only_numbers(char):
        return char.isdigit()
    validation = package_details.register(only_numbers)
    payment.config(validate="key", validatecommand=(validation, "%S"))

    #Making a button go to next page (final page)
    confirm_button=ctk.CTkButton(package_details, text='Confirm', corner_radius=0, command=lambda:load_page5()) 
    confirm_button.place(relx=0.9, rely=0.9, anchor='center')


#make separate page for packaging and ticket
def ticket_payment_page_summary():
    global payment
    #Creating a new frame to show the booking details
    ticket_details=btk.Frame(main_frame1)
    ticket_details.pack(expand=True, fill='both')

    #Creating a title for the booking details
    booking_details_title=btk.Label(ticket_details, text='Booking details', font=('Chalet Bold', 20), bootstyle='light' )
    booking_details_title.pack(side='top', padx=10, pady=10)

    #Creating a label to show the ticket type
    ticket_type_label=btk.Label(ticket_details, text='Ticket type\t: ', font=('Chalet Bold', 15), bootstyle='light' )
    ticket_type_label.place(relx=0.3, rely=0.3, anchor='w')

    #Creating a label to show the ticket amount
    ticket_amount_label=btk.Label(ticket_details, text='Ticket amount\t: ', font=('Chalet Bold', 15), bootstyle='light' )
    ticket_amount_label.place(relx=0.3, rely=0.4, anchor='w')

    #Creating a label to show the ride pass type
    ride_pass_type_label=btk.Label(ticket_details, text='Ride pass type\t: ', font=('Chalet Bold', 15), bootstyle='light' )
    ride_pass_type_label.place(relx=0.3, rely=0.5, anchor='w')

    #Creating a label to show the ride pass amount
    ride_pass_amount_label=btk.Label(ticket_details, text='Ride pass amount\t: ', font=('Chalet Bold', 15), bootstyle='light' )
    ride_pass_amount_label.place(relx=0.3, rely=0.6, anchor='w')

    #Creating a label to show the ticket type that the customers have chosen
    ticket_type_selected=btk.Label(ticket_details, text=selected_ticket_type, font=('Chalet Bold', 15), bootstyle='light' )
    ticket_type_selected.place(relx=0.6, rely=0.3, anchor='w')

    #Creating a label to show the ticket amount that the customers have chosen
    ticket_amount_selected=btk.Label(ticket_details, text=selected_ticket_amount, font=('Chalet Bold', 15), bootstyle='light' )
    ticket_amount_selected.place(relx=0.6, rely=0.4, anchor='w')

    #Creating a label to show the ride pass type that the customers have chosen
    ride_pass_type_selected=btk.Label(ticket_details, text=selected_ride_pass_type, font=('Chalet Bold', 15), bootstyle='light' )
    ride_pass_type_selected.place(relx=0.6, rely=0.5, anchor='w')

    #Creating a label to show the ride pass amount that the customers have chosen
    ride_pass_amount_selected=btk.Label(ticket_details, text=selected_ride_pass_amount, font=('Chalet Bold', 15), bootstyle='light' )
    ride_pass_amount_selected.place(relx=0.6, rely=0.6, anchor='w')

    #Creating a label to show the total price
    total_price_label=btk.Label(ticket_details, text='Total price\t: ', font=('Chalet Bold', 15), bootstyle='light' )
    total_price_label.place(relx=0.3, rely=0.7, anchor='w')

    #Creating a label to show the total price that the customers have to pay
    total_price_selected=btk.Label(ticket_details, text='RM'+str(total_price), font=('Chalet Bold', 15), bootstyle='light' )
    total_price_selected.place(relx=0.6, rely=0.7, anchor='w')

    #Creating a place for the customers to pay
    payment_menu=btk.Label(ticket_details, text='Payment\t\t:', font=('Chalet Bold', 15), bootstyle='light' )
    payment_menu.place(relx=0.3, rely=0.9, anchor='w')

    payment_var=tk.IntVar()
    payment_var=None
    payment=btk.Entry(ticket_details, font=('Chalet Bold', 15), bootstyle='light', textvariable=payment_var )
    payment.place(relx=0.53, rely=0.9, anchor='w')

    #Making sure that the customers can only enter numbers in the payment entry
    def only_numbers(char):
        return char.isdigit()
    validation = ticket_details.register(only_numbers)
    payment.config(validate="key", validatecommand=(validation, "%S"))

    #Making a button go to next page (final page)
    confirm_button=ctk.CTkButton(ticket_details, text='Confirm', corner_radius=0, command=lambda:load_page5())
    confirm_button.place(relx=0.9, rely=0.9, anchor='center')

def children_and_adult_or_senior_ticket_summary():
    global payment
    
    #Creating a new frame to show the booking details
    ticket_details=btk.Frame(main_frame1)
    ticket_details.pack(expand=True, fill='both')

    #Creating a title for the booking details
    booking_details_title=btk.Label(ticket_details, text='Booking details', font=('Chalet Bold', 20), bootstyle='light' )
    booking_details_title.pack(side='top', padx=10, pady=10)

    #Creating a label to show the children ticket type
    ticket_type_children_label=btk.Label(ticket_details, text='Ticket type\t: ', font=('Chalet Bold', 15), bootstyle='light' )
    ticket_type_children_label.place(relx=0.3, rely=0.2, anchor='w')

    #Creating a label to show the children ticket amount
    ticket_amount_children_label=btk.Label(ticket_details, text='Ticket amount\t: ', font=('Chalet Bold', 15), bootstyle='light' )
    ticket_amount_children_label.place(relx=0.3, rely=0.3, anchor='w')

    #Creating a label to show the ticket type
    ticket_type_label=btk.Label(ticket_details, text='Ticket type\t: ', font=('Chalet Bold', 15), bootstyle='light' )
    ticket_type_label.place(relx=0.3, rely=0.4, anchor='w')

    #Creating a label to show the ticket amount
    ticket_amount_label=btk.Label(ticket_details, text='Ticket amount\t: ', font=('Chalet Bold', 15), bootstyle='light' )
    ticket_amount_label.place(relx=0.3, rely=0.5, anchor='w')

    #Creating a label to show the ride pass type
    ride_pass_type_label=btk.Label(ticket_details, text='Ride pass type\t: ', font=('Chalet Bold', 15), bootstyle='light' )
    ride_pass_type_label.place(relx=0.3, rely=0.6, anchor='w')

    #Creating a label to show the ride pass amount
    ride_pass_amount_label=btk.Label(ticket_details, text='Ride pass amount\t: ', font=('Chalet Bold', 15), bootstyle='light' )
    ride_pass_amount_label.place(relx=0.3, rely=0.7, anchor='w')

    #Creating a label to show the children ticket type that the customers have chosen
    ticket_type_selected=btk.Label(ticket_details, text=selected_children_ticket, font=('Chalet Bold', 15), bootstyle='light' )
    ticket_type_selected.place(relx=0.6, rely=0.2, anchor='w')

    #Creating a label to show the  ticket amount that the customers have chosen
    ticket_amount_selected=btk.Label(ticket_details, text=selected_children_ticket_amount, font=('Chalet Bold', 15), bootstyle='light' )
    ticket_amount_selected.place(relx=0.6, rely=0.3, anchor='w')

    #Creating a label to show the ticket type that the customers have chosen
    ticket_type_selected=btk.Label(ticket_details, text=selected_ticket_type2, font=('Chalet Bold', 15), bootstyle='light' )
    ticket_type_selected.place(relx=0.6, rely=0.4, anchor='w')

    #Creating a label to show the ticket amount that the customers have chosen
    ticket_amount_selected=btk.Label(ticket_details, text=selected_ticket_amount2, font=('Chalet Bold', 15), bootstyle='light' )
    ticket_amount_selected.place(relx=0.6, rely=0.5, anchor='w')

    #Creating a label to show the ride pass type that the customers have chosen
    ride_pass_type_selected=btk.Label(ticket_details, text=selected_ride_pass_type, font=('Chalet Bold', 15), bootstyle='light' )
    ride_pass_type_selected.place(relx=0.6, rely=0.6, anchor='w')

    #Creating a label to show the ride pass amount that the customers have chosen
    ride_pass_amount_selected=btk.Label(ticket_details, text=selected_ride_pass_amount, font=('Chalet Bold', 15), bootstyle='light' )
    ride_pass_amount_selected.place(relx=0.6, rely=0.7, anchor='w')

    #Creating a label to show the total price
    total_price_label=btk.Label(ticket_details, text='Total price\t: ', font=('Chalet Bold', 15), bootstyle='light' )
    total_price_label.place(relx=0.3, rely=0.8, anchor='w')

    #Creating a label to show the total price that the customers have to pay
    total_price_selected=btk.Label(ticket_details, text='RM'+str(total_price), font=('Chalet Bold', 15), bootstyle='light' )
    total_price_selected.place(relx=0.6, rely=0.8, anchor='w')

    #Creating a place for the customers to pay
    payment_menu=btk.Label(ticket_details, text='Payment\t\t:', font=('Chalet Bold', 15), bootstyle='light' )
    payment_menu.place(relx=0.3, rely=0.9, anchor='w')

    payment_var=tk.IntVar()
    payment=btk.Entry(ticket_details, font=('Chalet Bold', 15), bootstyle='light', textvariable=payment_var )
    payment.place(relx=0.53, rely=0.9, anchor='w')

    #Making sure that the customers can only enter numbers in the payment entry
    def only_numbers(char):
        return char.isdigit()
    validation = ticket_details.register(only_numbers)
    payment.config(validate="key", validatecommand=(validation, "%S"))

    #Making a button go to next page (final page)
    confirm_button=ctk.CTkButton(ticket_details, text='Confirm', corner_radius=0, command=lambda:load_page5())
    confirm_button.place(relx=0.9, rely=0.9, anchor='center')

def load_page5():
    global payment_page
    global finish_page
    finish_page=True
    #This is total payment from customer
    if sum.repayment_page==True:
        payment_data= sum.payment_var()
        sum.repayment_page=False
        print('hi')
    else:
        payment_data= payment.get()
        print('hello')
    
    payment_page= True

    #Clearing the previous page
    clear_page(main_frame1)

    if payment_data and payment_data.isdigit():
    #Determine whenever that the payment is enough or not
        if int(payment_data) < int(total_price) :
            sum.load_repayment_page(main_frame1, total_price, clear_page,load_page5)
        elif int(payment_data) > int(total_price):
            sum.change_page(main_frame1, total_price, payment_data, load_page2)
        elif int(payment_data) == int(total_price):
            sum.thank_you_page(main_frame1, load_page2)
        else:
            print('error')
    else:
        sum.load_repayment_page()    
#This is the final page
# def load_page5():
#     global payment_page
#     global finish_page
#     finish_page=True
#     #This is total payment from customer
#     payment_data= payment.get()
#     payment_page= True

#     #Clearing the previous page
#     clear_page(main_frame1)

#     # #Creating a new main frame to show the process of the payment
#     # main_frame3=btk.Frame(window)
#     # main_frame3.grid(row=0, rowspan=5, column=0, columnspan=5, sticky='news')
#     if payment_data and payment_data.isdigit():
#     #Determine whenever that the payment is enough or not
#         if int(payment_data) < int(total_price) :
#             sum.load_repayment_page(main_frame1, total_price, clear_page,sum.load_page5)
#         elif int(payment_data) > int(total_price):
        
#             #If the payment is enough, a new frame will be created to show the change
#             change_frame=btk.Frame(main_frame1)
#             change_frame.pack(expand=True, fill='both')

#             #Allow the customer to see the change
#             change_label=btk.Label(change_frame, text='Change: RM'+str(int(payment_data)-total_price), font=('Chalet Bold', 15), bootstyle='light' )
#             change_label.place(relx=0.5, rely=0.5, anchor='center')

#             thank_you=btk.Label(change_frame, text='Thank you for your purchase', font=('Chalet Bold', 15), bootstyle='light' )
#             thank_you.place(relx=0.5, rely=0.6, anchor='center')
#             #Creating a button to allow the customer to go back to the first page
#             back_button=ctk.CTkButton(change_frame, text='Book again', corner_radius=0, command=lambda:load_page2())
#             back_button.place(relx=0.5, rely=0.7, anchor='center')

#         elif int(payment_data) == int(total_price):
        
#             #If the payment is just enough, a new frame will be created to show the thank you message
#             thank_you_frame=btk.Frame(main_frame1)
#             thank_you_frame.pack(expand=True, fill='both')

#             thank_you_label=btk.Label(thank_you_frame, text='Thank you for your purchase', font=('Chalet Bold', 15), bootstyle='light' )
#             thank_you_label.place(relx=0.5, rely=0.5, anchor='center')
#             #Creating a button to allow the customer to go back to the first page
#             back_button=ctk.CTkButton(thank_you_frame, text='Book again', corner_radius=0, command=lambda:load_page2())
#             back_button.place(relx=0.5, rely=0.7, anchor='center')
#         else:
#             print('error')
#     else:
#         sum.load_repayment_page()        
#Creating a new page to allow the customer to pay again
# def load_repayment_page():
    # global payment_page
    # global payment
    # global payment_var
    # global total_price
    # global repayment_page 
    # repayment_page=True
    # #Clearing the previous page
    # clear_page(main_frame1)

    # #Creating a new frame to show the process of the payment
    # repayment_frame=btk.Frame(main_frame1)
    # repayment_frame.pack(expand=True, fill='both')

    # #Creating a label to show the error message
    # error_label=btk.Label(repayment_frame, text='Payment is not enough', font=('Chalet Bold', 15), bootstyle='light' )
    # error_label.place(relx=0.5, rely=0.4, anchor='center')

    # #Creating a label to show the total price
    # total_price_label=btk.Label(repayment_frame, text='Total price\t: ', font=('Chalet Bold', 15), bootstyle='light' )
    # total_price_label.place(relx=0.3, rely=0.5, anchor='w')

    # #Creating a label to show the total price that the customers have to pay
    # total_price_selected=btk.Label(repayment_frame, text='RM'+str(total_price), font=('Chalet Bold', 15), bootstyle='light' )
    # total_price_selected.place(relx=0.6, rely=0.5, anchor='w')

    # #Creating a label to show the payment
    # payment_menu=btk.Label(repayment_frame, text='Payment\t\t:', font=('Chalet Bold', 15), bootstyle='light' )
    # payment_menu.place(relx=0.3, rely=0.6, anchor='w')
    # payment_var=tk.IntVar()
    # payment=btk.Entry(repayment_frame, font=('Chalet Bold', 15), bootstyle='light', textvariable=payment_var )
    # payment.place(relx=0.53, rely=0.6, anchor='w')

    # #Making sure that the customers can only enter numbers in the payment entry
    # def only_numbers(char):
    #     return char.isdigit()
    # validation = repayment_frame.register(only_numbers)
    # payment.config(validate="key", validatecommand=(validation, "%S"))

    # #Creating a button to confirm the payment
    # confirm_button=ctk.CTkButton(repayment_frame, text='Confirm', corner_radius=0, command=lambda:load_page5())
    # confirm_button.place(relx=0.9, rely=0.6, anchor='center')  

#This page is activated when children ticket is chosen
def load_parenting_page():

    global parent_page
    global ticket_type2
    global ticket_amount2
    parent_page=True
    #Clearing the previous page
    clear_page(main_frame1)   
    ticket_amount_var2=tk.IntVar()
    ticket_amount_var2.set('0')
    #Creating a label that show the children ticket and the amount choosen by customer
    children_label=btk.Label(main_frame1, text='Children ticket\t: '+str(selected_children_ticket_amount), font=('Chalet Bold', 15), bootstyle='light' )
    children_label.place(relx=0.5, rely=0.3, anchor='center')

    #Creating a combobox to allow the customer to choose the other two types of ticket (Senior,Adult)
    ticket_type2=ctk.CTkComboBox(main_frame1, values=['Adult', 'Senior citizen'], state='readonly')
    ticket_type2.place(relx=0.5, rely=0.45, anchor='center')

    #Creating a spinbox to allow the customer to choose the amount of ticket
    ticket_amount2=btk.Spinbox(main_frame1,text='Amount', from_=0, to=1000, textvariable=ticket_amount_var2)
    ticket_amount2.place(relx=0.75, rely=0.45, anchor='center')

    #Creating a button to confirm the ticket
    confirm_button=ctk.CTkButton(main_frame1, text='Confirm', corner_radius=0, command=lambda:children_others_details())
    confirm_button.place(relx=0.5, rely=0.7, anchor='center')

    #Creating a label for information
    information_label=btk.Label(main_frame1, text='There must be atleast one adult/senior ticket booked together with children ticket for safety purposes', font=('Chalet Bold', 15), bootstyle='light' )
    information_label.place(relx=0.5, rely=0.8, anchor='center')

#To prevent the spinbox from sycnhronizing with each others and setting the initial value to 0 for spinbox
ticket_amount_var = tk.IntVar()
ticket_amount_var.set('0')
ride_pass_amount_var = tk.IntVar()
ride_pass_amount_var.set('0')
package_amount_var = tk.IntVar()
package_amount_var.set('0')


load_page1()

#running
window.mainloop()


