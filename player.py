import pygame
from CircleShape import*
from constants import*
from shot import*
class Player(CircleShape):
    def __init__(self, x, y,):#constructor taking input of x and y integer
        super().__init__(x, y, PLAYER_RADIUS)# calling the parent class constructor
        self.rotation = 0
        self.shoot_cooldown = 0  # Track time since last shot

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt): 
        self.rotation += PLAYER_TURN_SPEED*dt
        return self.rotation

    def update(self, dt):
        keys = pygame.key.get_pressed()
        
        # Update cooldown timer
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= dt

        if keys[pygame.K_a]:
            return self.rotate(-dt)
        if keys[pygame.K_d]:
            return self.rotate(dt)
        if keys[pygame.K_w]:
            return self.move(-dt)
        if keys[pygame.K_s]:
            return self.move(dt)
        if keys[pygame.K_SPACE] and self.shoot_cooldown <= 0:
            self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN  # Reset cooldown
            return self.shoot(dt)
        
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
        return self.position
    
    def shoot(self, dt):
        # Create a new shot at player's position
        shot = Shot(self.position.x, self.position.y)
        # Set shot's velocity based on player's rotation
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        return shot