#!/usr/bin/env python
# coding: utf-8

# In[1]:


from basepokemon import BasePokemon, BaseMove, Type


# In[ ]:


class Pokemon(BasePokemon):
    def __init__(self):
        BasePokemon.__init__(self)
        # Has to sum to 100
        self.spend_hp(30)
        self.spend_attack(25)
        self.spend_defence(45)
        self.add_move(Chancla_fuego())
        self.add_move(Escupir())
        self.add_move(Taco_picante())
        self.add_move(Agua_horchata())
        self.set_type(Type.FIRE)
        self.move = 0
        self.moves = ['Mano de Dios', "Mordida en la oreja", "AMLO te dice fifi", "Cabezaso del Bicho"]


    def get_name(self):
        return "Juan Manuel"

    def choose_move(self, enemy):
        mov = self.moves[self.move]
        self.move = self.move + 1 if self.move < len(self.moves) - 1 else 0
        return self.get_move_by_name(mov)

class Mano_de_dios(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(1)
        self.set_type(Type.WATER)

    def get_name(self):
        return "Mano de Dios"

class Mordida_Tyson(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(1)
        self.set_type(Type.FIRE)

    def get_name(self):
        return "Mordida en la oreja"


class Amlo_fifi(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(1)
        self.set_type(Type.EARTH)

    def get_name(self):
        return "AMLO te dice fifi"


class El_bicho(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(1)
        self.set_type(Type.WATER)

    def get_name(self):
        return "Cabezaso del Bicho"

