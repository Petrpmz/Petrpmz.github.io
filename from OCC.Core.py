
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox

from OCC.Core.BRepFilletAPI import BRepFilletAPI_MakeFillet
from OCC.Core.gp import gp_Pnt
from OCC.Display.SimpleGui import init_display
from OCC.Core.TopExp import TopExp_Explorer
from OCC.Core.TopAbs import TopAbs_EDGE
from OCC.Core.BRep import BRep_Tool

# Inicializace zobrazení
display, start_display, add_menu, add_function_to_menu = init_display()

# 1. Vytvoření základní desky klávesnice
keyboard_base = BRepPrimAPI_MakeBox(180, 60, 5).Shape()  # (šířka, hloubka, výška)

# 2. Zaoblení hran základní desky
fillet = BRepFilletAPI_MakeFillet(keyboard_base)
edge_explorer = TopExp_Explorer(keyboard_base, TopAbs_EDGE)

while edge_explorer.More():
    edge = edge_explorer.Current()
    fillet.Add(3, edge)  # Poloměr zaoblení 3 mm
    edge_explorer.Next()

keyboard_base = fillet.Shape()

# 3. Vytvoření kláves
keys = []
rows, cols = 4, 12  # Počet řádků a sloupců klávesnice
key_width, key_height, key_depth = 14, 14, 3  # Rozměry kláves
spacing = 2  # Mezery mezi klávesami

for i in range(rows):
    for j in range(cols):
        x = j * (key_width + spacing) + 10  # Odsazení zleva
        y = i * (key_height + spacing) + 10  # Odsazení shora
        key = BRepPrimAPI_MakeBox(gp_Pnt(x, y, 5), key_width, key_height, key_depth).Shape()
        keys.append(key)

# Zobrazení modelu
display.DisplayShape(keyboard_base, update=True)
for key in keys:
    display.DisplayShape(key, color="WHITE")

start_display()
