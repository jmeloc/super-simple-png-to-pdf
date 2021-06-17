# -*- coding: utf-8 -*-

import cairo, array


def LUcorner(bgsize, fgsize):
    return tuple( int((x-y)/2) for x, y in zip(bgsize, fgsize) )


# coversion constants
# width_in_points (float) – width of the surface, in points (1 point == 1/72.0 inch)
in_to_point = 72. # point/in
in_to_mm = 25.4   # mm/in
mm_to_point = in_to_point/in_to_mm # point/mm

# parameters
A4_in = (8.267, 11.693)
ppi = 300
A4_mm = tuple(inches*in_to_mm for inches in A4_in)
A4_ppi = tuple( int(inches*ppi) for inches in A4_in ) # A4 (8.267, 11.693) in * 300 ppi

# cairo context
pdfname = 'e_receipt.pdf'
pdf = cairo.PDFSurface( pdfname, 
                        A4_mm[0]*mm_to_point,
                        A4_mm[1]*mm_to_point
                        )

cr = cairo.Context(pdf)

# background
cr.set_source_rgb(128/255, 128/255, 128/255) # gray
cr.paint()

# foreground: image

# If you want to download the image
#import urllib.request, io
#from PIL import Image
#f = urllib.request.urlopen("https://docs.oracle.com/cd/E92727_01/webhelp/Content/obdx/introduction/ereceipt/e_reciept.png")
#i = io.BytesIO(f.read())
#im = Image.open(i)
#imagebuffer = io.BytesIO()
#im.save(imagebuffer, format="PNG")
#imagebuffer.seek(0)
#fg = cairo.ImageSurface.create_from_png(imagebuffer)

# If the image is in local storage
fg = cairo.ImageSurface.create_from_png("e_receipt.png")

# foreground scaling
fg_ppi = (fg.get_width(), fg.get_height())
fg_point = tuple(pixel/ppi*in_to_point for pixel in fg_ppi)
scale = tuple(point/ppi for point,ppi in zip(fg_point,fg_ppi))
xy_ppi = LUcorner(A4_ppi, fg_ppi)
cr.scale(scale[0], scale[1])

# stampling
cr.set_source_surface(fg, xy_ppi[0], xy_ppi[1])
cr.paint()

# saving
cr.show_page()
