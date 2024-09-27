class Virsune():
    def __init__(self, virsunes_id):        
        self.virsunes_id = virsunes_id
        self.edges={}
    def add_edge(self,  sekantis: 'Virsune' ,svoris):
        self.edges[sekantis.virsunes_id]=svoris
    def __str__(self):
        krastines = ', '.join([f"{sekantis_id} (svoris {svoris})" for sekantis_id, svoris in self.edges.items()])
        return f"Viršūnė {self.virsunes_id} su kraštinėmis: {krastines}"