from basepokemon import BasePokemon, BaseMove, Type

class Pokemon(BasePokemon):
    def __init__(self):
        BasePokemon.__init__(self)
        # Has to sum to 100
        self.spend_hp(30)
        self.spend_attack(50)
        self.spend_defence(20)
        self.add_move(Escupitajo_nuclear())
        self.add_move(Agua_contaminada())
        self.add_move(Mirada_tierna())
        self.add_move(Patada_pequena())
        self.set_type(Type.WATER)
        self.move = 0
        self.moves = ['Escupitajo nuclear', "Chorro de agua contaminada", "Mirada tierna", "Patada pequeña"]

    def get_name(self):
        return "Axolotin"

    def choose_move(self, enemy):
        mov = self.moves[self.move]
        self.move = self.move + 1 if self.move < len(self.moves) - 1 else 0
        return self.get_move_by_name(mov)

class Escupitajo_nuclear(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(1)
        self.set_type(Type.WATER)

    def get_name(self):
        return "Escupitajo nuclear"

class Agua_contaminada(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(1)
        self.set_type(Type.WATER)

    def get_name(self):
        return "Chorro de agua contaminada"


class Mirada_tierna(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(1)
        self.set_type(Type.NORMAL)

    def get_name(self):
        return "Mirada tierna"


class Patada_pequena(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(1)
        self.set_type(Type.NORMAL)

    def get_name(self):
        return "Patada pequeña"
