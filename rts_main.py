import tk_simple_canvas
import unit_data
import canvas_entities as ce
import game_environment as game_environment

class RTSMain:
    def __init__(self):
        self.display_environment: tk_simple_canvas.DisplayEnvironment = tk_simple_canvas.DisplayEnvironment()
        self.game_environment = game_environment.GameEnvironment()

        #tie-environments-together
        self.display_environment.import_game_environment(self.game_environment)
        self.game_environment.import_display_environment(self.display_environment)

        #for-key_bindings
        self.main_window = self.display_environment.get_main_window()
        #self.display_environment.set_display_key_bindings()#don'tneedtopass-here-because-main_window-comes-from-display_environment
        #self.game_environment.set_display_key_bindings(self.main_window)

    def tick(self):
        self.main_window.after(60, self.tick)
        self.display_environment.tick()
        self.game_environment.tick()

rtsmain = RTSMain()
rtsmain.tick()
rtsmain.display_environment.run_main_window()