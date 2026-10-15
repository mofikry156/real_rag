from fastapi import FastAPI,APIRouter
import os
base_router=APIRouter()
@base_router.get("/")
def welcome():
    return {
        "version": os.getenv("app_version"),
        "message": "Welcome to the FastAPI application!"
        }
