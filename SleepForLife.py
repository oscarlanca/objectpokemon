from basepokemon import BasePokemon, BaseMove, Type

class Pokemon(BasePokemon):
    def __init__(self):
        BasePokemon.__init__(self)
        # Has to sum to 100
        self.spend_hp()
        self.spend_attack(50)
        self.spend_defence(50)
        self.add_move(LetMeSleep())
        self.add_move(KickingInTheSleep())
        self.add_move(SleepingOnYourFace())
        self.set_type(Type.NORMAL)
        self.move = 0
        self.moves = ["Let Me Sleep!!!", "I Will Kick You Sleeping", "See me Sleeping On Your Face"]

    def get_name(self):
        return "Saturday Morning Sleeping"

    def choose_move(self, enemy):
        mov = self.moves[self.move]
        self.move = self.move + 1 if self.move < len(self.moves) - 1 else 0
        return self.get_move_by_name(mov)

class LetMeSleep(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(7)
        self.set_type(Type.FIRE)

    def get_name(self):
        return "Let Me Sleep!!!"

class KickingInTheSleep(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(7)
        self.set_type(Type.WATER)

    def get_name(self):
        return "I Will Kick You Sleeping"

class SleepingOnYourFace(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(7)
        self.set_type(Type.EARTH)

    def get_name(self):
        return "See me Sleeping On Your Face"