# converting json to txt and adding to labels dir
import json, numpy as np, os

def handle_json_labels(keypoint_labels, keypoint_labels_2):
    # reading labels from json file and writing to txt files
    f = open(keypoint_labels)
    data = json.load(f)
    f.close()

    # required structure for yolov8-OBB
    # class_index, x1,       y1,     x2,       y2,     x3,     y3,       x4,     y4
    # 0         0.780811 0.743961 0.782371 0.74686 0.777691 0.752174 0.776131 0.749758

    if os.path.isdir(os.path.join('labels')):
        pass
    else:
        os.mkdir(os.path.join('labels'))
    # writing labels to txt
    for value in data.values():
        f = open(os.path.join('labels', f"{value['filename']}.txt").replace('.jpg', ''), 'w')
        for region in value['regions']:
            arr_x = np.array(region['shape_attributes']['all_points_x'][:4])
            arr_y = np.array(region['shape_attributes']['all_points_y'][:4])
            arr_x = arr_x/640
            arr_y = arr_y/640
            # print(f"0 {arr_x[0]} {arr_y[0]} {arr_x[1]} {arr_y[1]} {arr_x[2]} {arr_y[2]} {arr_x[3]} {arr_y[3]}")
            f.write(f"0 {arr_x[0]} {arr_y[0]} {arr_x[1]} {arr_y[1]} {arr_x[2]} {arr_y[2]} {arr_x[3]} {arr_y[3]}\n")
        f.close()


    # reading labels from json file and writing to txt files
    f = open(keypoint_labels_2)
    data = json.load(f)
    f.close()


    if os.path.isdir(os.path.join('labels')):
        pass
    else:
        os.mkdir(os.path.join('labels'))

    for value in data.values():
        f = open(os.path.join('labels', f"{value['filename']}.txt").replace('.jpg', ''), 'w')
        for region in value['regions']:
            arr_x = np.array(region['shape_attributes']['all_points_x'][:4])
            arr_y = np.array(region['shape_attributes']['all_points_y'][:4])
            arr_x = arr_x/640
            arr_y = arr_y/640
            # print(f"0 {arr_x[0]} {arr_y[0]} {arr_x[1]} {arr_y[1]} {arr_x[2]} {arr_y[2]} {arr_x[3]} {arr_y[3]}")
            f.write(f"0 {arr_x[0]} {arr_y[0]} {arr_x[1]} {arr_y[1]} {arr_x[2]} {arr_y[2]} {arr_x[3]} {arr_y[3]}\n")
        f.close()

    
    print(f"number of original labels: {len(os.listdir(os.path.join('labels')))}")