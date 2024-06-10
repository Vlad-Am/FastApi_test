from typing import List

from fastapi import FastAPI

from src.app.validators import User, Trade

app = FastAPI(
    title="Trading App"
)

fake_users = [
    {
        'id': 1,
        'name': 'John Doe',
        "degree": [{"id": 1,
                    "created_at": "2022-01-01T00:00:00",
                    "type_degree": "expert"}]
    },
    {
        'id': 2,
        'name': 'Jane Doe',
        "degree": [{"id": 2,
                    "created_at": "2024-02-02T00:11:00",
                    "type_degree": "professor"}]
    }

]

fake_trades = [
    {"id": 1, "user_id": 1, "currency": "USD", "side": "buy", "price": 123, "amount": 2.11,
     },
    {"id": 2, "user_id": 2, "currency": "USD", "side": "buy", "price": 123, "amount": 2.11,
     }
]


@app.get('/users/{user_id}', response_model=List[User])
def get_user(user_id: int):
    return [user for user in fake_users if user['id'] == user_id]


@app.get('/trades')
def get_trades(limit: int = 1, offset: int = 0):
    return fake_trades[offset:][:limit]


@app.post('/users/{user_id}')
def change_user_name(user_id: int, new_name: str):
    current_user = list(filter(lambda user: user.get('id') == user_id, fake_users))[0]
    current_user['name'] = new_name
    return {'status': 200, 'data': current_user}


# Post запрос на добавление данных, требующих валидацию
@app.post('/trades')
def add_trades(trades: List[Trade]):
    fake_trades.extend(trades)
    return {'status': 200, 'data': fake_trades}
