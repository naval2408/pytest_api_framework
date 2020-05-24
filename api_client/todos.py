from .base_url import BaseUrl

"""
Defining the get all and
get by id method for todos API.
"""


class ToDos(BaseUrl):
    _todo_path = '/todos'

    def get_todos(self):
        # Get all To Dos

        return self._connection.do_get(
            path=self._todo_path
        )

    def get_todos_by_id(self, todo_id):
        # Get a to do by id

        return self._connection.do_get(
            path=f'{self._todo_path}/{todo_id}'
        )







