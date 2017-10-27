import pygame as pg
from sprites import *
from settings import *
from random import randint

class Game():
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
        pg.display.set_caption("Game Downloading Simulator")
        pg.display.set_icon(pg.image.load("images/icon.png"))
        self.clock = pg.time.Clock()
        self.l = LanguageHandler()
        self.all_sprites = pg.sprite.Group()
        self.loadingBar = LoadingBar(self)
        self.all_sprites.add(self.loadingBar)
        self.text = Text(self)
        self.games = Games(self)
        self.all_sprites.add(self.games)
        self.shop_button = ShopButton(self)
        self.all_sprites.add(self.shop_button)
        self.pressableButton = PressableButton(self)
        self.ch_game_name = "--"
        self.shop_show = False
        self.byte_am = 0
        self.upgrades = {"file_size":False, "driver_update":False, "fullscreen":False, "loading_color":False, "pressable_button":False}
        self.download_speed = 1
        self.f_screen = False
        self.finished = 0
        self.credits = False
        self.running = True

    def loop(self):
        self.clock.tick(60)
        self.events()
        self.update()
        self.draw()

    def events(self):
        self.mouse_pos = pg.mouse.get_pos()
        if self.mouse_pos[0] >= 316.5 and self.mouse_pos[0] <= 410.5 and self.mouse_pos[1] >= 29 and self.mouse_pos[1] <= 123:
            self.text.info_to_show = "file"
        elif self.mouse_pos[0] >= 116.5 and self.mouse_pos[0] <= 210.5 and self.mouse_pos[1] >= 29 and self.mouse_pos[1] <= 123:
            self.text.info_to_show = "driver"
        elif self.mouse_pos[0] >= 416.5 and self.mouse_pos[0] <= 510.5 and self.mouse_pos[1] >= 128 and self.mouse_pos[1] <= 228:
            self.text.info_to_show = "fullscreen"
        elif self.mouse_pos[0] >= 216.5 and self.mouse_pos[0] <= 310.5 and self.mouse_pos[1] >= 128 and self.mouse_pos[1] <= 228:
            self.text.info_to_show = "color"
        elif self.mouse_pos[0] >= 516.5 and self.mouse_pos[0] <= 610.5 and self.mouse_pos[1] >= 29 and self.mouse_pos[1] <= 123:
            self.text.info_to_show = "button"
        if pg.mouse.get_pressed()[0]:
            if self.upgrades["pressable_button"]:
                if self.mouse_pos[0] >= 584 and self.mouse_pos[0] <= 671 and self.mouse_pos[1] >= 255 and self.mouse_pos[1] <= 312:
                    self.pressableButton.pressed()
                else:
                    self.pressableButton.default_img()
        else:
            self.pressableButton.default_img()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                g.running = False
            if event.type == pg.MOUSEBUTTONUP:
                if self.mouse_pos[1] >= 490 and self.mouse_pos[1] <= 590:
                    if self.mouse_pos[0] >= 12.5 and self.mouse_pos[0] <= 112.5:
                        self.games.choose("img0")
                        self.ch_game_name = "Hole 3"
                    elif self.mouse_pos[0] >= 125 and self.mouse_pos[0] <= 225:
                        self.games.choose("img1")
                        self.ch_game_name = "Full Life 3"
                    elif self.mouse_pos[0] >= 237.5 and self.mouse_pos[0] <= 337.5:
                        self.games.choose("img2")
                        self.ch_game_name = "Overtale 2"
                    elif self.mouse_pos[0] >= 350 and self.mouse_pos[0] <= 450:
                        self.games.choose("img3")
                        self.ch_game_name = "Upnautica"
                    elif self.mouse_pos[0] >= 462.5 and self.mouse_pos[0] <= 562.5:
                        self.games.choose("img4")
                        self.ch_game_name = "TwoShot"
                    elif self.mouse_pos[0] >= 575 and self.mouse_pos[0] <= 675:
                        self.games.choose("img5")
                        self.ch_game_name = "Dirtaria"
                    elif self.mouse_pos[0] >= 687.5 and self.mouse_pos[0] <= 787.5:
                        self.games.choose("img6")
                        self.ch_game_name = "Four Nights at Ydderf's"
                elif not self.shop_show and self.mouse_pos[1] >= 107.5 and self.mouse_pos[1] <= 192.5:
                    if self.mouse_pos[0] >= 325 and self.mouse_pos[0] <= 475:
                        self.shop_show = True
                elif self.shop_show:
                    if self.mouse_pos[0] >= 668.5 and self.mouse_pos[0] <= 712.5 and self.mouse_pos[1] >= 0 and self.mouse_pos[1] <= 44:
                        self.shop_show = False
                    elif self.mouse_pos[0] >= 316.5 and self.mouse_pos[0] <= 410.5 and self.mouse_pos[1] >= 29 and self.mouse_pos[1] <= 123:
                        if not self.upgrades["file_size"]:
                            if self.byte_am >= 30:
                                self.byte_am -= 30
                                self.upgrades["file_size"] = True
                    elif self.mouse_pos[0] >= 116.5 and self.mouse_pos[0] <= 210.5 and self.mouse_pos[1] >= 29 and self.mouse_pos[1] <= 123:
                        if not self.upgrades["driver_update"]:
                            if self.byte_am >= 55:
                                self.byte_am -= 55
                                self.download_speed = 2
                                self.upgrades["driver_update"] = True
                    elif self.mouse_pos[0] >= 416.5 and self.mouse_pos[0] <= 510.5 and self.mouse_pos[1] >= 128 and self.mouse_pos[1] <= 228:
                        if not self.upgrades["fullscreen"]:
                            if self.byte_am >= 40:
                                self.byte_am -= 40
                                self.upgrades["fullscreen"] = True
                    elif self.mouse_pos[0] >= 216.5 and self.mouse_pos[0] <= 310.5 and self.mouse_pos[1] >= 128 and self.mouse_pos[1] <= 228:
                        if not self.upgrades["loading_color"]:
                            if self.byte_am >= 35:
                                self.byte_am -= 35
                                self.upgrades["loading_color"] = True
                    elif self.mouse_pos[0] >= 516.5 and self.mouse_pos[0] <= 610.5 and self.mouse_pos[1] >= 29 and self.mouse_pos[1] <= 123:
                        if not self.upgrades["pressable_button"]:
                            if self.byte_am >= 20:
                                self.byte_am -= 20
                                self.upgrades["pressable_button"] = True
                if self.upgrades["loading_color"]:
                    if self.mouse_pos[0] >= 173 and self.mouse_pos[0] <= 227 and self.mouse_pos[1] >= 273 and self.mouse_pos[1] <= 327:
                        self.loadingBar.color()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_F9:
                    if self.upgrades["fullscreen"]:
                        if self.f_screen:
                            self.screen = pg.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
                            self.f_screen = False
                        elif not self.f_screen:
                            self.screen = pg.display.set_mode((GAME_WIDTH, GAME_HEIGHT), pg.FULLSCREEN)
                            self.f_screen = True
    
    def update(self):
        self.all_sprites.update()
        if self.games.ch_game_string != "":
            self.loadingBar.progress = self.loadingBar.progress_games[self.games.ch_game_string]
            if self.loadingBar.progress <= 9:
                self.loadingBar.loading_progress[self.games.ch_game_string] += 1*self.download_speed
                self.loadingBar.loading_byte_progress[self.games.ch_game_string] += 1*self.download_speed
                if self.loadingBar.loading_byte_progress[self.games.ch_game_string] >= self.loadingBar.needed_for_byte[self.games.ch_game_string]:
                    self.byte_am += 1
                    self.loadingBar.loading_byte_progress[self.games.ch_game_string] = 0
                if self.loadingBar.loading_progress[self.games.ch_game_string] >= self.loadingBar.needed_progress_size[self.games.ch_game_string]:
                    self.loadingBar.progress += 1
                    self.loadingBar.progress_games[self.games.ch_game_string] += 1
                    self.loadingBar.loading_progress[self.games.ch_game_string] = 0
        for current_game in self.loadingBar.progress_games:
            if self.loadingBar.progress_games[current_game] == 10:
                self.finished += 1
        if self.finished == 7:
            self.credits = True
        else:
            self.finished = 0

    def draw(self):
        if not self.credits:
            self.screen.fill((10,10,10))
            self.all_sprites.draw(self.screen)
            self.loadingBar.load()
            self.text.current_loading(self.ch_game_name)
            self.text.show_byte_am()
            if self.upgrades["file_size"]:
                self.text.show_size()
            self.text.shop_but()
            if self.upgrades["pressable_button"]:
                self.text.show_pr_count()
                self.pressableButton.blit_button()
            self.games.draw_images()
            self.games.blit_choose()
            if self.upgrades["loading_color"]:
                self.loadingBar.picker()
            if self.shop_show:
                self.shop_button.show_shop()
                self.text.show_shop_info(self.text.info_to_show)
        else:
            self.screen.fill((235,235,235))
            self.text.show_credits()
        pg.display.flip()


g = Game()
while g.running:
    g.loop()
pg.quit()
