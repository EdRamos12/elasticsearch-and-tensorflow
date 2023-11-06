# TensorFlow with ElasticSearch DataFrames

1. Clone this repository
```bash
# Clone this repository
$ git clone -b master https://github.com/EdRamos12/elasticsearch-and-tensorflow

# Go into the repository
$ cd elasticsearch-and-tensorflow
```
2. Set up the .env file with the `ELASTIC_PASSWORD` and `KIBANA_PASSWORD`
```dotenv
# Password for the 'elastic' user (at least 6 characters)
ELASTIC_PASSWORD=

# Password for the 'kibana_system' user (at least 6 characters)
KIBANA_PASSWORD=
```
3. Run docker compose
```bash
# Run docker compose
$ docker compose up -d
```
4. After finishing initial configuration of the Kibana server, log in to the server through `http://localhost:5601`
- Username: elastic
- Password is the one you configured on `.env`
5. Once logged in to Kibana, load the `heart.csv` dataset into ElasticSearch, and put `heart-rates` as index names
6. Install all the packages required
```bash
# Run the script
$ pip install -r ./requirements.txt
```
7. Run the script
```bash
# Run the script
$ python ./main.py
```