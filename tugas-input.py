__version__ = "1.1.0"

from prettytable import PrettyTable

file = open("tugas.txt", "w")
x = PrettyTable()
x.field_names = [
    "Task",
    "Due date"
]

while True:
    tugas = input("masukan tugas: ")
    tanggal = input("masukan tanggal (yyyy-mm-dd): ")
    action = input("action: ")

    if action == "save":
        x.add_row([tugas, tanggal])

        cont = input("Lanjut? ")
        if cont == "yes":
            continue
        else:
            break

file.write(x.get_string())
file.close()