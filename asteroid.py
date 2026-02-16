import pygame
import random
from logger import log_event
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
    def draw(self,surface):
        pygame.draw.circle(surface,"white",self.position,self.radius,LINE_WIDTH)
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        random_angle = random.uniform(20, 50)
        velocity_multiplier = 1.2
        new_asteroid1_velocity : pygame.Vector2 = self.velocity.rotate(random_angle)
        new_asteroid2_velocity : pygame.Vector2 = self.velocity.rotate(-random_angle)
        new_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid1 = Asteroid (self.position.x,self.position.y,new_asteroid_radius)
        new_asteroid2 = Asteroid (self.position.x,self.position.y,new_asteroid_radius)
        new_asteroid1.velocity = new_asteroid1_velocity * velocity_multiplier
        new_asteroid2.velocity = new_asteroid2_velocity * velocity_multiplier
        






