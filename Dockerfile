# Build the React app first
FROM node:16 as build

WORKDIR /app/frontend

COPY package.json package-lock.json ./
RUN npm install

COPY ./frontend /app/frontend
RUN npm run build

# Now serve the React app with Nginx
FROM nginx:alpine
COPY frontend/nginx/nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=build /app/frontend/build /usr/share/nginx/html
EXPOSE 8080

# Use an official lightweight Python image
FROM python:3.10-slim

RUN pip install poetry==1.6

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

# Set the working directory in the container
WORKDIR /app/backend

COPY ./backend/pyproject.toml ./backend/poetry.lock ./

# Copy the requirements file into the container
RUN poetry install --no-root && rm -rf $POETRY_CACHE_DIR

ENV VIRTUAL_ENV=/app/backend/.venv \
    PATH="/app/backend/.venv/bin:$PATH"

# Copy the content of the local src directory to the working directory
COPY ./backend /app/backend

EXPOSE 8000

# Specify the command to run on container start
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"] 
# CMD ["nginx", "-g", "daemon off;"]