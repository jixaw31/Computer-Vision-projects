import os, numpy as np, cv2
from glob import glob

def add_ro_lbls(train_lbl_path, val_lbl_path, train_img_path, val_img_path):

    # # creating the directory
    # if os.path.isdir('rotated_lbls'):
    #     pass
    # else:
    #     os.mkdir('rotated_lbls')

    # checking whether the rotated labels exists in dataset
    if len(glob(os.path.join(train_lbl_path, 'ro_*'))):
        pass
    else:
        # adding rotated labels from train labels to rotated_lbls directory
        for img_path in os.listdir(train_img_path): 
            for lbl_path in os.listdir(train_lbl_path):

                if img_path[3:] == lbl_path.replace('.txt', '.jpg'):
                    lbl_arr = np.genfromtxt(os.path.join(train_lbl_path, lbl_path))
                    if len(lbl_arr.shape) > 1:
                        pass
                    else:
                        lbl_arr = np.expand_dims(lbl_arr, axis=0)
                        # print(lbl_arr)
                    f = open(os.path.join(train_lbl_path, f"ro_{lbl_path}"), 'w')
                    for item in lbl_arr:
                        # print(item[1])
                        box_coords = np.array([[ item[1] * 640, item[2] * 640],\
                                                [item[3] * 640, item[4] * 640], \
                                                [item[5] * 640, item[6] * 640],\
                                                [item[7] * 640, item[8] * 640]])

                        M = cv2.getRotationMatrix2D((640//2, 640//2), 45, 1.0)

                        rotated_box_coords = []
                        for coord in box_coords:
                            rotated_coord = np.dot(M, np.array([coord[0], coord[1], 1]))
                            rotated_box_coords.append(rotated_coord)

                        x1 = np.round(rotated_box_coords[0][0]/640, 5)
                        y1 = np.round(rotated_box_coords[0][1]/640, 5)
                        x2 = np.round(rotated_box_coords[1][0]/640, 5)
                        y2 = np.round(rotated_box_coords[1][1]/640, 5)
                        x3 = np.round(rotated_box_coords[2][0]/640, 5)
                        y3 = np.round(rotated_box_coords[2][1]/640, 5)
                        x4 = np.round(rotated_box_coords[3][0]/640, 5)
                        y4 = np.round(rotated_box_coords[3][1]/640, 5)

                        f.write(f"0 {x1} {y1} {x2} {y2} {x3} {y3} {x4} {y4}\n")
                    f.close()
    # checking whether the rotated labels exists in dataset
    if len(glob(os.path.join(val_lbl_path, 'ro_*'))):
        pass
    else:
        # adding rotated labels from val labels to rotated_lbls directory
        for img_path in os.listdir(val_img_path):

            for lbl_path in os.listdir(val_lbl_path):

                if img_path[3:] == lbl_path.replace('.txt', '.jpg'):
                    lbl_arr = np.genfromtxt(os.path.join(val_lbl_path, lbl_path))
                    if len(lbl_arr.shape) > 1:
                        pass
                    else:
                        lbl_arr = np.expand_dims(lbl_arr, axis=0)
                        # print(lbl_arr)
                    f = open(os.path.join(val_lbl_path, f"ro_{lbl_path}"), 'w')
                    for item in lbl_arr:
                        # print(item[1])
                        box_coords = np.array([[ item[1] * 640, item[2] * 640],\
                                                [item[3] * 640, item[4] * 640], \
                                                [item[5] * 640, item[6] * 640],\
                                                [item[7] * 640, item[8] * 640]])

                        M = cv2.getRotationMatrix2D((640//2, 640//2), 45, 1.0)


                        rotated_box_coords = []
                        for coord in box_coords:
                            rotated_coord = np.dot(M, np.array([coord[0], coord[1], 1]))
                            rotated_box_coords.append(rotated_coord)


                        x1 = np.round(rotated_box_coords[0][0]/640, 5)
                        y1 = np.round(rotated_box_coords[0][1]/640, 5)
                        x2 = np.round(rotated_box_coords[1][0]/640, 5)
                        y2 = np.round(rotated_box_coords[1][1]/640, 5)
                        x3 = np.round(rotated_box_coords[2][0]/640, 5)
                        y3 = np.round(rotated_box_coords[2][1]/640, 5)
                        x4 = np.round(rotated_box_coords[3][0]/640, 5)
                        y4 = np.round(rotated_box_coords[3][1]/640, 5)

                        f.write(f"0 {x1} {y1} {x2} {y2} {x3} {y3} {x4} {y4}\n")
                    f.close()


    print(f"number of train labels :{len(os.listdir(train_lbl_path))}")
    print(f"number of val labels :{len(os.listdir(val_lbl_path))}")
    