# 
FROM python:3.9.13

# 
WORKDIR /back_end

# 
COPY ./requirements.txt /back_end/requirements.txt

# 
RUN apt-get update 
RUN apt-get install -y python3-opencv && apt-get install -y poppler-utils
RUN pip install --upgrade pip setuptools wheel cython
RUN pip install --no-cache-dir --upgrade -r /back_end/requirements.txt

# 
COPY . /back_end

# 
CMD ["uvicorn", "app:app", "--host=0.0.0.0", "--port=80", "--reload"]

EXPOSE 80/tcp