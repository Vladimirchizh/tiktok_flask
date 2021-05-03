## TikTok api 

#### Task 1: Show 10 most trending videos, GET '/api/trending_videos'

Example of curl command

    curl https://tiktok5flask-fwoqorahna-lm.a.run.app/api/trending_videos

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

    
#### Task 2: Get popular videos for user

TikTok ain't giving neither popular videos for the user nor his feed, so I've made up the method which gives really detailed info about th user GET'/api/user/<user_id>/info'.

Example of curl command
    
    curl https://tiktok5flask-fwoqorahna-lm.a.run.app/api/user/gabrielymayra/info

*caching response for this method*
```
{"$language": "en", 
  "seoProps": {
    "itemList": [], 
    "jsonldList": [
      [
        "ItemList", 
        {
          "itemList": []
        }
      ], 
      [
        "Breadcrumb", 
        {
          "urlList": [
            {
              "name": "TikTok", 
              "url": "https://www.tiktok.com"
            }, 
            {
              "name": "Gabriel Mayra Hernan (@gabrielymayra) | TikTok", 
              "url": "https://www.tiktok.com/@gabrielymayra"
            }
          ]
        }
      ], 
      [
        "Person", 
        {
          "alternateName": "gabrielymayra", 
          "description": "", 
          "mainEntityOfPage": {
            "@id": "https://www.tiktok.com/@gabrielymayra", 
            "@type": "ProfilePage"
          }, 
          "name": "Gabriel Mayra Hernan"
        }
      ]
    ], 
    "metaParams": {
      "applicableDevice": "pc, mobile", 
      "canonicalHref": "https://www.tiktok.com/@gabrielymayra", 
      "description": "Gabriel Mayra Hernan (@gabrielymayra) en TikTok | 23.6K me gusta. 2.6K fans. Mira el \u00faltimo video de Gabriel Mayra Hernan (@gabrielymayra).", 
      "keywords": "Gabriel Mayra Hernan,gabrielymayra,TikTok, \u30c6\u30a3\u30c3\u30af\u30c8\u30c3\u30af, tik tok, tick tock, tic tok, tic toc, tictok, \u0442\u0438\u043a \u0442\u043e\u043a, ticktock", 
      "robotsContent": "index, follow", 
      "title": "TikTok de Gabriel Mayra Hernan (@gabrielymayra) | Mira los \u00faltimos videos de Gabriel Mayra Hernan en TikTok"
    }, 
    "pageId": "6814187084179702789", 
    "pageType": 1, 
    "predictedLanguage": "es"
  }, 
  "statusCode": 0, 
  "statusMsg": "", 
  "userInfo": {
    "itemList": [], 
    "stats": {
      "diggCount": 525, 
      "followerCount": 2574, 
      "followingCount": 446, 
      "heart": 23600, 
      "heartCount": 23600, 
      "videoCount": 131
    }, 
    "user": {
      "avatarLarger": "https://p16-sign-va.tiktokcdn.com/musically-maliva-obj/1663627540720645~c5_1080x1080.jpeg?x-expires=1620147600&x-signature=XxfOqUgGJGrPNfT9F1ADkC5Iytg%3D", 
      "avatarMedium": "https://p16-sign-va.tiktokcdn.com/musically-maliva-obj/1663627540720645~c5_720x720.jpeg?x-expires=1620147600&x-signature=tGSAvnun4yhjYEbNb%2Bm1ov9G4bw%3D", 
      "avatarThumb": "https://p16-sign-va.tiktokcdn.com/musically-maliva-obj/1663627540720645~c5_100x100.jpeg?x-expires=1620147600&x-signature=DT5heNZIK2U1t6W8QzovULxlvzc%3D", 
      "commentSetting": 0, 
      "createTime": 1586558857, 
      "duetSetting": 0, 
      "ftc": false, 
      "id": "6814187084179702789", 
      "isADVirtual": false, 
      "nickname": "Gabriel Mayra Hernan", 
      "openFavorite": true, 
      "privateAccount": false, 
      "relation": 0, 
      "roomId": "", 
      "secUid": "MS4wLjABAAAAcxpAUhFfDiVrN90XgWlWZLqAkXDR-k7VY5PKJQIVOq59aK-u0ISHQ4v0UIAdMi6L", 
      "secret": false, 
      "shortId": "0", 
      "signature": "", 
      "stitchSetting": 0, 
      "uniqueId": "gabrielymayra", 
      "verified": false
    }
  }
}
```
#### Task 3: Get likes count, GET '/api/user/<user_id>/<video_id>/likes_count'

Example of curl command

    curl https://tiktok5flask-fwoqorahna-lm.a.run.app/api/user/tatyanka_yak/6954415245976751361/likes_count

    curl https://tiktok5flask-fwoqorahna-lm.a.run.app/api/user/tatyanka_yak/6943996796519681281/likes_count
    
*caching response for this method*

    For video 6943996796519681281 it is total of 15700000 likes

