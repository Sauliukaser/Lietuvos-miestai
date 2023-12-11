import turtle

from tkinter import *
from tkinter import messagebox,ttk

from vezlys import Zymejimas
from duomenys import lt_apskritys_ir_miestai

import pandas

def apskirities_pasirinkimas(apskritis):
    global pavadinimas_apsk
    pavadinimas_apsk = apskritis
    for miestas in lt_apskritys_ir_miestai[apskritis]:
        zymeklio_vieta = lt_apskritys_ir_miestai[apskritis][miestas]["loc"]
        zymejimas.taskas(zymeklio_vieta)
        apskrities_miestai.append(miestas)
    langas.destroy()
    langas.quit()

def visi_miestai():
    if len(ivardinti_miestai) == len(lt_apskritys_ir_miestai[pavadinimas_apsk]):
        messagebox.showinfo(message="Įvardijote visus apskrities miestus!")
        langas2.destroy()
        langas2.quit()

def user_miestas():
    ivardintas_miestas = entry.get().title()
    if ivardintas_miestas in lt_apskritys_ir_miestai[pavadinimas_apsk]:
        ivardinti_miestai.append(ivardintas_miestas)
        zymeklio_vieta = lt_apskritys_ir_miestai[pavadinimas_apsk][ivardintas_miestas]["loc"]
        teksto_vieta = lt_apskritys_ir_miestai[pavadinimas_apsk][ivardintas_miestas]["text_loc"]
        if teksto_vieta is not None:
            zymejimas.pavadinimas(teksto_vieta,ivardintas_miestas)
        else:
            zymejimas.pavadinimas_2(zymeklio_vieta,ivardintas_miestas)
    else:
        list_box.insert(0,f"{pavadinimas_apsk} apskrityje nėra miesto: {entry.get().title()}")
    entry.delete(0, END)
    visi_miestai()

def exit_and_save():
    answer = messagebox.askyesnocancel(title="Išjungti programą", message="Ar norite išsaugoti neįvardintus miestus kaip .txt failą?")
    if answer == True:
        for miestas in ivardinti_miestai:
            apskrities_miestai.remove(miestas)
        mokytis = pandas.DataFrame(apskrities_miestai)
        mokytis.to_csv(f"{pavadinimas_apsk}_apskirtis_neivardinti.txt")
        langas2.destroy()
        langas.quit()
    elif answer == False:
        langas2.destroy()
        langas.quit()
def off():
    global is_on
    is_on = False
    langas.destroy()
    screen.bye()

is_on = True

while is_on:
    pavadinimas_apsk = ""
    ivardinti_miestai = []
    apskrities_miestai = []

    screen = turtle.Screen()
    screen.clear()
    screen.title("Lietuvos žemėlapis")
    image = "C:\\Users\\mariu\\PycharmProjects\\tkinter_bandymas\\images\\blank_map.gif"
    screen.addshape(image)
    turtle.shape(image)
    screen.setup(1350,1000)
    screen.tracer(0)
    zymejimas = Zymejimas()

    langas = Tk()
    langas.title("Lietuvos apskirtys")
    langas.geometry("800x800")

    separator = ttk.Separator(langas)
    separator.pack(fill="x",pady=5)

    uzrasas = Label(langas, text="Pasirinkite apskritį",anchor="center",font=("Arial", 30, "bold"))
    uzrasas.pack()

    separator2 = ttk.Separator(langas)
    separator2.pack(fill="x",pady=5)

    apskirtys = ["Šiaulių", "Alytaus", "Utenos", "Kauno", "Vilniaus", "Panevėžio", "Klaipėdos", "Marijampolės", "Tauragės", "Telšių"]
    for apskritis in apskirtys:
        mygtukas = Button(langas, borderwidth=3, text=apskritis, width=12, font=("Arial", 25), command=lambda a=apskritis: apskirities_pasirinkimas(a))
        mygtukas.pack()

    mygtukas_off = Button(langas,text="Išjungti",width=5,font=15,command=off,fg="red")
    mygtukas_off.place(x=740,y=760)
    langas.mainloop()

    langas2 = Tk()
    langas2.title("Miestų įvestis")
    langas2.geometry("500x500")
    langas2.bind("<Return>", lambda x: user_miestas())

    separator2 = ttk.Separator(langas2)
    separator2.pack(fill="x", pady=5)

    uzrasas2 = Label(langas2,text=f"Įveskite {pavadinimas_apsk} apskrities miestą",font=("Arial", 20))
    uzrasas2.pack(pady=5)

    entry = Entry(langas2, borderwidth=3, font=("Arial", 20))
    entry.pack()

    mygtukas1 = Button(langas2,borderwidth=3, text="Įvesti", command=user_miestas, font=("Arial", 20))
    mygtukas1.pack()

    mygtukas2 = Button(langas2, borderwidth=3, text="Išjungti", font=("Arial", 20), command=exit_and_save)
    mygtukas2.pack(side=BOTTOM)

    list_box = Listbox(langas2,borderwidth=3, height=20, width=40, font=15,activestyle="none")
    list_box.pack()

    if is_on == False:
        langas2.destroy()

    langas2.mainloop()
