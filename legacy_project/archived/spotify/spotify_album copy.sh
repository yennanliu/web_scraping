#!/bin/sh


# http://stackoverflow.com/questions/41566971/how-to-get-spotify-artist-id-for-the-spotify-endpoint-url


# input artist name 
echo 'plz enter artist name '
read  varname
echo  'varname = ' $varname

# modify usl
url="https://api.spotify.com/v1/search?q=${varname}&type=artist"
echo $url


# query 
API_ARTIST_URL=$(curl -s $url | jq -r '.artists.items[0].href')

echo 'API_ARTIST_URL : '   $API_ARTIST_URL
echo 'ALBUM'
echo '=================='

# print album
curl -s "$API_ARTIST_URL/top-tracks?country=US" | jq -r '.tracks[].name'