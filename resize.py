from PIL import Image

import argparse
import os

def parse_args():
    desc = "Vehicle Classification"
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('--dir', type=str, default='dataset/train/ships', help='Where is Target Directory?')
    parser.add_argument('--size', type=int, default=224, help='Image Output Size?')

    return parser.parse_args()

def crop_center(pil_img, crop_width, crop_height):
    img_width, img_height = pil_img.size
    return pil_img.crop(((img_width - crop_width) // 2,
                         (img_height - crop_height) // 2,
                         (img_width + crop_width) // 2,
                         (img_height + crop_height) // 2))

def keep_aspect_ratio( pil_img, base_size ):
    wpercent = (base_size/float(pil_img.size[0]))
    hsize = int((float(pil_img.size[1])*float(wpercent)))
    return pil_img.resize((base_size,hsize), Image.ANTIALIAS)

def main():
    args = parse_args()
    if args is None:
        exit()
    
    target_folder = args.dir
    folder_files = os.listdir(target_folder)
    for index, item in enumerate(folder_files):
        if os.path.isfile(f'{target_folder}/{item}'):
            im = Image.open(f'{target_folder}/{item}')
            resize_im = keep_aspect_ratio( im, 500 )
            im_new = resize_im.resize((args.size, args.size))
            # im_new = crop_center( resize_im, args.size, args.size )
            f, e = os.path.splitext(f'{target_folder}')
            im_new.save(f'{f}/{index+1}.jpg', 'JPEG', quality=90)

if __name__ == '__main__':
    main()