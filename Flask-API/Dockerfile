FROM python:3.12.5-slim

WORKDIR /usr/src/app

COPY docker-req.note requirements.txt
# COPY requirements.txt ./

# RUN python -m pip install --upgrade pip
# RUN pip install --upgrade tensorflow-intel
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
# CMD [“python”, “./app.py”]
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]

# FROM python:3.7.3-stretch
# RUN mkdir /app
# WORKDIR /app
# COPY . .
# RUN python -m pip install --upgrade pip
# RUN pip install -r requirements.txt
# CMD [ "python", "./app.py" ]

# # Base image, you can change it as you want
# FROM python:3.10-slim-buster

# # Install necessary system dependencies
# RUN apt-get update \
#     && apt-get install -y --no-install-recommends \
#         build-essential \
#         libblas3 \
#         liblapack3 \
#         libopenblas-dev \
#         liblapack-dev \
#         libatlas-base-dev \
#         gfortran \
#     && rm -rf /var/lib/apt/lists/*

# # Install Python dependencies
# COPY requirements.txt /app/requirements.txt
# WORKDIR /app
# RUN pip install --no-cache-dir --upgrade pip \
#     && pip install --no-cache-dir -r requirements.txt \
#     && rm -rf /root/.cache/pip