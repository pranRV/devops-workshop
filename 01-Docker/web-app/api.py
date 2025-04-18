import requests
from constants import DOCKER_COMPOSE

BASE_URL = "http://127.0.0.1:8000"

async def get_team_probability(team_name, position, simulation):
    url = f"{BASE_URL}/team/{team_name}?position={position}&simulations={simulation}"
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return {"error": "Failed to fetch data from the API"}

async def get_ipl_schedule():
    url = f'{BASE_URL}/schedule'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return {"error": "Failed to fetch data from the API"}

async def get_points_table():
    url = f'{BASE_URL}/points-table'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return {"error": "Failed to fetch data from the API"}