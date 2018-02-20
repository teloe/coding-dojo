class Patients(object):
    def __init__(self, id, name, allergies, bed):
        self.id = id
        self.name = name
        self.allergies = allergies
        self.bed = bed

class Hospital(object):
    def __init__(self, patients, name, capacity):

        
