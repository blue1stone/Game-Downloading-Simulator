import pygame as pg
from settings import *
from random import randint

class LoadingBar(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("images/loadingBar.png").convert()
        self.rect = self.image.get_rect()
        self.rect.center = (GAME_WIDTH / 2, GAME_HEIGHT / 2)
        self.progress = 0
        self.game = game
        self.progress_games = {"img0":0, "img1":0, "img2":0, "img3":0, "img4":0, "img5":0, "img6":0, "":0}
        self.loading_progress = {"img0":0, "img1":0, "img2":0, "img3":0, "img4":0, "img5":0, "img6":0}
        self.loading_byte_progress = {"img0":0, "img1":0, "img2":0, "img3":0, "img4":0, "img5":0, "img6":0}
        self.needed_progress_size = {"img0":1260, "img1":1080, "img2":180, "img3":720, "img4":210, "img5":390, "img6":330}
        self.needed_for_byte = {"img0":240, "img1":240, "img2":120, "img3":240, "img4":120, "img5":180, "img6":180}
        self.rgb_val = (0,255,0)
        self.img_picker = pg.image.load("images/color_picker.png").convert()

    def load(self):
        for i in range(10):
            pg.draw.rect(self.game.screen, GREY, ((GAME_WIDTH/2-LOADING_BAR_WIDTH/2)+2+((LOADING_BAR_WIDTH-21)/10)*i+2*i, GAME_HEIGHT/2-44/2, (LOADING_BAR_WIDTH-21)/10, 44))
        for i in range(self.progress):
            pg.draw.rect(self.game.screen, self.rgb_val, ((GAME_WIDTH/2-LOADING_BAR_WIDTH/2)+2+((LOADING_BAR_WIDTH-21)/10)*i+2*i, GAME_HEIGHT/2-44/2, (LOADING_BAR_WIDTH-21)/10, 44))

    def color(self):
        self.r = randint(0,255)
        self.g = randint(0,255)
        self.b = randint(0,255)
        self.rgb_val = []
        self.rgb_val.append(self.r)
        self.rgb_val.append(self.g)
        self.rgb_val.append(self.b)
        self.rgb_val = tuple(self.rgb_val)

    def picker(self):
        self.game.screen.blit(self.img_picker, (GAME_WIDTH/2-227, GAME_HEIGHT/2-27))

class Text():
    def __init__(self, game):
        self.def_font = pg.font.SysFont("Arial Black", 30)
        self.info_font = pg.font.SysFont("Arial Black", 20)
        self.game = game
        self.game_sizes = {0:self.game.l.str_size_vl, 1:self.game.l.str_size_vl, 2:self.game.l.str_size_s, 3:self.game.l.str_size_l, 4:self.game.l.str_size_s, 5:self.game.l.str_size_n, 6:self.game.l.str_size_n}
        self.driver_info = self.info_font.render(self.game.l.str_i_driver, False, BLACK, (255,187,51))
        self.file_info = self.info_font.render(self.game.l.str_i_files, False, BLACK, (255,187,51))
        self.fullscreen_info = self.info_font.render(self.game.l.str_i_fscreen, False, BLACK, (255,187,51))
        self.color_info = self.info_font.render(self.game.l.str_i_color, False, BLACK, (255,187,51))
        self.button_info = self.info_font.render(self.game.l.str_i_button, False, BLACK, (255,187,51))
        self.credits_texts = [self.game.l.str_cr_congrat, self.game.l.str_cr_down, self.game.l.str_cr_nope, "", self.game.l.str_cr_cred, self.game.l.str_cr_1, "", self.game.l.str_cr_th, self.game.l.str_cr_th_player, "", "", "PS:", self.game.l.str_cr_py1, self.game.l.str_cr_py2, self.game.l.str_cr_py3]
        self.info_to_show = ""
        self.dot_counter = 0
        self.dot_am = 0

    def current_loading(self, game_name):
        if self.game.loadingBar.progress_games[self.game.games.ch_game_string] <= 9 and self.game.ch_game_name != "--":
            self.dot_counter += 1
            if self.dot_counter == 50 and self.dot_am <= 2:
                self.dot_am += 1
                self.dot_counter = 0
            elif self.dot_counter == 50 and self.dot_am >= 3:
                self.dot_am = 1
                self.dot_counter = 0
        else:
            self.dot_counter = 0
            self.dot_am = 0
        if self.game.loadingBar.progress_games[self.game.games.ch_game_string] <= 9:
            self.c_load_text = self.def_font.render(self.game.l.str_cur_down+game_name+"."*self.dot_am, False, WHITE)
        else:
            self.c_load_text = self.def_font.render(self.game.l.str_fin_down+game_name, False, WHITE)
        self.c_load_text_pos = self.c_load_text.get_rect(center= (GAME_WIDTH/2, GAME_HEIGHT/2+50))
        self.game.screen.blit(self.c_load_text, self.c_load_text_pos)

    def shop_but(self):
        self.shop_but_text = self.def_font.render(self.game.l.str_shop, False, WHITE)
        self.shop_but_text = pg.transform.scale(self.shop_but_text, (130, 80))
        self.shop_but_pos = self.shop_but_text.get_rect(center= (GAME_WIDTH/2, GAME_HEIGHT/2-154))
        self.game.screen.blit(self.shop_but_text, self.shop_but_pos)

    def show_byte_am(self):
        self.byte_am_text = self.def_font.render(self.game.l.str_total+str(self.game.byte_am), False, WHITE)
        self.byte_am_pos = self.byte_am_text.get_rect(left= 10, top= GAME_HEIGHT/2+100)
        self.game.screen.blit(self.byte_am_text, self.byte_am_pos)

    def show_size(self):
        self.size_text = self.def_font.render(self.game.l.str_f_sizes, False, YELLOW)
        self.size_pos = self.size_text.get_rect(right= GAME_WIDTH-10, top= GAME_HEIGHT-200)
        self.game.screen.blit(self.size_text, self.size_pos)
        for cur_num in range(7):
            self.game_size_text = self.def_font.render(self.game_sizes[cur_num], False, YELLOW)
            self.game_size_text = pg.transform.scale(self.game_size_text, (80,50))
            self.game.screen.blit(self.game_size_text, (12.5+100*cur_num+12.5*cur_num+10, GAME_HEIGHT-167))

    def show_shop_info(self, item):
        self.info_pos_right = list(self.game.mouse_pos)
        self.info_pos_left = list(self.game.mouse_pos)
        self.info_pos_right[1] += 10
        self.info_pos_left[1] += 10
        self.info_pos_left[0] -= 300
        self.info_pos_right = tuple(self.info_pos_right)
        self.info_pos_left = tuple(self.info_pos_left)
        if item == "driver":
            self.game.screen.blit(self.driver_info, self.info_pos_right)
        elif item == "file":
            self.game.screen.blit(self.file_info, self.info_pos_right)
        elif item == "fullscreen":
            self.game.screen.blit(self.fullscreen_info, self.info_pos_left)
        elif item == "color":
            self.game.screen.blit(self.color_info, self.info_pos_right)
        elif item == "button":
            self.game.screen.blit(self.button_info, self.info_pos_left)
        self.game.text.info_to_show = ""

    def show_pr_count(self):
        self.pr_count_text = self.def_font.render(str(self.game.pressableButton.pressed_count), False, WHITE)
        self.pr_count_pos = self.pr_count_text.get_rect(center= (GAME_WIDTH/2+327, GAME_HEIGHT/2))
        self.game.screen.blit(self.pr_count_text, self.pr_count_pos)

    def show_credits(self):
        self.text_count = 0
        for text in self.credits_texts:
            text = self.def_font.render(text, False, BLACK)
            text_pos = text.get_rect(center= (GAME_WIDTH/2, 100+30*self.text_count))
            self.game.screen.blit(text, text_pos)
            self.text_count += 1
        
class Games(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((GAME_WIDTH, 120))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (GAME_WIDTH / 2, GAME_HEIGHT-60)
        self.game = game
        self.img0 = pg.image.load("images/img0.png").convert()
        self.img1 = pg.image.load("images/img1.png").convert()
        self.img2 = pg.image.load("images/img2.png").convert()
        self.img3 = pg.image.load("images/img3.png").convert()
        self.img4 = pg.image.load("images/img4.png").convert()
        self.img5 = pg.image.load("images/img5.png").convert()
        self.img6 = pg.image.load("images/img6.png").convert()
        self.images = [self.img0, self.img1, self.img2, self.img3, self.img4, self.img5, self.img6]
        self.num = 0
        self.ch_over = pg.image.load("images/over.png").convert_alpha()
        self.games_dic = {"img0":self.img0, "img1":self.img1, "img2":self.img2, "img3":self.img3, "img4":self.img4, "img5":self.img5, "img6":self.img6}
        self.ch_game_string = ""

    def draw_images(self):
        self.num = 0
        for img in self.images:
            self.game.screen.blit(img, (12.5+100*self.num+12.5*self.num, GAME_HEIGHT-120+10))
            self.num += 1

    def choose(self, ch_game):
        self.ch_game_string = ch_game
        self.ch_game = self.games_dic[ch_game]
        self.ch_num = self.images.index(self.ch_game)

    def blit_choose(self):
        try:
            self.game.screen.blit(self.ch_over, (12.5+100*self.ch_num+12.5*self.ch_num, GAME_HEIGHT-120+10))
        except:
            pass

class ShopButton(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("images/shop_button.png").convert()
        self.rect = self.image.get_rect()
        self.rect.center = (GAME_WIDTH / 2, GAME_HEIGHT/2-150)
        self.game = game

    def show_shop(self):
        self.shop_img = pg.image.load("images/shop.png").convert()
        self.game.screen.blit(self.shop_img, (87.5, 0))

class PressableButton():
    def __init__(self, game):
        self.default_image = pg.image.load("images/button.png").convert_alpha()
        self.pressed_image = pg.image.load("images/button_pressed.png").convert_alpha()
        self.image = self.default_image
        self.image_pos = self.image.get_rect(center= (GAME_WIDTH/2+227, GAME_HEIGHT/2-15))
        self.pressed_count = 0
        self.pressed_bool = False
        self.game = game

    def pressed(self):
        self.image = self.pressed_image
        if not self.pressed_bool:
            self.pressed_count += 1
            self.pressed_bool = True

    def default_img(self):
        self.image = self.default_image
        self.pressed_bool = False

    def blit_button(self):
        self.game.screen.blit(self.image, self.image_pos)

class LanguageHandler():
    def __init__(self):
        self.langs = ["ENG","DEU"]
        self.str_en = open("strings/strings-en.txt", "r").read().splitlines()
        self.str_de = open("strings/strings-de.txt", "r").read().splitlines()
        self.ch_lang = open("CHOOSE_LANGUAGE.txt","r").read().splitlines()[1]
        if self.ch_lang == "English":
            self.str_l = self.str_en
        elif self.ch_lang == "Deutsch":
            self.str_l = self.str_de
        self.str_shop = self.str_l[0]
        self.str_cur_down = self.str_l[1]
        self.str_fin_down = self.str_l[2]
        self.str_total = self.str_l[3]
        self.str_f_sizes = self.str_l[4]
        self.str_size_vl = self.str_l[5]
        self.str_size_l = self.str_l[6]
        self.str_size_n = self.str_l[7]
        self.str_size_s = self.str_l[8]
        self.str_i_driver = self.str_l[9]
        self.str_i_files = self.str_l[10]
        self.str_i_fscreen = self.str_l[11]
        self.str_i_color = self.str_l[12]
        self.str_i_button = self.str_l[13]
        self.str_cr_congrat = self.str_l[14]
        self.str_cr_down = self.str_l[15]
        self.str_cr_nope = self.str_l[16]
        self.str_cr_cred = self.str_l[17]
        self.str_cr_1 = self.str_l[18]+" BlueStone"
        self.str_cr_th = self.str_l[19]
        self.str_cr_th_player = self.str_l[20]
        self.str_cr_py1 = self.str_l[21]
        self.str_cr_py2 = self.str_l[22]
        self.str_cr_py3 = self.str_l[23]
