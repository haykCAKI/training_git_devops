FROM python:3.9

WORKDIR /usr/src/app

# Install dependencies first (copy requirements.txt first for caching)
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install "fastapi[standard]"  # This installs uvicorn and other required dependencies

COPY . .

EXPOSE 80
# Correct command to run the FastAPI app with uvicorn
CMD ["fastapi", "run", "main.py", "--port", "80"]