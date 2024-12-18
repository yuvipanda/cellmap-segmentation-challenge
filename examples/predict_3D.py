# This file is used to predict the segmentation of the 3D dataset using the trained model.
# %%

from cellmap_segmentation_challenge import predict

# Load the model specified in the train_3D.py script (will load the latest model or the one that performed best on the validation set, depending on the script) #TODO: docs
from train_3D import model, classes, input_array_info

# %%
base_input_path = "./test.zarr/{dataset_name}/raw"
dataset_names = [...]
outpath = "./predictions.zarr/{dataset_name}"

for dataset_name in dataset_names:
    dataset_path = base_input_path.format(dataset_name=dataset_name)
    outpath = outpath.format(dataset_name=dataset_name)

    # TODO: Decide how to handle data scales
    # Predict the segmentation of the dataset
    predict(model, dataset_path, outpath, classes, input_array_info["shape"])
