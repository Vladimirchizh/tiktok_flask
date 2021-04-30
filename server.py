from flask import Flask, request
from flask_caching import Cache
from TikTokAPI import TikTokAPI

config = {
    "DEBUG": True, 
    "CACHE_TYPE": "SimpleCache",
    "CACHE_DEFAULT_TIMEOUT": 300
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
def trending_videos():
    return TikTokAPI(cookie=cookie) \
        .getTrending(count=10)

# Get user feeds


# Get a list of user videos
@app.route('/api/user/<user_id>/videos', methods=['GET'])
def user_videos(user_id):
    print(user_id)
    return TikTokAPI(cookie=cookie) \
        .getVideosByUserName(user_name=user_id, count=10)

# Get popular videos for user
@app.route('/api/user/<user_id>/popular_videos', methods=['GET'])
def popular_videos(user_id):
    return 

# Get likes count
@app.route('/api/user/<user_id>/<video_id>/likes_count', methods=['GET'])
def likes_count(user_id,video_id):
    return TikTokAPI(cookie=cookie) \
        .getVideoById(video_id)

# POST /api/user/videos {“user_id”:”<user_id>”, “update_cache”:True }
@app.route('/api/user/videos', methods=['POST'])
@cache.cached(timeout=3600)
def post_vid():
    data = request.get_json()
    print('Data Received: "{data}"'.format(data=data))
    return request.get_json()



# POST /api/user/likes_count {“user_id”:”<user_id>”, ” video_id”:”<video_id>”, “update_cache”:True}
@app.route('/api/user/likes_count', methods=['POST'])
@cache.cached(timeout=3600)
def post_likes():
    data = request.get_json()
    print('Data Received: "{data}"'.format(data=data))
    return "Request Processed.\n"


app.run()