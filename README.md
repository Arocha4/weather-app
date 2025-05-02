# weather-app


#Before running the app, ensure the following are installed on your machine:

Python 3.10+

pip (Python package installer)

Virtualenv (optional, but recommended)


if not using a virtual env
pip install -r requrements.txt


To start the Streamlit app locally, use:
streamlit run main.py



#Docker:

prerequisit Docker installed 

Bulid the Docker image using the docker file
docker build -t weather-app .

Run the Docker container:
docker run -p 8501:8501 weather-app


clean up 
docker stop weather-app
docker rm weather-app
docker rmi weather-app
