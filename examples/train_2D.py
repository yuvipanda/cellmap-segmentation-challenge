# %% Imports
import os
import torch
import numpy as np
from tqdm import tqdm
from cellmap_segmentation_challenge import (
    get_dataloader,
    CellMapLossWrapper,
    load_latest,
    load_best_val,
)
from cellmap_segmentation_challenge.models import UNet_2D, ResNet
from tensorboardX import SummaryWriter
from cellmap_data.utils import get_image_dict

# %% Set hyperparameters and other configurations
learning_rate = 0.0001  # learning rate for the optimizer
batch_size = 8  # batch size for the dataloader
input_array_info = {
    "shape": (1, 128, 128),
    "scale": (8, 8, 8),
}  # shape and voxel size of the data to load for the input
target_array_info = {
    "shape": (1, 128, 128),
    "scale": (8, 8, 8),
}  # shape and voxel size of the data to load for the target
epochs = 1000  # number of epochs to train the model for
iterations_per_epoch = 1000  # number of iterations per epoch
random_seed = 42  # random seed for reproducibility
init_model_features = 32  # number of initial features for the model

classes = ["nuc", "er"]  # list of classes to segment

# Defining model (comment out all that are not used)
# 2D UNet
model_name = "2d_unet"  # name of the model to use
model_to_load = "2d_unet"  # name of the pre-trained model to load
model = UNet_2D(1, len(classes))

# # 2D ResNet
# model_name = "2d_resnet"  # name of the model to use
# model_to_load = "2d_resnet"  # name of the pre-trained model to load
# model = ResNet(ndims=2, output_nc=len(classes))


# Define the paths for saving the model and logs, etc.
data_base_path = "data"  # base path where the data is stored
logs_save_path = "tensorboard/{model_name}"  # path to save the logs from tensorboard
model_save_path = (
    "checkpoints/{model_name}_{epoch}.pth"  # path to save the model checkpoints
)
datasplit_path = "datasplit.csv"  # path to the datasplit file that defines the train/val split the dataloader should use


# Define the spatial transformations to apply to the training data
spatial_transforms = {  # dictionary of spatial transformations to apply to the data
    "mirror": {"axes": {"x": 0.5, "y": 0.5}},
    "transpose": {"axes": ["x", "y"]},
    "rotate": {"axes": {"x": [-180, 180], "y": [-180, 180]}},
}

# %% Make sure the save path exists
os.makedirs(os.path.dirname(model_save_path), exist_ok=True)

# %% Set the random seed
torch.manual_seed(random_seed)
np.random.seed(random_seed)

# %% Check that the GPU is available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Training device: {device}")

# %% Move model to device
model = model.to(device)
load_model = "latest"  # load the latest model or the best validation model

if __name__ == "__main__":
    from cellmap_segmentation_challenge import train

    train(__file__)
