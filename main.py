from dataspecs import original, transfer, target
from trainer import VesselSegTrainer, BinarySemSegImgPatchDatasetCustomTransform
from easytorch.config import boolean_string
from easytorch import default_ap
from easytorch import EasyTorch
import argparse
import os
import sys

sys.path.append("..")
dataset_list = [original.DRIVE, original.STARE, original.AV_WIDE, original.CHASEDB, original.HRF,
                original.IOSTAR]


def main(args, dataspecs, **kw):
    runner = EasyTorch(dataspecs, args, load_sparse=True, **kw)
    runner.run(VesselSegTrainer, BinarySemSegImgPatchDatasetCustomTransform)


def pooled_main(args, dataspecs, **kw):
    runner = EasyTorch(dataspecs, args, load_sparse=True, **kw)
    runner.run_pooled(VesselSegTrainer,
                      BinarySemSegImgPatchDatasetCustomTransform)


def has_dspec(dname, given_dnames):
    clean_dname = ''.join(i for i in dname if not i.isdigit())
    return clean_dname in given_dnames


def predict_on_dataset():
    """Run on target dataset with best model."""
    #pt = f"{args['log_dir']}{os.sep}Pooled_{len(dataset_list)}{os.sep}best_pooled_chk.tar"
    pt = "net_logsRdClsWtsBsz8R1/Pooled_8/best_pooled_chk.tar"
    target_list = [target.eyePACS_SAMPLE, target.DUKE, target.HRF]
    if len(args['target_datasets']) > 0:
        target_list = [d for d in target_list if has_dspec(
            d['name'], args['target_datasets'])]

    for t in target_list:
        t['name'] = t['name'] + f"_{len(dataset_list)}"
    main(args, target_list, phase='test', split_ratio=[0, 0, 1], pretrained_path=pt,
         log_dir="net_logs", force=True)


if __name__ == "__main__":
    ap = argparse.ArgumentParser(parents=[default_ap], add_help=False)
    ap.add_argument('--training-datasets', default=[],
                    nargs='*', help='Which Datasets to use')
    ap.add_argument('-r', '--model-scale', default=1, type=int,
                    help='Model scale factor.[Default: 1]')
    ap.add_argument('--target-datasets', default=[],
                    nargs='*', help='Target domains.')
    ap.add_argument('-nch', '--num-channel', default=1, type=int,
                    help='Number of input channel[Default: 1]')
    ap.add_argument('-ncl', '--num-class', default=2, type=int,
                    help='Number of class[Default: 2]')
    ap.add_argument('-rcw', '--random-class-weights', default=False, type=boolean_string,
                    help='Random class weights [Default: False]')
    ap.add_argument('-pred', '--predict-on-dataset', default=False, type=boolean_string,
                    help='Predict on Dataset [Default: False]')

    args = vars(ap.parse_args())

    if args['predict_on_dataset']:
        predict_on_dataset()

    else:

        if args['random_class_weights']:
            args['log_dir'] = args['log_dir'] + 'RdClsWts'
        args['log_dir'] = f"{args['log_dir']}Bsz{args['batch_size']}R{args['model_scale']}"

        if len(args['target_datasets']) == 0:
            """If no target, datasets train individually(Original dataspecs)"""
            if len(args['training_datasets']) > 0:
                dataset_list = [d for d in dataset_list if has_dspec(
                    d['name'], args['training_datasets'])]
            main(args, dataset_list, log_dir=args['log_dir'])

        else:
            """
            If target datasets are specified, use all the available dataset(with ground truth) to train a single model 
            and use the best to generate vessels mask for given target datasets.
            """
            dataset_list = transfer.get(
                resize=(800, 800)) + transfer.get(resize=(896, 896))

            if len(args['training_datasets']) > 0:
                dataset_list = [d for d in dataset_list if has_dspec(
                    d['name'], args['training_datasets'])]

            pooled_main(args, dataset_list, log_dir=args['log_dir'])

            """Run on target dataset with best model."""
            pt = f"{args['log_dir']}{os.sep}Pooled_{len(dataset_list)}{os.sep}best_pooled_chk.tar"
            target_list = [target.eyePACS_SAMPLE, target.DUKE]
            if len(args['target_datasets']) > 0:
                target_list = [d for d in target_list if has_dspec(
                    d['name'], args['target_datasets'])]

            for t in target_list:
                t['name'] = t['name'] + f"_{len(dataset_list)}"
            main(args, target_list, phase='test', split_ratio=[0, 0, 1], pretrained_path=pt,
                 log_dir=args['log_dir'], force=True)
