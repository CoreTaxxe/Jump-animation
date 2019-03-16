class Player(pygame.sprite.Sprite):
    change_x = 0
    change_y = 0
    direction = "R"

    def __init__(self):
        #konstruktor
        
    def update(self):
        self.calc_grav()

        # Move left/right
        self.rect.x += self.change_x

        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we hit anything
        #hit plat

    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += 0.5

        # See if we are on the ground.
        if self.rect.y >= constants.SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = constants.SCREEN_HEIGHT - self.rect.height

    def jump(self):
        """ Called when user hits 'jump' button. """
        """if player is on ground call set change_y to -10"""
        #u can also use it without if statement but then teh player is allowed to press jump whil in air
        if self.rect.bottom >= constants.SCREEN_HEIGHT:
            self.change_y = -10


