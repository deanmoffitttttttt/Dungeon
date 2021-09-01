def on_button_pressed():
    controller.move_sprite(mySprite, 100, 100)
controller.any_button.on_event(ControllerButtonEvent.PRESSED, on_button_pressed)

def on_left_pressed():
    animation.run_image_animation(mySprite, assets.animation("""
        myAnim0
    """), 200, True)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_right_pressed():
    animation.run_image_animation(mySprite, assets.animation("""
        myAnim
    """), 200, True)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

mySprite: Sprite = None
tiles.set_tilemap(tilemap("""level1"""))
mySprite = sprites.create(img("""
        . . . . . . f f f f f f . . . . 
            . . . . f f e e e e f 2 f . . . 
            . . . f f e e e e f 2 2 2 f . . 
            . . . f e e e f f e e e e f . . 
            . . . f f f f e e 2 2 2 2 e f . 
            . . . f e 2 2 2 f f f f e 2 f . 
            . . f f f f f f f e e e f f f . 
            . . f f e 4 4 e b f 4 4 e e f . 
            . . f e e 4 d 4 1 f d d e f . . 
            . . . f e e e 4 d d d d f . . . 
            . . . . f f e e 4 4 4 e f . . . 
            . . . . . 4 d d e 2 2 2 f . . . 
            . . . . . e d d e 2 2 2 f . . . 
            . . . . . f e e f 4 5 5 f . . . 
            . . . . . . f f f f f f . . . . 
            . . . . . . . f f f . . . . . .
    """),
    SpriteKind.player)
scene.camera_follow_sprite(mySprite)