from basepokemon import BasePokemon, BaseMove, Type

class Pokemon(BasePokemon):
    def __init__(self):
        BasePokemon.__init__(self)
        # Has to sum to 100
        self.spend_hp(30)
        self.spend_attack(30)
        self.spend_defence(40)
        self.add_move(Mirada_Intimidante())
        self.add_move(Maullido_Feroz())
        self.add_move(Michi_Feliz())
        self.add_move(Ronrroneo())
        self.set_type(Type.EARTH)
        self.move=0
        self.moves = ['Mirada Intimidante', "Maullido Feroz", "Michi Feliz", "Ronrroneo"]

    def get_name(self):
        return "Pitufa"

    def choose_move(self, enemy):
        mov = self.moves[self.move]
        self.move = self.move + 1 if self.move < len(self.moves) - 1 else 0
        return self.get_move_by_name(mov)

class Mirada_Intimidante(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(1)
        self.set_type(Type.EARTH)

    def get_name(self):
        return "Mirada Intimidante"

class Maullido_Feroz(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(1)
        self.set_type(Type.FIRE)

    def get_name(self):
        return "Maullido Feroz"


class Michi_Feliz(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(1)
        self.set_type(Type.EARTH)

    def get_name(self):
        return "Michi Feliz"


class Ronrroneo(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(1)
        self.set_type(Type.NORMAL)

    def get_name(self):
        return "Ronrroneo"