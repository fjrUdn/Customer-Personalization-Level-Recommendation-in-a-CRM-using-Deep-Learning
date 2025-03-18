# Kodein AI Classification

API Service yang digunakan untuk melakukan prediksi apakah client memiliki kemungkinan besar melakukan deals atau tidak

## Tech Stack

**Server:** Flask and Waitress

**Model:** Tensorflow, Sastrawi, Pandas

## Run Locally

Clone the project

~~~bash
git clone https://gitlab.com/kodein3/ai.git
~~~

Go to the project directory

~~~bash
cd ai
~~~

Install dependencies

~~~bash
pip install -r requirements.txt
~~~

Start the server

~~~bash
python app.py
~~~

## API Reference

### Endpoint List

|  Endpoint           |  Method  |
|  :--------          |  :------ |
| `/`                 | `ANY`    |
| `/status`           | `ANY`    |
| `/predict`          | `POST`   |
| `/predict/time`     | `GET`    |
| `/predict/type`     | `GET`    |
| `/predict/stage`    | `GET`    |

#### Get predicted label

~~~http
  POST /predict
~~~

| Parameter | Type     | Description                                      |
| :-------- | :------- | :-------------------------                       |
| `name`    | `string` | **Required**. Deal name                          |
| `type`    | `string` | **Required**. Deal type (TASK, MEETING, etc)     |
| `note`    | `string` | **Required**. Deal note                          |
| `stage`   | `string` | **Required**. Deal stage (NEW, CALL, DEAL, etc)  |

- Usage/Example (object)

~~~bash
curl --location 'localhost:5000/predict' \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--data '{
    "name": "Deal 1",
    "type": "TASK",
    "note": "menunggu info dari atasan",
    "stage": "CALL"
}'
~~~

- Usage/Example (array)

~~~bash
curl --location 'localhost:5000/predict' \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--data '[
    {
        "name": "Deal 1",
        "type": "TASK",
        "note": "menunggu info dari atasan",
        "stage": "CALL"
    },
    {
        "name": "Deal 2",
        "type": "TASK",
        "note": "menunggu info dari atasan",
        "stage": "CALL"
    }
]'
~~~

## Notes

- Error importing libraries

Make sure you are already installed all dependencies without any error relevant.
if you meet it, then fix it, after done with it, run again

- Error importing configuration and handler

If you meet this error, make sure path for config, enums, and handler is correct.
don't change \__init__.py file, due registering folder path

- Do not use it in a production deployment

To solve this error you need to change value of APP_DEBUG,
it's located at config/app.py, set it to FALSE

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/en/3.0.x)
- [Deployment](https://flask.palletsprojects.com/en/3.0.x/deploying/uwsgi)

## Feedback

If you have any feedback, please make an issue with detail description, proof of concept, and python dependencies list
