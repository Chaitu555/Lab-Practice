from fastapi import FastAPI
app=FastAPI()
@app.get('/')
def r(): return {'Hello':'Docker'}

from fastapi import FastAPI
app=FastAPI()
@app.get('/')
def r(): return {'Hello':'Git'}

from fastapi i port FastAPI
app=FastAPI()
@app.get('/')
def r(): return {'Hello':'K8s'}
