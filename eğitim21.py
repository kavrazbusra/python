"""
müzik uygulaması gibi def kullanarak çalma, ekleme, listeye ekleme, def kullanarak yap
Listeme ekleme yapsın, listeden çalma yapsın, listeden silme yapsın.

"""

class MyMusic:
    def __init__(self):
        self.myplaylist = []

    def add_song(self, song):
        self.myplaylist.append(song)
        print(f' "{song}" çalma listesine eklendi.')

    def play_song(self, song):
        if song in self.myplaylist:
            print(f'"{song}" çalınıyor...')
        else:
            print(f'"{song}" çalma listesinde olmadığından dolayı çalınamadı.')

    def remove_song(self, song):
        if song in self.myplaylist:
            self.myplaylist.remove(song)
            print(f'"{song}" çalma listesinden çıkarıldı.')
        else:
            print(f'"{song}" çalma listesinde bulunamadı.')

    def show_playlist(self):
        if self.myplaylist:
            print("Çalma Listesi:")
            for song in self.myplaylist:
                print(f"{song}")
        else:
                print("Çalma listesi boş.")
