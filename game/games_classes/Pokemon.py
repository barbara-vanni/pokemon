from .Type import Type

class Pokemon(Type):
    # Constructeur
    def __init__(self, name, types, level, power_attack, defense, speed, pv, pv_max, xp, xp_max, image_front, evolution_level, evolution_name, matrice, statut = 0, in_stockage = 0):
        Type.__init__(self, types, matrice)
        self._name = name
        self._level = level
        self._power_attack = power_attack
        self._defense = defense
        self._speed = speed
        self._pv = pv
        self._pv_max = pv_max
        self._xp = xp
        self._xp_max = xp_max
        self._image_front = image_front
        self._evolution_level = evolution_level
        self._evolution_name = evolution_name
        self._statut = statut
        self._in_stockage = in_stockage

    # name
    def get_name(self):
        return self._name   
    def set_name(self, name):
        self._name = name

    # Power_attack
    def get_power_attack(self):
        return self._power_attack
    def set_power_attack(self, power_attack):
        self._power_attack = power_attack

    # Defense
    def get_defense(self):
        return self._defense
    def set_defense(self, defense):
        self._defense = defense

    # Speed
    def get_speed(self):
        return self._speed
    def set_speed(self, speed):
        self._speed = speed

    # Pv
    def get_pv(self):
        return self._pv
    def set_pv(self, pv):
        self._pv = max(pv , 0) 

    # Pv_max
    def get_pv_max(self):
        return self._pv_max
    def set_pv_max(self, pv_max):
        self._pv_max = pv_max


    # Xp
    def get_xp(self):
        return self._xp
    def set_xp(self, xp):
        self._xp = xp

    # Xp_max
    def get_xp_max(self):
        return self._xp_max   
    def set_xp_max(self, xp_max):
        self._xp_max = xp_max

    # Level
    def get_level(self):
        return self._level
    def set_level(self, level):
        self._level = level

    # image_front
    def get_image_front(self):
        return self._image_front
    def set_image_front(self, image_front):
        self._image_front = image_front

    # evolution_level
    def get_evolution_level(self):
        return self._evolution_level
    def set_evolution_level(self, evolution_level):
        self._evolution_level = evolution_level

    # evolution_name
    def get_evolution_name(self):
        return self._evolution_name
    def set_evolution_name(self, evolution_name):
        self._evolution_name = evolution_name

    # Statut
    def get_statut(self):
        return self._statut
    def set_statut(self, statut):
        self._statut = statut
    
    # In_stockage
    def get_in_stockage(self):
        return self._in_stockage
    def set_in_stockage(self, new_in_stockage):
        self._in_stockage = new_in_stockage

        


