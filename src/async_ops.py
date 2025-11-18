"""
Data fetching module with asynchronous operations.
"""
import time
import requests
from typing import Callable, List, Dict, Any

# VIOLATION: Using callback pattern instead of async/await

def fetch_user_data(user_id: int, callback: Callable[[Dict[str, Any]], None]) -> None:
    """
    Fetch user data from API using callback pattern.
    
    VIOLATION: This should use async/await instead of callbacks.
    See /docs/style-guide.md for required patterns.
    """
    def _fetch():
        # Simulate API call
        time.sleep(0.5)
        user_data = {
            'user_id': user_id,
            'name': f'User {user_id}',
            'email': f'user{user_id}@example.com'
        }
        callback(user_data)
    
    # Execute fetch in callback style
    _fetch()

def fetch_multiple_users(user_ids: List[int], on_complete: Callable[[List[Dict]], None]) -> None:
    """
    Fetch multiple users using nested callbacks.
    
    VIOLATION: Callback hell - should use asyncio.gather with async/await.
    """
    results = []
    
    def process_user(index: int):
        if index >= len(user_ids):
            on_complete(results)
            return
        
        def user_callback(user_data):
            results.append(user_data)
            process_user(index + 1)
        
        fetch_user_data(user_ids[index], user_callback)
    
    process_user(0)

def fetch_with_processing(user_id: int, 
                          success_callback: Callable[[Dict], None],
                          error_callback: Callable[[Exception], None]) -> None:
    """
    Fetch data with error handling using callbacks.
    
    VIOLATION: Error handling should use try/except with async/await.
    """
    try:
        def data_callback(data):
            # Process data
            processed = {**data, 'processed': True}
            success_callback(processed)
        
        fetch_user_data(user_id, data_callback)
    except Exception as e:
        error_callback(e)

# Example usage showing callback hell
def example_usage():
    """Demonstrates the problematic callback pattern."""
    def on_user_fetched(user):
        print(f"Got user: {user['name']}")
        
        def on_posts_fetched(posts):
            print(f"Got {len(posts)} posts")
            
            def on_comments_fetched(comments):
                print(f"Got {len(comments)} comments")
            
            # Nested callbacks (callback hell)
            fetch_comments(posts[0]['id'], on_comments_fetched)
        
        fetch_posts(user['user_id'], on_posts_fetched)
    
    fetch_user_data(1, on_user_fetched)

def fetch_posts(user_id: int, callback: Callable) -> None:
    """Simulate fetching posts."""
    posts = [{'id': 1, 'title': 'Post 1'}]
    callback(posts)

def fetch_comments(post_id: int, callback: Callable) -> None:
    """Simulate fetching comments."""
    comments = [{'id': 1, 'text': 'Comment 1'}]
    callback(comments)

if __name__ == '__main__':
    example_usage()
