from dataclasses import dataclass


@dataclass
class Genere:
    GenreId:int
    Name:str

    def __hash__(self):
        return hash(self.GenredId)

    def __eq__(self, other):
        return self.GenredId == other.GenredId

    def __str__(self):
        return f"{self.GenredId} ---> {self.Name}"
