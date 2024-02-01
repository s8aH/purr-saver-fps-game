import pygame as pg


class Sound:
    def __init__(self, game):
        self.game = game
        pg.mixer.init()
        self.path = 'resources/sound/'
        self.npc_attack = pg.mixer.Sound(self.path + 'npc_attack.wav')
        self.coyote_pain = pg.mixer.Sound(self.path + 'coyote-pain.wav')
        self.coyote_death = pg.mixer.Sound(self.path + 'coyote-death.wav')
        self.npc_attack.set_volume(0.2)
        self.player_hurt = pg.mixer.Sound(self.path + 'player_hurt.mp3')
        self.theme = pg.mixer.music.load(self.path + 'club-seamus.mp3')
        self.meow = pg.mixer.Sound(self.path + 'meow2.mp3')
        pg.mixer.music.set_volume(0.3)