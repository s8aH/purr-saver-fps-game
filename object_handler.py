from sprite_object import *
from npc import *
from random import choices, randrange


class ObjectHandler:
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.npc_list = []
        self.npc_sprite_path = 'resources/sprites/npc/'
        self.static_sprite_path = 'resources/sprites/static_sprites/'
        self.anim_sprite_path = 'resources/sprites/animated_sprites/'
        add_sprite = self.add_sprite
        add_npc = self.add_npc
        self.npc_positions = {}

        # Spawn npc's
        self.enemies = 20  # npc count
        self.npc_types = [CoyoteNPC]
        self.weights = [70, 20, 10]
        self.restricted_area = {(i, j) for i in range(10) for j in range(10)}

        self.spawn_npc()

        # Spawn kitten sprite
        self.spawn_static_sprite(KittenSpriteObject, 'cat4.png')

        # Add static and animated sprites
        add_sprite(AnimatedSprite(game))
        add_sprite(AnimatedSprite(game, pos=(1.5, 1.5)))
        add_sprite(AnimatedSprite(game, pos=(1.5, 7.5)))
        add_sprite(AnimatedSprite(game, pos=(5.5, 3.25)))
        add_sprite(AnimatedSprite(game, pos=(5.5, 4.75)))
        add_sprite(AnimatedSprite(game, pos=(7.5, 2.5)))
        add_sprite(AnimatedSprite(game, pos=(7.5, 5.5)))
        add_sprite(AnimatedSprite(game, pos=(14.5, 1.5)))
        add_sprite(AnimatedSprite(game, pos=(14.5, 4.5)))
        # add_sprite(AnimatedSprite(game, pos=(14.5, 5.5)))
        # add_sprite(AnimatedSprite(game, pos=(14.5, 7.5)))
        # add_sprite(AnimatedSprite(game, pos=(12.5, 7.5)))
        # add_sprite(AnimatedSprite(game, pos=(9.5, 7.5)))
        # add_sprite(AnimatedSprite(game, pos=(14.5, 12.5)))
        # add_sprite(AnimatedSprite(game, pos=(9.5, 20.5)))
        # add_sprite(AnimatedSprite(game, pos=(10.5, 20.5)))
        # add_sprite(AnimatedSprite(game, pos=(3.5, 14.5)))
        # add_sprite(AnimatedSprite(game, pos=(3.5, 18.5)))
        add_sprite(AnimatedSprite(game, pos=(14.5, 24.5)))
        add_sprite(AnimatedSprite(game, pos=(14.5, 30.5)))
        add_sprite(AnimatedSprite(game, pos=(1.5, 30.5)))
        add_sprite(AnimatedSprite(game, pos=(1.5, 24.5)))

    def spawn(self):
        pos = x, y = randrange(self.game.map.cols), randrange(self.game.map.rows)
        while (pos in self.game.map.world_map) or (pos in self.restricted_area):
            pos = x, y = randrange(self.game.map.cols), randrange(self.game.map.rows)
        return x, y

    def spawn_npc(self):
        for i in range(self.enemies):
            npc = self.npc_types[0]
            x, y = self.spawn()
            self.add_npc(npc(self.game, pos=(x + 0.5, y + 0.5)))

    def spawn_static_sprite(self, sprite_type, file_name):
        x, y = self.spawn()
        self.add_sprite(sprite_type(self.game, path=self.static_sprite_path + file_name, pos=(x + 0.5, y + 0.5)))


    def check_win(self):
        if self.game.player.kitten_rescued:
            self.game.object_renderer.win()
            pg.display.flip()
            pg.time.delay(1500)
            self.game.new_game()

    def update(self):
        self.npc_positions = {npc.map_pos for npc in self.npc_list if npc.alive}
        [sprite.update() for sprite in self.sprite_list]
        [npc.update() for npc in self.npc_list]
        self.check_win()

    def add_npc(self, npc):
        self.npc_list.append(npc)

    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)