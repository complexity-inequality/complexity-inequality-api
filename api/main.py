from fastapi import FastAPI
import pandas as pd
import json

app = FastAPI()

@app.get("/")
async def root():    
    return {"Database": "CI-API"}

df_uf = pd.read_csv("data/db_uf.csv")
res_uf = df_uf.to_json()
parsed_uf = json.loads(res_uf)
@app.get("/uf")
async def get_df_uf():    
    return parsed_uf

# df_mun = pd.read_csv("data/db_mun.csv")
# res_mun = df_mun.to_json()
# parsed_mun = json.loads(res_mun)
# @app.get("/mun")
# async def get_df_mun():    
#     return parsed_mun

# df_meso = pd.read_csv("data/db_meso.csv")
# res_meso = df_meso.to_json()
# parsed_meso = json.loads(res_meso)
# @app.get("/meso")
# async def get_df_meso():    
#     return parsed_meso

# df_micro = pd.read_csv("data/db_micro.csv")
# res_micro = df_micro.to_json()
# parsed_micro = json.loads(res_micro)
# @app.get("/micro")
# async def get_df_micro():    
#     return parsed_micro

# df_rgint = pd.read_csv("data/db_rgint.csv")
# res_rgint = df_rgint.to_json()
# parsed_rgint = json.loads(res_rgint)
# @app.get("/rgint")
# async def get_df_rgint():    
#     return parsed_rgint

# df_rgime = pd.read_csv("data/db_rgime.csv")
# res_rgime = df_rgime.to_json()
# parsed_rgime = json.loads(res_rgime)
# @app.get("/rgime")
# async def get_df_rgime():    
#     return parsed_rgime

