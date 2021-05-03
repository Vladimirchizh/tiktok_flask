from flask import Flask, request
from flask_caching import Cache
from TikTokAPI import TikTokAPI
import os

config = {
    "DEBUG": True, 
    "CACHE_TYPE": "SimpleCache",
    "CACHE_DEFAULT_TIMEOUT": 3600
}

cookie = {
  "s_v_web_id": "verify_ko8vd9uf_6WIQwVSR_fDnQ_4zTb_AfQi_vqJhZR7Er44L",
  "tt_webid": "6937647666549769733"
}


app = Flask(__name__)
app.config.from_mapping(config)
cache = Cache(app)

 
def str_to_bool(s):
    if s == 'True':
         return True
    elif s == 'False':
         return False

# Show 10 most trending videos
@app.route('/api/trending_videos', methods=['GET'])
@cache.cached()
def trending_videos():
    videos = dict()
    trends = TikTokAPI(cookie=cookie) \
        .getTrending(count=10)
    for i in trends['items']:
        videos[str(i['id'])] = str(i['video']['downloadAddr'])
    return videos


# Get user by his tiktok name
@app.route('/api/user/<user_id>/info', methods=['GET'])
@cache.cached()
def popular_videos(user_id):
    return TikTokAPI(cookie=cookie) \
        .getUserByName(user_id)


# Get likes count
@app.route('/api/user/<user_id>/<video_id>/likes_count', methods=['GET'])
@cache.cached()
def likes_count(user_id,video_id,forced_update=None):
    cache.cached(key_prefix='/<user_id>/<video_id>/likes_count', 
                 forced_update=str_to_bool(forced_update))

    likes = TikTokAPI(cookie=cookie) \
        .getVideoById(video_id)["itemInfo"]["itemStruct"]['stats']['diggCount']
    
    return 'For video %s it is total of %s likes'%(str(video_id), str(likes))


# POST /api/user/likes_count {“user_id”:”<user_id>”, ” video_id”:”<video_id>”, “update_cache”:True}
@app.route('/api/user/likes_count', methods=['POST'])
def post_likes():
    data = request.get_json()
    likes = likes_count(data['user_id'],
                        data['video_id'],
                        data['update_cache'])
    return likes


# Get a list of user videos
@app.route('/api/user/<user_id>/videos', methods=['GET'])
@cache.cached()
def user_videos(user_id, forced_update=None):
    cache.cached(key_prefix='/<user_id>/videos', 
                 forced_update=str_to_bool(forced_update))
    videos = dict()
    vids = TikTokAPI(cookie=cookie) \
        .getVideosByUserName(user_name=user_id, count=10)
    for i in vids['items']:
        videos[i['id']] = str(i['video']['downloadAddr'])
    return videos

# POST /api/user/videos {“user_id”:”<user_id>”, “update_cache”:True }
@app.route('/api/user/videos', methods=['POST'])
def post_vid():
    data = request.get_json()
    vids = user_videos(data['user_id'],
                       data['update_cache'])
    return vids


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))