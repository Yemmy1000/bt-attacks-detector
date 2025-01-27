import logging

import numpy as np
import pandas as pd

import data
import scripts.utils as utils

LOGGER = logging.getLogger(__name__)
"""Data preprocessing logger."""

_data_types = {
    "No.": int,
    "Time": float,
    "Source": object,
    "Destination": object,
    "Protocol": object,
    "Length": int,
    "Info": object,
}


def run():
    """Run the data preprocessing script."""
    LOGGER.info("Preprocessing dataset...")

    LOGGER.debug("Loading datasets...")
    attack_train = pd.read_csv(data.ATTACK_TRAIN)
    benign_train = pd.read_csv(data.BENIGN_TRAIN)
    attack_test = pd.read_csv(data.ATTACK_TEST)
    benign_test = pd.read_csv(data.BENIGN_TEST)

    # data types check
    LOGGER.debug("Checking data types...")
    for dataset in [attack_train, benign_train, attack_test, benign_test]:
        for column, data_type in _data_types.items():
            assert (
                dataset[column].dtype == data_type
            ), f"Invalid data type for {column}"

    # add type column indicating attack or benign
    attack_train["Type"] = 1
    attack_test["Type"] = 1
    benign_train["Type"] = 0
    benign_test["Type"] = 0

    # combine datasets
    LOGGER.debug("Combining datasets...")
    train_dataset = pd.concat([attack_train, benign_train], ignore_index=True)
    test_dataset = pd.concat([attack_test, benign_test], ignore_index=True)

    # shuffle datasets
    LOGGER.debug("Shuffling datasets...")
    train_dataset = train_dataset.sample(frac=1).reset_index(drop=True)
    test_dataset = test_dataset.sample(frac=1).reset_index(drop=True)

    # generate labels
    train_labels = train_dataset["Type"]
    train_dataset.drop(columns=["Type"], inplace=True)
    test_labels = test_dataset["Type"]
    test_dataset.drop(columns=["Type"], inplace=True)

    # summary statistics
    LOGGER.debug("Summarizing datasets...")
    LOGGER.warning(f"Training data:\n{attack_train.describe()}")
    LOGGER.warning(f"Testing data:\n{attack_test.describe()}")

    # write modified dataset to files
    LOGGER.debug("Writing final datasets to files...")
    train_dataset.to_csv(data.PREPROCESSED_TRAIN, index=False)
    test_dataset.to_csv(data.PREPROCESSED_TEST, index=False)
    np.save(data.LABELS_TRAIN, train_labels)
    np.save(data.LABELS_TEST, test_labels)

    LOGGER.debug("Data preprocessing complete")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Data preprocessing script.")
    args = parser.parse_args()

    utils.setup_logging(debug=True)
    try:
        run()
    except KeyboardInterrupt:
        LOGGER.warning("Execution interrupted")
        exit(0)
    except Exception as exception:
        LOGGER.exception(exception)
        LOGGER.error(f"Execution failed")
        exit(1)
