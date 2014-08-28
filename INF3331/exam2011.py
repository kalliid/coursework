import os
import Image

def update_image(filename):
    try:
        im = Image.open(filename)
    except:
        print "Failed to open image '%s'." % filename
        print "File not found, or it is not a recognized image format."
        return
    
    logo = Image.open('Twilight_Sparkle.jpeg')
    im_xsize, im_ysize = im.size
    logo_xsize, logo_ysize = logo.size
        
    box = (0, im_ysize-logo_ysize, logo_xsize, im_ysize)
    new_logo = logo.crop((0, 0, logo_xsize, logo_ysize))
    
    im.paste(new_logo, box)
    
    outfile = im.resize((1280, 720))

    out_filename = os.path.splitext(filename)[0] + ".jpeg"
    outfile.save(out_filename)






update_image('Twilight_Sparkle.png')    
