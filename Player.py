class Player():
    inventory:list[list[str, int]]
    occupation:str = None
    def __init__(self, Name:str="Player", Health:int=50):
        self.Name = Name
        self.Health = Health
    def __str__(self):
        return f"{self.Name}, {self.Health}"
    def __repr__(self):
        return f"{self.Name}, {self.Health}"