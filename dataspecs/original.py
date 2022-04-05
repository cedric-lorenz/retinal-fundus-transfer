import os

sep = os.sep
data_path = "/dhc/groups/bp2021cl1/data/retinas/"

"""--------------------------------------------------------------------------"""


def get_label_drive(file_name):
    return file_name.split('_')[0] + '_manual1.gif'


def get_mask_drive(file_name):
    return file_name.split('_')[0] + '_mask.gif'


DRIVE = {
    'name': 'DRIVE',
    'patch_shape': (388, 388),
    'patch_offset': (300, 300),
    'expand_by': (184, 184),
    'data_dir': data_path + 'DRIVE' + sep + 'images',
    'label_dir': data_path + 'DRIVE' + sep + 'manual',
    'split_dir': data_path + 'DRIVE' + sep + 'splits',
    'mask_dir': data_path + 'DRIVE' + sep + 'mask',
    'label_getter': get_label_drive,
    'mask_getter': get_mask_drive
}

"""--------------------------------------------------------------------"""


def get_labels_stare(file_name):
    return file_name.split('.')[0] + '.ah.pgm'


STARE = {
    'name': 'STARE',
    'patch_shape': (388, 388),
    'patch_offset': (300, 300),
    'expand_by': (184, 184),
    'data_dir': data_path + 'STARE' + sep + 'images',
    'label_dir': data_path + 'STARE' + sep + 'labels-vk',
    'split_dir': data_path + 'STARE' + sep + 'splits',
    'label_getter': get_labels_stare,
}

"""--------------------------------------------------------------------------"""


def get_label_wide(file):
    return file.split('.')[0] + '_vessels.png'


AV_WIDE = {
    'name': 'WIDE',
    'patch_shape': (388, 388),
    'patch_offset': (300, 300),
    'expand_by': (184, 184),
    'data_dir': 'AV-WIDE' + sep + 'images',
    'label_dir': 'AV-WIDE' + sep + 'manual',
    'split_dir': 'AV-WIDE' + sep + 'splits',
    'label_getter': get_label_wide
}

"""--------------------------------------------------------------------------"""


def get_label_chasedb(file):
    return file.split('.')[0] + '_1stHO.png'


CHASEDB = {
    'name': 'CHASEDB',
    'patch_shape': (388, 388),
    'patch_offset': (300, 300),
    'expand_by': (184, 184),
    'data_dir': data_path + 'CHASEDB1' + sep + 'images',
    'label_dir': data_path + 'CHASEDB1' + sep + 'manual',
    'split_dir': data_path + 'CHASEDB1' + sep + 'splits',
    'label_getter': get_label_chasedb
}

"""--------------------------------------------------------------------------"""


def get_label_HRF(file_name):
    return file_name.split('.')[0] + '.tif'


def get_mask_HRF(file_name):
    return file_name.split('.')[0] + '_mask.tif'


HRF = {
    'name': 'HRF',

    'patch_shape': (836, 836),
    'patch_offset': (650, 650),
    'expand_by': (184, 184),
    'data_dir': data_path + 'HRF' + sep + 'images',
    'label_dir': data_path + 'HRF' + sep + 'manual',
    'mask_dir': data_path + 'HRF' + sep + 'mask',
    'split_dir': data_path + 'HRF' + sep + 'splits',
    'label_getter': get_label_HRF,
    'mask_getter': get_mask_HRF
}

"""--------------------------------------------------------------------------"""


def get_label_iostar(file_name):
    return file_name.split('.')[0] + '_GT.tif'


def get_mask_iostar(file_name):
    return file_name.split('.')[0] + '_Mask.tif'


IOSTAR = {
    'name': 'IOSTAR',
    'patch_shape': (388, 388),
    'patch_offset': (300, 300),
    'expand_by': (184, 184),
    'data_dir': 'IOSTAR' + sep + 'image',
    'label_dir': 'IOSTAR' + sep + 'Vessel_GT',
    'mask_dir': 'IOSTAR' + sep + 'mask',
    'split_dir': 'IOSTAR' + sep + 'splits',
    'label_getter': get_label_iostar,
    'mask_getter': get_mask_iostar
}
