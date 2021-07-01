"""A video player class."""

from .video_library import VideoLibrary
from random import choice


class VideoPlayer:
    """A class used to represent a Video Player."""

    playing = 0             # 0 - nothing; 1 - paused; 2 - playing
    played = ""
    playlists = {}


    def __init__(self):
        self._video_library = VideoLibrary()

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        out = []
        for key in self._video_library._videos:
            out.append( str( self._video_library._videos[ key ]) )
        out.sort()

        print(f"Here's a list of all available videos:")
        for vid in out:
            print ( f"  {vid}" )

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        if video_id in self._video_library._videos:
            if self.playing > 0:
                print(f"Stopping video: {self.played.title}" )  
            self.playing = 2
            self.played = self._video_library._videos[ video_id ]
            print(f"Playing video: {self.played.title}" )
        else:
            print (f"Cannot play video: Video does not exist")

    def stop_video(self):
        """Stops the current video."""
        if self.playing > 0:
            print(f"Stopping video: {self.played.title}")
            self.playing = False
        else:
            print(f"Cannot stop video: No video is currently playing")

    def play_random_video(self):
        """Plays a random video from the video library."""
        self.play_video( choice(list( self._video_library._videos.keys() )) )

    def pause_video(self):
        """Pauses the current video."""
        if self.playing == 0:
            print(f"Cannot pause video: No video is currently playing")
        elif self.playing == 1:
            print(f"Video already paused: {self.played.title}")
        else:
            print(f"Pausing video: {self.played.title}")
            self.playing = 1

    def continue_video(self):
        """Resumes playing the current video."""
        if self.playing == 0:
            print(f"Cannot continue video: No video is currently playing")
        elif self.playing == 1:
            print(f"Continuing video: {self.played.title}")
            self.playing = 2
        else:
            print(f"Cannot continue video: Video is not paused")

    def show_playing(self):
        """Displays video currently playing."""
        if self.playing == 0:
            print(f"No video is currently playing")
        elif self.playing == 1:
            print(f"Currently playing: {self.played} - PAUSED")
        else:
            print(f"Currently playing: {self.played}")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        found = False
        if len(self.playlists) > 0:
            temp = list(self.playlists.keys())
            for pl in temp:
                if playlist_name.lower() == pl.lower():
                    playlist_name = pl
                    found = True
                    break

        if found == False:
            print(f"Successfully created new playlist: {playlist_name}")
            self.playlists[ playlist_name ] = []
        else:
            print(f"Cannot create playlist: A playlist with the same name already exists")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        found = False
        if len(self.playlists) > 0:
            temp = list(self.playlists.keys())
            for pl in temp:
                if playlist_name.lower() == pl.lower():
                    playlist_name = pl
                    found = True
                    break

        if found == False:
            print(f"Cannot add video to {playlist_name}: Playlist does not exist")
        elif video_id not in self._video_library._videos:
            print(f"Cannot add video to {playlist_name}: Video does not exist")
        elif video_id in self.playlists[playlist_name]:
            print(f"Cannot add video to {playlist_name}: Video already added")
        else:
            self.playlists[ playlist_name ].append( video_id )
            print(f"Added video to {playlist_name}: {self._video_library._videos[video_id].title}")

    def show_all_playlists(self):
        """Display all playlists."""
        
        print ( f"Showing all playlists:")
        if self.playlists:
            out = sorted( self.playlists, key=str.casefold )
            for pl in out:
                print( f"   {pl}" )
        else:
            print( "No playlists exist yet")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        found = False
        if len(self.playlists) > 0:
            temp = list(self.playlists.keys())
            for pl in temp:
                if playlist_name.lower() == pl.lower():
                    playlist_name = pl
                    found = True
                    break

        if found == True:
            print ( f"Showing playlist: {playlist_name}")
            if len( self.playlists[playlist_name] ) == 0:
                print( "   No videos here yet" )
            else:
                for pl in self.playlists[playlist_name]:
                    print ( f"  {self._video_library._videos[pl]}" )
        else:
            print(f"Cannot show playlist {playlist_name}: Playlist does not exist")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        found = False
        if len(self.playlists) > 0:
            temp = list(self.playlists.keys())
            for pl in temp:
                if playlist_name.lower() == pl.lower():
                    playlist_name = pl
                    found = True
                    break

        if found == False:
            print(f"Cannot remove video from {playlist_name}: Playlist does not exist")
        elif video_id not in self._video_library._videos:
            print(f"Cannot remove video from {playlist_name}: Video does not exist")
        elif video_id not in self.playlists[playlist_name]:
            print(f"Cannot remove video from {playlist_name}: Video not in playlist")
        else:
            self.playlists[ playlist_name ].remove( video_id )
            print(f"Removed video from {playlist_name}: {self._video_library._videos[video_id].title}")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        found = False
        if len(self.playlists) > 0:
            temp = list(self.playlists.keys())
            for pl in temp:
                if playlist_name.lower() == pl.lower():
                    playlist_name = pl
                    found = True
                    break

        if found == True:
            self.playlists[ playlist_name ].clear()
            print( f"Successfully removed all videos from {playlist_name}")
        else:
            print( f"Cannot clear playlist {playlist_name}: Playlist does not exist")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        found = False
        if len(self.playlists) > 0:
            temp = list(self.playlists.keys())
            for pl in temp:
                if playlist_name.lower() == pl.lower():
                    playlist_name = pl
                    found = True
                    break

        if found == True:
            self.playlists.pop( playlist_name )
            print( f"Deleted playlist: {playlist_name}")
        else:
            print( f"Cannot delete playlist {playlist_name}: Playlist does not exist")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
