import os
import pygame
import constants


def load_img(filename, size, path="data/img",colorkey = constants.BLACK):
    img = pygame.image.load(os.path.join(path, filename))
    img = pygame.transform.scale(img, size)
    img = img.convert()
    img.set_colorkey(colorkey)
    return img


def rotate_img(img, angle,colorkey = constants.BLACK):
    img = img
    img = pygame.transform.rotate(img, angle)
    img.convert()
    img.set_colorkey(colorkey)
    return img
