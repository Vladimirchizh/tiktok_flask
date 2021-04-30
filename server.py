import flask
from TikTokAPI import TikTokAPI

cookie = {
  "s_v_web_id": "<your_key>",
  "tt_webid": "<your_key>"
}



app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Show 10 most trending videos
@app.route('/api/trending_videos', methods=['GET'])
def home():
    retval = TikTokAPI(cookie=cookie) \
        .getTrending(count=10)
    return 

# Get user feeds



# Get a list of user videos
@app.route('/api/user/<user_id>/videos', methods=['GET'])
def user_videos():
    user_videos = TikTokAPI(cookie=cookie) \
        .getVideosByUserName("fcbarcelona", count=10)
    return 

# Get popular videos for user
@app.route('/api/user/<user_id>/popular_videos', methods=['GET'])
def home():
    return 

# Get likes count
@app.route('/api/user/<user_id>/<video_id>/likes_count', methods=['GET'])
def home():
    return 

# POST /api/user/videos {“user_id”:”<user_id>”, “update_cache”:True }
@app.route('/api/user/videos', methods=['POSt'])
def home():
    return 
# POST /api/user/likes_count {“user_id”:”<user_id>”, ” video_id”:”<video_id>”, “update_cache”:True}


app.run()