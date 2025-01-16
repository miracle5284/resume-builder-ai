from fastapi import FastAPI
from . import routes

# Initialize the FastAPI application
app = FastAPI()

# Include API routes
app.include_router(routes.router)