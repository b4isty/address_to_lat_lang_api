## ADDRESS TO LOCATION COORDINATES 

```
python -V
Python 3.8
FLASK REST PLUS
```

### Install pip first
```
sudo apt-get install python3-pip
```

### Create virtualenv (Python3.8)
```
python3.8 -m venv env-name
```

### Activate virtualenv using
```
source env-name/bin/activate
```
### Clone this repo
```
git clone 
```

### Install dependencies
```
pip install -r requirements.txt
```

### Setup environment variable
- create .env file and keep your Google Map API Key
- check .env_sample file to follow the variable name and format

### To run this project use this command
```
python app.py
```
### To run this project using docker
- Go to project directory 
```shell
docker-compose up --build
```

### API Endpoint
```
http://localhost:<port>/v1/getAddressDetails
```
### API Docs Endpoint
```
http://localhost:<port>/docs
```

