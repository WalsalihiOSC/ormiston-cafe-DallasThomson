from tkinter import *
from PIL import ImageTk, Image
from pathlib import Path
from random import *  

class Item:
    def __init__(self, data):
        self.name = data[0]
        self.price = float(data[1])

class Main:
    def __init__(self, parent):
        self.parent = parent
        current_dir = Path(__file__).absolute().parent
        self.logo = ImageTk.PhotoImage(Image.open(current_dir / "img/ormiston_logo.png"))
        self.sandwiches = []
        self.salads = []
        self.rice_meals = []
        self.drinks = []
        for sandwich in list((current_dir / "menu/sandwiches.txt").read_text().split("\n")):
            self.sandwiches.append(Item(list(sandwich.split(";"))))
        

        self.create_pages()
        self.update_current_page()


    def create_pages(self):
        self.current_page = 0
        self.pages = []
        self.create_title_page()
        self.create_menu_page()
        self.create_order_page()
        self.create_pay_method_page()
        self.create_card_page()
        self.create_number_page()

    def create_title_page(self):
        title_screen = Frame(self.parent, width=WIDTH, height=HEIGHT)
        Label(title_screen, image=self.logo).place(relx=1/50, rely=1/12)
        Frame(title_screen, width=WIDTH/1.2, height=HEIGHT/2, bg="#775B59", highlightbackground="#595959", highlightthickness=3).place(relx=0.5, rely=0.51, anchor=CENTER)
        Frame(title_screen, width=WIDTH/1.2, height=HEIGHT/6, bg="#5BC5DA", highlightbackground="#595959", highlightthickness=3).place(relx=0.5, rely=1/3, anchor=CENTER)
        Label(title_screen, background="#5BC5DA", fg="black", text="OSC's Cafe Kiosk", font=("Verdana", 52, "bold")).place(relx=0.5, rely=1/3, anchor=CENTER)
        Button(title_screen, cursor=MOUSE_HOVER, background="#A6D3A0", activebackground="#86C380", text="Proceed", font=("Verdana", 23, "bold"), command=self.next_page).place(relx=0.5, rely=0.575, anchor=CENTER)
        self.pages.append(title_screen)

    def create_menu_page(self):
        menu_screen = Frame(self.parent, width=WIDTH, height=HEIGHT)
        Label(menu_screen, image=self.logo).place(relx=0.69, rely=0.06)
        Label(menu_screen, text="OSC's Cafe Kiosk", font=("Verdana", 52, "bold")).place(relx=1/3, rely=0.12, anchor=CENTER)
        Frame(menu_screen, width=WIDTH/1.044, height=HEIGHT/1.57, bg="#775B59", highlightbackground="#595959", highlightthickness=3).place(relx=0.5, rely=0.55, anchor=CENTER)
        Frame(menu_screen, width=WIDTH/1.044, height=HEIGHT/6, bg="#5BC5DA", highlightbackground="#595959", highlightthickness=3).place(relx=0.5, rely=0.29, anchor=CENTER)
        Label(menu_screen, background="#5BC5DA", text="Menu", font=("Verdana", 42, "bold")).place(relx=0.5, rely=0.29, anchor=CENTER)
        Button(menu_screen, cursor=MOUSE_HOVER, background="#A6D3A0", activebackground="#86C380", text="Cancel", font=("Verdana", 16, "bold"), command=self.prev_page).place(relx=0.1, rely=0.935, anchor=CENTER)
        Button(menu_screen, cursor=MOUSE_HOVER, background="#A6D3A0", activebackground="#86C380", text="Confirm", font=("Verdana", 16, "bold"), command=self.next_page).place(relx=0.9, rely=0.935, anchor=CENTER)
        f = Frame(menu_screen, width=WIDTH/1.1, height=HEIGHT/2.5)
        f.place(relx=0.5, rely=0.62, anchor=CENTER)
        c = Canvas(f)
        scroll = Scrollbar(c, orient="vertical", command=c.yview)
        c.configure(yscrollcommand=scroll.set)
        scroll.pack(side="right", fill="y")
        c.pack(padx=10, pady=10)
        c.configure(scrollregion=c.bbox("all"))
        c.grid_propagate(False)
        self.menu_elements = Frame(c, width=WIDTH/1.13, height=HEIGHT/2.5)
        self.menu_elements.pack()
        self.menu_elements.grid_propagate(False)
        self.menu_elements.pack_propagate(False)
        self.fill_menu()
        self.pages.append(menu_screen)

    def fill_menu(self):
        for i in range(4):
            self.menu_elements.grid_columnconfigure(i, minsize=WIDTH/1.13/4)

        for index, sandwich in enumerate(self.sandwiches):
            f = Frame(self.menu_elements)
            f.grid(column=index%4, row=index//4, sticky=EW)
            Label(f, text=f"{sandwich.name}: ${sandwich.price:.2f}").pack()

    def create_order_page(self):
        order_screen = Frame(self.parent, width=WIDTH, height=HEIGHT)
        Label(order_screen, image=self.logo).place(relx=0.69, rely=0.06)
        Label(order_screen, text="OSC's Cafe Kiosk", font=("Verdana", 52, "bold")).place(relx=1/3, rely=0.12, anchor=CENTER)
        Frame(order_screen, width=WIDTH/1.044, height=HEIGHT/1.57, bg="#775B59", highlightbackground="#595959", highlightthickness=3).place(relx=0.5, rely=0.55, anchor=CENTER)
        Frame(order_screen, width=WIDTH/1.044, height=HEIGHT/6, bg="#5BC5DA", highlightbackground="#595959", highlightthickness=3).place(relx=0.5, rely=0.29, anchor=CENTER)
        Label(order_screen, background="#5BC5DA", text="Order Confirmation", font=("Verdana", 42, "bold")).place(relx=0.5, rely=0.29, anchor=CENTER)
        Button(order_screen, cursor=MOUSE_HOVER, background="#A6D3A0", activebackground="#86C380", text="Menu", font=("Verdana", 16, "bold"), command=self.prev_page).place(relx=0.1, rely=0.935, anchor=CENTER)
        Button(order_screen, cursor=MOUSE_HOVER, background="#A6D3A0", activebackground="#86C380", text="Confirm", font=("Verdana", 16, "bold"), command=self.next_page).place(relx=0.9, rely=0.935, anchor=CENTER)
        # ADD ACTUAL ORDERS PLEASE DONT FORGET
        self.pages.append(order_screen)

    def create_pay_method_page(self):
        pay_method_screen = Frame(self.parent, width=WIDTH, height=HEIGHT)
        Label(pay_method_screen, text="OSC's Cafe Kiosk", font=("Verdana", 52, "bold")).place(relx=1/3, rely=0.12, anchor=CENTER)
        Label(pay_method_screen, image=self.logo).place(relx=0.69, rely=0.06)
        Frame(pay_method_screen, width=WIDTH/1.044, height=HEIGHT/1.57, bg="#775B59", highlightbackground="#595959", highlightthickness=3).place(relx=0.5, rely=0.55, anchor=CENTER)
        Frame(pay_method_screen, width=WIDTH/1.044, height=HEIGHT/6, bg="#5BC5DA", highlightbackground="#595959", highlightthickness=3).place(relx=0.5, rely=0.29, anchor=CENTER)
        Label(pay_method_screen, background="#5BC5DA", text="Payment Options", font=("Verdana", 42, "bold")).place(relx=0.5, rely=0.29, anchor=CENTER)
        Button(pay_method_screen, cursor=MOUSE_HOVER, background="#EEE", activebackground="#CCC", text="Cash", font=("Verdana", 42, "bold"), command=self.last_page, width=14, height=4).place(relx=0.265, rely=0.62, anchor=CENTER)
        Button(pay_method_screen, cursor=MOUSE_HOVER, background="#EEE", activebackground="#CCC", text="Card", font=("Verdana", 42, "bold"), command=self.next_page, width=14, height=4).place(relx=0.735, rely=0.62, anchor=CENTER)
        Button(pay_method_screen, cursor=MOUSE_HOVER, background="#A6D3A0", activebackground="#86C380", text="Edit Order", font=("Verdana", 16, "bold"), command=self.prev_page).place(relx=0.5, rely=0.935, anchor=CENTER)
        self.pages.append(pay_method_screen)

    def create_card_page(self):
        card_screen = Frame(self.parent, width=WIDTH, height=HEIGHT)
        Label(card_screen, text="OSC's Cafe Kiosk", font=("Verdana", 52, "bold")).place(relx=1/3, rely=0.12, anchor=CENTER)
        Label(card_screen, image=self.logo).place(relx=0.69, rely=0.06)
        Frame(card_screen, width=WIDTH/1.044, height=HEIGHT/1.57, bg="#775B59", highlightbackground="#595959", highlightthickness=3).place(relx=0.5, rely=0.55, anchor=CENTER)
        Frame(card_screen, width=WIDTH/1.078, height=HEIGHT/2.399, bg="#EEE", highlightbackground="#595959", highlightthickness=3).place(relx=0.5, rely=0.615, anchor=CENTER)
        Frame(card_screen, width=WIDTH/1.044, height=HEIGHT/6, bg="#5BC5DA", highlightbackground="#595959", highlightthickness=3).place(relx=0.5, rely=0.29, anchor=CENTER)
        Label(card_screen, background="#5BC5DA", text="Please enter card details", font=("Verdana", 32, "bold")).place(relx=0.5, rely=0.29, anchor=CENTER)
        Button(card_screen, cursor=MOUSE_HOVER, background="#A6D3A0", activebackground="#86C380", text="Change Payment", font=("Verdana", 16, "bold"), command=self.prev_page).place(relx=0.15, rely=0.935, anchor=CENTER)
        Button(card_screen, cursor=MOUSE_HOVER, background="#A6D3A0", activebackground="#86C380", text="Confirm", font=("Verdana", 16, "bold"), command=self.next_page).place(relx=0.9, rely=0.935, anchor=CENTER)
        Label(card_screen, background="#EEE", text="Card Number:", font=("Verdana", 22, "bold")).place(relx=0.5, rely=0.49, anchor=CENTER)
        e1 = Entry(card_screen, cursor=MOUSE_TEXT, background="#FFF", fg="#CCC", font=("Verdana", 22, "bold"), justify="center")
        e1.insert(0, "XXXX-XXXX-XXXX-XXXX")
        e1.bind("<FocusIn>", lambda args: e1.config(fg="#000"))
        e1.bind("<FocusIn>", lambda args: e1.delete("0", "end") if (e1.get() == "XXXX-XXXX-XXXX-XXXX") else None, add="+")
        e1.bind("<FocusOut>", lambda args: e1.config(fg="#CCC") if (len(e1.get()) == 0) else None)
        e1.bind("<FocusOut>", lambda args: e1.insert(0, "XXXX-XXXX-XXXX-XXXX") if (len(e1.get()) == 0) else None, add="+")
        e1.place(relx=0.5, rely=0.55, anchor=CENTER)
        Label(card_screen, background="#EEE", text="PIN:", font=("Verdana", 22, "bold")).place(relx=0.5, rely=0.64, anchor=CENTER)
        e2 = Entry(card_screen, cursor=MOUSE_TEXT, background="#FFF", fg="#CCC", font=("Verdana", 22, "bold"), justify="center")
        e2.insert(0, "XXXX")
        e2.bind("<FocusIn>", lambda args: e2.config(fg="#000"))
        e2.bind("<FocusIn>", lambda args: e2.delete("0", "end") if (e2.get() == "XXXX") else None, add="+")
        e2.bind("<FocusOut>", lambda args: e2.config(fg="#CCC") if (len(e2.get()) == 0) else None)
        e2.bind("<FocusOut>", lambda args: e2.insert(0, "XXXX") if (len(e2.get()) == 0) else None, add="+")
        e2.place(relx=0.5, rely=0.7, anchor=CENTER)
        self.pages.append(card_screen)

    def create_number_page(self):
        number_screen = Frame(self.parent, width=WIDTH, height=HEIGHT)
        Label(number_screen, text="OSC's Cafe Kiosk", font=("Verdana", 52, "bold")).place(relx=1/3, rely=0.12, anchor=CENTER)
        Label(number_screen, image=self.logo).place(relx=0.69, rely=0.06)
        Frame(number_screen, width=WIDTH/1.044, height=HEIGHT/1.57, bg="#775B59", highlightbackground="#595959", highlightthickness=3).place(relx=0.5, rely=0.55, anchor=CENTER)
        Frame(number_screen, width=WIDTH/1.078, height=HEIGHT/2.399, bg="#EEE", highlightbackground="#595959", highlightthickness=3).place(relx=0.5, rely=0.615, anchor=CENTER)
        Frame(number_screen, width=WIDTH/1.044, height=HEIGHT/6, bg="#5BC5DA", highlightbackground="#595959", highlightthickness=3).place(relx=0.5, rely=0.29, anchor=CENTER)
        Label(number_screen, background="#5BC5DA", text="Thank you for ordering!", font=("Verdana", 42, "bold")).place(relx=0.5, rely=0.29, anchor=CENTER)
        Label(number_screen, background="#EEE", text=f"Order Number: #{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}", font=("Verdana", 52, "bold")).place(relx=0.5, rely=0.615, anchor=CENTER)
        Button(number_screen, cursor=MOUSE_HOVER, background="#A6D3A0", activebackground="#86C380", text="Finish", font=("Verdana", 16, "bold"), command=self.first_page).place(relx=0.5, rely=0.935, anchor=CENTER)
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
        
        Button(self.parent, cursor=MOUSE_HOVER, background="#F00", activebackground="#E32A2A", text=" X ", font=("Verdana", 13, "bold"), command=self.parent.destroy).place(relx=1, rely=0, anchor=NE)

root = Tk()
root.overrideredirect(True)
WIDTH = root.winfo_screenwidth()
HEIGHT = root.winfo_screenheight()
MOUSE_HOVER = "hand2"
MOUSE_TEXT = "xterm"
root.geometry(f"{WIDTH}x{HEIGHT}")
main = Main(root)
root.mainloop()