import customtkinter as ctk
import openpyxl
from openpyxl import Workbook
#Creating function to calculate the total price for adult ticket

def price_calculation_ticket(type,amt):
    if type=='Adult':
        adult_price=int(amt)*20
        return adult_price
    elif type=='Children':
        child_price=int(amt)*12
        return child_price
    elif type=='Senior citizen':
        senior_price=int(amt)*16
        return senior_price
    else :
        print('Invalid input')

def price_calculation_pass(type,amt):
    if type=='Roller coaster ride':
        roller_price=int(amt)*12
        return roller_price
    elif type=='Ghost house':
        ghost_price=int(amt)*10
        return ghost_price
    elif type=='Pirate ship ride':
        pirate_price=int(amt)*11
        return pirate_price
    else :
        print('Invalid input')

def price_calculation_package(type,amt):
    if type=='Group of 5 individuals':
        group_price=int(amt)*75
        return group_price
    elif type=='Family':
        family_price=int(amt)*50
        return family_price
    else :
        print('Invalid input')


#Creating a slidebar class
class slidebar(ctk.CTkFrame):
    def __init__(self, parent, start_pos, end_pos):
        super().__init__(parent)

    #general attributes
        self.start_pos=start_pos+0.008
        self.end_pos=end_pos
        self.height=abs(start_pos-end_pos)

    #animation logic
        self.pos = start_pos
        self.in_start_pos = True

    #layout
        self.place(relx=0.05,rely=self.start_pos,relwidth=0.9,relheight=self.height)  
    
    #determining whenever the sliderbar is in start position or end position
    def animate(self):
        if self.in_start_pos:
            self.animate_upwards()
        else:
            self.animate_downwards()
    
    #when the sliderbar is in start position, it will move upwards
    def animate_upwards(self):
        if self.pos > self.end_pos:
            self.pos -= 0.005
            self.place(relx=0.05,rely=self.pos,relwidth=0.9,relheight=self.height)
            self.after(10, self.animate_upwards)
        else:
            self.in_start_pos = False
    #when the sliderbar is in end position, it will move downwards
    def animate_downwards(self):
        if self.pos < self.start_pos:
            self.pos += 0.005
            self.place(relx=0.05,rely=self.pos,relwidth=0.9,relheight=self.height)
            self.after(10, self.animate_downwards)
        else:
            self.in_start_pos = True




#  if ticket_pass_page==True:
#         if ride_pass_page==True:
#             selected_ticket_type=tk.StringVar()
#             selected_ticket_amount=tk.IntVar()
            
#             selected_ride_pass_type=tk.StringVar()
#             selected_ride_pass_amount=tk.IntVar()

#             selected_ticket_type=ticket_type.get()
#             selected_ticket_amount=ticket_amount.get()

#             selected_ride_pass_type=ride_pass_type.get()
#             selected_ride_pass_amount=ride_pass_amount.get()

#             if selected_ticket_type=='Adult':
#                 adult_price=cal.total_adult_price(selected_ticket_amount)
#                 if selected_ride_pass_type=='Roller coaster ride':
#                     roller_price=cal.total_roller_price(selected_ride_pass_amount)
#                     total_price=adult_price+roller_price
#                 elif selected_ride_pass_type=='Ghost house':
#                     ghost_price=cal.total_ghost_price(selected_ride_pass_amount)
#                     total_price=adult_price+ghost_price
#                 elif selected_ride_pass_type=='Pirate ship ride':
#                     pirate_price=cal.total_pirate_price(selected_ride_pass_amount)
#                     total_price=adult_price+pirate_price
#             elif selected_ticket_type=='Children':
#                 selected_children_ticket_amount=selected_ticket_amount
#                 #This will active the parent page
#                 children_price=cal.total_child_price(selected_children_ticket_amount)
#                 if selected_ride_pass_type=='Roller coaster ride':
#                     roller_price=cal.total_roller_price(selected_ride_pass_amount)
#                     total_price=children_price+roller_price
#                 elif selected_ride_pass_type=='Ghost house':
#                     ghost_price=cal.total_ghost_price(selected_ride_pass_amount)
#                     total_price=children_price+ghost_price
#                 elif selected_ride_pass_type=='Pirate ship ride':
#                     pirate_price=cal.total_pirate_price(selected_ride_pass_amount)
#                     total_price=children_price+pirate_price
#             elif selected_ticket_type=='Senior citizen':
#                 senior_price=cal.total_senior_price(selected_ticket_amount)
#                 if selected_ride_pass_type=='Roller coaster ride':
#                     roller_price=cal.total_roller_price(selected_ride_pass_amount)
#                     total_price=senior_price+roller_price
#                 elif selected_ride_pass_type=='Ghost house':
#                     ghost_price=cal.total_ghost_price(selected_ride_pass_amount)
#                     total_price=senior_price+ghost_price
#                 elif selected_ride_pass_type=='Pirate ship ride':
#                     pirate_price=cal.total_pirate_price(selected_ride_pass_amount)
#                     total_price=senior_price+pirate_price
#         else:
#             selected_ticket_type=tk.StringVar()
#             selected_ticket_amount=tk.IntVar()

