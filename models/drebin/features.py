import datetime
from zipfile import ZipFile, ZIP_DEFLATED
import json
import pandas as pd
import numpy as np


def load_features(features_path):
    """

    Parameters
    ----------
    features_path :
        Absolute path of the features compressed file.

    Returns
    -------
    generator of list of strings
        Iteratively returns the textual feature vector of each sample.
    """
    for filename in features_path.iterdir():
        if filename.suffix == ".json":
            with open(filename) as fp:
                js = json.load(fp)
                yield [f"{k}::{v}" for k in js for v in js[k] if js[k]]


def load_labels(features_path, ds_data_path, return_timestamp=False):
    """

    Parameters
    ----------
    features_path : str
        Absolute path of the features compressed file.
    ds_data_path : str
        Absolute path of the data file (json or compressed csv) containing
        the labels.
    i : int
        If a json file is provided, specify the index to select.

    Returns
    -------
    np.ndarray
        Array of shape (n_samples,) containing the class labels.
    """

    ds_csv = pd.read_csv(ds_data_path)[["sha256", "label", "timestamp"]]
    labels_json = {k: v for k, v in zip(ds_csv.sha256.values, ds_csv.label.values)}
    labels = [
        labels_json[f.stem.lower()]
        for f in features_path.iterdir()
        if f.suffix == ".json"
    ]
    if return_timestamp:
        timestamps = {
            k: v for k, v in zip(ds_csv.sha256.values, ds_csv.timestamp.values)
        }
        timestamps = [
            datetime.datetime.strptime(timestamps[f.stem.lower()], "%Y-%m-%d %H:%M:%S")
            for f in features_path.iterdir()
            if f.suffix == ".json"
        ]
        return (np.array(labels), np.array(timestamps))
    return np.array(labels)


def load_sha256_list(features_path):
    """

    Parameters
    ----------
    features_path :
        Absolute path of the features compressed file.

    Returns
    -------
    list of strings
        List containing the sha256 hash of the APK files.
    """
    return [
        filename.split(".")[0]
        for filename in features_path.iterdir()
        if filename.suffix == ".json"
    ]
