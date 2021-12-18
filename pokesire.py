from basepokemon import BasePokemon, BaseMove, Type

class Pokemon(BasePokemon):
    def __init__(self):
        BasePokemon.__init__(self)
        # Has to sum to 100
        self.spend_hp(10)
        self.spend_attack(20)
        self.spend_defence(70)
        self.add_move(Chorro_agua())
        self.add_move(Furia_marina())
        self.add_move(Sunami())
        self.set_type(Type.WATER)
        self.move = 0
        self.moves = ['Chorro_agua', "Furia_marina", "Sunami"]


    def get_name(self):
        return "pokesire"

    def choose_move(self, enemy):
        mov = self.moves[self.move]
        self.move = self.move + 1 if self.move < len(self.moves) - 1 else 0
        return self.get_move_by_name(mov)

class Chorro_agua(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(1)
        self.set_type(Type.WATER)

    def get_name(self):
        return "Chorro_agua"

class Furia_marina(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(1)
        self.set_type(Type.WATER)

    def get_name(self):
        return "Furia_marina"


class Sunami(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(1)
        self.set_type(Type.WATER)

    def get_name(self):
        return "Sunami"





