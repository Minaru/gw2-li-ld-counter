from gw2api import GuildWars2Client
import json

def retrieve_raw_li(gw2_client):
    return 0
    
def retrieve_raw_ld(gw2_client):
    return 0

def retrieve_prowess_li(gw2_client):
    return 0

def retrieve_envoy_insignia_li(gw2_client):
    return 0
    
def retrieve_refined_envoy_armor_li(gw2_client):
    return 0
    
def retrieve_perfected_envoy_armor_li(gw2_client):
    return 0
    
def retrieve_coalescence_ld(gw2_client):
    return 0
    
def retrieve_compassion_ld(gw2_client):
    return 0

# https://github.com/Maselkov/GW2Bot/blob/1dc01e938dc56ebbf0fba36d6dc83baaf5b9881e/guildwars2/account.py#L101
def retrieve_li(key):
    count = 0
    
    count += retrieve_raw_li(gw2_client)
    count += retrieve_prowess_li(gw2_client)
    count += retrieve_envoy_insignia_li(gw2_client)
    count += retrieve_refined_envoy_armor_li(gw2_client)
    count += retrieve_perfected_envoy_armor_li(gw2_client)
    
    return count
    
def retrieve_ld(key):
    count = 0

    count += retrieve_raw_ld(gw2_client)
    count += retrieve_coalescence_ld(gw2_client)
    count += retrieve_compassion_ld(gw2_client)
    
    return count

with open('config.json') as json_file:  
    data = json.load(json_file)
    
    if not 'output_file' in data:
        raise ValueError('Output file isnt properly set in json config file')
    if not 'api_keys' in data:
        raise ValueError('API keys arent properly set in json config file')
    
    li = 0
    ld = 0
    
    for key in data['api_keys']:
        gw2_client = GuildWars2Client(api_key=key)
        
        li += retrieve_li(gw2_client)
        ld += retrieve_ld(gw2_client)
    
    print(li)
    print(ld)