class AllProjectiles():
    def __init__(self):
        #ALL
        #UPDATE-to-ADD-to-when-laser-shot-is-created-REMOVE-when-laser-shot-is-destroyed
        self.all_projectiles = []

        #TYPE-DESTINCTIONS
        #FOR->infantry
        self.laser_shots = []

    def add(self, projectile):
        self.all_projectiles.append(projectile)

    def add_group(self, projectiles):
        #for projectile in projectiles:
        [self.all_projectiles.append(projectile) for projectile in projectiles]

    #UPDATE-to-INCLUDE-self.all_projectiles-UPDATE
    def remove_disabled_projectiles(self):
        [self.laser_shots.remove(laser_shot) for laser_shot in self.laser_shots if laser_shot.disabled()]
        # for laser_shot in self.laser_shots:
        #     #possibly-optimize-later-to-not-need-to-sort-through-all-projectiles
        #     if laser_shot.disabled():
        #         #not-yet-used
        #         #self.all_projectiles.remove(projectile)
        #         self.laser_shots.remove(laser_shot)

    def tick(self):
        #for laser_shot in self.laser_shots:
        #    laser_shot.tick()
        [laser_shot.tick() for laser_shot in self.laser_shots]
        self.remove_disabled_projectiles()