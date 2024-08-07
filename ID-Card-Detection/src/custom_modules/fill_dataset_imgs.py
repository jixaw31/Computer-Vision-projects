import cv2, numpy as np, os
import random


def fill_dataset_imgs(train_img_path, val_img_path):
    
    # defining length of training data
    len_train = len(os.listdir('images')) * 0.9
    len_train = int(len_train)

    random.seed(42)
    orig_images = os.listdir('images')
    random.shuffle(orig_images)

    # adding original images to train dataset
    for img_path in orig_images[:len_train]:
        # print(img_path)
        img = cv2.imread(os.path.join('images', img_path))
        cv2.imwrite(os.path.join(train_img_path, img_path), img)

    

    # adding original images to val dataset
    for img_path in orig_images[len_train:]:
        # print(img_path)
        img = cv2.imread(os.path.join('images', img_path))
        # print(img_path)
        cv2.imwrite(os.path.join(val_img_path, img_path), img)

    # rotating images 90 clock-wise train
    for img_path in orig_images[:len_train]:
        # print(img_path)
        img = cv2.imread(os.path.join('images', img_path))
        img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
        cv2.imwrite(os.path.join(train_img_path, f"cw_{img_path}"), img)

    # rotating images 90 clock-wise val
    for img_path in orig_images[len_train:]:
        # print(img_path)
        img = cv2.imread(os.path.join('images', img_path))
        img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
        cv2.imwrite(os.path.join(val_img_path, f"cw_{img_path}"), img)

    # rotating images 90 counter clock-wise val
    for img_path in orig_images[:len_train]:
        # print(img_path)
        img = cv2.imread(os.path.join('images', img_path))
        img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
        cv2.imwrite(os.path.join(train_img_path, f"ccw_{img_path}"), img)

        
    # rotating images 90 counter clock-wise val
    for img_path in orig_images[len_train:]:
        # print(img_path)
        img = cv2.imread(os.path.join('images', img_path))
        img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
        cv2.imwrite(os.path.join(val_img_path, f"ccw_{img_path}"), img)


    # flipping images horizontally train
    for img_path in orig_images[:len_train]:
        # print(img_path)
        img = cv2.imread(os.path.join('images', img_path))
        img = cv2.flip(img, 0)
        cv2.imwrite(os.path.join(train_img_path, f"hr_{img_path}"), img)

    # flipping images horizontally val
    for img_path in orig_images[len_train:]:
        # print(img_path)
        img = cv2.imread(os.path.join('images', img_path))
        img = cv2.flip(img, 0)
        cv2.imwrite(os.path.join(val_img_path, f"hr_{img_path}"), img)

    # flipping images vertically train
    for img_path in orig_images[:len_train]:
        # print(img_path)
        img = cv2.imread(os.path.join('images', img_path))
        img = cv2.flip(img, 1)
        cv2.imwrite(os.path.join(train_img_path, f"vt_{img_path}"), img)

    # flipping images vertically val
    for img_path in orig_images[len_train:]:
        # print(img_path)
        img = cv2.imread(os.path.join('images', img_path))
        img = cv2.flip(img, 1)
        cv2.imwrite(os.path.join(val_img_path, f"vt_{img_path}"), img)

    

    print(f"number of val images: {len(os.listdir(val_img_path))}")
    print(f"number of train images: {len(os.listdir(train_img_path))}")




def sum_():
    return 2+2