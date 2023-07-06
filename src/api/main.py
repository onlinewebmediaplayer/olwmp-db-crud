import uvicorn

from pathlib import Path
from fastapi import FastAPI
from mangum import Mangum

from database.db import create_tables
from routes.song import routes_song, routes_prefix

from os import environ
from sys import argv
from random import randint


env_file_path=".env"

if len(argv)>1 :
    port=argv[1]
else:
    port=environ.get('PORT', randint(1000,8000))

debug=environ.get('DEBUG', True)


app = FastAPI()
handler = Mangum(app)

app.include_router(routes_song, prefix=routes_prefix)

create_tables()

if __name__ == "__main__":
    
    uvicorn.run(    
        f"{Path(__file__).stem}:app", 
        host="0.0.0.0", 
        port=port, 
        env_file=env_file_path
    )
    