from requests import get

SUCCESSFUL_STATUS_CODE = 200
CLIENT_ERROR_CODE = 404
SERVER_ERROR_CODE = 500
params = {
    "ll": "30.314494,59.938676",
    "spn": "0.016457,0.00619",
    "l": "map"
}
response = None

try:
    response = get("https://static-maps.yandex.ru/1.x/", params = params)
except response.status_code == CLIENT_ERROR_CODE:
    print("Некорректный запрос!")
except response.status_code == SERVER_ERROR_CODE:
    print("Ошибка на стороне сервера.")
except response.status_code != SUCCESSFUL_STATUS_CODE:
    print("Не удалось сохранить изображение.")
else:
    with open("my_place.png", "wb") as file:
            file.write(response.content)
    print("Изображение карты сохранено в файл my_place.png.")