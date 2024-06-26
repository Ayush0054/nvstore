FROM python:latest

# Set the working directory

WORKDIR  /VectorStore

COPY  . /VectorStore 

# Install dependencies
RUN pip install --upgrade pip && \
    pip install -r /VectorStore/requirements.txt


CMD ["python", "main.py"]   