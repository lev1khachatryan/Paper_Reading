# GSCNN
Based on https://github.com/NVIDIA/semantic-segmentation.

#### Python requirements 

Currently, the code supports Python 3
* numpy 
* PyTorch (>=1.1.0)
* torchvision
* scipy 
* scikit-image
* tensorboardX
* tqdm
* torch-encoding
* opencv
* PyYAML

#### Download pretrained models

Download the pretrained model from the [Google Drive Folder](https://drive.google.com/file/d/1wlhAXg-PfoUM-rFy2cksk43Ng3PpsK2c/view), and save it in 'checkpoints/'

#### Download inferred images

Download (if needed) the inferred images from the [Google Drive Folder](https://drive.google.com/file/d/105WYnpSagdlf5-ZlSKWkRVeq-MyKLYOV/view)

#### Evaluation (Cityscapes)
```bash
python train.py --evaluate --snapshot checkpoints/best_cityscapes_checkpoint.pth
```

#### Training

A note on training- we train on 8 NVIDIA GPUs, and as such, training will be an issue with WiderResNet38 if you try to train on a single GPU.
