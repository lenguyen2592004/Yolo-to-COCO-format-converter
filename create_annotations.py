from pathlib import Path


def create_image_annotation(file_path: Path, width: int, height: int, image_id: int):
    file_path = file_path.name
    image_annotation = {
        "file_name": file_path,
        "height": height,
        "width": width,
        "id": image_id,
    }
    return image_annotation


def create_annotation_from_yolo_format(
    min_x, min_y, width, height, image_id, category_id, annotation_id, segmentation=True
):
    bbox = (float(min_x), float(min_y), float(width), float(height))
    area = width * height
    max_x = min_x + width
    max_y = min_y + height
    if segmentation:
        seg = [[min_x, min_y, max_x, min_y, max_x, max_y, min_x, max_y]]
    else:
        seg = []

    annotation = {
        "id": annotation_id,
        "image_id": image_id,
        "bbox": bbox,
        "area": area,
        "iscrowd": 0,
        "category_id": 1,
        "segmentation": seg,
    }

    return annotation

def create_annotation_from_yolo_results_format(
    min_x, min_y, width, height, image_id, category_id, conf
):
    bbox = (float(min_x), float(min_y), float(width), float(height))
    
    annotation = [{
        "image_id": image_id,
        "category_id": 1,
        "bbox": bbox,
        "score": conf
    }]

    return annotation

# Create the annotations of the ECP dataset (Coco format)
coco_format = {"images": [{}], "categories": [], "annotations": [{}]}
