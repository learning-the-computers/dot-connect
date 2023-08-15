We are committed to providing a safe and welcoming environment for all members.

We expect all members to adhere to our Code of Conduct, which includes the following principles:

- Be respectful and considerate of others.
- Be open to constructive criticism and feedback.
- Contribute positively to the community.

# Testing
Various components of this solution require testing, although each component may
not apply to every user. Here are ways to use Docker to run these backends.

Add the following .env file and provide values for compatibility with most backends. These
align with the specific in the run commands below.
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=my-secret-pw
POSTGRES_HOST=localhost
POSTGRES_USER=postgres
POSTGRES_PASSWORD=mysecretpassword

## Postgres
```
docker run --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -p 5432:5432 -d postgres
```

## MySQL
```
docker run --name some-mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw -p 3306:3306 -d mysql
```
