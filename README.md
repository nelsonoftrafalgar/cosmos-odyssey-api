## Start backend

1. Create Python virtual environment
2. #### `$ pip install -r requirements.txt`
3. Setup Postgres locally or in a Docker container
   #### `USER: postgres`
   #### `PASSWORD: postgres`
   #### `HOST: localhost`
   #### `DATABASE: postgres`
4. #### `$ export FLASK_ENV=development`
5. #### `$ export API_URL=https://cosmos-odyssey.azurewebsites.net/api/v1.0/TravelPrices`
6. #### `$ python app.py`
