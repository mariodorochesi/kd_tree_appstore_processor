
class Aplicacion:
    def __init__(self, id, track_name, size_bytes, price,
    user_rating, version, cont_rating, prime_genre, idiomas):
        self.id = id
        self.track_name = track_name.lower()
        self.size_bytes = size_bytes
        self.price = price
        self.user_rating = user_rating
        self.version = version
        self.cont_rating = cont_rating
        self.prime_genre = prime_genre
        self.idiomas = idiomas
        self.vector = None

    def __str__(self):
        return f"ID : {self.id}\n"\
            f"Nombre : {self.track_name}\n"\
            f"Tamano : {self.size_bytes} bytes\n"\
            f"Precio : {self.price}\n"\
            f"User Rating : {self.user_rating}\n"\
            f"Version : {self.version}\n"\
            f"Content Rating : {self.cont_rating}\n"\
            f"Genero : {self.prime_genre}\n"\
            f"Idiomas Soportados : {self.idiomas}\n"\
            f"Vector Caracteristicas Normalizado: {self.vector}"