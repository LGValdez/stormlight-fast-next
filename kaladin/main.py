import uvicorn
from fastapi import FastAPI
from kaladin.routes import customer, product, side_dish

app = FastAPI()
app.include_router(customer.router)
app.include_router(product.router)
app.include_router(side_dish.router)


if __name__ == "__main__":

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
