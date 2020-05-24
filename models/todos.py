from dataclasses import dataclass

"""
This class defines the structure of 
the response for the get todo API. 
"""

@dataclass
class ToDos:
    user_id: int
    id: int
    title: str
    completed: bool

    def __init__(self, data: dict):
        self.user_id = data.get('userId')
        self.id = data.get('id')
        self.title = data.get('title')
        self.completed = data.get('completed')
