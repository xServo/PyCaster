**PyCaster** is a raycasting renderer using PyGame. 

In a raycaster, a 2D map represents the game world as a grid. The player navigates within this grid, and rays are cast from the player's position. These rays measure distances to walls or obstacles, and a corresponding slice of the screen is rendered for each ray to create the illusion of depth and perspective. 

On the left, a display of the 2D map and the rays cast from the player. On the right, is the 3D perspective created using those rays.

<img width="400" alt="Screenshot 2024-09-07 at 6 20 25 PM" src="https://github.com/user-attachments/assets/82d29ea5-4646-4eee-b111-030fc052ec78">
<img width="400" alt="Screenshot 2024-09-07 at 6 20 14 PM" src="https://github.com/user-attachments/assets/911e12a9-5694-4166-be23-e38129ffe825">

## Dependencies

+ Python 3
+ PyGame

```pip3 install pygame```

## To Run
```python3 app.py```
## For MacOs
#### Installing PyGame on MacOS
This is not straightforward like other operating systems. A virtual environment is required for install. 

From the PyCaster directory:

```python -m venv pygame_install```

```source pygame_install/bin/activate```

```pip install pygame```

```deactivate``` to exit venv

#### To Run
```source pygame_install/bin/activate```

```python app.py```
