import pygame
import constants
import sys
from player import Player


def main():
    pygame.init()

    size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Side Scroller")
    clock = pygame.time.Clock()

    player = Player()

    all_sprites = pygame.sprite.Group()

    all_sprites.add(player)

    while True:
        screen.fill([0, 0, 255])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP:
                    player.jump()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()

        all_sprites.update()

        """every draw code below this comment"""
        all_sprites.draw(screen)
        """every draw code above tis comment"""

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
