from sys import exit
from random import randint
import time
import math
import iua as i

# Class Hierarchy
# * Map
#   - next_scene
#   - opening_scene
# * Engine
#   - play
# * Scene
#   - enter
#   * Death
# #Add more scenes later....

class Scene(object):
    def enter(self):
        print("This scene is not yet configured.")
        exit(1)
        #this is what happens for all scenes

class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map
    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')
        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
        # be sure to print out the last scene
        current_scene.enter()

class Death(Scene):
    def enter(self):
        print('You died. ')
        exit(1)

class Start(Scene):
    def enter(self):
        print('You enter a room only to see a massive, fire breathing, dungeoness crab.')
        #print(i.is_alive())
        print('\n You and your party can either: 1. Run 2. Fight')
        action = input("> ")
        if action.lower() == "run" or "1":
            print('You run into an even bigger crab, which eats you.')
            return 'death'

class Map(object):
    scenes = {
        'start': Start(),
        'death': Death(), #can add more scenes here..
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('start')
a_game = Engine(a_map)
a_game.play()