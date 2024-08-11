from fastapi import FastAPI, HTTPException
from sqlmodel import select

from app.model.user_model import UserModel, User, UserUpdateModel
from app.db.db_connector import DB_SESSION, create_db_and_tables

### ================================================================== ###

app = FastAPI(lifespan= create_db_and_tables)

@app.get('/')
def root_route():
    return 'hello api'

### ================================================================== ###

def get_users_from_db(session:DB_SESSION):   ## define function to retive data
    user_data = session.exec(select(User)).all()
    if not user_data:
        raise HTTPException(status_code=404, detail=f'Not Found')
    return user_data  

@app.get('/api/get_users_data' )  
def get_users_data(session:DB_SESSION):
    user_list = get_users_from_db(session)  ## call function
    if not user_list:
        raise HTTPException(status_code=404, detail=f'Not Found')
    return user_list

### ================================================================== ###

def add_user_in_db(form_data: UserModel, session: DB_SESSION ):  ## define function
    user = User(**form_data.model_dump())
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

@app.post('/api/add-user', response_model=User)
def add_user(new_user: UserModel, session: DB_SESSION ):
    created_user = add_user_in_db(new_user, session)    ## call function
    if not created_user:
        raise HTTPException(status_code=404, detail=f"Can't Add User")
    return created_user

### ================================================================== ###

def update_user_from_db(select_id:int, form_data: UserUpdateModel, session: DB_SESSION):
    user_query = select(User).where(User.user_id == select_id)
    user_statement = session.exec(user_query).first()

    if not user_statement:
        raise HTTPException(status_code=404, detail='Not Found')
    
    ## update user 
    ## db                    =  form_data
    user_statement.user_name = form_data.user_name
    user_statement.address = form_data.address
    user_statement.phone_number = form_data.phone_number
    user_statement.user_password = form_data.user_password

    session.add(user_statement)
    session.commit()
    session.refresh(user_statement)

    return user_statement

## create update route
@app.put('/api/update_user')
def update_user(id:int, user_detail: UserUpdateModel, session: DB_SESSION):
    # call update function
    updated_user = update_user_from_db(id,user_detail, session)
    if not update_user:
        raise HTTPException(status_code=404, detail='Not Found')
    return update_user

### ================================================================== ###














    
    