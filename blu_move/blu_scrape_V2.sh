#!/bin/sh

# scraper V2 on user booking page  : remove start & end time parameter, since the output looks the same
# whatever the value of start & end  





#curl 'https://rest.bluemove.es/api/fleet/availability' -H 'pragma: no-cache' -H 'origin: https://webapp.bluemove.es' -H 'accept-encoding: gzip, deflate, br' -H 'accept-language: zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6' -H 'user-agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Mobile Safari/537.36' -H 'content-type: application/x-www-form-urlencoded; charset=UTF-8' -H 'accept: application/json, text/javascript, */*; q=0.01' -H 'cache-control: no-cache' -H 'authority: rest.bluemove.es' -H 'referer: https://webapp.bluemove.es/en/my-bluemove' --data 'cityId=100&userId=142961&token=549mNphfCEefL2iYCwdM96GMFqqnTj56UhHLE70V21idilcfl3&product=cs&usageReason=private' --compressed | jq

curl 'https://rest.bluemove.es/api/fleet/availability' -H 'pragma: no-cache' -H 'origin: https://webapp.bluemove.es' -H 'accept-encoding: gzip, deflate, br' -H 'accept-language: zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6' -H 'user-agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Mobile Safari/537.36' -H 'content-type: application/x-www-form-urlencoded; charset=UTF-8' -H 'accept: application/json, text/javascript, */*; q=0.01' -H 'cache-control: no-cache' -H 'authority: rest.bluemove.es' -H 'referer: https://webapp.bluemove.es/en/my-bluemove' --data 'cityId=100&userId=142961&token=549mNphfCEefL2iYCwdM96GMFqqnTj56UhHLE70V21idilcfl3&product=cs&usageReason=private' --compressed > blu_.json