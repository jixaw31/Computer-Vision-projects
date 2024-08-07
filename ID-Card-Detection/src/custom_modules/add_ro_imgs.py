import cv2, os
from glob import glob


def add_ro_imgs(train_img_path, val_img_path):

    # # rotated images directory
    # if os.path.isdir('rotated_imgs'):
    #     pass
    # else:
    #     os.mkdir('rotated_imgs')

    # creating 45degrees rotated images out of train images
    if len(glob(os.path.join(train_img_path, 'ro_*'))) > 0: # checking whether rotated images are in the directory
        pass
    else:
        for img_path in os.listdir(train_img_path):
            dum_img = os.path.join(train_img_path, img_path)
            # print(dum_img)
            image = cv2.imread(dum_img)

            # 45degrees rotation formula
            (h, w) = image.shape[:2]
            center = (w // 2, h // 2)
            M = cv2.getRotationMatrix2D(center, 45, 1.0)  # 45 is the angle, 1.0 is the scale
            rotated = cv2.warpAffine(image, M, (w, h))
            
            # writing images
            cv2.imwrite(os.path.join(train_img_path, f"ro_{img_path}"), rotated)

    


    # creating 45degrees rotated images out of val images
    if len(glob(os.path.join(val_img_path, 'ro_*'))) > 0:
        pass
    else:
        for img_path in os.listdir(val_img_path):
            dum_img = os.path.join(val_img_path, img_path)
            # print(dum_img)
            image = cv2.imread(dum_img)
            (h, w) = image.shape[:2]
            center = (w // 2, h // 2)
            # Define the rotation matrix
            M = cv2.getRotationMatrix2D(center, 45, 1.0)  # 45 is the angle, 1.0 is the scale
            rotated = cv2.warpAffine(image, M, (w, h))

            cv2.imwrite(os.path.join(val_img_path, f"ro_{img_path}"), rotated)

    print(f"number of train images :{len(os.listdir(train_img_path))}")
    print(f"number of val images :{len(os.listdir(val_img_path))}")