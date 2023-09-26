from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('my_character_resource.png')

def handle_events():
    global running, dir, state
    # fill here

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            state = "running"
            if event.key == SDLK_RIGHT:
                dir[0] += 1
            elif event.key == SDLK_LEFT:
                dir[0] -= 1
            elif event.key == SDLK_UP:
                dir[1] += 1
            elif event.key == SDLK_DOWN:
                dir[1] -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            state = "idle"
            if event.key == SDLK_RIGHT:
                dir[0] -= 1
            elif event.key == SDLK_LEFT:
                dir[0] += 1
            elif event.key == SDLK_UP:
                dir[1] -= 1
            elif event.key == SDLK_DOWN:
                dir[1] += 1

def checkScreenOut():
    global x, y
    if x > TUK_WIDTH:
        x = TUK_WIDTH
    elif x < 0:
        x = 0
    if y > TUK_HEIGHT:
        y = TUK_HEIGHT
    elif y < 0:
        y = 0


running = True
state = "idle"
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
dir = [0, 0]
# hide_cursor()

while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    if state == "idle":
        character.clip_draw(frame*49+18, 100, 44, 60, x, y, 100, 100)
    elif state == "running":
        character.clip_draw(frame*47+27, 250, 44, 60, x, y, 100, 100)
    update_canvas()
    handle_events()
    frame = (frame+1) % 8
    x += dir[0] * 20
    y += dir[1] * 20
    checkScreenOut()
    delay(0.05)


close_canvas()

