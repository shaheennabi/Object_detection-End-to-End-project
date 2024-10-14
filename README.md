# Object_detection-End-to-End-project

## Project Overview

* Objective: Develop an object detection system using the YOLOv5s pretrained model.

* Dataset:

    Total Images: 2,086 images
    Training Images: 1,461
    Validation Images: 417
    Testing Images: 208
    Annotation Tool: Data was annotated using Roboflow for efficient labeling.
    Model Training:

* Framework: Utilized the YOLOv5s model, known for its speed and accuracy.
* Environment: Training conducted on Google Colab with GPU support.
* Epochs: The model was trained for 250 epochs, resulting in significant improvements in detection accuracy.
* Performance: The trained model demonstrated great accuracy on the validation and testing datasets.

* Additional Information: Further details, including setup instructions and usage, can be found in the project repository

### Project Tree Structure 
```bash

Object_Detection-End-to-End-project/
  ├── .github/
  │   └── workflows/
  │       └── main.yaml
  ├── .jenkins/
  │   └── Jenkinsfile
  ├── artifact/
  │   └── 10_05_2024_03_23_14 (or time Stamp)/
  │       ├── data_ingestion/
  │       │   ├── feature_store/
  │       │   │   ├── test
  │       │   │   ├── train
  │       │   │   ├── valid
  │       │   │   └── data.yaml
  │       └── SignLangData.Zip
  │       ├── data_validation/
  │       │   └── status.txt           
  │       └── model_trainer/
  │           └── best.pt
  ├── data/
  │   ├── .gitkeep
  │   └── inputImage.jpg
  ├── flowchart/
  ├── logs/
  ├── notebook/
  │   ├── Object_Detection_with_Yolov5.ipynb
  │   └── test.ipynb
  ├── scripts/
  │   ├── ec2_setup.sh
  │   └── jenkins.sh
  ├── SignLanguage or src/
  │   ├── components/
  │   │   ├── __pycache__/
  │   │   ├── __init__.py
  │   │   ├── data_ingestion.py
  │   │   ├── data_validation.py
  │   │   ├── model_pusher.py
  │   │   └── model_trainer.py
  │   ├── configuration/
  │   │   ├── __pycache__/
  │   │   ├── logs/
  │   │   ├── __init__.py
  │   │   ├── gdown_connection.py
  │   │   └── s3_operations.py
  │   ├── constants/
  │   │   ├── __pycache__/
  │   │   ├── __init__.py
  │   │   └── training_pipeline/
  │   └── entity/
  │       ├── __pycache__/
  │       ├── __init__.py
  │       ├── artifact_entity.py
  │       └── config_entity.py
  ├── templates/
  │   └── index.html
  ├── yolov5/
  ├── app.py
  ├── data_collector.py
  ├── docker_compose.yml
  ├── Dockerfile
  ├── README.md
  ├── requirements.txt
  ├── setup.py
  └── template.py

  ```
## Installation Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/shaheennabi/Object_detection-End-to-End-project.git
   cd Object_detection-End-to-End-project
   ```


* Create a new conda environment and activate it:

```bash
conda create -n signLanguage python=3.10 -y

```
```bash
conda activate signlanguage
```
* Install the required dependencies:

```bash
pip install -r requirements.txt
```


### Export the  environment variable(anaconda prompt)

```bash
set DATA_DOWNLOAD_URL=https://drive.google.com/uc?/export=download&id=  your file_id goes here"
```
### Export the  environment variable(git bash)

```bash
export DATA_DOWNLOAD_URL="https://drive.google.com/file/d/ your file_id goes here"
```



# Workflow
After creating project template
 * Update constants 
 * Update Entiry modules
 * Update respective component
 * Update pipeline
 * Endpoint - (app.py)


## Model Training

1. Ensure the dataset is properly loaded in the `data/` folder.
2. Run the training script:

   ```bash
   python  cd yolov5/ && python train.py --img 416 --batch 16 --epochs 300 --data '../data.yaml' --cfg ./models/custom_yolov5s.yaml --weights 'yolov5s.pt' --name yolov5s_results  --cache
   ```

To use the trained model for inference on new images, run:
```bash
python cd yolov5/ && python detect.py --weights /content/runs/train/yolov5s_results/weights/best.pt --img 416 --conf 0.5 --source /content/test/images
  ```




## Deployment

To deploy the application locally:
1. Install the dependencies in `requirements.txt`.
2. Run the Flask app:
   ```bash
   python app.py


### Deployment  (CI/CD)

# Run these commands on EC2 Machine

* Update package lists
```bash
sudo apt update
```

* Update package lists (alternate command)
```bash
sudo apt-get update

```

* Upgrade the system
```bash
sudo apt upgrade -y

```

* Download Docker installation script
```bash
curl -fsSL https://get.docker.com -o get-docker.sh

```

* Run the Docker installation script
```bash
sudo sh get-docker.sh

```

* Add current user to the Docker group (run both lines)
```bash
sudo usermod -aG docker $USER
sudo usermod -aG docker $USER

```


* Install AWS CLI
```bash
sudo apt install awscli -y  (if not worked- install with curl -check doc)

```


* AWS Configuration
```bash
aws configure

```


### Run these commands to install Jenkins on EC2

* Update package lists

```bash
sudo apt update
```
* Install OpenJDK 8

```bash
sudo apt install openjdk-8-jdk -y
```

```bash
# Jenkins repository (links for reference)
# https://pkg.jenkins.io/
# https://pkg.jenkins.io/debian-stable/
```
* Start Jenkins service
```bash
sudo systemctl start jenkins
```


* Enable Jenkins to start on boot
```bash
sudo systemctl enable jenkins
```

* Check the status of Jenkins service
```bash
sudo systemctl status jenkins
```

* Download Docker installation script
```bash
curl -fsSL https://get.docker.com -o get-docker.sh
```
 
* Run the Docker installation script
```bash
sudo sh get-docker.sh
```

* Add current user to Docker group
```bash
sudo usermod -aG docker $USER
```


* Add Jenkins user to Docker group
```bash
sudo usermod -aG docker jenkins
```

* Activate Docker group changes
```bash
newgrp docker
```


* Install AWS CLI
```bash
sudo apt install awscli -y
```

* Add Jenkins to Docker group again to ensure it has access
```bash
sudo usermod -a -G docker jenkins
```

* Download Docker installation script
```bash
curl -fsSL https://get.docker.com -o get-docker.sh
```


* Run the Docker installation script
```bash
sudo sh get-docker.sh
```

* Add current user to Docker group
```bash
sudo usermod -aG docker $USER
```

* Add Jenkins user to Docker group
```bash
sudo usermod -aG docker jenkins
```

* Activate Docker group changes
```bash
newgrp docker
```

* Install AWS CLI
```bash
sudo apt install awscli -y
```

* Add Jenkins to Docker group again to ensure it has access
```bash
sudo usermod -a -G docker jenkins
```

* Retrieve the initial Jenkins admin passwo
```bash
sudo cat /var/lib/jenkins/secrets/initialAdminPassword
```

