## TikTok api 

Task 1: Show 10 most trending videos, GET '/api/trending_videos'
    
    curl http://127.0.0.1:5000/api/trending_videos

Task 2: Get a list of user videos, GET '/api/user/<user_id>/videos'
    
    curl http://127.0.0.1:5000/api/user/gabrielymayra/videos
    
Task 3: Get popular videos for user, GET'/api/user/<user_id>/popular_videos'
    
    curl http://127.0.0.1:5000/api/user/gabrielymayra/popular_videos

Task 4: Get likes count, GET '/api/user/<user_id>/<video_id>/likes_count'

    curl http://127.0.0.1:5000/api/user/tatyanka_yak/6954415245976751361/likes_count

    curl http://127.0.0.1:5000/api/user/tatyanka_yak/6943996796519681281/likes_count
    
    curl http://127.0.0.1:5000/api/user/likes_count -d "{\"user_id\": \"luna_the_pantera\",\"update_cache\":\"False\",\"video_id\":\"6943996796519681281\"}" -H 'Content-Type: application/json'
Task 5: Update cache of likes count, POST /api/user/likes_count {“user_id”:”<user_id>”, ” video_id”:”<video_id>”, “update_cache”:True}