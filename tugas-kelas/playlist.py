# Class Playlist
class Playlist:
    """
    Playlist memiliki atribut
     - daftar_lagu = sebuah list yang berisi daftar objek Lagu
     - track_saat_ini = penanda indeks lagu saat ini
    """
    
    
    # Definisi konstruktor: 
    # Saat playlist baru dibuat, playlist kosong 
    # daftar_lagu = None dan track_saat_ini = None
    
    def __init__(self):
        daftar_lagu = ['tanpa emir', 'anak ambis', 'ga jelas']
        daftar_lagu = None
        track_saat_ini = None
        
    
    # Fungsi tambah lagu:
    # Menambahkan satu objek lagu pada akhir list daftar_lagu
    # ARGUMEN: `new_lagu` merupakan sebuah objek lagu yang akan ditambahkan
    def tambah_lagu(self, new_lagu):
        self.newLagu = new_lagu
    
    # Fungsi private set lagu:
    # Set lagu yang akan diputar dan mainkan lagu tersebut. Kondisi yang mungkin:
    # - Jika playlist kosong, lagu tidak dapat diputar. Anda harus mencetak: "GAGAL MEMUTAR LAGU: PLAYLIST KOSONG"
    # - Jika lagu saat ini merupakan lagu pertama, lagu sebelumnya adalah lagu terakhir
    # - Setelah memutar lagu terakhir, lagu selanjutnya kembali ke lagu pertama
    # Pada bagian akhir fungsi ini, anda hanya perlu mencetak informasi lagu yang diputar saat ini dengan memanggil fungsi now_playing 
    # ARGUMEN: `track` merupakan nomor indeks lagu dalam playlist
    def __set_and_play(self, track):
        # implementasi

        # akhir pemanggilan fungsi, berikan parameter yang sesuai
        Playlist.now_playing(None)
    
    # Fungsi putar lagu pertama:
    # Memutar lagu pada indeks pertama dari daftar_lagu
    def play_first(self):
        # contoh implementasi
        self.__set_and_play(0)
    
    # Fungsi putar lagu terakhir:
    # Memutar lagu pada indeks terakhir dari daftar_lagu
    def play_last(self):
        # implementasi
        pass
        
    # Fungsi putar lagu:
    # Memutar lagu sesuai indeks yang ditujuk oleh track_saat_ini
    def play(self):
        # implementasi
        pass
    
    # Fungsi putar lagu selanjutnya:
    # Memutar lagu selanjutnya
    def play_next(self):
        # implementasi
        pass
    
    # Fungsi putar lagu sebelumnya:
    # Memutar lagu selanjutnya
    def play_previous(self):
        # implementasi
        pass

    # JANGAN UBAH FUNGSI INI
    # Fungsi static menampilkan informasi lagu yang sedang diputar
    # ARGUMEN: `lagu` merupakan sebuah objek dari kelas Lagu 
    @staticmethod
    def now_playing(lagu):
        if lagu is None:
            print("<b>GAGAL MEMUTAR LAGU</b>: PLAYLIST KOSONG")
        else:
            print("Memutar lagu <b>{:s}</b> by <b>{:s}<b>".format(lagu.judul_lagu, lagu.artis))
