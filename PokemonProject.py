skill_multiplier_map = {
    "Fire": {"Water": 0.5,
             "Grass": 2},
    "Water": {
        "Fire": 2,
        "Grass": 0.5
    },
    "Grass": {"Fire": 0.5,
              "Water": 2}

}


class Pokemon:
    def __init__(self, name, level, skill_type, current_health=10, is_knocked_out=False, experience=0):
        self.name = name
        self.level = level
        self.skill_type = skill_type
        self.max_health = level * 5
        self.current_health = current_health
        self.is_knocked_out = is_knocked_out
        self.experience = experience

    def lose_health(self, health_to_lose):
        self.current_health -= health_to_lose
        if self.current_health <= 0:
            self.current_health = 0
            self.knocked_out()
        else:
            print("{} lost {} health points. Current health level is: {}-health".format(
                self.name, health_to_lose, self.current_health))

    def gain_health(self, health_to_gain):
        self.current_health += health_to_gain
        if self.current_health >= self.max_health:
            self.current_health = self.max_health
        if self.is_knocked_out:
            self.revive()
        else:
            print("{} gained {} health point(s). Current health level is: {}-health".format(
                self.name, health_to_gain, self.current_health))

    def knocked_out(self):
        self.is_knocked_out = True
        print("{} is knocked out. Current health point is: {}-health".format(self.name, self.current_health))

    def revive(self):
        self.is_knocked_out = False
        print("{} has been revived. Current health status: {} health points".format(
            self.name, self.current_health))

    def __repr__(self):
        return "\n Name: {}\n Level:{}\n Experience:{} \n Current health: {} health points\n Skill Type: {}".format(self.name, self.level, self.experience, self.current_health, self.skill_type)

    def attack(self, other_pokemon):
        damage = 1
        multiplier = skill_multiplier_map.get(
            self.skill_type).get(other_pokemon.skill_type)
        damage *= multiplier
        if multiplier == 0.5:
            print("{} attacking {}. Damage potential: {}\n This move isn't effective".format(
                self.name, other_pokemon.name, damage))
        elif multiplier == 2:
            print("{} attacking {}. Damage potential: {}\n This is a Super Effective Move!!".format(
                self.name, other_pokemon.name, damage))
        other_pokemon.lose_health(damage)
        self.gain_experience(1)

    def gain_experience(self, experience_gained):
        self.experience += experience_gained
        print("You just earned {} Experience badge.".format(experience_gained))
        if self.experience >= 3:
            self.increase_level()

    def increase_level(self):
        self.experience = 0
        self.level += 1
        print("Congratulations!!! You have advanved to the Next Level")


class Trainer:
    def __init__(self, name, pokemonTeam, potion):
        self.name = name
        self.pokemonTeam = pokemonTeam[:6]
        self.potion = potion
        self.active_pokemon = pokemonTeam[0]

    def get_active_pokemon(self):
        print("{}'s current pokemon is: {}".format(
            self.name, self.active_pokemon))
        return self.active_pokemon

    def attack_other_trainer(self, other_trainer):
        if self.active_pokemon.is_knocked_out == False:
            self.active_pokemon.attack(other_trainer.active_pokemon)
        else:
            print("{} is currently knocked out. Select another pokemon".format(
                self.active_pokemon))

    def get_team(self):
        names = [member for member in self.pokemonTeam]
        print("Team {}--->\n".format(self.name), names)

    def use_potion(self):
        if self.potion > 0:
            if self.active_pokemon.current_health < self.active_pokemon.max_health:
                self.active_pokemon.gain_health(1)
                self.potion -= 1
                print("You used up 1 healing potion. You have {} potion(s) left.".format(
                    self.potion))
            else:
                print("Failed to use potion. Your pokemon has maximum health.")
        else:
            print("You are out of healing potions")

    def swap_pokemon(self, new_pokemon):
        if new_pokemon.is_knocked_out == True:
            print("You can't switch to an inactive pokemon.")
        elif new_pokemon in self.pokemonTeam:
            self.active_pokemon = new_pokemon
            print("Pokemon Swap Successful. Your current pokemon is \n {}".format(
                self.active_pokemon))


class FirePoke(Pokemon):
    def __init__(self, name, level, skill_type="Fire", current_health=10, is_knocked_out=False, experience=0):
        super().__init__(name, level, skill_type,
                         current_health, is_knocked_out, experience)


class GrassPoke(Pokemon):
    def __init__(self, name, level, skill_type="Grass", current_health=10, is_knocked_out=False, experience=0):
        super().__init__(name, level, skill_type,
                         current_health, is_knocked_out, experience)


tobemon = FirePoke("Tobemon", 2)
judithmon = GrassPoke("Judithmon", 2)
ririmon = FirePoke("Ririmon", 2)
desolamon = GrassPoke("Desolamon", 2)

tobe = Trainer("Tobe", [tobemon, ririmon], 5)
desola = Trainer("Desola", [judithmon, desolamon], 5)


def test_logic():
    print("*********** TESING GAME LOGIC *****************************")
    tobe.get_team()
    print("***********************************************************")
    tobe.get_active_pokemon()
    print("***********************************************************")
    tobe.attack_other_trainer(desola)
    print("***********************************************************")
    tobe.attack_other_trainer(desola)
    print("***********************************************************")
    tobe.attack_other_trainer(desola)
    print("***********************************************************")
    desola.use_potion()
    print("***********************************************************")
    desola.swap_pokemon(desolamon)
    print("***********************************************************")
    desola.get_team()
    print("*********** TEST SESSION ENDED *****************************")


test_logic()


# print(tobe.get_active_pokemon())
# desola.get_active_pokemon()
# tobe.attack_other_trainer(desola)
# tobe.attack_other_trainer(desola)
# desola.get_team()
# tobe.get_team()
# desola.use_potion()
# tobe.get_active_pokemon()
# desola.swap_pokemon(desolamon)
