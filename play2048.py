from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random

def play2048():
    browser = webdriver.Chrome()
    # open 2048
    browser.get('https://play2048.co/')

    arrow_keys = [Keys.ARROW_UP, Keys.ARROW_DOWN, Keys.ARROW_LEFT, Keys.ARROW_RIGHT]

    while True:
        # If game over, stop playing
        if len(browser.find_elements_by_class_name('game-message.game-over')) != 0:
            print('Game over!')
            return
            # press random arrow key
            htmlElem = browser.find_element_by_tag_name('html')
            htmlElem.send_keys(random.choice(arrow_keys))

play2048()
