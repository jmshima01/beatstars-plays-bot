import requests
import re
import random
import sys
import time

# Beatstars Plays B0t (not a DOS!)
def play_beat(beat):
    url = "https://main.v2.beatstars.com/stats/track_play"
    valid_beat_url = re.search("https://www.beatstars.com/beat/.+-\d+", beat).group()
    user_beat_url = ""
    if valid_beat_url:
        user_beat_id = re.search("\-\d+$",valid_beat_url).group()
    else:
        raise Exception("invaild beat url try again...")
    
    if not user_beat_id:
        raise Exception("unable to parse beat id from url ending :( contact script owner")
    data = {
        "id": user_beat_id,
        "sponsored":False,
        "store_type": "<script>alert(1);</script>"
    }
    headers = {
        "Host": "main.v2.beatstars.com",
        "User-Agent": "<script>alert(1);</script>",}
    print()
    response = requests.post(url,json=data,headers=headers)
    print(response.content)
    
if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise Exception("usage: python3 main.py <beat_url>")
    beat = sys.argv[1]
    while 1:
        play_beat(beat)
        time.sleep(random.randint(0,2)) # do not DOS!!