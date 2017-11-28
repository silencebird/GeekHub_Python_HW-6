class Bike:
    def __init__(self, type, weight, gender, frame_material, gear_number, chain_type, tyre_size):
        self.type = type
        self.weight = weight
        self.gender = gender
        self.frame_material = frame_material
        self.gear_number = gear_number
        self.chain_type = chain_type
        self.tyre_size = tyre_size

class KidsBike(Bike):
    def __init__(self,type, weight, gender, frame_material, chain_type, tyre_size, age):
        super(KidsBike,self).__init__(type, weight, gender, frame_material, chain_type, tyre_size)
        self.age = age

class MountainBike(Bike):
    def __init__(self,type, weight, gender, frame_material, chain_type, tyre_size, gear_number):
        super(KidsBike,self).__init__(type, weight, gender, frame_material, gear_number, chain_type, tyre_size)
        self.gear_number = gear_number

