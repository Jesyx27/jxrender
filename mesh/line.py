import pygame

class Line:
    def __init__(self, p1, p2, color=(255, 255, 255)) -> None:
        self.p1 = p1
        self.p2 = p2
        self.color = (255, 255, 255)
        self.visible = True
        self.color = color

    def get_vertices(self):
        return [self.p1, self.p2]

    def length(self):
        return self.p1.distance(self.p2)

    def __str__(self):
        return f"Line({self.p1}, {self.p2})"

    def __repr__(self):
        return str(self)
    
    def draw(self, sheet, camera):
        screen_pos1 = self.p1._pos_on_screen(camera, sheet.get_width(), sheet.get_height())
        screen_pos2 = self.p2._pos_on_screen(camera, sheet.get_width(), sheet.get_height())
        self.p1.draw(sheet, camera)
        self.p2.draw(sheet, camera)
        pygame.draw.line(sheet, self.color, screen_pos1, screen_pos2)

