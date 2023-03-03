import requests as req
import os
import json

query = "minecraft"
exclude_banned_tags = 1

banned_tags = 'insect insects bondage rape bodysuit tentacle tentacles big_belly chubby_female chubby_male chubby obese femboy morbit gay lesbian pregnant vore futa futanari ai_generated piss urine_stream urine shitting shit yaoi yuri furry puffy_anus deflation inflation hyper gore guro horse zoophilia fat birth'

if query not in os.listdir():
  os.mkdir(query)
query_dir = os.listdir(query)

def download(url,path):
  data = req.get(url).content
  with open(path, 'wb') as file:
   file.write(data)

links = []

def writelinks():
  f = open(f"./{query}.txt","w")
  for link in links:
    f.write(link+"\n")
  f.close()

def tag_check(tags):
  tags = tags.split(" ")
  for tag in tags:
    if tag in banned_tags:
      return False
  return True

url = "https://api.rule34.xxx/index.php?page=dapi&s=post&json=1&q=index&tags=" + query

running = True
pid = 0
while running:
  posts = req.get(url+f'&pid={pid}').json()

  if posts == []:
    running = False
  pid = pid + 1
  for post in posts:
    if tag_check(post['tags']) and exclude_banned_tags:
      fname = post['file_url'].split("/")[-1]
      print(fname ,pid,"\n",post['tags'])
      if fname not in query_dir:
        download(post['file_url'],query+"/"+fname)
        links.append(post['file_url'])
        #f = open(query+"/"+fname+"_tags.txt","w")
        #f.write(post['tags'])
        #f.close()

  writelinks()