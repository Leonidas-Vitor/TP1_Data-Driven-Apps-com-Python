from fastapi import FastAPI
from routers.tp1_a import router as tp1_a_router
from routers.tp1_b import router as tp1_b_router
from routers.tp1_c import router as tp1_c_router

api = FastAPI()
api.include_router(tp1_a_router)
api.include_router(tp1_b_router)
api.include_router(tp1_c_router)

@api.get("/")
def read_root():
    return {"message": "API do TP1"}
