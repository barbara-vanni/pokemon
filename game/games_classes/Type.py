class Type:
    # Constructeur
    def __init__(self, types, matrice):
        self._types = types
        self._matrice = matrice

    # Types
    def get_types(self):
        return self._types
    def set_types(self, types):
        self._types = types

    # Matrice
    def get_matrice(self):
        return self._matrice
    def set_matrice(self, matrice):
        self._matrice = matrice