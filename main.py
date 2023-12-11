import turtle

from tkinter import *
from tkinter import messagebox, ttk

from turtlee import Marking
from data import districts_and_cities

import pandas

import os
ROOT_DIR = os.getcwd()


def district_choice(district):
    global user_district_name
    user_district_name = district
    for city in districts_and_cities[district]:
        mark_location = districts_and_cities[district][city]["loc"]
        marking.dot_mark(mark_location)
        district_city_list.append(city)
    window_main.destroy()
    window_main.quit()

def all_cities():
    if len(user_named_cities) == len(districts_and_cities[user_district_name]):
        messagebox.showinfo(message="Įvardijote visus apskrities miestus!")
        window_secondary.destroy()
        window_secondary.quit()

def user_city_mark():
    user_city = entry.get().title()
    if user_city in districts_and_cities[user_district_name]:
        user_named_cities.append(user_city)
        mark_location = districts_and_cities[user_district_name][user_city]["loc"]
        text_location = districts_and_cities[user_district_name][user_city]["text_loc"]
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
        window_secondary.destroy()
        window_main.quit()
    elif answer == False:
        window_secondary.destroy()
        window_main.quit()
def off():
    global is_on
    is_on = False
    window_main.destroy()
    screen.bye()

is_on = True

while is_on:
    user_district_name = ""
    user_named_cities = []
    district_city_list = []

    screen = turtle.Screen()
    screen.clear()
    screen.title("Lietuvos žemėlapis")
    image = ROOT_DIR +"\\images\\blank_map.gif"
    screen.addshape(image)
    turtle.shape(image)
    screen.setup(1350,1000)
    screen.tracer(0)

    marking = Marking()

    window_main = Tk()
    window_main.title("Lietuvos apskirtys")
    window_main.geometry("800x800")

    separator = ttk.Separator(window_main)
    separator.pack(fill="x",pady=5)

    label = Label(window_main, text="Pasirinkite apskritį", anchor="center", font=("Arial", 30, "bold"))
    label.pack()

    separator2 = ttk.Separator(window_main)
    separator2.pack(fill="x",pady=5)

    districts = ["Šiaulių", "Alytaus", "Utenos", "Kauno", "Vilniaus", "Panevėžio", "Klaipėdos", "Marijampolės", "Tauragės", "Telšių"]
    for district in districts:
        button = Button(window_main, borderwidth=3, text=district, width=12, font=("Arial", 25), command=lambda x=district: district_choice(x))
        button.pack()

    button_off = Button(window_main, text="Išjungti", width=5, font=15, command=off, fg="red")
    button_off.place(x=740, y=760)
    window_main.mainloop()

    window_secondary = Tk()
    window_secondary.title("Miestų įvestis")
    window_secondary.geometry("500x500")
    window_secondary.bind("<Return>", lambda x: user_city_mark())

    separator2 = ttk.Separator(window_secondary)
    separator2.pack(fill="x", pady=5)

    label_2 = Label(window_secondary, text=f"Įveskite {user_district_name} apskrities miestą", font=("Arial", 20))
    label_2.pack(pady=5)

    entry = Entry(window_secondary, borderwidth=3, font=("Arial", 20))
    entry.pack()

    button_insert = Button(window_secondary, borderwidth=3, text="Įvesti", command=user_city_mark, font=("Arial", 20))
    button_insert.pack()

    button_exit = Button(window_secondary, borderwidth=3, text="Išjungti", font=("Arial", 20), command=exit_and_save)
    button_exit.pack(side=BOTTOM)

    list_box = Listbox(window_secondary, borderwidth=3, height=20, width=40, font=15, activestyle="none")
    list_box.pack()

    if is_on == False:
        window_secondary.destroy()

    window_secondary.mainloop()
