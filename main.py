"""
aplikasi deteksi gempa terkini
modularisasi dengan fucntion
"""


def ekstraksi_data():
    """
    tanggal: 08 Juni 2022
    waktu: 21:25:20 WIB
    magnitudo: 2.5
    kedalaman: 10 km
    lokasi: 3.26 LS - 128.34 BT
    pusat gempa: Pusat gempa berada di darat 9 km utara Kairatu
    dirasakan: Dirasakan (Skala MMI): II Kairatu
    :return:
    """
    hasil = dict()
    hasil['tanggal'] = '08 Juni 2022'
    hasil['waktu'] = '21:25:20 WIB'
    hasil['magnitudo'] = 2.5
    hasil['kedalaman'] = '10 km'
    hasil['lokasi'] = {'ls': 3.26, 'bt': 128.34}
    hasil['pusat'] = 'Pusat gempa berada di darat 9 km utara Kairatu'
    hasil['dirasakan'] = 'Dirasakan (Skala MMI): II Kairatu'
    return hasil


def tampilkan_data(result):
    print('gempa terakhir berdasarkan BMKG')
    print(f"tanggal {result['tanggal']}")
    print(f"waktu {result['waktu']}")
    print(f"magnitudo {result['magnitudo']}")
    print(f"kedalaman {result['kedalaman']}")
    print(f"lokasi: ls = {result['lokasi']['ls']}, bt = {result['lokasi']['bt']}")
    print(f"pusat {result['pusat']}")
    print(f"dirasakan {result['dirasakan']}")


if __name__ == '__main__':
    print('aplikasi utama')
    result = ekstraksi_data()
    tampilkan_data(result)

