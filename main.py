import pygame as pg
import random
import time



# A knight dodging creatures in a cave 

# --CONSTANTS--
# COLOURS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
EMERALD = (21, 219, 147)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)

WIDTH = 1280  # Pixels
HEIGHT = 720
SCREEN_SIZE = (WIDTH, HEIGHT)
BACKGROUND = "./images/cave.jpg"
screen = pg.display.set_mode(SCREEN_SIZE)
clock = pg.time.Clock()

class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("./images/knight.png")
        # Scales the image smaller
        self.image = pg.transform.scale(self.image, (140, 140))
        self.rect = self.image.get_rect()

        # Velocity of the player
        
        self.vel_x = 6
        self.vel_y = -6

        # Makes the player spawn in the corner of the screen
        self.rect.centerx = 0
        self.rect.centery = HEIGHT

        # hitbox dimensions
        hitbox_width = 50
        hitbox_height = 50
        # hitbox Rect
        self.hitbox = pg.Rect(0, 0, hitbox_width, hitbox_height)
        # position hitbox to player's rect
        self.hitbox.center = self.rect.center

        

    def update(self):
        self.calc_grav()

        self.rect.y += self.vel_y

   
    # Gravity
    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.vel_y == 0:
            self.vel_y = 1
        else:
            self.vel_y += .35
 
        # See if we are on the ground.
        if self.rect.y >= HEIGHT - self.rect.height and self.vel_y >= 0:
            self.vel_y = 0
            self.rect.y = HEIGHT - self.rect.height
    
    def jump(self):
        self.vel_y = -5

    def move_left(self):
        self.rect.x -= self.vel_x

    def move_right(self):
        self.rect.x += self.vel_x

