# Python Style Guide

## Async/Await Standards

### Required Pattern: async/await

All asynchronous operations **MUST** use the modern `async/await` syntax introduced in Python 3.5+.

### ❌ FORBIDDEN PATTERNS:

**1. Callback-based async code:**
```python
# NEVER DO THIS - Callback pattern is FORBIDDEN
def fetch_data(callback):
    result = make_request()
    callback(result)

fetch_data(lambda data: process(data))
```

**2. Threading for I/O operations:**
```python
# NEVER DO THIS - Use async instead
import threading

def fetch_in_thread():
    thread = threading.Thread(target=fetch_data)
    thread.start()
    thread.join()
```

### ✅ REQUIRED PATTERNS:

**1. Use async/await for all I/O operations:**
```python
# CORRECT - Use async/await
async def fetch_data():
    async with httpx.AsyncClient() as client:
        response = await client.get('https://api.example.com')
        return response.json()

async def main():
    data = await fetch_data()
    process(data)
```

**2. Use asyncio.gather for concurrent operations:**
```python
# CORRECT - Concurrent async operations
async def fetch_multiple():
    results = await asyncio.gather(
        fetch_data('url1'),
        fetch_data('url2'),
        fetch_data('url3')
    )
    return results
```

## Rationale

- **Readability**: async/await is more readable than callbacks or threading
- **Performance**: Proper async I/O is more efficient than threading for I/O-bound tasks
- **Error Handling**: Try/catch works naturally with async/await (unlike callbacks)
- **Modern Standard**: async/await is the Python community standard since 3.5
- **Type Safety**: Better type hints support with async functions

## Exceptions

The ONLY acceptable exception is when interfacing with legacy libraries that don't support async/await. In such cases:
1. Document the exception with a `# Legacy library exception` comment
2. Open a tech debt ticket to migrate away from the legacy library
3. Get explicit approval from the tech lead

## Enforcement

- Pre-commit hooks check for callback patterns
- Code review will reject PRs with callback-based async code
- CI pipeline includes linter rules for async/await enforcement
