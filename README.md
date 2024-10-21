# Blog API

## Overview

The Blog API is a RESTful web service built using Django and Django Rest Framework. It allows users to create, read, update, and delete blog posts. The API provides filtering options to search for posts based on title and content, and it includes permission checks to ensure that users can only modify their own posts.

## Features

- **User Authentication**: Each blog post is associated with a user, ensuring that only the creator can modify it.
- **Create, Read, Update, Delete (CRUD)**: Full functionality for managing blog posts.
- **Filtering**: Filter blog posts by title, content, and creation date using Django Filters.
- **Permissions**: Role-based access control, allowing users to view all posts but only edit their own.

## Technologies Used

- Django
- Django Rest Framework
- Django Filter
- Python 3.x
- SQLite (or any other database of your choice)
- Django Admin for managing models

## Installation

### Prerequisites

- Python 3.x installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).
- pip (Python package installer).

### Clone the Repository

1. **Clone the repository**:
   ```bash
   git clone https://github.com/anageguchadze/Blog
