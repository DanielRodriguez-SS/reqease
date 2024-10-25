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

### Example 1: Using get Without Headers:

This example sends a basic GET request without any headers.

```python
import reqease

# Define the URL
url = "https://jsonplaceholder.typicode.com/posts/1"

# Send the request and capture the response
response = reqease.get(url)

# Access and print details from the response
print("Status Code:", response.status_code)
print("Response Headers:", response.headers)
print("Body (as string):", response.body_str)
```

### Example 2: Using get With Custom Headers:

In this example, we specify custom headers for the GET request, including a `Authorization` and `Accept` header.

```python
import reqease
# Define the URL and custom headers
url = "https://jsonplaceholder.typicode.com/posts/1"
headers = {
    "Authorization": "Bearer your_access_token",
    "Accept": "application/json"
}

# Send the request and capture the response
response = reqease.get(url, headers)

# Access and print details from the response
print("Status Code:", response.status_code)
print("Response Headers:", response.headers)
print("Body (as string):", response.body_str)
```

## Save URL Content to a File

The `to_file` function fetches content from a specified URL and saves it to a file. If the file path ends with .json, the content is saved as a formatted JSON file; otherwise, it’s saved as plain text.

### Example 1: Saving Content as a JSON File

```python
import reqease

# Define the URL and the file path
url = "https://jsonplaceholder.typicode.com/posts/1"
file_path = "output.json"

# This will save the content from the URL to 'output.json' in JSON format.
reqease.to_file(url, file_path)

print(f"Content saved to {file_path}")
```

### Example 2: Saving Content as Plain Text

```python
import reqease

# Define the URL and the file path
url = "https://jsonplaceholder.typicode.com/posts/1"
file_path = "output.txt"

# This will save the content from the URL to 'output.json' in JSON format.
reqease.to_file(url, file_path)

print(f"Content saved to {file_path}")
```

### Example 3: Adding Custom Headers

```python
import reqease

# Define the URL, the file path and headers
url = "https://jsonplaceholder.typicode.com/posts/1"
file_path = "output.json"
headers = {
    "Authorization": "Bearer your_access_token",
    "Accept": "application/json"
}

# This will save the content from the URL to 'output.json' in JSON format.
reqease.to_file(url, file_path, headers)

print(f"Content saved to {file_path}")
```

## Fetch JSON Data from a URL

The `to_dict` function sends an HTTPS GET request to the specified URL, parses the response as JSON, and returns the data as a Python dictionary. This is useful when you expect the response to be in JSON format and want to work with it programmatically in Python.

### Example 1: Fetching JSON from a URL

```python
import reqease

# Define the URL containing JSON data
url = "https://jsonplaceholder.typicode.com/posts"

# This sends a GET request and returns the JSON data as a Python dictionary.
data = reqease.to_dict(url)
print(data)

# Access specific fields in the JSON object (if applicable)
for post in data:
    print(f"Post ID: {post['id']}, Title: {post['title']}")
```

### Example 2: Adding Custom Headers

```python
import reqease

# Define the URL containing JSON data
url = "https://jsonplaceholder.typicode.com/posts"
headers = {
    "Authorization": "Bearer your_access_token",
    "Accept": "application/json"
}

# This sends a GET request and returns the JSON data as a Python dictionary.
data = reqease.to_dict(url, headers)
print(data)

# Access specific fields in the JSON object (if applicable)
for post in data:
    print(f"Post ID: {post['id']}, Title: {post['title']}")
```

# Dependencies

**Reqease** has a minimal dependency footprint, making it a clean and lean library. The only external dependency required for this project is:

- **`certifi`**: This library provides a curated collection of root certificates for validating the trustworthiness of SSL/TLS certificates. It ensures that HTTPS requests made by the library are secure and reliable.

By using only standard libraries of Python, alongside `certifi`, Reqease maintains a lightweight design that focuses on simplicity and efficiency in performing HTTP operations.