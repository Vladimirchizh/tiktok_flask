from flask import Flask, request
from flask_caching import Cache
from TikTokAPI import TikTokAPI

config = {
    "DEBUG": True, 
    "CACHE_TYPE": "SimpleCache",
    "CACHE_DEFAULT_TIMEOUT": 3600
}

cookie = {
  "s_v_web_id": "verify_ko4oaav9_ZxHRwiaE_riue_4oIf_BXla_GLtAvfif7KCI",
  "tt_webid": "6937647666549769733"
}

app = Flask(__name__)
app.config.from_mapping(config)
cache = Cache(app)

# Show 10 most trending videos
@app.route('/api/trending_videos', methods=['GET'])
@cache.cached()
def trending_videos():
    return TikTokAPI(cookie=cookie) \
        .getTrending(count=10)

# Get a list of user videos
@app.route('/api/user/<user_id>/videos', methods=['GET'])
@cache.cached()
def user_videos(user_id):
    print(user_id)
    return TikTokAPI(cookie=cookie) \
        .getVideosByUserName(user_name=user_id, count=10)

# Get popular videos for user
@app.route('/api/user/<user_id>/popular_videos', methods=['GET'])
@cache.cached()
def popular_videos(user_id):
    return TikTokAPI(cookie=cookie) \
        .getLikesByUserName(user_id,count=10)

# Get likes count
@app.route('/api/user/<user_id>/<video_id>/likes_count', methods=['GET'])
@cache.cached()
def likes_count(user_id,video_id):
    cache.cached(key_prefix='/<user_id>/<video_id>/likes_count')
    likes = TikTokAPI(cookie=cookie) \
        .getVideoById(video_id)["itemInfo"]["itemStruct"]['stats']['diggCount']
    return 'For this video it is total of %s likes'%str(likes)


# POST /api/user/likes_count {“user_id”:”<user_id>”, ” video_id”:”<video_id>”, “update_cache”:True}
@app.route('/api/user/likes_count', methods=['POST'])
@cache.cached()
def post_likes():
    data = request.get_json()
    if data['update_cache'] == 'True':
        #cache.delete(key='/%s/%s/likes_count'%(data['user_id'],data['video_id']))
        cache.cached(key_prefix='/%s/%s/likes_count'%(data['user_id'],data['video_id']), forced_update=True)
    likes = likes_count(data['user_id'],data['video_id'])
    return likes # "Posted results.\n user_id: "+data['user_id']+"\n video_id: "+data['video_id']


# POST /api/user/videos {“user_id”:”<user_id>”, “update_cache”:True }
@app.route('/api/user/videos', methods=['POST'])
@cache.cached()
def post_vid():
    if request.get_json()['update_cache'] == 'True':
        # TODO вписать сюда метод GET /api/user/videos
        cache.delete()

    return "Posted results.\n user_id: "+request.get_json()['user_id']



app.run()