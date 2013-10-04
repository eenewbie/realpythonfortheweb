import gdata.youtube
import gdata.youtube.service

youtube_service = gdata.youtube.service.YouTubeService()

user_id = raw_input("User id: ")

url = "http://gdata.youtube.com/feeds/api/users/"
playlist_url = url + user_id + "/playlists"

playlist_feed = youtube_service.GetYouTubePlaylistVideoFeed(playlist_url)
print "\nPlaylists for " + str.format(user_id) + ":\n"
for playlist in playlist_feed.entry:
	print playlist.title.text
	playlistid = playlist.id.text.split('/') [-1]
	video_feed = youtube_service.GetYouTubePlaylistVideoFeed(playlist_id=playlistid)
	for video in video_feed.entry:
		print "\t" + video.title.text
