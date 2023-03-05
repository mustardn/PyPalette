import xml.etree.ElementTree as ET
import os

# For this script to work, the tableau repository must be your current working directory
FILE = os.path.join(os.getcwd(), 'Preferences.tps')
colours_to_add = ['#eb912b', '#7099a5', '#c71f34']

tree = ET.parse(FILE)
root = tree.getroot()

# check if preferences tag in the file 
preferences = root.find('preferences')

if preferences is None:
    print('Adding preferences to the file')
    new_element = ET.Element('preferences')
    root.append(new_element)

preferences_element = tree.find('preferences')

def get_palette(name):
    
    element = ".//color-palette[@name='" + name + "']"
    return root.find(element)

def create_palette(palette_name, palette_type):

    '''
    Palette type: regular = categorical
    '''

    # add if statement to check if the colour palette already exists
    palette = get_palette(palette_name)
    if palette:
        print('palette already exists')
    else:
        palette = ET.Element('color-palette')
        palette.set('name', palette_name)
        palette.set('type', palette_type)
        
        preferences_element.append(palette)
        print('palette created')

    return palette

def get_colours(palette):
    return [colour.text for colour in palette]

def add_colour(palette, hex_code: list):

    colour_list = get_colours(palette)

    if isinstance(hex_code, list):
        for colour in hex_code:
            if colour in colour_list:
                print('this colour already exists')
            else:
                color = ET.SubElement(palette, 'color')
                color.text = colour
                print('new colour added')
    else:
        raise TypeError("hex_code must be given as a list")

def save_file(output_file):
    # save file
    tree = ET.ElementTree(root)
    ET.indent(tree, space="\t", level=0)
    tree.write(output_file, xml_declaration=True)

palette = create_palette("New New Palette", 'regular')
add_colour(palette, colours_to_add)
save_file(FILE)