#             selected_ticket_type=ticket_type.get()
#             selected_ticket_amount=ticket_amount.get()

#             if selected_ticket_type=='Adult':
#                 adult_price=cal.total_adult_price(selected_ticket_amount)
#                 total_price=adult_price
#             elif selected_ticket_type=='Children':
#                 children_price=cal.total_child_price(selected_ticket_amount)
#                 total_price=children_price
#             elif selected_ticket_type=='Senior citizen':
#                 senior_price=cal.total_senior_price(selected_ticket_amount)
#                 total_price=senior_price
            
#     elif package_pass_page==True:
#         if ride_pass_page==True:
#             selected_package_type=tk.StringVar()
#             selected_package_amount=tk.IntVar()
            
#             selected_ride_pass_type=tk.StringVar()
#             selected_ride_pass_amount=tk.IntVar()

#             selected_package_type=package_type.get()
#             selected_package_amount=package_amount.get()
#             selected_ride_pass_type=ride_pass_type.get()
#             selected_ride_pass_amount=ride_pass_amount.get()
#             if selected_package_type=='Group of 5 individuals':
#                 group_price=cal.total_group_price(selected_package_amount)
#                 if selected_ride_pass_type=='Roller coaster ride':
#                     roller_price=cal.total_roller_price(selected_ride_pass_amount)
#                     total_price=group_price+roller_price
#                 elif selected_ride_pass_type=='Ghost house':
#                     ghost_price=cal.total_ghost_price(selected_ride_pass_amount)
#                     total_price=group_price+ghost_price
#                 elif selected_ride_pass_type=='Pirate ship ride':
#                     pirate_price=cal.total_pirate_price(selected_ride_pass_amount)
#                     total_price=group_price+pirate_price
#             elif selected_package_type=='Family':
#                 family_price=cal.total_family_price(selected_package_amount)
#                 if selected_ride_pass_type=='Roller coaster ride':
#                     roller_price=cal.total_roller_price(selected_ride_pass_amount)
#                     total_price=family_price+roller_price
#                 elif selected_ride_pass_type=='Ghost house':
#                     ghost_price=cal.total_ghost_price(selected_ride_pass_amount)
#                     total_price=family_price+ghost_price
#                 elif selected_ride_pass_type=='Pirate ship ride':
#                     pirate_price=cal.total_pirate_price(selected_ride_pass_amount)
#                     total_price=family_price+pirate_price
#         else:
#             selected_package_type=tk.StringVar()
#             selected_package_amount=tk.IntVar()

#             selected_package_type=package_type.get()
#             selected_package_amount=package_amount.get()
#             if selected_package_type=='Group of 5 individuals':
#                 group_price=cal.total_group_price(selected_package_amount)
#                 total_price=group_price
#             elif selected_package_type=='Family':
#                 family_price=cal.total_family_price(selected_package_amount)
#                 total_price=family_price
#     if parent_page==True:



