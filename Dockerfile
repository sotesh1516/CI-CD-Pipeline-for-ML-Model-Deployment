#provides a lightweight version of linux with python already installed
FROM python:3.9-slim

#a folder that will be used inside the VM once an image is built
WORKDIR /app

#copy dependency list into the container
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

#Copy the rest of your app code
COPY . .

#port the application inside the container is listening on
EXPOSE 5000

#command to run the app
CMD ["python", "app"]