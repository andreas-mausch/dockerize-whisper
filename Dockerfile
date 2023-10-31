FROM python:3.11.6

# Create non-root user
RUN useradd -ms /bin/bash python
USER python
WORKDIR /home/python
SHELL ["/bin/bash", "-c"]

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY download_model.py .
RUN python ./download_model.py

COPY main.py .

ENTRYPOINT ["python", "./main.py"]
