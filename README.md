# The Caffeinity Experience

A scroll-driven woodcut film about Ibn Battuta's first filter kaapi, told in one continuous take.

- `index.html` is the finished page. It is self-contained: open it in a browser.
- `src/template.html` is the source: markup, styles, the WebGL stage and the shot list.
- `assets/` holds the woodcut plates and the two live clips.
- `python3 build.py` inlines the assets into the template and rewrites `index.html`.

To change the story, edit the `SHOTS` list near the top of the script in `src/template.html`:
each shot names its plate, its camera move, how much colour the world has earned, and how it hands over to the next.
