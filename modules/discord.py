from pypresence import Presence, PyPresenceException
import time
import datetime
from . configs import Config_Read, Config_Path
from dearpygui.dearpygui import *
import webbrowser
import multiprocessing

class Discord:
    pass
    # config = Config_Read()
    # presence = config.get('DEFAULT', 'discord_presence')

def Initialize_Discord_Presence():
    config = Config_Read()
    if config.get('DEFAULT', 'discord_presence'):
        if config.get('DEFAULT', 'discord_presence') == 'True':
            
            RPC = Presence(774666488690769930)
            # 
            # # Connect to Discord
            try:
                RPC.connect()
            except PyPresenceException as e:
                print(str(e))
                RPC = None
            # 
            # Set the Rich Presence information
            # RPC.update(
            #     state=None,
            #     details="Brainstorming",
            #     large_image="zamasu_and_vegito",
            #     small_image="gold_small_image",
            #     start=time.time(),
            #     # buttons=[{"label": "Test Button", "url": "https://example.com"}]
            #     # https://discord.gg/EWTyTnPhn7
            # )
            
            # config.set('DEFAULT', 'last_discord_connection', datetime.datetime.now())
            
        else:
            RPC = None
        
    return RPC


def Discord_Presence_Menu(data, sender):
    config = Config_Read()
    if sender:
        config.set('DEFAULT', 'discord_presence', 'True')
    else:
        config.set('DEFAULT', 'discord_presence', 'False')
        
    with open(Config_Path(), 'w') as config_file:
        config.write(config_file)
        
        
def Discord_Server():
    url = 'https://discord.gg/fGdxkZpUyz'
    webbrowser.open(url)