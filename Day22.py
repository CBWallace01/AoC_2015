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

    def buy_gear(self, item):
        self.gear.append((item[2], item[3]))

    def reset(self):
        self.hp = self.max_hp
        self.damage = self.base_damage
        self.armor = self.base_armor
        self.gear = []

    def fight(self, opp):
        self.damage += sum([x[0] for x in self.gear])
        self.armor += sum([x[1] for x in self.gear])
        return max(1, self.damage - opp.armor)

    def copy(self):
        new_war = Warrior(self.name, self.max_hp, self.base_damage, self.base_armor)
        new_war.name = self.name
        new_war.max_hp = self.max_hp
        new_war.hp = self.hp
        new_war.base_damage = self.base_damage
        new_war.damage = self.damage
        new_war.base_armor = self.base_armor
        new_war.armor = self.armor
        new_war.gear = self.gear
        return new_war


class Wizard:
    def __init__(self, name, hp, mana):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.base_mana = mana
        self.mana = mana
        self.armor = 0
        self.gear = []
        self.effects = {"Shield": 0, "Poison": 0, "Recharge": 0}
        self.mana_costs = {"Magic Missile": 53, "Drain": 73, "Shield": 113, "Poison": 173, "Recharge": 229}
        self.mana_spent = 0

    def buy_gear(self, item):
        self.gear.append((item[2], item[3]))

    def reset(self):
        self.hp = self.max_hp
        self.mana = self.base_mana
        self.armor = 0
        self.gear = []
        self.effects = {"Shield": 0, "Poison": 0, "Recharge": 0}
        self.mana_spent = 0

    def is_active(self, spell):
        return self.effects[spell] > 0

    def tick_effects(self):
        if self.effects["Shield"] > 0:
            self.effects["Shield"] -= 1
            if self.effects["Shield"] == 0:
                self.armor -= 7
        if self.effects["Recharge"] > 0:
            self.effects["Recharge"] -= 1
            self.mana += 101
        if self.effects["Poison"] > 0:
            self.effects["Poison"] -= 1
            return 3
        else:
            return 0

    def can_cast(self, spell):
        if spell in ["Shield", "Recharge", "Poison"] and self.effects[spell] > 0:
            return False
        return self.mana_costs[spell] <= self.mana

    def cast(self, spell):
        damage = 0
        if spell == "Shield":
            self.effects[spell] = 6
            self.armor = 7
        elif spell == "Poison":
            self.effects[spell] = 6
        elif spell == "Recharge":
            self.effects[spell] = 5
        elif spell == "Magic Missile":
            damage = 4
        elif spell == "Drain":
            damage = 2
            self.hp += 2
        else:
            raise ValueError("Invalid Spell", spell)
        self.mana -= self.mana_costs[spell]
        self.mana_spent += self.mana_costs[spell]
        return damage

    def copy(self):
        new_wiz = Wizard(self.name, self.max_hp, self.base_mana)
        new_wiz.name = self.name
        new_wiz.max_hp = self.max_hp
        new_wiz.hp = self.hp
        new_wiz.base_mana = self.base_mana
        new_wiz.mana = self.mana
        new_wiz.armor = self.armor
        new_wiz.gear = self.gear
        new_wiz.effects = self.effects
        new_wiz.mana_costs = self.mana_costs
        new_wiz.mana_spent = self.mana_spent
        return new_wiz


def try_turn(player, boss):
    boss.hp -= player.tick_effects()
    all_valid = []
    for spell in ["Recharge", "Shield", "Poison", "Magic Missile", "Drain"]:
        if not player.can_cast(spell):
            continue
        boss_copy = boss.copy()
        player_copy = player.copy()
        boss_copy.hp -= player.cast(spell)
        boss_copy.hp -= player.tick_effects()
        if boss_copy.hp <= 0:
            all_valid.append(player_copy.mana_spent)
            continue
        player_copy.hp -= boss.fight(player)
        if player_copy.hp <= 0:
            continue
        else:
            all_valid.extend(try_turn(player_copy, boss_copy))
    return all_valid


def part_a():
    player = Wizard("Player", 50, 500)
    boss = Warrior("Boss", 58, 9, 0)
    spent = try_turn(player, boss)
    return min(spent)


def part_b():
    pass


if __name__ == "__main__":
    print("Part A", part_a())
    print("Part B", part_b())
