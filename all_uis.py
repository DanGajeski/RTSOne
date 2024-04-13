#class-to-manage-all-ui-ticks
import start_screen as ss
import main_menu_screen as mms
import game_settings_screen as gss
import tk_simple_canvas as tsc
import exit_game_screen as egs
import pause_menu_screen as pms


class AllUIs():
    def __init__(self):
        self.all = {"start_screen": None, "main_menu_screen": None, "game_settings_screen": None, "canvas_screen": None, "exit_game_screen": None, "pause_menu_screen": None}

    def add_ui(self, name: str, ui):
        self.all[name] = ui

    #Possible-name-change?
    def reset_ui_to_none(self, name: str):
        self.all[name] = None

    def tick(self):
        #self.move_entities()
        for ui in self.all.values():
            ui.tick()