class Spider(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("./images/spider.png")
        self.image = pg.transform.scale(self.image, (110, 115))
        self.rect = self.image.get_rect()

        self.vel_x = random.choice([-6, -8, -10, -4])

        self.rect.centerx = WIDTH + 10
        self.rect.centery = HEIGHT - 30

         # hitbox dimensions
        hitbox_width = 10
        hitbox_height = 10
        # hitbox Rect
        self.hitbox = pg.Rect(0, 0, hitbox_width, hitbox_height)
        # position hitbox to player's rect
        self.hitbox.center = self.rect.center

    def update(self):
        self.rect.x += self.vel_x

        # If reaches end spawn back at spawn
        

    

class Black_bat(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("./images/black_bat.png")
        self.image = pg.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        
        self.rect.centerx = random.randrange(1290, 1300)
        self.rect.centery = random.randrange(300, 400)

        self.vel_x = random.choice([-3, -5, -6])

         # hitbox dimensions
        hitbox_width = 10
        hitbox_height = 10
        # hitbox Rect
        self.hitbox = pg.Rect(0, 0, hitbox_width, hitbox_height)
        # position hitbox to player's rect
        self.hitbox.center = self.rect.center

    def update(self):
        self.rect.x += self.vel_x

        # If reaches end spawn back at spawn
        

class Blue_bat(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("./images/blue_bat.png")
        self.image = pg.transform.scale(self.image, (135, 135))
        self.rect = self.image.get_rect()
        
        self.rect.centerx = random.randrange(1290, 1300)
        self.rect.centery = random.randrange(220, 350)

        self.vel_x = random.choice([-5, -7, -9])

         # hitbox dimensions
        hitbox_width = 10
        hitbox_height = 10
        # hitbox Rect
        self.hitbox = pg.Rect(0, 0, hitbox_width, hitbox_height)
        # position hitbox to player's rect
        self.hitbox.center = self.rect.center

    def update(self):
        self.rect.x += self.vel_x

        # If reaches end spawn back at spawn
        
        
class Red_bat(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("./images/red_bat.png")
        self.image = pg.transform.scale(self.image, (200, 257))
        self.rect = self.image.get_rect()
        
        self.rect.centerx = random.randrange(1290, 1300)
        self.rect.centery = random.randrange(50, 210)

        self.vel_x = random.choice([-4, -7, -9])

         # hitbox dimensions
        hitbox_width = 10
        hitbox_height = 10
        # hitbox Rect
        self.hitbox = pg.Rect(0, 0, hitbox_width, hitbox_height)
        # position hitbox to player's rect
        self.hitbox.center = self.rect.center

    def update(self):
        self.rect.x += self.vel_x

        # If reaches end spawn back at spawn

     

    
def start():
    """Environment Setup and Game Loop"""

    pg.init()

    # --Game State Variables--
    screen = pg.display.set_mode(SCREEN_SIZE)
    done = False
    clock = pg.time.Clock()

    # All sprites go in this sprite Group
    all_sprites = pg.sprite.Group()

    pg.display.set_caption("<cave>")

    font = pg.font.SysFont("Helvetica", 24)

    # Creates objects
    player = Player()
    spider = Spider()
    black_bat = Black_bat()
    red_bat = Red_bat()
    blue_bat = Blue_bat()

    # add to all sprites
    all_sprites.add(player)
    all_sprites.add(spider)
    all_sprites.add(black_bat)
    all_sprites.add(red_bat)
    all_sprites.add(blue_bat)

    # sprite groups
    black_bat_group = pg.sprite.Group()
    black_bat_group.add(black_bat)

    red_bat_group = pg.sprite.Group()
    red_bat_group.add(red_bat)

    blue_bat_group = pg.sprite.Group()
    blue_bat_group.add(blue_bat)
    
    spider_group = pg.sprite.Group()
    spider_group.add(spider)

    background_image = pg.image.load(BACKGROUND).convert()
    background_image = pg.transform.scale(background_image, (WIDTH, HEIGHT))

    player_death_time = 0

    # --Main Loop--
    while not done:
        # --- Event Listener
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True

        # If the arrows keys get pressed it will make the player move 
        keys = pg.key.get_pressed()

        # Makes the pressed arrow keys be able to control player movement
        if keys[pg.K_UP]:
            player.jump()

        if keys[pg.K_LEFT]:
            player.move_left()
            player.image = pg.transform.flip(player.image, True, False)

        if keys[pg.K_RIGHT]:
            player.move_right() 

        # --- Update the world state
        all_sprites.update()

        black_bat_group.update()
        red_bat_group.update()
        blue_bat_group.update()
        spider_group.update()

        

        # Makes the player not go off the screen
        if player.rect.right > WIDTH:
            player.rect.right = WIDTH

        if player.rect.left < 0:
            player.rect.left = 0

        if player.rect.top < 0:
            player.rect.top = 0

        if player.rect.bottom > HEIGHT:
            player.rect.bottom = HEIGHT

        # Kills the creature when it goes out of bounds

        for spider in spider_group:
            if spider.rect.left < 0:
                spider.kill()
                spider = Spider()
                all_sprites.add(spider)
                spider_group.add(spider)

        for red_bat in red_bat_group:
            if red_bat.rect.left < 0:
                red_bat.kill()
                red_bat = Red_bat()
                all_sprites.add(red_bat)
                red_bat_group.add(red_bat)

        for blue_bat in blue_bat_group:
            if blue_bat.rect.left < 0:
                blue_bat.kill()
                blue_bat = Blue_bat()
                all_sprites.add(blue_bat)
                blue_bat_group.add(blue_bat)

        for black_bat in black_bat_group:
            if black_bat.rect.left < 0:
                black_bat.kill()
                black_bat = Black_bat()
                all_sprites.add(black_bat)
                black_bat_group.add(black_bat)


        # Creatures collision
        blackbat_collide = pg.sprite.spritecollide(player, black_bat_group, False)
        redbat_collide = pg.sprite.spritecollide(player, red_bat_group, False) 
        bluebat_collide = pg.sprite.spritecollide(player, blue_bat_group, False)
        spider_collide = pg.sprite.spritecollide(player, spider_group, False)  
        if blackbat_collide or redbat_collide or bluebat_collide or spider_collide:
            player.rect.centerx = -100  # get the player out of the screen
            player.rect.centery = HEIGHT

            spider.rect.centerx = WIDTH + 10  # Reset spider position
            spider.rect.centery = HEIGHT - 30 
            # spider.vel_x = 0
            red_bat.rect.centerx = random.randrange(1290, 1300)  # Reset red bat position
            red_bat.rect.centery = random.randrange(50, 210)
            # red_bat.vel_x = 0
            blue_bat.rect.centerx = random.randrange(1290, 1300)  # Reset blue bat position
            blue_bat.rect.centery = random.randrange(220, 350) 
            # blue_bat.vel_x = 0
            black_bat.rect.centerx = random.randrange(1290, 1300)  # Reset black bat position
            black_bat.rect.centery = random.randrange(300, 400)
            # black_bat.vel_x = 0

            if player_death_time == 0:
                player_death_time = pg.time.get_ticks()
            if pg.time.get_ticks() - player_death_time >= 5000:
                player.rect.centerx = 0  # Reset player position
                player.rect.centery = HEIGHT  

                spider.vel_x = random.choice([-6, -8, -10, -4])
                red_bat.vel_x = random.choice([-4, -7, -9])
                blue_bat.vel_x = random.choice([-5, -7, -9])
                black_bat.vel_x = random.choice([-3, -5, -6])

                player_death_time = 0  # Reset death timer


            else:
                screen.fill(BLACK)
                text = font.render("You died, you will respawn in 5 seconds", True, WHITE)
                pg.time.delay(5000)
                screen.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 - text.get_height()//2))
                pg.display.flip()
                pg.time.delay(5000)

        else:
            screen.blit(background_image, (0,0))
            all_sprites.draw(screen)

           
           


            
        # Background
        screen.blit(background_image, (0, 0))

        # --- Draw items
        all_sprites.draw(screen)
        
       
        # Update the screen with anything new
        pg.display.flip()

        # --- Tick the Clock
        clock.tick(60)  # 60 fps

        

 
        

def main():
    start()
    


if __name__ == "__main__":
    main()