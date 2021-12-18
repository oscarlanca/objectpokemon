from basepokemon import BasePokemon, BaseMove, Type

class Pokemon(BasePokemon):
    def __init__(self):
        BasePokemon.__init__(self)
        # Has to sum to 100
        self.spend_hp(25)
        self.spend_attack(50)
        self.spend_defence(25)
        self.add_move(Navajazo_exlosivo())
        self.add_move(Navajazo_por_la_espalda())
        self.add_move(Asalto_Asessino())
        self.add_move(Bomba_molotov())
        self.set_type(Type.FIRE)
        self.move = 0
        self.moves = ['Navajazo_exlosivo', "Navajazo_por_la_espalda", "Asalto_Asessino", "Bomba_molotov"]


    def get_name(self):
        return "El_Navajasfire"

    def choose_move(self, enemy):
        mov = self.moves[self.move]
        self.move = self.move + 1 if self.move < len(self.moves) - 1 else 0
        return self.get_move_by_name(mov)

class Navajazo_exlosivo(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(1)
        self.set_type(Type.FIRE)

    def get_name(self):
        return "Navajazo_exlosivo"

class Navajazo_por_la_espalda(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(2)
        self.set_type(Type.NORMAL)

    def get_name(self):
        return "Navajazo_por_la_espalda"


class Asalto_Asessino(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(2)
        self.set_type(Type.NORMAL)

    def get_name(self):
        return "Asalto_Asessino!"


class Bomba_molotov(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(2)
        self.set_type(Type.FIRE)

    def get_name(self):
        return "Bomba_molotov"
