class human:
    Experience = 100
    Health = 10
    Armour = 100.0

    def life(self, Experience, Health):
        lifeXP = human.Experience / 100

        lifepoints = lifeXP * human.Health

        print(lifepoints)

    def armour():
        print(human.Armour, '%')
