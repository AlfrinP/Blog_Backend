# Next.js Blog Backend (FastAPI + MongoDB)

This is a backend API for a blog platform built with FastAPI and MongoDB. It provides CRUD operations for blogs and authors, and is designed to be used with a Next.js frontend.

## Features

- FastAPI for RESTful API endpoints
- MongoDB for data storage
- Pydantic models for validation
- UUID-based blog IDs
- Author management
- Recent and featured blog queries

## Getting Started

### Prerequisites

- Python 3.8+
- MongoDB (local or remote)
- Git

### Clone the Repository

```sh
git clone https://github.com/AlfrinP/Blog_Backend.git
cd Blog_Backend
```

### Set Up Environment

1. Create a virtual environment:
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Copy `.env.example` to `.env` and set your MongoDB URI and DB name:
   ```sh
   cp .env.example .env
   # Edit .env with your values
   ```

### Run the Server

```sh
uvicorn src/main:app --reload
```

### API Endpoints

- `/blogs/` - List all blogs
- `/blogs/recent` - Get recent blogs
- `/blogs/featured` - Get featured blogs
- `/blogs/{blogId}` - Get, update, or delete a blog by ID
- `/authors/` - List, create, update, or delete authors

## Project Structure

```
src/
  main.py
  blog/
    blog.py
    blogDAO.py
    blogDTO.py
    blogController.py
  author/
    author.py
    authorDAO.py
    authorDTO.py
```

## License

MIT
