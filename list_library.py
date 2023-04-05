import pandas as pd

class Library():
    def __init__(self):
        self.data_buku = dict()  # judul sebagai index
        self.buku_dipinjam = dict()

    def tambah_buku(self, judul, tahun, jumlah):
        self.data_buku[judul] = [tahun, jumlah]
    
    def update_judul(self, judul, judul_baru):
        self.data_buku[judul_baru] = self.data_buku.pop(judul)

    def update_tahun(self, judul, tahun_baru):
        try:
            self.data_buku[judul][0] = tahun_baru
        except KeyError:
            print('Buku Tersebut Tidak Ada')

    def update_jumlah(self, judul, jumlah_baru):
        try:
            self.data_buku[judul][1] = jumlah_baru
        except KeyError:
            print('Buku Tersebut Tidak Ada')

    def check_data_buku(self):
        data = pd.DataFrame((self.data_buku)).T
        data.columns = ['Tahun Terbit', 'Jumlah Tersedia']
        print(data.to_markdown())

    def pinjam_buku(self, judul):
        if(self.data_buku[judul][1] == 0):
            print('Buku Tidak Tersedia')
        else:
            # mengurangi data buku -1 di jumlah tersedia
            self.update_jumlah(judul, self.data_buku[judul][1]-1)
            # menambahkan data di buku yang dipinjam
            try:
                # judul buku yang dipinjam sudah ada di data buku_dipinjam
                self.buku_dipinjam[judul][1] = self.buku_dipinjam[judul][1] + 1
            except KeyError:
                # judul buku yang dipinjam belum ada di data buku_dipnijam
                self.buku_dipinjam[judul] = [self.data_buku[judul][0], 1]

    def kembali_buku(self, judul):
        if(self.buku_dipinjam[judul][1] == 1):
            self.buku_dipinjam.pop(judul)
        else:
            # mengurangi data buku -1 di buku_dipnijam
            self.buku_dipinjam[judul][1] = self.buku_dipinjam[judul][1] - 1
            # menambah jumlah buku di data buku
            self.data_buku[judul][1] = self.data_buku[judul][1] + 1

    def check_buku_dipinjam(self):
        data = pd.DataFrame((self.buku_dipinjam)).T
        data.columns = ['Tahun Terbit', 'Jumlah Dipinjam']
        print(data.to_markdown())