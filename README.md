# Book Manager API 

## Overview

The **Book Manager API** is a simple RESTful application built with **FastAPI** that allows users to manage a collection of books. The project demonstrates client-server communication over HTTP by pairing a FastAPI backend .

Users can:

* Add new books to the collection.
* View all stored books or retrieve individual books.
* Delete books from the collection.
* Store basic information such as the book title, author, and whether it has been read.

The backend uses **Pydantic** models to validate incoming data and an in-memory Python dictionary to store records.

---

## How to Start the FastAPI Server

### 1. Install the required dependencies

```bash
pip install -r requirements.txt
```

### 2. Start the FastAPI server

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

Interactive API documentation can be accessed at:

```
http://127.0.0.1:8000/docs
```


## Optional Bonus Features Implemented

For this version of the project:

* ❌ **SQLite Database Persistence**: Not implemented. The project currently uses an in-memory dictionary.
* ❌ **Advanced Querying and Filtering**: Not implemented.
* ❌ **Rich CLI Formatting**: Not implemented.
* ✅ **API Key Authentication**: Not implemented.

The current implementation focuses on demonstrating REST API development, request validation, and HTTP communication between a FastAPI backend and a custom Python CLI client.
