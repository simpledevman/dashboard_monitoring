import requests
from bs4 import BeautifulSoup


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
    try:
        content = requests.get('https://bmkg.go.id')
    except Exception:
        return None
    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')

        result = soup.find('span', {'class': 'waktu'})
        result = result.text.split(', ')
        tanggal = result[0]
        waktu = result[1]

        result = soup.find('div', {'class': 'col-md-6 col-xs-6 gempabumi-detail no-padding'})
        result = result.findChildren('li')
        i = 0
        for res in result:
            print(i, res)
            i = i + 1

        magnitudo = 0


        hasil = dict()
        hasil['tanggal'] = tanggal #'12 Juni 2022'
        hasil['waktu'] = waktu #'10:25:26 WIB'
        hasil['magnitudo'] = magnitudo #4.7
        hasil['kedalaman'] = '10 km'
        hasil['lokasi'] = {'ls': 9.72, 'bt': 119.08}
        hasil['pusat'] = 'Pusat gempa berada di laut 17 km Tenggara KODI-SUMBA BARAT DAYA'
        hasil['dirasakan'] = 'Dirasakan (Skala MMI): II - III Tambolaka, II Waikabubak'
        return hasil
    else:
        return None

def tampilkan_data(result):
    if result is None:
        print('tidak bisa menemukan data')
        return
    print('gempa terakhir berdasarkan BMKG')
    print(f"tanggal {result['tanggal']}")
    print(f"waktu {result['waktu']}")
    print(f"magnitudo {result['magnitudo']}")
    print(f"kedalaman {result['kedalaman']}")
    print(f"lokasi: LS= {result['lokasi']['ls']}, BT={result['lokasi']['bt']}")
    print(f"dirasakan {result['dirasakan']}")


if __name__=='__main__': # aplikasi gempa terkini
    print('ini adalah package gempa terkini')


