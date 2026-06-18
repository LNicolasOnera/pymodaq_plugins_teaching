import time

class Timer:
    def __init__(self):
        self._delai = 2 #s par default
        self.start_time = None
        self.elapsed = 0

    def start(self):
        """Démarre le chronomètre."""
        self.start_time = time.time()

    def get_time(self):
        """Retourne le temps écoulé en secondes depuis le démarrage."""
        if self.start_time is None:
            return 0
        self.elapsed = time.time() - self.start_time
        return self.elapsed

    @property
    def delai(self):
        """
        fetch the delay
        -------
        float: the current characteristic delay between 2 time grab

        """
        return self._delai

    @delai.setter
    def delai(self, value):
        """
        Set the current characteristic delay between 2 time grab
        ----------
        value: the current characteristic delay between 2 time grab
        """
        if value <= 0:
            raise ValueError(f'A characteristic time of {value} is not possible. It should be strictly positive')
        else:
            self._delai = value

    def run_for_duration(self, total_duration):
        """Fait tourner le chronomètre pendant total_duration secondes, en affichant le temps écoulé à chaque delai."""
        self.start()
        while self.get_time() < total_duration:
            print(int(self.get_time()))
            time.sleep(self.delai)
        print(int(self.get_time()))  # Affiche le temps final

# Exemple d'utilisation
# delai = float(input("Entrez le délai entre chaque affichage (en secondes) : "))
# duree_totale = float(input("Entrez la durée totale à mesurer (en secondes) : "))
#
# timer = Timer()
# timer.run_for_duration(duree_totale)