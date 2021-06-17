# -*- coding: utf-8 -*-

from PIL import Image


def LUcorner(bgsize, fgsize):
    return tuple( int((x-y)/2) for x, y in zip(bgsize, fgsize) )


bgcolor=(128,128,128)
A4_300ppi = tuple( int(x*300) for x in [8.267, 11.693] ) # A4 (8.267, 11.693) in * 300 ppi

fg=Image.open('e_receipt.png')
if fg.mode in ("RGBA", "P"): fg = fg.convert("RGB")
bg=Image.new(mode='RGB', size=A4_300ppi, color=bgcolor)

position=LUcorner(bg.size, fg.size)

bg.paste(fg, position)

#print(bg.info["dpi"])
#dpi_x, dpi_y = bg.info["dpi"]

rs=[50, 150, 300]
qs=[90, 95, 99]

from itertools import product

for r, q in product(rs, qs):
    #pass
    bg.save(f'e_receipt_r{r}_q{q}.pdf', format='PDF', resolution=r, quality=q, optimize=True)
