from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
root = Tk()
root.geometry("900x500")

burger = ImageTk.PhotoImage(Image.open("burger1.png"))
burger_image=Label(root)
burger_image["image"]= burger
burger_image.place(relx=0.7, rely=0.5, anchor=CENTER)

label_heading = Label(root, text="VFood", font=("times",40,"bold"), fg="Red")
label_heading.place(relx=0.7, rely=0.1, anchor=CENTER)

label_select_dish = Label(root,text="Select Dish",font=("times",15))
label_select_dish.place(relx=0.06, rely=0.02, anchor=CENTER)

dish=["burger","Lava_Cake"]
dish_dropdown = ttk.Combobox(root, state = "readonly", values = dish)
dish_dropdown.place(relx=0.25, rely=0.2, anchor=CENTER)

label_select_addons = Label(root,text="Select Add-Ons", font=("times",15))
label_select_addons.place(relx=0.08, rely=0.5,anchor=CENTER)

toppings=[]
toppings_dropdown = ttk.Combobox(root,state = "readonly", values = toppings)
toppings_dropdown.place(relx=0.25, rely=0.5, anchor=CENTER)

dish_amount = Label(root,font=("times",15,"bold"))
dish_amount.place(relx=0.2,rely=0.75, anchor=CENTER)

class parent():
    
    def __init__(self):
        print("This is a parent class")
        
    def menu(dish):
        if dish=="burger":
            print("You can add following toppings")
            toppings=["cheese","jalapeno"]
            toppings_dropdown["values"]=toppings
            print("More Chesse | Add jalapeno")
        elif dish=="Lava_Cake":
            print("You can add following toppings")
            toppings=["oreo","caramel"]
            toppings_dropdown["values"]=toppings
            print("Add Oreo flavour | Add caramel flavour")
        else:
            print("Please enter valid dish")
            
    def final_ammount(dish, add_ons):
        if dish=="burger" and add_ons=="cheese":
            dish_amount["text"]="You need to pay $ 250"
            print("You need to pay $ 250")
        elif dish=="burger" and add_ons=="jalepeeno":
            dish_amount["text"]="You need to pay $ 450"
            print("You need to pay $ 450")
        elif dish=="Lava_Cake" and add_ons=="oreo":
            dish_amount["text"]="You need to pay $ 350"
            print("You need to pay $ 350")
        elif dish=="Lava_Cake" and add_ons=="caramel":
            dish_amount["text"]="You need to pay $ 250"
            print("You need to pay $ 250")

class child1(parent):
    
    def __init__(self, dish):
        self.new_dish = dish
    def get_menu(self):
        new_dish=dish_dropdown.get()
        parent.menu(new_dish)
        
class child2(parent):
    
    def __init__(self ,dish,addons):
        self.new_dish = dish
        self.addons = addons
    
    def get_final_ammount(self):
        new_dish=dish_dropdown.get()
        addons=toppings_dropdown.get()
        parent.final_ammount(self.new_dish, self.addons)
        
child1_object=child1("burger",)
child1_object.get_menu()

root.mainloop()

child2_object=child2("iced_americano", "oreo")
child2_object.get_final_ammount()

root.mainloop()