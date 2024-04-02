# Bluetooth Attack Detector

Machine learning model designed to detect and analyze Bluetooth attacks.

## Prerequisites

- Python 3.12
- Git

## Development Environment Setup

For Linux or macOS, follow the steps below:

```sh
git clone https://github.com/mohdfareed/bt-attacks-detector.git
cd bt-attacks-detector
./setup.sh
```

For Windows, follow the steps below with PowerShell as an administrator:

```ps1
git clone https://github.com/mohdfareed/bt-attacks-detector.git
Set-Location -Path .\bt-attacks-detector
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
.\setup.ps1
```

## Usage

Download the [dataset](https://www.unb.ca/cic/datasets/iomt-dataset-2024.html)
and place the Bluetooth DDoS and DoS attack/benign dataset in the `data`
directory. Processed data and models will be saved in the `data` and `models`
directories. Logs will be saved to the root of the project. The following is
the expected directory structure of un-managed files:


```txt
project_root/
├── data/
│   ├── attack_test.csv
│   ├── attack_train.csv
│   ├── benign_test.csv
│   └── benign_train.csv
├── models/
└── dev.log
```

Run the following command to see the usage information:

```sh
./main.py --help
```

Admin privileges are required to run the demonstration script. Run the
following commands to run the demonstration script on Linux/macOS:

```sh
sudo ./main.py --demo [--verbose]
```

On Windows, run the following commands with PowerShell as an administrator:

```ps1
.\main.py --demo [--verbose]
```
