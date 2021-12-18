from basepokemon import BasePokemon, BaseMove, Type

class Pokemon(BasePokemon):
    def __init__(self):
        BasePokemon.__init__(self)
        # Has to sum to 100
        self.spend_hp(20)
        self.spend_attack(30)
        self.spend_defence(50)
        self.add_move(Ataque1())
        self.add_move(Ataque2())
        self.add_move(Ataque3())
        self.add_move(Ataque4())
        self.set_type(Type.WATER)
        self.move = 0
        self.moves = ['Ataque1', "Ataque2", "Ataque3", "Ataque4"]


    def get_name(self):
        return "Pokefran"

    def choose_move(self, enemy):
        mov = self.moves[self.move]
        self.move = self.move + 1 if self.move < len(self.moves) - 1 else 0
        return self.get_move_by_name(mov)

class Ataque1(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(1)
        self.set_type(Type.WATER)

    def get_name(self):
        return "Ataque1"

class Ataque2(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(1)
        self.set_type(Type.EARTH)

    def get_name(self):
        return "Ataque2"


class Ataque3(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(1)
        self.set_type(Type.EARTH)

    def get_name(self):
        return "Ataque3"


class Ataque4(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(1)
        self.set_type(Type.FIRE)

    def get_name(self):
        return "Ataque4"