import warnings
import pygame


class Face:
    def __init__(self, verteces, color, normal=0):
        self.verteces = verteces
        self.color = color
        self.visible = True

    def distance_to_camera(self, camera):
        return sum([v.distance_to_camera(camera) for v in self.verteces]) / len(self.verteces)

    def draw(self, sheet, camera):
        if self.visible:
            screen_positions = [v._pos_on_screen(camera, sheet.get_width(), sheet.get_height()) for v in self.verteces]
            if all(screen_positions):
                pygame.draw.polygon(sheet, self.color, screen_positions)