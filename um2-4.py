def validasi_9digit(nomor_telepon):
    result = ""
    depan = nomor_telepon[:3]
    sisa1 = nomor_telepon[3:6]
    sisa2 = nomor_telepon[6:]
    result = f"({depan}){sisa1}-{sisa2}"

    return result

def validasi_10digit(nomor_telepon):
    result = ""
    depan = nomor_telepon[:4]
    sisa1 = nomor_telepon[4:7]
    sisa2 = nomor_telepon[7:]
    result = f"({depan}){sisa1}-{sisa2}"

    return result

def validasi_11digit(nomor_telepon):
    result = ""
    depan = nomor_telepon[:4]
    sisa1 = nomor_telepon[4:7]
    sisa2 = nomor_telepon[7:]
    result = f"({depan}){sisa1}-{sisa2}"

    return result


def validasi_nomor_telepon(nomor_telepon):
    if len(nomor_telepon) == 9:
        return validasi_9digit(nomor_telepon)
    elif len(nomor_telepon) == 10:
        return validasi_10digit(nomor_telepon)
    elif len(nomor_telepon) == 11:
        return validasi_11digit(nomor_telepon)
    else:
        return "Nomor telepon tidak sah."


print(validasi_nomor_telepon("022828531"))
print(validasi_nomor_telepon("0265828531"))
print(validasi_nomor_telepon("02658285317"))
print(validasi_nomor_telepon("026582"))
print(validasi_nomor_telepon("0265829797979796969"))