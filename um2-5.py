tarif_kendaraan = {
    "golongan1": {
        "tipe_kendaraan": [
            "minibus", "jip",
            "sedan", "bus", "pick up"
        ],
        "tarif": 9000
    },
    "golongan2": {
        "tipe_kendaraan": ["truk kecil"],
        "tarif": 15000
    },
    "golongan3": {
        "tipe_kendaraan": ["truk sedang"],
        "tarif": 17500
    },
    "golongan4": {
        "tipe_kendaraan": ["truk besar", "truk tronton"],
        "tarif": 21500
    },
    "golongan5": {
        "tipe_kendaraan": ["truk gandengan",],
        "tarif": 23500
    }
}

jenis_mobil = input("masukan jenis mobil: ")
jenis_mobil = jenis_mobil.lower()

if jenis_mobil in tarif_kendaraan["golongan1"]["tipe_kendaraan"]:
    print(f'Tarif yang harus dibayar Rp. {tarif_kendaraan["golongan1"]["tarif"]}')
elif jenis_mobil in tarif_kendaraan["golongan2"]["tipe_kendaraan"]:
    print(f'Tarif yang harus dibayar Rp. {tarif_kendaraan["golongan2"]["tarif"]}')
elif jenis_mobil in tarif_kendaraan["golongan3"]["tipe_kendaraan"]:
    print(f'Tarif yang harus dibayar Rp. {tarif_kendaraan["golongan3"]["tarif"]}')
elif jenis_mobil in tarif_kendaraan["golongan4"]["tipe_kendaraan"]:
    print(f'Tarif yang harus dibayar Rp. {tarif_kendaraan["golongan4"]["tarif"]}')
elif jenis_mobil in tarif_kendaraan["golongan5"]["tipe_kendaraan"]:
    print(f'Tarif yang harus dibayar Rp. {tarif_kendaraan["golongan5"]["tarif"]}')