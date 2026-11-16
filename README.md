## запуск приложения

```
./venv/scripts/flask --app ./acme/server.py run
```


## cURL тестирование

### добавление нового события
```
curl http://127.0.0.1:5000/api/v1/calendar/ -X POST -d "2026-11-16|Встреча|Обсудить проект"
```

### получение всего списка событий
```
curl http://127.0.0.1:5000/api/v1/calendar/
```

### получение события по идентификатору / ID == 1
```
curl http://127.0.0.1:5000/api/v1/calendar/1/
```

### обновление события по идентификатору / ID == 1
```
curl http://127.0.0.1:5000/api/v1/calendar/1/ -X PUT -d "2026-11-17|Встреча|Новый текст"
```

### удаление события по идентификатору / ID == 1
```
curl http://127.0.0.1:5000/api/v1/calendar/1/ -X DELETE
```


## пример исполнения команд с выводом

```
$ curl http://127.0.0.1:5000/api/v1/calendar/ -X POST -d "2026-11-16|Встреча|Обсудить проект"
new id: 1

$ curl http://127.0.0.1:5000/api/v1/calendar/
1|2026-11-16|Встреча|Обсудить проект

$ curl http://127.0.0.1:5000/api/v1/calendar/1/
1|2026-11-16|Встреча|Обсудить проект

$ curl http://127.0.0.1:5000/api/v1/calendar/1/ -X PUT -d "2026-11-17|Встреча|Новый текст"
updated

$ curl http://127.0.0.1:5000/api/v1/calendar/1/
1|2026-11-17|Встреча|Новый текст

$ curl http://127.0.0.1:5000/api/v1/calendar/ -X POST -d "2026-11-17|Другое|Текст"
failed to CREATE with: event already exists for date: 2026-11-17

$ curl http://127.0.0.1:5000/api/v1/calendar/1/ -X PUT -d "2026-11-17|Встреча|loooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong text"
failed to UPDATE with: text lenght > MAX: 200

$ curl http://127.0.0.1:5000/api/v1/calendar/1/ -X PUT -d "2026-11-17|loooooooooooooooooooooooooooooong title|text"
failed to UPDATE with: title lenght > MAX: 30

$ curl http://127.0.0.1:5000/api/v1/calendar/1/ -X DELETE
deleted

$ curl http://127.0.0.1:5000/api/v1/calendar/
-- пусто --
```
