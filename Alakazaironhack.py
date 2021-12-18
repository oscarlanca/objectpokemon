from basepokemon import BasePokemon, BaseMove, Type

class Pokemon(BasePokemon):
    def __init__(self):
        BasePokemon.__init__(self)
        # Has to sum to 100
        self.spend_hp(70)
        self.spend_attack(30)
        self.spend_defence(0)
        self.add_move(HydroPump())
        self.add_move(HeavySlam())
        self.add_move(Licuado_de_lenteja())
        self.add_move(Cruda_horrible())
        
        self.set_type(Type.EARTH)
        self.move = 0
        self.moves = ['Licuado de lenteja', "Cruda horrible", "HydroPump", "HeavySlam"]

        

    def get_name(self):
        return "Alakazaironhack"

    def choose_move(self, enemy):
        mov = self.moves[self.move]
        self.move = self.move + 1 if self.move < len(self.moves) - 1 else 0
        return self.get_move_by_name(mov)


class HydroPump(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(1)
        self.set_type(Type.WATER)

    def get_name(self):
        return "HydroPump"
    
class HeavySlam(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(1)
        self.set_type(Type.NORMAL)

    def get_name(self):
        return "HeavySlam"

class Licuado_de_lenteja(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(1)
        self.set_type(Type.FIRE)

    def get_name(self):
        return "Licuado de lenteja"
    
class Cruda_horrible(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(1)
        self.set_type(Type.EARTH)

    def get_name(self):
        return "Cruda horrible"