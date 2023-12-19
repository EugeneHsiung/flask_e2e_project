# flask_e2e_project

## Summary
This repository is the final project submission for HHA 504. Within this repo, you can discover a web service designed to provide users with a sample dataset on Pregnancy Associated Mortality. The [dataset](https://github.com/EugeneHsiung/flask_e2e_project/blob/main/data/Clean-Pregnancy-Associated_Mortality.csv), as well as the Python script employed for [data cleaning](https://github.com/EugeneHsiung/flask_e2e_project/blob/main/data/clean.py), are available for reference. For more information on the dataset visit this [link](https://catalog.data.gov/dataset/pregnancy-associated-mortality)

## Note
Final Screenshots of what the web application service, Oauth, Dockerfile, Sentry, API example, Azure, MySQL database can be found in `docs` [folder](https://github.com/EugeneHsiung/flask_e2e_project/tree/main/docs) 

## Technologies Utilized
- Github (Version Control): Connected Google shell environment with Github
- Flask (Python; Frontend & Backend): Created an app to display data
- MySQL (Database via GCP or Azure): Data storage on MySQL Workbench
- SQLAlchemy (ORM): Product that uses a ORM
- .ENV (Environment Variables): tore all credentials
- Tailwind (Frontend Styling): Used tailwind for styling
- Authorization (Google OAuth): Used Authorization
- API Service (Flask Backend): Created routes that lead to JSON output
- Logger and or Sentry.io (Debugging & Logging): Used Sentry.io for performance monitoring
- Docker (Containerization): A product that is containerized
- GCP or Azure (Deployment): Used Azure to deploy web app service

## Running the Web Service
To run the code on a **local environment**, they will have to clone this repository along with its contents in the `app.py` [folder](https://github.com/EugeneHsiung/flask_e2e_project/tree/main/app). The individual will then have to `cd` into the directory and `cd` into the app then run the application with `python app.py`.

To run the code on a local environment with **Docker**, they will have to create a `Dockerfile` which includes these [contents](https://github.com/EugeneHsiung/flask_e2e_project/blob/main/app/Dockerfile) and a `requirements.txt` which includes these [contents](https://github.com/EugeneHsiung/flask_e2e_project/blob/main/app/requirements.txt). 
1. Create the Docker image with: `docker build -t <name> .`
2. Type: `docker images` to show the list of images
3. Type: `docker run -d -p 5000:5000 <name>` to run the image.
Final DockerFile:
<img width="1393" alt="Docker Success" src="https://github.com/EugeneHsiung/flask_e2e_project/assets/141866888/f2a73f43-39f4-4006-a1a3-c69a0f049787">

To run the code on **cloud** using **Azure**, they will need to: 
1. Install Azure CLI with `curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash`.
2. Type: `az` and `az login --use-device-code`. click on the link and paste the code that was given. This connects Azure with Google shell
3. Type: `az account list --output table` and select the correct subscription. If not type: `account set --subscription <paste the desired SubscriptionId here>` 
4. Type: `az group list`
5. Type: `az webapp up --resource-group <resource group that you named> --name <replace with what you would like to name the webapp> --runtime PYTHON:3.9 --sku B1`. This will start to create the web app.
6. Go to `App Service` in Azure and click on the link in `Default domain` for the link.
Final Deployment on Shell:
<img width="814" alt="Shell Azure Deployment" src="https://github.com/EugeneHsiung/flask_e2e_project/assets/141866888/f9ff28df-26a0-4900-a582-769d52f85ba7">

## .env File Template
<img width="710" alt="env" src="https://github.com/EugeneHsiung/flask_e2e_project/assets/141866888/e003dd71-6b17-4d11-8bcf-683e430bc4a5">








