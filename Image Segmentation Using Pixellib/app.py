import pixellib
from pixellib.instance import instance_segmentation
segment_image = instance_segmentation()
segment_image.load_model(r"C:\Users\USER\Desktop\Project\Learn-Implement-Predict\Image Segmentation Using Pixellib\mask_rcnn_coco.h5") 
segment_image.segmentImage(r"C:\Users\USER\Desktop\Project\Learn-Implement-Predict\Image Segmentation Using Pixellib\Roads.jpg", show_bboxes = True, output_image_name = r"C:\Users\USER\Desktop\Project\Learn-Implement-Predict\Image Segmentation Using Pixellib\output1.jpg")