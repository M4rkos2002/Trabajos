class Libro:
    def __init__(self, ISBN, titulo, autor, cantPag, SKU, precio):
        self.ISBN = ISBN
        self.titulo = titulo
        self.autor = autor
        self.cantPag = cantPag
        self.SKU = SKU
        self.precio = precio
    
class Juguete:
    def __init__(self, nombre, codBarra, SKU, precio):
        self.nombre = nombre
        self.codBarra = codBarra
        self.SKU = SKU
        self.precio = precio
    