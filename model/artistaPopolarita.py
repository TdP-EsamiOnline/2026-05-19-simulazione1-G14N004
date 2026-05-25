from dataclasses import dataclass


@dataclass
class ArtistaPopolarita:
    ArtistId: int
    Name: str
    popolarita:int

    def __hash__(self):
        return hash(self.ArtistId)

    def __eq__(self, other):
        return self.ArtistId == other.ArtistId

    def __str__(self):
        return f"{self.ArtistId} ---> {self.Name} ---> {self.popolarita}"
