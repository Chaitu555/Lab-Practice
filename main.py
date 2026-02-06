from fastapi import FastAPI
app=FastAPI()
@app.get('/')
def r(): return {'Hello':'Docker'}

from fastapi import FastAPI
app=FastAPI()
@app.get('/')
def r(): return {'Hello':'Git'}

print("Hello: World")
age=()
