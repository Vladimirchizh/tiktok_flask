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
def trending_videos():
    return TikTokAPI(cookie=cookie) \
        .getTrending(count=10)

# Get user feeds


# Get a list of user videos
@app.route('/api/user/<user_id>/videos', methods=['GET'])
def user_videos(user_id):
    return TikTokAPI(cookie=cookie) \
        .getVideosByUserName(user_id, count=10)

# Get popular videos for user
@app.route('/api/user/<user_id>/popular_videos', methods=['GET'])
def popular_videos(user_id):
    return 

# Get likes count
@app.route('/api/user/<user_id>/<video_id>/likes_count', methods=['GET'])
def likes_count(video_id):
    return TikTokAPI(cookie=cookie) \
        .getVideoById(self, video_id)

# POST /api/user/videos {“user_id”:”<user_id>”, “update_cache”:True }
@app.route('/api/user/videos', methods=['POST'])
def post_vid():
    return 


# POST /api/user/likes_count {“user_id”:”<user_id>”, ” video_id”:”<video_id>”, “update_cache”:True}
@app.route('/api/user/likes_count', methods=['POST'])
def post_likes(user_id):
    return 


app.run()