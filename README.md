## TikTok api 

#### Task 1: Show 10 most trending videos, GET '/api/trending_videos'
Example of curl command

    curl http://127.0.0.1:5000/api/trending_videos

*returns the dictionary with video ids and links to download them*
    
    {
    "6927694403037367553": "https://v58.tiktokcdn.com/video/tos/alisg/tos-alisg-pve-0037c001/87923323f1fb48b281f00a816714552f/?VExpiration=1620009546&VSignature=PmN7d0L1Qd3r9Qm2bvRWeQ&a=1233&br=1734&bt=867&cd=0%7C0%7C1&ch=0&cr=0&cs=0&cv=1&dr=0&ds=3&er=&l=20210502203857010234109084590EE915&lr=tiktok_m&mime_type=video_mp4&net=0&pl=0&qs=0&rc=ajQ4M3A0ZW80MzMzZjczM0ApOTc4aDplZzs2NztoNTQ8NGdgaWkxXjNobmZgLS0wMTRzc2EuMzQzX2FjMGAuYmNiNWI6Yw%3D%3D&vl=&vr=", 
    "6929569045972798722": "https://v58.tiktokcdn.com/video/tos/alisg/tos-alisg-pve-0037c001/7b97982cf174414daf2d35f2a6c900ca/?VExpiration=1620009549&VSignature=T-y4A0ILgiEusaO7ouc7Gw&a=1233&br=3886&bt=1943&cd=0%7C0%7C1&ch=0&cr=0&cs=0&cv=1&dr=0&ds=3&er=&l=20210502203857010234109084590EE915&lr=tiktok_m&mime_type=video_mp4&net=0&pl=0&qs=0&rc=M3Y5bHFnZGtmMzMzZDczM0ApZzo3aTlpNGQ0NzhmZ2Q6O2cxNmBwNDNeYGlgLS01MTRzc2BeNl5hXjAxYy1eLmEvLjU6Yw%3D%3D&vl=&vr=", 
    "6939968534478998786": "https://v58.tiktokcdn.com/video/tos/alisg/tos-alisg-pve-0037c001/685204a1dec04d2e966b4afeb76ce4db/?VExpiration=1620009557&VSignature=LRMIAS02ZneykuoA-GSwJg&a=1233&br=3724&bt=1862&cd=0%7C0%7C1&ch=0&cr=0&cs=0&cv=1&dr=0&ds=3&er=&l=20210502203857010234109084590EE915&lr=tiktok_m&mime_type=video_mp4&net=0&pl=0&qs=0&rc=ajhkZDN1Ozl1NDMzaTczM0ApaTc7NGQ1OTs2N2Y2OzdkaGdobGNrL2BwZTRgLS0tMTRzczQuNGFeMTZjYV9hLzJjMTI6Yw%3D%3D&vl=&vr=", 
    "6941289234409983233": "https://v58.tiktokcdn.com/video/tos/alisg/tos-alisg-pve-0037c001/dd799812fffa450db37f7d50921a9272/?VExpiration=1620009565&VSignature=lPaDk2sIk75_EfcGn5q4FQ&a=1233&br=788&bt=394&cd=0%7C0%7C1&ch=0&cr=0&cs=0&cv=1&dr=0&ds=3&er=&l=20210502203857010234109084590EE915&lr=tiktok_m&mime_type=video_mp4&net=0&pl=0&qs=0&rc=ajlwNzpzeGg5NDMzPDczM0ApPDs4NDVnM2U8N2k3Mzs3ZWc1ZTYycS5vZ15gLS00MTRzczAxYy0zNi0xYzYyYjItYGI6Yw%3D%3D&vl=&vr=", 
    "6941690273240042754": "https://v58.tiktokcdn.com/video/tos/alisg/tos-alisg-pve-0037c001/cf39c2986d864b7387219dbe044bc901/?VExpiration=1620009552&VSignature=rs-1fz6AJBuecybCWBvmGQ&a=1233&br=1402&bt=701&cd=0%7C0%7C1&ch=0&cr=0&cs=0&cv=1&dr=0&ds=3&er=&l=20210502203857010234109084590EE915&lr=tiktok_m&mime_type=video_mp4&net=0&pl=0&qs=0&rc=M3FzcGY8NTN3NDMzOjczM0ApNTc2OjkzNDxkNzY2OThoaWcuMi1mXzU1YV5gLS1iMTRzczViNjZhMF5gNi4zYjJhNmA6Yw%3D%3D&vl=&vr=", 
    "6941849161880849665": "https://v58.tiktokcdn.com/video/tos/alisg/tos-alisg-pve-0037c001/fb43e98275674bebb5bb7a2d2cb4b66e/?VExpiration=1620009554&VSignature=Dvd_7ROWQZ5u5ZxMObpvLg&a=1233&br=1980&bt=990&cd=0%7C0%7C1&ch=0&cr=0&cs=0&cv=1&dr=0&ds=3&er=&l=20210502203857010234109084590EE915&lr=tiktok_m&mime_type=video_mp4&net=0&pl=0&qs=0&rc=ajxtdGs2eDQ5NDMzZjczM0ApZzs1ZmU2OGU6N2Q4N2Y0O2doaXFyLnA1Yl9gLS02MTRzczMvMTFeMC4zXi40XjIxXzM6Yw%3D%3D&vl=&vr=", 
    "6944752172823235842": "https://v58.tiktokcdn.com/video/tos/alisg/tos-alisg-pve-0037c001/3f60732ed42b49c9a49f96be1405916e/?VExpiration=1620009556&VSignature=1RKoYFrYjXB-y3Rtz2dOAg&a=1233&br=4648&bt=2324&cd=0%7C0%7C1&ch=0&cr=0&cs=0&cv=1&dr=0&ds=3&er=&l=20210502203857010234109084590EE915&lr=tiktok_m&mime_type=video_mp4&net=0&pl=0&qs=0&rc=MzpkNjxoOHVlNDMzNDczM0ApOTZlZmdoaGVmN2YzZzw3OGctYnM2bmYtYWRgLS0vMTRzcy1gLi1iXjNhLjZgMDRgLTY6Yw%3D%3D&vl=&vr=", 
    "6947307088704064770": "https://v58.tiktokcdn.com/video/tos/alisg/tos-alisg-pve-0037c001/b2e5d254a1644bf185e4b4756f74703b/?VExpiration=1620009548&VSignature=eJ2yc3wfugZZwIiLSSCVFA&a=1233&br=3112&bt=1556&cd=0%7C0%7C1&ch=0&cr=0&cs=0&cv=1&dr=0&ds=3&er=&l=20210502203857010234109084590EE915&lr=tiktok_m&mime_type=video_mp4&net=0&pl=0&qs=0&rc=M3dtd2pnaGh2NDMzODczM0ApPDRmPDo4PGRnN2VlOzxpZmcuLzFycXJjaWhgLS1kMTRzc2BjNWBfLjFiXmIzNTFfMzA6Yw%3D%3D&vl=&vr=", 
    "6948474527445781761": "https://v58.tiktokcdn.com/video/tos/alisg/tos-alisg-pve-0037c001/5ff5defd2e9949fca15d4a4325b1ce29/?VExpiration=1620009551&VSignature=Y07ouyQjb9WXd_NaVvIjuA&a=1233&br=1080&bt=540&cd=0%7C0%7C1&ch=0&cr=0&cs=0&cv=1&dr=0&ds=3&er=&l=20210502203857010234109084590EE915&lr=tiktok_m&mime_type=video_mp4&net=0&pl=0&qs=0&rc=ajt1cWo3a2Z5NDMzODczM0ApZGQ4aDloOGU8NzplNzllOGc2aS5uM28yLmpgLS1kMTRzc18wNWEzMl5fYGMxX14uXzA6Yw%3D%3D&vl=&vr=", 
    "6950541591102704897": "https://v58.tiktokcdn.com/video/tos/alisg/tos-alisg-pve-0037c001/2381441e046f4d558e64960f1a5acd36/?VExpiration=1620009565&VSignature=DkhnPvLrqtw2m57daNqL8A&a=1233&br=212&bt=106&cd=0%7C0%7C0&ch=0&cr=0&cs=0&dr=0&ds=2&er=&l=20210502203857010234109084590EE915&lr=tiktok_m&mime_type=video_mp4&net=0&pl=0&qs=0&rc=andkNGY4ZGpuNDMzODczM0ApOTM6PDg2NGUzNzozOjhnNWdganNvLTFfZW5gLS1kMTRzc2BhMTVhY15gM2FhNDJeYDE6Yw%3D%3D&vl=&vr="\
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

    For video 6943996796519681281 it is total of 15700000 likes

#### Task 5: Update cache of likes count, POST /api/user/likes_count {“user_id”:”<user_id>”, ” video_id”:”<video_id>”, “update_cache”:True}
Example of curl command

    curl http://127.0.0.1:5000/api/user/likes_count -d "{\"user_id\": \"luna_the_pantera\",\"update_cache\":\"False\",\"video_id\":\"6943996796519681281\"}" -H 'Content-Type: application/json'

*caching response for this method*

    For video 6943996796519681281 it is total of 15701000 likes