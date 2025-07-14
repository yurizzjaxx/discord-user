import sys
import requests

# Python by yurizzjaxx

def getUser(id):
    if len(id) > 0:
       if id.startswith("exit"):
          sys.exit
          print("Success exit")
       else:
          api_url = f"https://japi.rest/discord/v1/user/{id}"
          mediaAvatar = f"https://media.discordapp.net/avatars"
          mediaEmbed = f"https://cdn.discordapp.com/embed/avatars/1.png"

          # Network request
          response = requests.get(api_url)
          data = response.json()

          # Json response
          if not data.get("error"):
             user = data.get("data", {})
             if user.get("message"):
                print("\n")
                print("=" * 25)
                print(" " * 2, "Error user ID again")
                print("=" * 25)
                print("\n")
                getInput()
             else:
                # avatar
                uid = user.get("id")
                format = user.get("avatar")
                if format:
                   avatar_url = f"{mediaAvatar}/{uid}/{format}.png?size=128"
                else:
                   avatar_url = mediaEmbed

                # User name
                username = user.get("global_name")
                nameTag = user.get("tag")

                #info log
                print("\n")
                print("=" * 25)
                print(f"Display Name: {username}")
                print(f"username: {nameTag}")
                print(f"Avatar URL: {avatar_url}")
                print("=" * 25)
                print("\n")
                getInput()
          else:
             print("\n")
             print("=" * 30)
             print(" " * 4, "Error with name again")
             print("=" * 30)
             print("\n")
             getInput()
    else:
       print("\n")
       print("=" * 30)
       print(" " * 2, "failed with user ID none")
       print("=" * 30)
       print("\n")
       getInput()

def getInput():
    # command edit
    edit = input("user-id: ")
    getUser(edit)




if __name__ == "__main__":
   getInput()
