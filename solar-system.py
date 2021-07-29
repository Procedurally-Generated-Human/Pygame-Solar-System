import pygame, random, math


def create_stars(list2d, number, w, h):
    for e in range(number):
        list2d.append([random.randint(0,w),random.randint(0,h)])

def draw_stars(list2d):
    for star in list2d:
        pygame.draw.circle(window, white, star, 1)


class Planet():
    def __init__(self, radius,speed, color, x_radius, y_radius, rings):
        self.radius = radius
        self.speed = speed
        self.degree = 0
        self.color = color
        self.x_radius = x_radius
        self.y_radius = y_radius
        self.rings = rings
    
    def draw(self):
            x1 = int(math.cos(self.degree * 2 * math.pi/360) * self.x_radius) + width/2
            y1 = int(math.sin(self.degree * 2 * math.pi/360) * self.y_radius) + height/2
            pygame.draw.circle(window, self.color, (x1, y1), self.radius)
            if self.rings == True:
                pygame.draw.line(window, white,(x1 - 40, y1),(x1 + 40, y1) ,3)

    def draw_orbit(self):
            pygame.draw.ellipse(window, white, [width/2 - self.x_radius,height/2-self.y_radius,2*(self.x_radius),2*(self.y_radius)] ,1)


class Sun:
    def __init__(self, radius, x, y, color):
        self.radius = radius
        self.x = x
        self.y = y
        self.color = color
        
    def draw_sun(self):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)


def draw_all_planets(all_planets):
    for planet in all_planets:
        planet.draw()
        planet.degree += planet.speed
        

def draw_all_orbits(all_planets):
    for planet in all_planets:
        planet.draw_orbit()


black = (0,0,0)
white = (255,255,255)
yellow = (255,255,0)
blue = (0,0,255)
red = (255,0,0)
grey = (125,125,125)
orange = (255, 204,0)
dark_orange = (180, 120, 0)
creamy = (255, 233, 128)
light_blue = (51, 173, 255)
mid_blue = (0, 107, 179)

width = 1200
height = 700
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Solar System")
fps = 30

stars = []    
create_stars(stars, 100, width, height)
sun = Sun(40,width/2,height/2,yellow)

mercury = Planet(4.8,2.35,grey, 90,45, False)
venus = Planet(9.5,1.8,orange, 140,60, False)
earth = Planet(10,1.5,mid_blue, 180,80, False)
mars = Planet(5.3,1.2,red, 230,100, False)
jupiter = Planet(30,0.65,creamy, 300, 160, False)
saturn = Planet(24,0.49,dark_orange, 400, 220, True)
uranus = Planet(18,0.34,light_blue, 500, 290, False)
neptune = Planet(15.8,0.27,blue, 580, 330, False)
planets = [ mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]


def update_window():
        window.fill(black)
        draw_stars(stars)
        draw_all_orbits(planets)
        draw_all_planets(planets)
        sun.draw_sun()
        pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        update_window()
      
    pygame.quit()


if __name__ == '__main__':
    main()
