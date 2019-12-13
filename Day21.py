class Warrior:
    def __init__(self, name, max_hp, damage, armor):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.base_damage = damage
        self.damage = damage
        self.base_armor = armor
        self.armor = armor
        self.gear = []
        self.spent = 0

    def buy_gear(self, item):
        self.gear.append((item[2], item[3]))
        self.spent += item[1]

    def reset(self):
        self.hp = self.max_hp
        self.damage = self.base_damage
        self.armor = self.base_armor
        self.gear = []
        self.spent = 0

    def fight(self, opp):
        player_turn = True
        self.damage += sum([x[0] for x in self.gear])
        self.armor += sum([x[1] for x in self.gear])
        opp.damage += sum([x[0] for x in opp.gear])
        opp.armor += sum([x[1] for x in opp.gear])
        while self.hp > 0 and opp.hp > 0:
            if player_turn:
                opp.hp -= max(1, self.damage - opp.armor)
            else:
                self.hp -= max(1, opp.damage - self.armor)
            player_turn = not player_turn
        # print("%s spent %s and %s" % (self.name, self.spent, "won" if self.hp > 0 else "lost"))
        output = (self.spent, self.hp > 0)
        self.reset()
        opp.reset()
        return output


weapons = [["Dagger", 8, 4, 0], ["Shortsword", 10, 5, 0], ["Warhammer", 25, 6, 0], ["Longsword", 40, 7, 0], ["Greataxe", 74, 8, 0]]
armor = [["No Armor", 0, 0, 0], ["Leather Armor", 12, 0, 1], ["Chainmail Armor", 31, 0, 2], ["Splintmail Armor", 53, 0, 3], ["Bandedmail Armor", 75, 0, 4], ["Platemail Armor", 102, 0, 5]]
rings = [["No Ring", 0, 0, 0], ["Dmg +1", 25, 1, 0], ["Dmg +2", 50, 2, 0], ["Dmg +3", 100, 3, 0], ["Def +1", 20, 0, 1], ["Def +2", 40, 0, 2], ["Def +3", 80, 0, 3]]


def part_a():
    player = Warrior("Player", 100, 0, 0)
    boss = Warrior("Boss", 100, 8, 2)
    gear = [[w, a, r1, r2] for w in weapons for a in armor for r1 in rings for r2 in rings if r2[1] == 0 or r2 != r1]
    gear.sort(key=lambda x: sum([y[1] for y in x]))
    for gear_set in gear:
        for item in gear_set:
            player.buy_gear(item)
        spent, won = player.fight(boss)
        if won:
            return spent


def part_b():
    player = Warrior("Player", 100, 0, 0)
    boss = Warrior("Boss", 100, 8, 2)
    gear = [[w, a, r1, r2] for w in weapons for a in armor for r1 in rings for r2 in rings if r2[1] == 0 or r2 != r1]
    gear.sort(key=lambda x: sum([y[1] for y in x]), reverse=True)
    for gear_set in gear:
        for item in gear_set:
            player.buy_gear(item)
        spent, won = player.fight(boss)
        if not won:
            return spent


if __name__ == "__main__":
    print("Part A", part_a())
    print("Part B", part_b())
