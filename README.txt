WIGGLESTUDIOO CODE LAB

Folders:  demos (live demo pages), downloads (zips and the python file), img (pictures).
Open index.html in your browser to preview. Be online for the cute fonts.

ADD A NEW CARD (after each new Short):
 1) Put the demo page in demos, for example demos/mynew.html
 2) Open build.py, add a line to a section:
    dict(id="mynew", emoji="🍓", title="My New Thing", desc="One short sentence.", tags=["HTML","CSS"], video=S("YOUTUBE_SHORT_ID")),
    (the Short id is the part after youtube.com/shorts/)
 3) Run: python3 build.py   (this refreshes data.js)
 No Python? Send the demo to Claude and ask for the updated data.js.

PREMIUM LATER: add premium=True, buy="your checkout link", img="img/x.jpg" to an item.
Do NOT put paid code in this folder. Anyone could open it.
