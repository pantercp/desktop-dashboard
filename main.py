# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 19:14:42 2023

@author: Ronaldo
"""

import productivity
import inspiration_image
import desktop_maker
import os
import struct
import ctypes


source_dir = os.getcwd()



SPI_SETDESKWALLPAPER = 20
WALLPAPER_PATH = (source_dir+r'\output\wallpaper.png')


def is_64_windows():
    """Find out how many bits is OS. """
    return struct.calcsize('P') * 8 == 64

def get_sys_parameters_info():
    """Based on if this is 32bit or 64bit returns correct version of SystemParametersInfo function. """
    return ctypes.windll.user32.SystemParametersInfoW if is_64_windows() \
        else ctypes.windll.user32.SystemParametersInfoA

def change_wallpaper():
    sys_parameters_info = get_sys_parameters_info()
    r = sys_parameters_info(SPI_SETDESKWALLPAPER, 0, WALLPAPER_PATH, 3)

    # When the SPI_SETDESKWALLPAPER flag is used,
    # SystemParametersInfo returns TRUE
    # unless there is an error (like when the specified file doesn't exist).
    if not r:
        print(ctypes.WinError())


change_wallpaper()
