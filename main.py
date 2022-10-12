import pygame
pygame.init()       # To initilise pygame
window = pygame.display.set_mode((1200, 400))       # dimention of image
track = pygame.image.load('track6.png')
car = pygame.image.load('tesla.png')
car = pygame.transform.scale(car, (30, 60))         # To transform the size of car
car_x = 155
car_y = 300
focal_dis = 25      # As camera is 15px inside car so take it 15px out and more 10px for saf turn
cam_x_offset = 0
cam_y_offset = 0
direction = 'up'
drive = True
clock = pygame.time.Clock()
while drive:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drive = False
    clock.tick(60)          # To decrease the speed of car
    cam_x = car_x + cam_x_offset + 15       # Camera_x which is in middle of car
    cam_y = car_y + cam_y_offset + 15
    up_px = window.get_at((cam_x, cam_y - focal_dis))[0]        # To check the colour of upper pixel
    down_px = window.get_at((cam_x, cam_y + focal_dis))[0]
    right_px = window.get_at((cam_x + focal_dis, cam_y))[0]
    print(up_px, right_px, down_px)

    # change direction (take turn)
    if direction == 'up' and up_px != 255 and right_px == 255:      # Turn Right and drive
        direction = 'right'
        cam_x_offset = 30               # To take camera at proper position while turning
        car = pygame.transform.rotate(car, -90)
    elif direction == 'right' and right_px != 255 and down_px == 255:
        direction = 'down'
        car_x = car_x + 30
        cam_x_offset = 0
        cam_y_offset = 30
        car = pygame.transform.rotate(car, -90)
    elif direction == 'down' and down_px != 255 and right_px == 255:
        direction = 'right'
        car_y = car_y + 30
        cam_x_offset = 30
        cam_y_offset = 0
        car = pygame.transform.rotate(car, 90)
    elif direction == 'right' and right_px != 255 and up_px == 255:
        direction = 'up'
        car_x = car_x + 30
        cam_x_offset = 0
        car = pygame.transform.rotate(car, 90)
    # drive
    if direction == 'up' and up_px == 255:      # Keep moving
        car_y = car_y - 2
    elif direction == 'right' and right_px == 255:      # Keep moving
        car_x = car_x + 2
    elif direction == 'down' and down_px == 255:        # Keep moving
        car_y = car_y + 2
    window.blit(track, (0, 0))      # Block Image Transfer  (0,0) is position as starting corner
    window.blit(car, (car_x, car_y))
    pygame.draw.circle(window, (0, 255, 0), (cam_x, cam_y), 5, 5)       # To draw circle with radius and width 5 and center is camera also the colour is green
    pygame.display.update()