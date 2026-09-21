import json 

def save_claim(claim):

    with open("claims.json", "a") as file:
        json.dump(claim, file, indent=4)



def get_all_claims():
    with open("claims.json", "r") as file:
        claims = file.read()
    return claims
