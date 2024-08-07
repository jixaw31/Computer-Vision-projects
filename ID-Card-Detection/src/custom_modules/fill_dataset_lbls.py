import numpy as np, os
import random

def fill_dataset_lbls(train_lbl_path, val_lbl_path):

    # defining length of training data
    len_train = len(os.listdir('images')) * 0.9
    len_train = int(len_train)

    # original labels listed
    random.seed(42)
    orig_labels = os.listdir('labels')
    random.shuffle(orig_labels)
    

    # adding original labels to train labels
    for lbl_path in orig_labels[:len_train]:
        # print(lbl_path)
        lbl = np.genfromtxt(os.path.join('labels', lbl_path))

        if len(lbl.shape) > 1:
            pass
        else:
            lbl = np.expand_dims(lbl, axis=0)
        # print(lbl)
        f = open(os.path.join(train_lbl_path, f"{lbl_path}"), 'w')
        for item in lbl:
            # print(item[1])
            x1, y1, x2, y2 ,x3, y3, x4, y4 = item[1], item[2], item[3], item[4], item[5],\
                                                            item[6], item[7], item[8]
            # print(str(f"0 {x1} {y1} {x2} {y2} {x3} {y3} {x4} {y4}"))
            f.write(str(f"0 {x1} {y1} {x2} {y2} {x3} {y3} {x4} {y4}\n"))

        f.close()

    # adding original labels to val labels
    for lbl_path in orig_labels[len_train:]:
        # print(lbl_path)
        lbl = np.genfromtxt(os.path.join('labels', lbl_path))

        if len(lbl.shape) > 1:
            pass
        else:
            lbl = np.expand_dims(lbl, axis=0)
        # print(lbl)
        f = open(os.path.join(val_lbl_path, f"{lbl_path}"), 'w')
        for item in lbl:
            # print(item[1])
            x1, y1, x2, y2 ,x3, y3, x4, y4 = item[1], item[2], item[3], item[4], item[5],\
                                                            item[6], item[7], item[8]
            # print(str(f"0 {x1} {y1} {x2} {y2} {x3} {y3} {x4} {y4}"))
            f.write(str(f"0 {x1} {y1} {x2} {y2} {x3} {y3} {x4} {y4}\n"))
        f.close()


    # adding vertically flipped labels to train labels
    for lbl_path in orig_labels[:len_train]:
        # print(lbl_path)
        lbl = np.genfromtxt(os.path.join('labels', lbl_path))

        if len(lbl.shape) > 1:
            pass
        else:
            lbl = np.expand_dims(lbl, axis=0)
        # print(lbl)

        # writing vt flipped labels
        f = open(os.path.join(train_lbl_path, f"vt_{lbl_path}"), 'w')
        for item in lbl:
            # print(item[1])
            x1, y1, x2, y2 ,x3, y3, x4, y4 = 1-item[1], item[2], 1-item[3], item[4], 1-item[5], item[6],\
                                                            1-item[7], item[8]
            # print(str(f"0 {x1} {y1} {x2} {y2} {x3} {y3} {x4} {y4}"))
            f.write(str(f"0 {x1} {y1} {x2} {y2} {x3} {y3} {x4} {y4}\n"))
        f.close()


    # adding vertically flipped labels to val labels
    for lbl_path in orig_labels[len_train:]:
        # print(lbl_path)
        lbl = np.genfromtxt(os.path.join('labels', lbl_path))

        if len(lbl.shape) > 1:
            pass
        else:
            lbl = np.expand_dims(lbl, axis=0)
        # print(lbl)

        # writing vt flipped labels
        f = open(os.path.join(val_lbl_path, f"vt_{lbl_path}"), 'w')
        for item in lbl:
            # print(item[1])
            x1, y1, x2, y2 ,x3, y3, x4, y4 = 1-item[1], item[2], 1-item[3], item[4], 1-item[5], item[6],\
                                                            1-item[7], item[8]
            # print(str(f"0 {x1} {y1} {x2} {y2} {x3} {y3} {x4} {y4}"))
            f.write(str(f"0 {x1} {y1} {x2} {y2} {x3} {y3} {x4} {y4}\n"))
        f.close()

    # adding horizontally flipped labels to train labels
    for lbl_path in orig_labels[:len_train]:
        # print(lbl_path)
        lbl = np.genfromtxt(os.path.join('labels', lbl_path))

        if len(lbl.shape) > 1:
            pass
        else:
            lbl = np.expand_dims(lbl, axis=0)
        # print(lbl)

        # writing hr flipped labels
        f = open(os.path.join(train_lbl_path, f"hr_{lbl_path}"), 'w')
        for item in lbl:
            # print(item[1])
            x1, y1, x2, y2 ,x3, y3, x4, y4 = item[1], 1-item[2], item[3], 1-item[4],item[5], 1-item[6],\
                                                            item[7],1-item[8]
            # print(str(f"0 {x1} {y1} {x2} {y2} {x3} {y3} {x4} {y4}"))
            f.write(str(f"0 {x1} {y1} {x2} {y2} {x3} {y3} {x4} {y4}\n"))

        f.close()

    # adding horizontally flipped labels to val labels
    for lbl_path in orig_labels[len_train:]:
        # print(lbl_path)
        lbl = np.genfromtxt(os.path.join('labels', lbl_path))

        if len(lbl.shape) > 1:
            pass
        else:
            lbl = np.expand_dims(lbl, axis=0)
        # print(lbl)

        # writing hr flipped labels
        f = open(os.path.join(val_lbl_path, f"hr_{lbl_path}"), 'w')
        for item in lbl:
            # print(item[1])
            x1, y1, x2, y2 ,x3, y3, x4, y4 = item[1], 1-item[2], item[3], 1-item[4],item[5], 1-item[6],\
                                                            item[7],1-item[8]
            # print(str(f"0 {x1} {y1} {x2} {y2} {x3} {y3} {x4} {y4}"))
            f.write(str(f"0 {x1} {y1} {x2} {y2} {x3} {y3} {x4} {y4}\n"))

        f.close()


    # adding 90degree counter clockwise labels to train labels
    for lbl_path in orig_labels[:len_train]:
        # print(lbl_path)
        lbl = np.genfromtxt(os.path.join('labels', lbl_path))

        if len(lbl.shape) > 1:
            pass
        else:
            lbl = np.expand_dims(lbl, axis=0)
        # print(lbl)

        # writing counter clockwise rotated labels
        f = open(os.path.join(train_lbl_path, f"ccw_{lbl_path}"), 'w')
        for item in lbl:
            # print(item[1])
            x1, y1, x2, y2 ,x3, y3, x4, y4 = item[2], 1-item[1], item[4], 1-item[3],item[6], 1-item[5],\
                                                            item[8],1-item[7]
            # print(str(f"0 {x1} {y1} {x2} {y2} {x3} {y3} {x4} {y4}"))
            f.write(str(f"0 {x1} {y1} {x2} {y2} {x3} {y3} {x4} {y4}\n"))
        f.close()


    # adding 90degree counter clockwise labels to val labels
    for lbl_path in orig_labels[len_train:]:
        # print(lbl_path)
        lbl = np.genfromtxt(os.path.join('labels', lbl_path))

        if len(lbl.shape) > 1:
            pass
        else:
            lbl = np.expand_dims(lbl, axis=0)
        # print(lbl)

        # writing counter clockwise rotated labels
        f = open(os.path.join(val_lbl_path, f"ccw_{lbl_path}"), 'w')
        for item in lbl:
            # print(item[1])
            x1, y1, x2, y2 ,x3, y3, x4, y4 = item[2], 1-item[1], item[4], 1-item[3],item[6], 1-item[5],\
                                                            item[8],1-item[7]
            # print(str(f"0 {x1} {y1} {x2} {y2} {x3} {y3} {x4} {y4}"))
            f.write(str(f"0 {x1} {y1} {x2} {y2} {x3} {y3} {x4} {y4}\n"))
        f.close()

    # adding 90degree clockwise labels to train labels
    for lbl_path in orig_labels[:len_train]:
        # print(lbl_path)
        lbl = np.genfromtxt(os.path.join('labels', lbl_path))

        if len(lbl.shape) > 1:
            pass
        else:
            lbl = np.expand_dims(lbl, axis=0)
        # print(lbl)

        # writing clockwise rotated labels
        f = open(os.path.join(train_lbl_path, f"cw_{lbl_path}"), 'w')
        for item in lbl:
            # print(item[1])
            x1, y1, x2, y2 ,x3, y3, x4, y4 = 1 - item[2], item[1],1-item[4], item[3],1-item[6], item[5],\
                                                            1-item[8],item[7]
            # print(str(f"0 {x1} {y1} {x2} {y2} {x3} {y3} {x4} {y4}"))
            f.write(str(f"0 {x1} {y1} {x2} {y2} {x3} {y3} {x4} {y4}\n"))
        f.close()


    # adding 90degree clockwise labels to val labels
    for lbl_path in orig_labels[len_train:]:
        # print(lbl_path)
        lbl = np.genfromtxt(os.path.join('labels', lbl_path))

        if len(lbl.shape) > 1:
            pass
        else:
            lbl = np.expand_dims(lbl, axis=0)
        # print(lbl)

        # writing clockwise rotated labels
        f = open(os.path.join(val_lbl_path, f"cw_{lbl_path}"), 'w')
        for item in lbl:
            # print(item[1])
            x1, y1, x2, y2 ,x3, y3, x4, y4 = 1-item[2], item[1], 1- item[4], item[3],1-item[6], item[5],\
                                                            1- item[8],item[7]
            # print(str(f"0 {x1} {y1} {x2} {y2} {x3} {y3} {x4} {y4}"))
            f.write(str(f"0 {x1} {y1} {x2} {y2} {x3} {y3} {x4} {y4}\n"))
        f.close()


    # adding 90degree clockwise labels to train labels
    for lbl_path in orig_labels[:len_train]:
        # print(lbl_path)
        lbl = np.genfromtxt(os.path.join('labels', lbl_path))

        if len(lbl.shape) > 1:
            pass
        else:
            lbl = np.expand_dims(lbl, axis=0)
        # print(lbl)

        # writing clockwise rotated labels
        f = open(os.path.join(train_lbl_path, f"cw_{lbl_path}"), 'w')
        for item in lbl:
            # print(item[1])
            x1, y1, x2, y2 ,x3, y3, x4, y4 = 1 - item[2], item[1],1-item[4], item[3],1-item[6], item[5],\
                                                            1-item[8],item[7]
            # print(str(f"0 {x1} {y1} {x2} {y2} {x3} {y3} {x4} {y4}"))
            f.write(str(f"0 {x1} {y1} {x2} {y2} {x3} {y3} {x4} {y4}\n"))
        f.close()


    print(f"number of train labels :{len(os.listdir(train_lbl_path))}")
    print(f"number of train labels :{len(os.listdir(val_lbl_path))}")