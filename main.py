"""
aplikasi deteksi gempa terkini
modularisasi dengan fucntion
modularisasi dengan package

"""
import gempaterkini

if __name__ == '__main__':
    print('aplikasi utama')
    result = gempaterkini.ekstraksi_data()
    gempaterkini.tampilkan_data(result)

