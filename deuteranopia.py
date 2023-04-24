import numpy as np
import cv2

def sim(filename):
    print(filename)
    og_img = cv2.imread(f'static/uploads/{filename}')
    img = og_img[..., ::-1]

    def rgb_to_lms(img):
        lms_matrix = np.array(
            [[0.3904725 , 0.54990437, 0.00890159],
            [0.07092586, 0.96310739, 0.00135809],
            [0.02314268, 0.12801221, 0.93605194]]
            )
        return np.tensordot(img, lms_matrix, axes=([2], [1]))
    def lms_to_rgb(img):
        rgb_matrix = np.array(
            [[ 2.85831110e+00, -1.62870796e+00, -2.48186967e-02],
            [-2.10434776e-01,  1.15841493e+00,  3.20463334e-04],
            [-4.18895045e-02, -1.18154333e-01,  1.06888657e+00]]
            )
        return np.tensordot(img, rgb_matrix, axes=([2], [1]))

    lms_img = rgb_to_lms(img)
    d_sim_matrix = np.array([[1, 0, 0], [1.10104433,  0, -0.00901975], [0, 0, 1]], dtype=np.float16)
    lms_img = np.tensordot(lms_img, d_sim_matrix, axes=([2], [1]))
    rgb_img = lms_to_rgb(lms_img)


    colorblind_img = rgb_img.astype(np.uint8)

    height, width, channels = colorblind_img.shape
    max_width = 800
    max_height = 600
    if width > max_width or height > max_height:
        # Calculate the scale factor to resize the image
        scale_factor = min(max_width / width, max_height / height)
        
        # Resize the image
        colorblind_img = cv2.resize(colorblind_img, (int(scale_factor * width), int(scale_factor * height)))
        og_img = cv2.resize(og_img, (int(scale_factor * width), int(scale_factor * height)))

    # cv2.imshow('cb_img', colorblind_img)
    # cv2.imshow('img', og_img)
    cv2.imwrite('static/sim/deut.png',colorblind_img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

















