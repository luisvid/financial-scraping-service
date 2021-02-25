# Financial data scraping service

Financial information RESTful service using Python and Flask_restful

### Prerequisites

Python 3.9.0

### Installing

## Clone the repo:

```sh
git clone https://github.com/luisvid/financial-scraping-service.git
```

## Install dependencies:

```sh
pip install -r requirements.txt
```

## some installed dependencies are:

    Flask

    Flask-RESTful API

    beautifulsoup4 

    requests

    pandas


Heroku deploy

```sh
heroku login
```

```sh
heroku create — will create an app in heroku
```

```sh
heroku git:remote -a remote-repo-name — connects to the remote repository
```

```sh
git push heroku main — pushes the changes to heroku
```

### Documentation 

Refer to:

[Pandas DataFrame is not JSON serializable](https://github.com/flask-restful/flask-restful/issues/269)
Flask-RESTful's json serialization isn't at fault here. If you return an object from a restful.Resource method, Flask-RESTful will call json.dumps on it. In this case, you're using a custom class that defines it's own serialization method: to_json(). To bypass Flask-RESTful's json.dumps attempt create a raw Response object.