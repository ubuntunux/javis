from functools import partial

from kivy.graphics import Color, Rectangle


# listen to size and position changes
def update_rect(rect, instance, value):
    rect.pos = instance.pos
    rect.size = instance.size


def create_rect(instance, color):
    with instance.canvas.before:
        Color(*color)
        instance.rect = Rectangle(pos=instance.pos, size=instance.size, size_hint=(1, 1))
    instance.bind(pos=partial(update_rect, instance.rect), size=partial(update_rect, instance.rect))