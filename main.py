from flask import Flask, request
from flask_caching import Cache
from TikTokAPI import TikTokAPI
from TikTokApi import TikTokApi
import os



api = TikTokApi.get_instance()
s_v_web_id = "verify_ko8vd9uf_6WIQwVSR_fDnQ_4zTb_AfQi_vqJhZR7Er44L"
results=10

config = {
    "DEBUG": True, 
    "CACHE_TYPE": "SimpleCache",
    "CACHE_DEFAULT_TIMEOUT": 3600
}


cookie = {
  "s_v_web_id": s_v_web_id,
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
    trending = api.trending(count=results, custom_verifyFp=s_v_web_id)
    for i in trending:
        videos[str(i['id'])] = str(i['video']['playAddr'])
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
    vids = api.by_username(count=results,username=user_id, custom_verifyFp=s_v_web_id)
    for i in vids:
        videos[i['id']] = str(i['video']['playAddr'])
    return videos

# POST /api/user/videos {“user_id”:”<user_id>”, “update_cache”:True }
@app.route('/api/user/videos', methods=['POST'])
def post_vid():
    data = request.get_json()
    vids = user_videos(data['user_id'],
                       data['update_cache'])
    return vids

@app.route('/api/user/<user_id>/liked', methods=['GET'])
@cache.cached()
def user_liked(user_id):
    cache.cached(key_prefix='/<user_id>/liked')
    videos = dict()
    vids = api.user_liked(count=results,username=user_id, custom_verifyFp=s_v_web_id)
    for i in vids:
        videos[i['id']] = str(i['video']['playAddr'])
    return videos

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))