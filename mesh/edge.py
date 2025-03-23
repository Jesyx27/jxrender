import pygame

class Edge:
    def __init__(self, p1, p2, color=(255, 255, 255), width=2) -> None:
        self.p1 = p1
        self.p2 = p2
        self.color = (255, 255, 255)
        self.visible = True
        self.color = color
        self.width = width

    def get_vertices(self):
        return [self.p1, self.p2]

    def length(self):
        return self.p1.distance(self.p2)

    def __str__(self):
        return f"Edge({self.p1}, {self.p2})"

    def __repr__(self):
        return str(self)
    
    def draw(self, sheet, camera):
        if not self.visible:
            return
        screen_pos1 = self.p1._pos_on_screen(camera, sheet.get_width(), sheet.get_height())
        screen_pos2 = self.p2._pos_on_screen(camera, sheet.get_width(), sheet.get_height())
        if screen_pos1 and screen_pos2:
            pygame.draw.line(sheet, self.color, screen_pos1, screen_pos2, self.width)

