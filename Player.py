class Player():
    inventory:list[list[str, int]]
    occupation:str = None
    def __init__(self, Name:str="Player", Health:int=50, Lv:int=1, Mana:int=100):
        self.Name = Name
        self.Health = Health
        self.Lv = Lv
        self.Mana = Mana
    def __str__(self):
        return f"{self.Name} has {self.Health} health, is lv {self.Lv} and has {self.Mana} mana."