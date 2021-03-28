# FastAPI Trains

A basic FastAPI backend projects to get my hand dirty on it.

## Getting Started

TODO

### Prerequisites

You'll need `python@3.8`, `pipenv` and `postgresql@13` installed on your system to run the project.

### Installing

Run the following command to install all the project dependencies.
```shell script
pipenv install
```
Make sure your local PostgreSQL server is running on `http://localhost:5432`. Then, create a new database called `fastapi_db`.
```shell script
psql postgres
postgres=create database fastapi_trains;
```
**Note:** If you have a different database URL, set it in the `.env` environment file.

Now, run the `prestart.sh` script that'll create the tables and add initial data.
```shell script
sh prestart.sh
```r
If there are any changes to the `SQLALCHEMY_DATABASE_URI` key in the `.env` file, please run the `prestart.sh` script again.

### Running

After all the above mentioned steps, you can start the application using the following command:
```shell script
python -m app.main
```
The application will be available at https://localhost:8000.

## Development

TODO

### Migrations

If there are any changes to the SQLAlchemy ORM models, you can run the following command to generate `alembic` migrations.
```shell script
alembic revision --autogenerate -m "<migration message>"
```
This command will generate a new migration file in the `migrations` directory. Remember to check the generated migration file before committing.

## Testing

The application unit tests are inside the `app/tests` module.

Run the following command in the terminal to execute the application unit tests.
```shell script
pytest app/tests
```

## Deployment

The application can be deployed in production using `gunicorn`, you don't need to make any code changes for the same.
Head over to the [Uvicorn Deployment](https://www.uvicorn.org/deployment/) documentation for complete instructions.

## Built With

* [FastAPI](https://fastapi.tiangolo.com/) - The API framework used
* [SQLAlchemy](https://www.sqlalchemy.org/) - Database ORM
* [Pipenv](https://pypi.org/project/pipenv/) - Dependency and virtual environment manager

## Authors

* **Ronak Dhoot** - *Initial work* - [dhoot](https://github.com/dhoot)

## License

TODO
