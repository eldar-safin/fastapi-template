#!/usr/bin/env python3
import uvicorn
from fastapi import FastAPI
from sqlalchemy import create_engine

engine = create_engine('sqlite+pysqlite:///:memory:', echo=True)

app = FastAPI()

@app.get('/')
async def index():
  return {'status': 'OK'}


if __name__ == '__main__':
  uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)
