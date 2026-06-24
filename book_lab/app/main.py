from fastapi import FastAPI , HTTPException , status
from typing import List

from app.database import BOOK_DATASTORE
from app.schemas import BookCreate , BookResponse , BookUpdate

from fastapi import FastAPI, HTTPException, Security, status
from fastapi.security.api_key import APIKeyHeader

API_KEY = 'mysecretkey'
API_KEY_NAME = 'Access_key'

api_key_header = APIKeyHeader(name = API_KEY_NAME, auto_error = False)
def verify_api_key(api_key :str = Security(api_key_header)) :
    if api_key != API_KEY :
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED , detail = 'Invalid API Key')
    return api_key




app = FastAPI(title = 'Book Management API' , version = '1.0.0')
@app.get('/books', response_model = List[BookResponse],status_code = status.HTTP_200_OK)
def get_books(api_key : str = Security(verify_api_key)):
    return list(BOOK_DATASTORE.values())


@app.get('/books/{book_id}' , response_model = BookResponse)
def read_single_book(book_id : int , api_key : str = Security(verify_api_key)) :
    book = BOOK_DATASTORE.get(book_id)
    if not book :
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND , detail = 'Book not found')
    return book 


@app.post('/books' , response_model = BookResponse , status_code = status.HTTP_201_CREATED) 
def create_book(payload : BookCreate , api_key : str = Security(verify_api_key)) :
    new_id = max(BOOK_DATASTORE.keys(),default = 0) +1
    new_book = {
        
        'id' : new_id ,
        'title' : payload.title ,
        'author' : payload.author ,
        'is_read' : False
    }
    BOOK_DATASTORE[new_id] = new_book
    return new_book

@app.put('/book/{book_id}' , response_model = BookResponse)
def update_book(book_id : int , payload : BookUpdate , api_key : str = Security(verify_api_key)) :
    book = BOOK_DATASTORE.get(book_id)
    if not book :
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND , detail = 'Book not found')
    
    updated_book = book.copy()
    if payload.title is not None :
        updated_book['title'] = payload.title
    if payload.author is not None :
        updated_book['author'] = payload.author
    if payload.is_read is not None :
        updated_book['is_read'] = payload.is_read
    
    BOOK_DATASTORE[book_id] = updated_book
    return updated_book

@app.delete('/book/{book_id}' , status_code = status.HTTP_204_NO_CONTENT)
def delete_book(book_id : int , api_key : str = Security(verify_api_key)) :
    book = BOOK_DATASTORE.get(book_id)
    if not book :
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND , detail = 'Book not found')
    del BOOK_DATASTORE[book_id]
    return None