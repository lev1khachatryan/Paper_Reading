import sys
file='/home/levon/MyProjects/Paper_Reading/SemanticSegmentation/BiSeNet-V2-Ours/'
# sys.path.insert(0, '/'.join(__file__.split('/')[:-3]))
sys.path.insert(0, file)

from trainner.mixed_8K import mixed_8K_bisenetv2_single_gpu_trainner as single_gpu_trainner
from trainner.mixed_8K import mixed_8K_bisenetv2_multi_gpu_trainner as multi_gpu_trainner
from local_utils.log_util import init_logger
from local_utils.config_utils import parse_config_utils

LOG = init_logger.get_logger('train_bisenetv2_mixed_8k_mask')
CFG = parse_config_utils.mixed_8K_cfg

def train_model():
    """

    :return:
    """
    if CFG.TRAIN.MULTI_GPU.ENABLE:
        LOG.info('Using multi gpu trainner ...')
        # worker = multi_gpu_trainner.BiseNetV2CelebamaskhqMultiTrainer()
    else:
        LOG.info('Using single gpu trainner ...')
        worker = single_gpu_trainner.BiseNetV2Mixed8KTrainer()

    worker.train()
    return


if __name__ == '__main__':
    """
    main function
    """
    train_model()
