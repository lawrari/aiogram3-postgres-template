# Setting up
1. Rename .env.dist to .env
2. Fill in the .env file with your credentials
3. **If you want to use docker**
   1. `docker-compose up -d`
4. **Without docker**
   1. Create a virtual environment: `python3 -m venv venv`
   2. Activate the virtual environment: `source venv/bin/activate`
   3. Install the requirements: `pip install -r requirements.txt`
   4. Start your bot: `python3 -m bot`
# Using Alembic
1. From source folder, run `scripts/alembic.ps1`
2. Enter your database credentials