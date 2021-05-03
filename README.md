## TikTok api 

#### Task 1: Show 10 most trending videos, GET '/api/trending_videos'
Example of curl command

    curl http://127.0.0.1:5000/api/trending_videos

*returns the dictionary with video ids and links to download them*
    
    {
    "6925312482038828289": "https://v58.tiktokcdn.com/video/tos/alisg/tos-alisg-pve-0037c001/492c5abc13b84e11840a7df36d1f09c2/?VExpiration=1620071970&VSignature=P3uXqx2ACiK4qscoPfde6Q&a=1233&br=1888&bt=944&cd=0%7C0%7C1&ch=0&cr=0&cs=0&cv=1&dr=0&ds=3&er=&l=20210503135921010115151101084418C6&lr=tiktok_m&mime_type=video_mp4&net=0&pl=0&qs=0&rc=anJ0cmg3Znh0MzMzMzczM0ApOjszZDQ1ODw8NzQ0aDs7Z2cyb2MvNC5oYWFgLS1fMTRzczNfYi8vYC8xLmM1LWAyLjA6Yw%3D%3D&vl=&vr="
    }

#### Task 2: Get a list of user videos, GET '/api/user/<user_id>/videos'
Example of curl command
    
    curl http://127.0.0.1:5000/api/user/gabrielymayra/videos
    
#### Task 3: Get popular videos for user, GET'/api/user/<user_id>/popular_videos'
Example of curl command
    
    curl http://127.0.0.1:5000/api/user/gabrielymayra/popular_videos

#### Task 4: Get likes count, GET '/api/user/<user_id>/<video_id>/likes_count'
Example of curl command

    curl http://127.0.0.1:5000/api/user/tatyanka_yak/6954415245976751361/likes_count

    curl http://127.0.0.1:5000/api/user/tatyanka_yak/6943996796519681281/likes_count
    
*caching response for this method*

    For video 6943996796519681281 it is total of 15700000 likes%

#### Task 5: Update cache of likes count, POST /api/user/likes_count {“user_id”:”<user_id>”, ” video_id”:”<video_id>”, “update_cache”:True}
Example of curl command

    curl http://127.0.0.1:5000/api/user/likes_count -d "{\"user_id\": \"luna_the_pantera\",\"update_cache\":\"False\",\"video_id\":\"6943996796519681281\"}" -H 'Content-Type: application/json'

*caching response for this method*

    For video 6943996796519681281 it is total of 15701000 likes