# Project Description

**Reqease** is a lightweight, minimalistic library designed for performing essential HTTP operations with minimal complexity. It focuses on streamlining common HTTP tasks such as `GET` and `POST` requests, while avoiding the overhead of larger libraries.

Whether you're interacting with APIs, retrieving data from a web service, or submitting forms, Reqease offers a clean and intuitive interface that allows you to perform these tasks effortlessly. It handles HTTPS requests and responses, parses JSON content, and manages basic file handling, all with a simple and elegant design.

### Key Features:
- **Minimalistic**: Focuses on core HTTP functionality without unnecessary bloat.
- **Intuitive API**: Easy-to-use methods for common tasks like `GET` and `POST`.
- **SSL/TLS Support**: Ensures secure HTTPS connections out of the box.
- **JSON Handling**: Built-in functionality to decode and return JSON responses as Python objects.
- **File Support**: Write response data directly to files with simple method calls.

Reqease is perfect for developers who need basic HTTP operations without the complexity of larger frameworks, keeping the codebase clean and efficient.

# Installation

To install **Reqease**, use the following pip command:

```bash
pip install reqease
```

# Usage

## Simple GET Request

You can use the `get` function to fetch data from a URL over HTTPS:

### Example:

```python
import reqease

# Fetch data from a URL
url = "https://jsonplaceholder.typicode.com/posts/1"
response = reqease.get(url)

# Display the response status code
print(f"Status Code: {response.status_code}")

# Display the response body as a string
print(f"Body: {response.body_str}")
```

## Save URL Content to a File

The `to_file` function fetches data from a given URL and saves the content to a specified file.

### Example:

```python
import reqease

# Define the URL and the file path
url = "https://jsonplaceholder.typicode.com/posts/1"
file_path = "output.txt"

# Save the content of the URL to a file
reqease.to_file(url, file_path)

print(f"Content saved to {file_path}")
```

## Fetch JSON Data from a URL

The `to_json` function retrieves JSON data from a specified URL and returns it as a Python object (dictionary or list).

### Example:

```python
import reqease

# Define the URL containing JSON data
url = "https://jsonplaceholder.typicode.com/posts"

# Fetch and parse the JSON data from the URL
data = reqease.to_json(url)

# Display the fetched JSON data
print(data)

# Access specific fields in the JSON object (if applicable)
for post in data:
    print(f"Post ID: {post['id']}, Title: {post['title']}")
```

# Dependencies

**Reqease** has a minimal dependency footprint, making it a clean and lean library. The only external dependency required for this project is:

- **`certifi`**: This library provides a curated collection of root certificates for validating the trustworthiness of SSL/TLS certificates. It ensures that HTTPS requests made by the library are secure and reliable.

By using only standard libraries of Python, alongside `certifi`, Reqease maintains a lightweight design that focuses on simplicity and efficiency in performing HTTP operations.
