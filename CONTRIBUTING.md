We are committed to providing a safe and welcoming environment for all members.

We expect all members to adhere to our Code of Conduct, which includes the following principles:

- Be respectful and considerate of others.
- Be open to constructive criticism and feedback.
- Contribute positively to the community.

# Testing
There are various components of this solution that require testing although each component may
not be applicable to every user. Here are ways to use Docker to run these backends.

For compatibility with most backends, add the following .env file and provide values. These
align with the specific in the run commands below.
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=my-secret-pw
POSTGRES_HOST=localhost
POSTGRES_USER=postgres
POSTGRES_PASSWORD=mysecretpassword

## Postgres
docker run --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -p 5432:5432 -d postgres

## MySQL
docker run --name some-mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw -p 3306:3306 -d mysql
