import requests
import json
from datetime import datetime
import sys

def get_discord_user_info(user_id):
    # API endpoint
    url = f"https://japi.rest/discord/v1/user/{user_id}"
    
    try:
        # Make the API request
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        # Parse the JSON response
        data = response.json()
        user_data = data.get('data', {})
        
        # Extract relevant information
        display_name = user_data.get('global_name', user_data.get('username', 'N/A'))
        username = user_data.get('username', 'N/A')
        discriminator = user_data.get('discriminator', '0')
        created_at = user_data.get('createdAt', '')
        
        # Format the creation date if available
        if created_at:
            created_date = datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%S.%fZ")
            formatted_date = created_date.strftime("%Y-%m-%d %H:%M:%S")
        else:
            formatted_date = "N/A"
        
        # Print the information in the requested format
        print(f"Nome de exibição: {display_name}")
        print(f"Nome de usuário: {username}#{discriminator}")
        print(f"Data de criação: {formatted_date}")
        print("\n==============")
        print("Sucesso √")
        print("==============")
        
    except requests.exceptions.RequestException as e:
        print(f"Erro ao fazer a requisição: {e}")
        print("\n==============")
        print("Falhou ×")
        print("==============")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python script.py <user_id>")
        sys.exit(1)
    
    user_id = sys.argv[1]
    get_discord_user_info(user_id)
