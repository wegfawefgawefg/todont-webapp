'''
todont app
list of todonts
time created, description and a checkbox of whether its done or not 
'''


from fastapi import FastAPI
app = FastAPI()


db = [
    Todont(id=0, created_ts=datetime.now(), description='Buy milk'),
    Todont(id=1, created_ts=datetime.now(), description='Buy eggs'),
    Todont(id=2, created_ts=datetime.now(), description='Buy bread')]

@app.get("/")
async def root():
    # return a list of todonts
    return {"todonts": db}

@app.post("/todonts")
async def add_todont(todont_input: TodontInput):
    # add a todont
    todont = Todont(**todont_input.dict(), 
        id=len(db), 
        created_ts=datetime.now())
    db.append(todont)
    return todont

@app.delete("/todonts/{id}")
async def remove_todont(id: int):
    # remove a todont
    if todont := next(filter(lambda t: t.id == id, db), None):
        db.remove(todont)
        return todont
    return {"message": "Todont not found"}

@app.put("/todonts/{id}")
async def set_done(id: int):
    # set the todont to done
    if todont := next(filter(lambda t: t.id == id, db), None):
        todont.done = True
        return todont
    return {"message": "Todont not found"}