#### Task 4: Update cache of likes count, POST /api/user/likes_count {“user_id”:”<user_id>”, ” video_id”:”<video_id>”, “update_cache”:True}

Example of curl command

    curl https://tiktok5flask-fwoqorahna-lm.a.run.app/api/user/likes_count -d "{\"user_id\": \"luna_the_pantera\",\"update_cache\":\"False\",\"video_id\":\"6943996796519681281\"}" -H 'Content-Type: application/json'

*caching response for this method*

    For video 6943996796519681281 it is total of 15701000 likes


#### Task 5: Get a list of user videos, GET '/api/user/<user_id>/videos'

Example of curl command
    
    curl https://tiktok5flask-fwoqorahna-lm.a.run.app/api/user/gabrielymayra/videos

*returns the dictionary with video ids and links to download them*
```
{
    "6953287268723477766": "https://v16-web.tiktok.com/video/tos/useast2a/tos-useast2a-ve-0068c002/c7c61c7f43a44323805ea82d94ec85c3/?a=1988&br=2124&bt=1062&cd=0%7C0%7C0&ch=0&cr=0&cs=0&dr=0&ds=3&er=&expire=1620087955&l=202105031825410102340990182952594C&lr=tiktok_m&mime_type=video_mp4&net=0&pl=0&policy=2&qs=0&rc=MztncjhpbmxqNDMzNzczM0ApNDloZzo1Zjw0N2dlNWk2aGdzc2BhYTZpZ3NgLS1kMTZzc2AyLzMwYmBjYGE2MC5gYC06Yw%3D%3D&signature=d7ef0012f9d99d32a702c875e4249e49&tk=tt_webid_v2&vl=&vr=",
    "6953006636151639301": "https://v16-web.tiktok.com/video/tos/useast2a/tos-useast2a-ve-0068c003/b7e7d5a141024649af95ae553b7856d6/?a=1988&br=2052&bt=1026&cd=0%7C0%7C0&ch=0&cr=0&cs=0&dr=0&ds=3&er=&expire=1620088004&l=2021050318260901011514922810527373&lr=tiktok_m&mime_type=video_mp4&net=0&pl=0&policy=2&qs=0&rc=M3J4dXQ5ZjozNDMzNzczM0ApOjhpODk4Njs1N2k7aDg5N2dzNmRvZ25yaXNgLS1kMTZzcy40M2MzMl81MzQtLS8xLmE6Yw%3D%3D&signature=70fc21a591fb17a4163c28fa5f1bd1f7&tk=tt_webid_v2&vl=&vr=",
    "6949586476929715461": "https://v16-web.tiktok.com/video/tos/useast2a/tos-useast2a-ve-0068c002/2e949486273c41aeb5edbdfbb9881da1/?a=1988&br=2972&bt=1486&cd=0%7C0%7C1&ch=0&cr=0&cs=0&cv=1&dr=0&ds=3&er=&expire=1620088031&l=2021050318265601011500405209543FE7&lr=tiktok_m&mime_type=video_mp4&net=0&pl=0&policy=2&qs=0&rc=anNtaW9uMzV4NDMzNzczM0ApOmdnOzc0OmU0N2g2MzY8M2cyNTMxcDM1NWxgLS1kMTZzc2BiMi00NC0xNDUzNi0wLmI6Yw%3D%3D&signature=3a61d8b1aa8cdbf3c7934ce260942e7e&tk=tt_webid_v2&vl=&vr=",
    "6942356836809035014": "https://v16-web.tiktok.com/video/tos/useast2a/tos-useast2a-ve-0068c003/526dac25b2434b88919680dd825877fd/?a=1988&br=1998&bt=999&cd=0%7C0%7C0&ch=0&cr=0&cs=0&dr=0&ds=3&er=&expire=1620088062&l=202105031827200102341090843352B562&lr=tiktok_m&mime_type=video_mp4&net=0&pl=0&policy=2&qs=0&rc=ajh3ODNkbjM2NDMzMzczM0ApMzc7ZTpmZTw1NzpoZTw4M2dlLWkzLWQ1NmBgLS0vMTZzczEyLS8tLmBjMmM0LTJhNDM6Yw%3D%3D&signature=4b916fdd978dd0c56d4f34c45410568b&tk=tt_webid_v2&vl=&vr=",
    "6941886441005927686": "https://v16-web.tiktok.com/video/tos/useast2a/tos-useast2a-ve-0068c001/f2c0aef436a6445298838daed6db21d8/?a=1988&br=1102&bt=551&cd=0%7C0%7C0&ch=0&cr=0&cs=0&dr=0&ds=3&er=&expire=1620088061&l=202105031827310101151510371C524952&lr=tiktok_m&mime_type=video_mp4&net=0&pl=0&policy=2&qs=0&rc=anM3dGhmOnQ7NDMzaDczM0ApNTppNGhlN2VpN2Y2NzpkaGcyZy9oNmU0ZV9gLS1gMTZzcy9eYDNfYS02Yi4uMDRhMmI6Yw%3D%3D&signature=fcfaf1cda9be6042f4d7bd2cedb2139f&tk=tt_webid_v2&vl=&vr="
}
```

