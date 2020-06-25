import sys
file='/home/levon/MyProjects/Paper_Reading/SemanticSegmentation/BiSeNet-V2-Ours/'
# sys.path.insert(0, '/'.join(__file__.split('/')[:-3]))
sys.path.insert(0, file)

from data_provider.mixed_8K import mixed_8K_tf_io
from local_utils.log_util import init_logger

LOG = init_logger.get_logger(log_file_name_prefix='generate_mixed_8K_tfrecords')


def generate_tfrecords():
    """

    :return:
    """
    io = mixed_8K_tf_io.mixed_8K_TfIO()
    io.writer.write_tfrecords()

    return


if __name__ == '__main__':
    """
    test
    """
    generate_tfrecords()
