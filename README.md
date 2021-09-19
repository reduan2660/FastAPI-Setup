## Setup

pip install -r requirement.txt

## Virtual Environmet

### Setting up

Windows:

```cmd
py -m venv venv
```

Linux:

```bash
python3 -m venv venv
```

### Activating

> Activate Virtual Environment

Windows:

```cmd
cd venv/Scripts
activate
```

Linux:

```bash
source venv/bin/activate
```

## Docker

> Building app for _first time_

```docker
docker-compose build
```

> Running Docker

```docker
docker-compose up
```

## Make Migrations

```docker
docker-compose run app alembic revision --autogenerate -m "New Migration"

docker-compose run app alembic upgrade head
```
