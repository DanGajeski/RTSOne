class AllProjectiles():
    def __init__(self):
        #ALL
        self.all_projectiles = []

        #TYPE-DESTINCTIONS
        #FOR->infantry
        self.laser_shots = []

    def add(self, projectile):
        self.all_projectiles.append(projectile)

    def add_group(self, projectiles):
        for projectile in projectiles:
            self.all_projectiles.append(projectile)

    def remove_disabled_projectiles(self):
        for projectile in self.all_projectiles:
            #possibly-optimize-later-to-not-need-to-sort-through-all-projectiles
            if projectile.disabled():
                #not-yet-used
                #self.all_projectiles.remove(projectile)
                self.laser_shots.remove(projectile)

    def tick(self):
        for projectile in self.all_projectiles:
            projectile.tick()