# Object_detection-End-to-End-project

## Project Overview
This project focuses on building an end-to-end object detection pipeline using YOLOv5 for detecting objects in images or video streams. The dataset used consists of images related to [insert specific use case, e.g., sign language detection]. The project aims to demonstrate the integration of data processing, model training, and deployment.




## Installation Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/shaheennabi/Object_detection-End-to-End-project.git
   cd Object_detection-End-to-End-project
   ```


* Create a new conda environment and activate it:

```bash
conda create -n signLanguage python=3.8 -y

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
   python src/train.py --config config/train_config.yaml

   ```

To use the trained model for inference on new images, run:
```bash
python src/inference.py --input_image_path data/test_image.jpg --model_path models/trained_model.pth
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

