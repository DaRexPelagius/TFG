# #!/usr/bin/python
# # -*- coding: latin-1 -*-
import cairo
from igraph.drawing.text import TextDrawer
from igraph import *
from FuncionesNucleo import generaGrafo

g1 = generaGrafo("Scale_Free", n = 200)

# Asignamos colores
for v in VertexSeq(g1):
    if v.degree() > 9:
        v['color'] = 'cyan'
        v['size'] = 50
    elif v.degree() > 8:
        v['color'] = 'yellow'
        v['size'] = 40
    elif v.degree() > 7:
        v['color'] = 'green'
        v['size'] = 30
    elif v.degree() > 6:
        v['color'] = 'pink'
        v['size'] = 20

# Construimos el plot
plot = Plot("scalefree.png", bbox=(600, 400), background="white")
plot.add(g1, bbox=(20, 80, 500, 300))
# Añadimos el grafo al plot
plot.redraw()
# Preparamos el canvas donde escribiremos el grafo
ctx = cairo.Context(plot.surface)
ctx.set_font_size(14)
## Dibujamos la leyenda
drawer = TextDrawer(ctx,"Cyan : Degree(v)>9", halign=TextDrawer.RIGHT)
drawer.draw_at(0, 20, width=580)
drawer = TextDrawer(ctx,"Amarillo : Degree(v)>8", halign=TextDrawer.RIGHT)
drawer.draw_at(0, 40, width=580)
drawer = TextDrawer(ctx,"Verde : Degree(v)>7", halign=TextDrawer.RIGHT)
drawer.draw_at(0, 60, width=580)
drawer = TextDrawer(ctx,"Rosa : Degree(v)>6", halign=TextDrawer.RIGHT)
drawer.draw_at(0, 80, width=580)
drawer = TextDrawer(ctx,"Rojo : Degree(v)<=5", halign=TextDrawer.RIGHT)
drawer.draw_at(0, 100, width=580)


# Save the plot
plot.save()
plot.show()
