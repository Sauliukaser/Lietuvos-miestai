import turtle

from tkinter import *
from tkinter import messagebox, ttk

from turtlee import Marking
from data import lt_apskritys_ir_miestai

import pandas

def district_choice(district):
    global user_district_name
    user_district_name = district
    for city in lt_apskritys_ir_miestai[district]:
        mark_location = lt_apskritys_ir_miestai[district][city]["loc"]
        marking.dot_mark(mark_location)
        district_city_list.append(city)
    window.destroy()
    window.quit()

def all_cities():
    if len(user_named_cities) == len(lt_apskritys_ir_miestai[user_district_name]):
        messagebox.showinfo(message="Įvardijote visus apskrities miestus!")
        window_2.destroy()
        window_2.quit()

def user_city_mark():
    user_city = entry.get().title()
    if user_city in lt_apskritys_ir_miestai[user_district_name]:
        user_named_cities.append(user_city)
        mark_location = lt_apskritys_ir_miestai[user_district_name][user_city]["loc"]
        text_location = lt_apskritys_ir_miestai[user_district_name][user_city]["text_loc"]
        if text_location is not None:
            marking.name_location_1(text_location, user_city)
        else:
            marking.name_location_2(mark_location, user_city)
    else:
        list_box.insert(0,f"{user_district_name} apskrityje nėra miesto: {entry.get().title()}")
    entry.delete(0, END)
    all_cities()

def exit_and_save():
    answer = messagebox.askyesnocancel(title="Išjungti programą", message="Ar norite išsaugoti neįvardintus miestus kaip .txt failą?")
    if answer == True:
        for city in user_named_cities:
            district_city_list.remove(city)
        mokytis = pandas.DataFrame(district_city_list)
        mokytis.to_csv(f"{user_district_name}_apskirtis_neivardinti.txt")
        window_2.destroy()
        window.quit()
    elif answer == False:
        window_2.destroy()
        window.quit()
def off():
    global is_on
    is_on = False
    window.destroy()
    screen.bye()

is_on = True

while is_on:
    user_district_name = ""
    user_named_cities = []
    district_city_list = []

    screen = turtle.Screen()
    screen.clear()
    screen.title("Lietuvos žemėlapis")
    image = "C:\\Users\\mariu\\PycharmProjects\\Apskriciu - miestai\\images\\blank_map.gif"
    image = "images/blank_map.gif"
    screen.addshape(image)
    turtle.shape(image)
    screen.setup(1350,1000)
    screen.tracer(0)
    marking = Marking()

    window = Tk()
    window.title("Lietuvos apskirtys")
    window.geometry("800x800")

    separator = ttk.Separator(window)
    separator.pack(fill="x",pady=5)

    label = Label(window, text="Pasirinkite apskritį", anchor="center", font=("Arial", 30, "bold"))
    label.pack()

    separator2 = ttk.Separator(window)
    separator2.pack(fill="x",pady=5)

    districts = ["Šiaulių", "Alytaus", "Utenos", "Kauno", "Vilniaus", "Panevėžio", "Klaipėdos", "Marijampolės", "Tauragės", "Telšių"]
    for district in districts:
        mygtukas = Button(window, borderwidth=3, text=district, width=12, font=("Arial", 25), command=lambda x=district: district_choice(x))
        mygtukas.pack()

    button_off = Button(window, text="Išjungti", width=5, font=15, command=off, fg="red")
    button_off.place(x=740, y=760)
    window.mainloop()

    window_2 = Tk()
    window_2.title("Miestų įvestis")
    window_2.geometry("500x500")
    window_2.bind("<Return>", lambda x: user_city_mark())

    separator2 = ttk.Separator(window_2)
    separator2.pack(fill="x", pady=5)

    label_2 = Label(window_2, text=f"Įveskite {user_district_name} apskrities miestą", font=("Arial", 20))
    label_2.pack(pady=5)

    entry = Entry(window_2, borderwidth=3, font=("Arial", 20))
    entry.pack()

    button_w2 = Button(window_2, borderwidth=3, text="Įvesti", command=user_city_mark, font=("Arial", 20))
    button_w2.pack()

    button_w2_2 = Button(window_2, borderwidth=3, text="Išjungti", font=("Arial", 20), command=exit_and_save)
    button_w2_2.pack(side=BOTTOM)

    list_box = Listbox(window_2, borderwidth=3, height=20, width=40, font=15, activestyle="none")
    list_box.pack()

    if is_on == False:
        window_2.destroy()

    window_2.mainloop()