#### Task 6: Post new values to refreshe cache, POST /api/user/videos {“user_id”:”<user_id>”, “update_cache”:True }


Example of curl command
    
    curl https://tiktok5flask-fwoqorahna-lm.a.run.app/api/user/videos d "{\"user_id\": \"gabrielymayra\",\"update_cache\":\"True\"}" -H 'Content-Type: application/json'

*returns the dictionary with video ids and links to download them*
```
{
    "6953287268723477766": "https://v16-web.tiktok.com/video/tos/useast2a/tos-useast2a-ve-0068c002/c7c61c7f43a44323805ea82d94ec85c3/?a=1988&br=2124&bt=1062&cd=0%7C0%7C0&ch=0&cr=0&cs=0&dr=0&ds=3&er=&expire=1620087955&l=202105031825410102340990182952594C&lr=tiktok_m&mime_type=video_mp4&net=0&pl=0&policy=2&qs=0&rc=MztncjhpbmxqNDMzNzczM0ApNDloZzo1Zjw0N2dlNWk2aGdzc2BhYTZpZ3NgLS1kMTZzc2AyLzMwYmBjYGE2MC5gYC06Yw%3D%3D&signature=d7ef0012f9d99d32a702c875e4249e49&tk=tt_webid_v2&vl=&vr=",
    "6953006636151639301": "https://v16-web.tiktok.com/video/tos/useast2a/tos-useast2a-ve-0068c003/b7e7d5a141024649af95ae553b7856d6/?a=1988&br=2052&bt=1026&cd=0%7C0%7C0&ch=0&cr=0&cs=0&dr=0&ds=3&er=&expire=1620088004&l=2021050318260901011514922810527373&lr=tiktok_m&mime_type=video_mp4&net=0&pl=0&policy=2&qs=0&rc=M3J4dXQ5ZjozNDMzNzczM0ApOjhpODk4Njs1N2k7aDg5N2dzNmRvZ25yaXNgLS1kMTZzcy40M2MzMl81MzQtLS8xLmE6Yw%3D%3D&signature=70fc21a591fb17a4163c28fa5f1bd1f7&tk=tt_webid_v2&vl=&vr=",
    "6949586476929715461": "https://v16-web.tiktok.com/video/tos/useast2a/tos-useast2a-ve-0068c002/2e949486273c41aeb5edbdfbb9881da1/?a=1988&br=2972&bt=1486&cd=0%7C0%7C1&ch=0&cr=0&cs=0&cv=1&dr=0&ds=3&er=&expire=1620088031&l=2021050318265601011500405209543FE7&lr=tiktok_m&mime_type=video_mp4&net=0&pl=0&policy=2&qs=0&rc=anNtaW9uMzV4NDMzNzczM0ApOmdnOzc0OmU0N2g2MzY8M2cyNTMxcDM1NWxgLS1kMTZzc2BiMi00NC0xNDUzNi0wLmI6Yw%3D%3D&signature=3a61d8b1aa8cdbf3c7934ce260942e7e&tk=tt_webid_v2&vl=&vr=",
    "6942356836809035014": "https://v16-web.tiktok.com/video/tos/useast2a/tos-useast2a-ve-0068c003/526dac25b2434b88919680dd825877fd/?a=1988&br=1998&bt=999&cd=0%7C0%7C0&ch=0&cr=0&cs=0&dr=0&ds=3&er=&expire=1620088062&l=202105031827200102341090843352B562&lr=tiktok_m&mime_type=video_mp4&net=0&pl=0&policy=2&qs=0&rc=ajh3ODNkbjM2NDMzMzczM0ApMzc7ZTpmZTw1NzpoZTw4M2dlLWkzLWQ1NmBgLS0vMTZzczEyLS8tLmBjMmM0LTJhNDM6Yw%3D%3D&signature=4b916fdd978dd0c56d4f34c45410568b&tk=tt_webid_v2&vl=&vr=",
    "6941886441005927686": "https://v16-web.tiktok.com/video/tos/useast2a/tos-useast2a-ve-0068c001/f2c0aef436a6445298838daed6db21d8/?a=1988&br=1102&bt=551&cd=0%7C0%7C0&ch=0&cr=0&cs=0&dr=0&ds=3&er=&expire=1620088061&l=202105031827310101151510371C524952&lr=tiktok_m&mime_type=video_mp4&net=0&pl=0&policy=2&qs=0&rc=anM3dGhmOnQ7NDMzaDczM0ApNTppNGhlN2VpN2Y2NzpkaGcyZy9oNmU0ZV9gLS1gMTZzcy9eYDNfYS02Yi4uMDRhMmI6Yw%3D%3D&signature=fcfaf1cda9be6042f4d7bd2cedb2139f&tk=tt_webid_v2&vl=&vr="
}
```
