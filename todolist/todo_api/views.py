from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from todo.models import Todo
from todo.serializers import TodoSerializer

# LIST:
# request: GET /api/v1/todos/
# response: 200, [{'id': 1, 'content': 'test', 'created': '20210202', 'completed': false}...]
# CREATE:
# request: POST /api/v1/todos/
# response: 202, {'id': 1, 'content': 'test', 'created': '20210202'}
# UPDATE:
# request: PUT/PATCH/api/v1/todos/1/
# response: 200, {'id': 1, 'content': 'test', 'created': '20210202', 'completed': true}
# DELETE:
# request: DELETE /api/v1/todos/1/
# response: 204


# req : todo_api/todo/
@api_view(['GET', 'POST'])
def todo(request):

    # 'GET' - list
    if request.method == 'GET':
        todos = Todo.objects.all()
        # todos_serializer = TodoSerializer(todos)
        todos_serializer = TodoSerializer(todos, many=True)
        return Response(todos_serializer.data)

    # 'POST' - create
    elif request.method == 'POST':
        todos_serializer = TodoSerializer(data=request.data)
        if todos_serializer.is_valid():
            todos_serializer.save()
            return Response(todos_serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(todos_serializer.error, status=status.HTTP_400_BAD_REQUEST)


# req : todo_api/todo/99
@api_view(['GET', 'PUT', 'DELETE'])
def todo_get_put_delete(request, pk):
    try:
        todo = Todo.objects.get(pk=pk)
    except Todo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # 'GET' - detail
    if request.method == 'GET':
        todo_serializer = TodoSerializer(todo)
        return Response(todo_serializer.data)

    # 'PUT' - update
    elif request.method == 'PUT':
        if todo.check:
            todo.check = False
        else:
            todo.check = True
        todo.save()
        todo_serializer = TodoSerializer(todo)
        return Response(todo_serializer.data)

    # 'DELETE' - delete
    elif request.method == 'DELETE':
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
