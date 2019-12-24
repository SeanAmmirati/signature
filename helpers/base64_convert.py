import base64
import os

def convert_image(filepath):
    with open(filepath, 'rb') as img:
        b64 = base64.b64encode(img.read())
    return b64


def convert_icons(dir='../img'):
    imgs = [x for x in os.listdir(dir) if os.path.splitext(x)[1] == '.png']
    for img in imgs:
        print(f'For icon {img}, base64 encoded is:')
        print(convert_image(os.path.join(dir, img)))

if __name__ == '__main__':
    convert_icons()