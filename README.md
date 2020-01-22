# Culminating
ICS3U Culminating

run src/main.py to start game

depending on where you run main.py from you made need to change line 38 in tilemap.py
from:

```python
new_tilemap.source = pygame.image.load(os.path.join('../assets/', src_img_name))
```
to:
```python
new_tilemap.source = pygame.image.load(os.path.join('assets/', src_img_name))
```
