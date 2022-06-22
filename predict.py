from keras.models import load_model

import argparse
import script.utils

def parse_args():
    desc = "Vehicle Classification"
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('--model', type=str, default='model/vehicle_model_saved.h5', help='Where Is Model File?')
    parser.add_argument('--img', type=str, default='data/1.jpg', help='What Is Images Path?')

    return parser.parse_args()

def main():
    args = parse_args()
    if args is None:
        exit()

    # Load Model
    model = load_model(args.model)
    # Convert Image To Numpy Array
    image = script.utils.load_image(args.img)
    # Predict Image Based On Model
    label = model.predict(image)
    # Print Result
    print("Predicted Class (0 - Cars , 1- Planes): ", round(label[0][0], 2))

if __name__ == '__main__':
    main()