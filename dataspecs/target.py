import os

sep = os.sep
data_path = "/dhc/groups/bp2021cl1/data/retinas/"

resize = (896, 896)

DDR_TRAIN = {
    "name": "DDR_train",
    'patch_shape': (388, 388),
    'patch_offset': (300, 300),
    'expand_by': (184, 184),
    "data_dir": "DDR" + sep + "DR_grading" + sep + "train",
    "extension": "jpg",
    "bbox_crop": True,
    'resize': resize,
    'thr_manual': 50
}

DDR_VALID = {
    "name": "DDR_valid",
    'patch_shape': (388, 388),
    'patch_offset': (300, 300),
    'expand_by': (184, 184),
    "data_dir": "DDR" + sep + "DR_grading" + sep + "valid",
    "extension": "jpg",
    "bbox_crop": True,
    'resize': resize,
    'thr_manual': 50
}

DDR_TEST = {
    "name": "DDR_test",
    'patch_shape': (388, 388),
    'patch_offset': (300, 300),
    'expand_by': (184, 184),
    "data_dir": "DDR" + sep + "DR_grading" + sep + "test",
    "extension": "jpg",
    "bbox_crop": True,
    'resize': resize,
    'thr_manual': 50
}

eyePACS_SAMPLE = {
    "name": "eyePACS_sample",
    'patch_shape': (388, 388),
    'patch_offset': (300, 300),
    'expand_by': (184, 184),
    "data_dir": data_path + "eyePACS" + sep + "sample",
    "extension": "jpg",
    "bbox_crop": True,
    'resize': resize,
    'thr_manual': 50
}

DUKE = {
    "name": "Duke",
    'patch_shape': (388, 388),
    'patch_offset': (300, 300),
    'expand_by': (184, 184),
    "data_dir": data_path + "Duke" + sep + "cropped" + sep + "retinas",
    "extension": "jpg",
    "bbox_crop": True,
    'resize': resize,
    'thr_manual': 50
}

HRF = {
    'name': f'HRF{resize[0]}',
    'patch_shape': (388, 388),
    'patch_offset': (300, 300),
    'expand_by': (184, 184),
    'data_dir': data_path + 'HRF' + sep + 'images',
    "extension": "jpg",
    "bbox_crop": True,
    'resize': resize,
    'thr_manual': 50
}
