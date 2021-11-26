# parent class
class Dad:
    name = "Peter"
    hair = "black"
    eyes = "black"
    skin = "brown"
    legs = 2
    arms = 2

    def boss(self):
        msg = "\nName: {}\nHair: {}\nEyes: {}\nSkin: {}\nLegs: {}\nArms: {}".format(self.name,self.hair,self.eyes,self.skin,self.legs,self.arms)
        return msg



# child class instance
class mom(Dad):
    name = "Sally"
    hair = "Blond"
    eyes = "Blue"
    skin = "White"
    legs = 2
    arms = 2

    def realboss(self):
        msg = "\nShe is the real boss of the family but lets Dad think he is!"
        return msg

    
























if __name__ == "__main__":
    dad = Dad()
    print(dad.boss())
    
    realboss = RealBoss()
    print(real_boss.boss())
    print(mom.real_boss())
