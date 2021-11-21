from functools import partial


class Player(object):
    def __init__(self, *args, **kwargs):
        self.last_action = "walk"
        self.health = 20

    def play_turn(self, warrior):
        self.warrior = warrior
        actions = {
            "walk": self.warrior.walk_,
            "rest": self.warrior.rest_,
            "attack": self.warrior.attack_,
            "shoot": self.warrior.shoot_,
            "rescue": self.warrior.rescue_,
            "pivot": self.warrior.pivot_,
        }
        meth = actions["rest"] if self.should_rest() else actions["walk"]
        if self.should_pivot():
            meth = actions["pivot"]
        elif self.should_attack():
            meth = actions["attack"]
        elif self.should_attack_from_distance():
            meth = actions["shoot"]
        elif self.should_backoff():
            meth = partial(actions["walk"], "backward")
        elif self.should_rescue():
            meth = actions["rescue"]

        self.health = self.warrior.health()
        self.last_action = {v: k for k, v in actions.items()}.get(meth, "backward")
        return meth()

    def under_attack(self):
        return self.warrior.health() < self.health

    def should_rest(self):
        current_health = self.warrior.health()
        return current_health < 20 and not self.under_attack()

    def should_attack(self):
        return not self.warrior.feel().is_empty() and not self.should_rescue()

    def should_rescue(self):
        return self.warrior.feel().is_captive()

    def should_backoff(self):
        damage_from_distance = self.under_attack() and self.warrior.feel().is_empty()  # noqa
        archer_in_sight = 'archer' in [str(e).lower() for e in self.warrior.look()][1]
        return damage_from_distance and self.warrior.health() < 14 and not archer_in_sight

    def should_pivot(self):
        return self.warrior.feel().is_wall()

    def should_attack_from_distance(self):
        return self.has_mage_too_close() and self.warrior.feel().is_empty()

    def has_mage_too_close(self):
        return 'wizard' in [str(e).lower() for e in self.warrior.look()][2]
