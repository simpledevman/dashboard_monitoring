def ekstraksi_data():
    """
    tanggal: 12 Juni 2022
    waktu: 10:25:26 WIB
    skala: 4.7
    kedalaman: 10 km
    lokasi: 9.72 LS - 119.08 BT
    pusat gempa: Pusat gempa berada di laut 17 km Tenggara KODI-SUMBA BARAT DAYA
    dirasakan: Dirasakan (Skala MMI): II - III Tambolaka, II Waikabubak
    :return:
    """
    hasil = dict()
    hasil['tanggal'] = '12 Juni 2022'
    hasil['waktu'] = '10:25:26 WIB'
    hasil['magnitudo'] = 4.7
    hasil['kedalaman'] = '10 km'
    hasil['lokasi'] = {'ls': 9.72, 'bt': 119.08}
    hasil['pusat gempa'] = 'Pusat gempa berada di laut 17 km Tenggara KODI-SUMBA BARAT DAYA'
    hasil['dirasakan'] = 'Dirasakan (Skala MMI): II - III Tambolaka, II Waikabubak'

    return hasil

def tampilkan_data(result):
    print('gempa terakhir berdasarkan BMKG')
    print(f"tanggal {result['tanggal']}")
    print(f"waktu {result['waktu']}")
    print(f"magnitudo {result['magnitudo']}")
    print(f"kedalaman {result['kedalaman']}")
    print(f"lokasi: LS= {result['lokasi']['ls']}, BT={result['lokasi']['bt']}")
    print(f"dirasakan {result['dirasakan']}")
