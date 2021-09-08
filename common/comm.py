import os
from config.config import img_path


def save_img(driver,img_name):
    driver.get_screenshot_as_file(f'{os.path.abspath(img_path)}/{img_name}.png')