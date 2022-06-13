from tkinter import *
from PIL import ImageTk, Image
from pathlib import Path
from random import *

class Main:
    def __init__(self, parent):
        self.parent = parent
        current_dir = Path(__file__).absolute().parent
        self.logo = ImageTk.PhotoImage(Image.open(current_dir / "img/ormiston_logo.png"))
        self.create_pages()
        self.update_current_page()

    def create_pages(self):
        self.current_page = 0
        self.pages = []


        # Title Page
        title_screen = Frame(self.parent, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
        Label(title_screen, image=self.logo).place(x=30, y=30)
        Frame(title_screen, 
              width=root.winfo_screenwidth()/1.2, height=root.winfo_screenheight()/2, 
              bg="#775B59", highlightbackground="#595959", highlightthickness=3).place(relx=0.5, rely=0.51, anchor=CENTER)
        Frame(title_screen, 
              width=root.winfo_screenwidth()/1.2, height=root.winfo_screenheight()/6, 
              bg="#5BC5DA", highlightbackground="#595959", highlightthickness=3).place(relx=0.5, rely=1/3, anchor=CENTER)
        Label(title_screen, background="#5BC5DA", text="OSC's Cafe Kiosk", font=("Verdana", 52, "bold")).place(relx=0.5, rely=1/3, anchor=CENTER)
        Button(title_screen, background="#A6D3A0", activebackground="#86C380", text="Proceed", font=("Verdana", 23, "bold"), command=self.next_page).place(relx=0.5, rely=0.575, anchor=CENTER)
        self.pages.append(title_screen)


        # Menu Page
        menu_screen = Frame(self.parent, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
        Label(menu_screen, image=self.logo).place(relx=0.69, rely=0.06)
        Label(menu_screen, text="OSC's Cafe Kiosk", font=("Verdana", 52, "bold")).place(relx=1/3, y=100, anchor=CENTER)
        Frame(menu_screen, 
              width=root.winfo_screenwidth()/1.044, height=root.winfo_screenheight()/1.57, 
              bg="#775B59", highlightbackground="#595959", highlightthickness=3).place(relx=0.5, rely=0.55, anchor=CENTER)
        Frame(menu_screen, 
              width=root.winfo_screenwidth()/1.044, height=root.winfo_screenheight()/6, 
              bg="#5BC5DA", highlightbackground="#595959", highlightthickness=3).place(relx=0.5, rely=0.29, anchor=CENTER)
        Label(menu_screen, background="#5BC5DA", text="Menu", font=("Verdana", 42, "bold")).place(relx=0.5, rely=0.29, anchor=CENTER)
        Button(menu_screen, background="#A6D3A0", activebackground="#86C380", text="Cancel", font=("Verdana", 16, "bold"), command=self.prev_page).place(relx=0.1, rely=0.935, anchor=CENTER)
        Button(menu_screen, background="#A6D3A0", activebackground="#86C380", text="Confirm", font=("Verdana", 16, "bold"), command=self.next_page).place(relx=0.9, rely=0.935, anchor=CENTER)
        # ADD MENU PLEASE DONT FORGET
        self.pages.append(menu_screen)


        # Order Confirm Page
        order_screen = Frame(self.parent, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
        Label(order_screen, image=self.logo).place(relx=0.69, rely=0.06)
        Label(order_screen, text="OSC's Cafe Kiosk", font=("Verdana", 52, "bold")).place(relx=1/3, y=100, anchor=CENTER)
        Frame(order_screen, 
              width=root.winfo_screenwidth()/1.044, height=root.winfo_screenheight()/1.57, 
              bg="#775B59", highlightbackground="#595959", highlightthickness=3).place(relx=0.5, rely=0.55, anchor=CENTER)
        Frame(order_screen, 
              width=root.winfo_screenwidth()/1.044, height=root.winfo_screenheight()/6, 
              bg="#5BC5DA", highlightbackground="#595959", highlightthickness=3).place(relx=0.5, rely=0.29, anchor=CENTER)
        Label(order_screen, background="#5BC5DA", text="Order Confirmation", font=("Verdana", 42, "bold")).place(relx=0.5, rely=0.29, anchor=CENTER)
        Button(order_screen, background="#A6D3A0", activebackground="#86C380", text="Menu", font=("Verdana", 16, "bold"), command=self.prev_page).place(relx=0.1, rely=0.935, anchor=CENTER)
        Button(order_screen, background="#A6D3A0", activebackground="#86C380", text="Confirm", font=("Verdana", 16, "bold"), command=self.next_page).place(relx=0.9, rely=0.935, anchor=CENTER)
        # ADD ORDERS PLEASE DONT FORGET
        self.pages.append(order_screen)


        # Payment Method Page
        pay_method_screen = Frame(self.parent, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
        Label(pay_method_screen, text="OSC's Cafe Kiosk", font=("Verdana", 52, "bold")).place(relx=1/3, y=100, anchor=CENTER)
        Label(pay_method_screen, image=self.logo).place(relx=0.69, rely=0.06)
        Frame(pay_method_screen, 
              width=root.winfo_screenwidth()/1.044, height=root.winfo_screenheight()/1.57, 
              bg="#775B59", highlightbackground="#595959", highlightthickness=3).place(relx=0.5, rely=0.55, anchor=CENTER)
        Frame(pay_method_screen, 
              width=root.winfo_screenwidth()/1.044, height=root.winfo_screenheight()/6, 
              bg="#5BC5DA", highlightbackground="#595959", highlightthickness=3).place(relx=0.5, rely=0.29, anchor=CENTER)
        Label(pay_method_screen, background="#5BC5DA", text="Payment Options", font=("Verdana", 42, "bold")).place(relx=0.5, rely=0.29, anchor=CENTER)
        Button(pay_method_screen, background="#EEE", activebackground="#CCC", text="Cash", font=("Verdana", 42, "bold"), command=self.last_page, width=14, height=4).place(relx=0.265, rely=0.62, anchor=CENTER)
        Button(pay_method_screen, background="#EEE", activebackground="#CCC", text="Card", font=("Verdana", 42, "bold"), command=self.next_page, width=14, height=4).place(relx=0.735, rely=0.62, anchor=CENTER)
        Button(pay_method_screen, background="#A6D3A0", activebackground="#86C380", text="Edit Order", font=("Verdana", 16, "bold"), command=self.prev_page).place(relx=0.5, rely=0.935, anchor=CENTER)
        self.pages.append(pay_method_screen)


        # Paying With Card Page
        card_screen = Frame(self.parent, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
        Label(card_screen, text="OSC's Cafe Kiosk", font=("Verdana", 52, "bold")).place(relx=1/3, y=100, anchor=CENTER)
        Label(card_screen, image=self.logo).place(relx=0.69, rely=0.06)
        Frame(card_screen, 
              width=root.winfo_screenwidth()/1.044, height=root.winfo_screenheight()/1.57, 
              bg="#775B59", highlightbackground="#595959", highlightthickness=3).place(relx=0.5, rely=0.55, anchor=CENTER)
        Frame(card_screen, 
              width=root.winfo_screenwidth()/1.078, height=root.winfo_screenheight()/2.399, 
              bg="#EEE", highlightbackground="#595959", highlightthickness=3).place(relx=0.5, rely=0.615, anchor=CENTER)
        Frame(card_screen, 
              width=root.winfo_screenwidth()/1.044, height=root.winfo_screenheight()/6, 
              bg="#5BC5DA", highlightbackground="#595959", highlightthickness=3).place(relx=0.5, rely=0.29, anchor=CENTER)
        Label(card_screen, background="#5BC5DA", text="Please enter card details", font=("Verdana", 32, "bold")).place(relx=0.5, rely=0.29, anchor=CENTER)
        Button(card_screen, background="#A6D3A0", activebackground="#86C380", text="Change Payment", font=("Verdana", 16, "bold"), command=self.prev_page).place(relx=0.15, rely=0.935, anchor=CENTER)
        Button(card_screen, background="#A6D3A0", activebackground="#86C380", text="Confirm", font=("Verdana", 16, "bold"), command=self.next_page).place(relx=0.9, rely=0.935, anchor=CENTER)
        Label(card_screen, background="#EEE", text="Card Number:", font=("Verdana", 22, "bold")).place(relx=0.5, rely=0.49, anchor=CENTER)
        e1 = Entry(card_screen, background="#FFF", fg="#CCC", font=("Verdana", 22, "bold"), justify="center")
        e1.insert(0, "XXXX-XXXX-XXXX-XXXX")
        e1.bind("<FocusIn>", lambda args: e1.delete("0", "end"))
        e1.bind("<FocusIn>", lambda args: e1.config(fg="#000"), add="+")
        e1.place(relx=0.5, rely=0.55, anchor=CENTER)
        Label(card_screen, background="#EEE", text="PIN:", font=("Verdana", 22, "bold")).place(relx=0.5, rely=0.64, anchor=CENTER)
        e2 = Entry(card_screen, background="#FFF", fg="#CCC", font=("Verdana", 22, "bold"), justify="center")
        e2.insert(0, "XXXX")
        e2.bind("<FocusIn>", lambda args: e2.delete("0", "end"))
        e2.bind("<FocusIn>", lambda args: e2.config(fg="#000"), add="+")
        e2.place(relx=0.5, rely=0.7, anchor=CENTER)
        self.pages.append(card_screen)

        
        # Order Number Page
        number_screen = Frame(self.parent, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
        Label(number_screen, text="OSC's Cafe Kiosk", font=("Verdana", 52, "bold")).place(relx=1/3, y=100, anchor=CENTER)
        Label(number_screen, image=self.logo).place(relx=0.69, rely=0.06)
        Frame(number_screen, 
              width=root.winfo_screenwidth()/1.044, height=root.winfo_screenheight()/1.57, 
              bg="#775B59", highlightbackground="#595959", highlightthickness=3).place(relx=0.5, rely=0.55, anchor=CENTER)
        Frame(number_screen, 
              width=root.winfo_screenwidth()/1.078, height=root.winfo_screenheight()/2.399, 
              bg="#EEE", highlightbackground="#595959", highlightthickness=3).place(relx=0.5, rely=0.615, anchor=CENTER)
        Frame(number_screen, 
              width=root.winfo_screenwidth()/1.044, height=root.winfo_screenheight()/6, 
              bg="#5BC5DA", highlightbackground="#595959", highlightthickness=3).place(relx=0.5, rely=0.29, anchor=CENTER)
        Label(number_screen, background="#5BC5DA", text="Thank you for ordering!", font=("Verdana", 42, "bold")).place(relx=0.5, rely=0.29, anchor=CENTER)
        Label(number_screen, background="#EEE", text=f"Order Number: #{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}", font=("Verdana", 52, "bold")).place(relx=0.5, rely=0.615, anchor=CENTER)
        Button(number_screen, background="#A6D3A0", activebackground="#86C380", text="Finish", font=("Verdana", 16, "bold"), command=self.first_page).place(relx=0.5, rely=0.935, anchor=CENTER)
        self.pages.append(number_screen)

    def next_page(self):
        self.current_page += 1
        self.update_current_page()

    def prev_page(self):
        self.current_page -= 1
        self.update_current_page()

    def first_page(self):
        self.current_page = 0
        self.update_current_page()

    def last_page(self):
        self.current_page = 5
        self.update_current_page()

    def update_current_page(self):
        for page in self.pages:
            page.pack_forget()

        self.pages[self.current_page].pack()
        
        Button(self.parent, background="#F00", activebackground="#E32A2A", text=" X ", font=("Verdana", 13, "bold"), command=self.parent.destroy).place(relx=1, rely=0, anchor=NE)

root = Tk()
root.overrideredirect(True)
root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
main = Main(root)
root.mainloop()
