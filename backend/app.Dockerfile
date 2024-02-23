# Use an official Python runtime as an image
FROM python:latest

# The EXPOSE instruction indicates the ports on which a container 
# will listen for connections
# Since Flask apps listen to port 5000  by default, we expose it
EXPOSE 5000

# Sets the working directory for following COPY and CMD instructions
# Notice we haven’t created a directory by this name - this instruction 
# creates a directory with this name if it doesn’t exist
WORKDIR /backend

# Install any needed packages specified in requirements.txt
COPY ./backend/requirements.txt .
COPY ./backend/.flaskenv .
COPY ./backend/app.py .

RUN pip install -r requirements.txt

CMD ["flask", "run", "--host", "0.0.0.0"]
