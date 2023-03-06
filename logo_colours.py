from PIL import Image

def rgb_to_hex(colour_tuple):

    r, g, b = colour_tuple

    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def get_logo_hex(logo, palette_size):

    im = Image.open(logo)
    colours = im.getcolors(1000)
    sorted_list = sorted(colours, key=lambda x: -x[0])
    logo_colours = sorted_list[:palette_size]
   
    rgb_colours = [i[1] for i in logo_colours]
    hex_colours = [rgb_to_hex(i) for i in rgb_colours]

    return hex_colours
