__version__ = "1.0.0"

import json

from prettytable import PrettyTable
import requests
import statistics as stc

# 1 - definisiin table dan request
x = PrettyTable()
r = requests.get("https://apicovid19indonesia-v2.vercel.app/api/indonesia/provinsi")

# 2 - Dapeting json-nya
data_covid = r.json()

# 3 - Bikin 3 variabel kolom untuk dihitung rata2nya
data_kasus = []
data_dirawat = []
data_sembuh = []

# 4 - Masukin setiap kolom yang sesuai
for data in data_covid:
    data_kasus.append(data['kasus'])
    data_dirawat.append(data['dirawat'])
    data_sembuh.append(data['sembuh'])

# Tentukan header table
x.field_names = [
    "Jenis", "Rata2"
]

# Tambahkan baris
x.add_row(["Kasus", stc.mean(data_kasus)])
x.add_row(["Rawat", stc.mean(data_dirawat)])
x.add_row(["Sembuh", stc.mean(data_sembuh)])

# Simpan ke txt
file = open("rata-covid-provinsi.txt", "w")
file.write(x.get_string())
file.close()

# Simpan ke json
data_json = {
    "kasus": stc.mean(data_kasus),
    "rawat": stc.mean(data_dirawat),
    "sembuh": stc.mean(data_sembuh)
}
data_json = json.dumps(data_json)

file = open("rata-covid-provinsi.json", "w")
file.write(data_json)
file.close()