# def main():
#     favorite_movies = []

#     for i in range(5):
#         movie = input("Masukkan judul film favorit ke-{}: ".format(i+1))
#         favorite_movies.append(movie)

#     print("\nFilm-film favorit Anda adalah:")
#     for movie in favorite_movies:
#         print(movie)

# if __name__ == "__main__":
#     main()

class Film:
    def __init__(self, judul, tahun_rilis, sutradara):
        self.judul = judul
        self.tahun_rilis = tahun_rilis
        self.sutradara = sutradara

class DaftarFilm:
    def __init__(self):
        self.daftar_film = []

    def tambah_film(self, film):
        self.daftar_film.append(film)

    def tampilkan_film(self):
        print("Daftar Film Favorit:")
        for film in self.daftar_film:
            print("Judul:", film.judul)
            print("Tahun Rilis:", film.tahun_rilis)
            print("Sutradara:", film.sutradara)
            print()

def main():
    daftar_film_saya = DaftarFilm()

    daftar_film_saya.tambah_film(Film("Laskar Pelangi", 2008, "Riri Riza"))
    daftar_film_saya.tambah_film(Film("Ada Apa dengan Cinta?", 2002, "Rudi Soedjarwo"))
    daftar_film_saya.tambah_film(Film("Gie", 2005, "Riri Riza"))
    daftar_film_saya.tambah_film(Film("AADC 2", 2016, "Riri Riza"))
    daftar_film_saya.tambah_film(Film("Pengabdi Setan", 2017, "Joko Anwar"))

    daftar_film_saya.tampilkan_film()

if __name__ == "__main__":
    main()
