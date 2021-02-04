from easytorch import EasyTorch
from classification import MyTrainer, MyDataset
import os

sep = os.sep

DRIVE = {
    'name': 'DRIVE',
    'data_dir': 'DRIVE' + sep + 'images',
    'label_dir': 'DRIVE' + sep + 'manual',
    'mask_dir': 'DRIVE' + sep + 'mask',
    'label_getter': lambda file_name: file_name.split('_')[0] + '_manual1.gif',
    'mask_getter': lambda file_name: file_name.split('_')[0] + '_mask.gif'
}
STARE = {
    'name': 'STARE',
    'data_dir': 'STARE' + sep + 'stare-images',
    'label_dir': 'STARE' + sep + 'labels-ah',
    'label_getter': lambda file_name: file_name.split('.')[0] + '.ah.pgm',
}


runner = EasyTorch([DRIVE,STARE],
                   phase='train', batch_size=2, epochs=11,
                   load_sparse=True, num_channel=1, num_class=2,
                   model_scale=2, num_iterations=2,
                   verbose=True, gpus=[0, 1], num_folds=3, force=True)

if __name__ == "__main__":
    runner.run(MyDataset, MyTrainer)
    # runner.run_pooled(MyDataset, MyTrainer)
#