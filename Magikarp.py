from basepokemon import BasePokemon, BaseMove, Type

class Pokemon(BasePokemon):
    def __init__(self):
        BasePokemon.__init__(self)
        # Has to sum to 100
        self.spend_hp(0)
        self.spend_attack(10)
        self.spend_defence(90)
        self.add_move(Salpicar())
        self.add_move(Salpicar_duro())
        self.add_move(Quedarse_tieso())
        self.add_move(Te_mira_fijamente())
        self.move = 0
        self.moves = ['Salpicar', "Salpicar duro", "Quedarse tieso", "Te mira fijamente"]
        self.set_type(Type.FIRE)

    def get_name(self):
        return "Magikarp"

    def choose_move(self, enemy):
        mov = self.moves[self.move]
        self.move = self.move + 1 if self.move < len(self.moves) - 1 else 0
        return self.get_move_by_name(mov)


class Salpicar(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(1)
        self.set_type(Type.WATER)

    def get_name(self):
        return "salpicar"

class Salpicar_duro(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(1)
        self.set_type(Type.WATER)

    def get_name(self):
        return "salpicar duro"

class Quedarse_tieso(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(1)
        self.set_type(Type.WATER)

    def get_name(self):
        return "quedarse tieso"

class Te_mira_fijamente(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(1)
        self.set_type(Type.WATER)

    def get_name(self):
        return "te mira fijamente"