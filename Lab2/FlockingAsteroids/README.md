## Flocking Behaviour
This simulation represents a classical flocking behaviour. 


### Environment
Python 3.8.5

### Third party libraries
SimpleGUICS2Pygame

#### If you want to run it locally
Import simplegui as follows
```python
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
```

### Library integration
```python
from rock_behaviour import update_rock_position
```

### use the update_rock_position function
The update function should be used in the update method of the Sprite class and this function should be used only for the sprites that represent a rock.
```python
    def update(self):
        if self.angle_vel == 0:
            for i in range(DIMENSIONS):
                self.pos[i] %= CANVAS_RES[i]
                self.pos[i] += self.vel[i]
        else:
            update_rock_position(self, rock_group, my_ship, missile_group)
            
        self.angle += self.angle_vel 
        self.age   += 1
        
        # return True if the sprite is old and needs to be destroyed
        if self.age < self.lifespan: 
            return False
        else:
            return True
```

### Run locally
```shell
$ python Simulation.py
```

