import os
import random
import pyglet

# Set the path to the directory containing the video files
path = '/path/to/video/files/'

# Get a list of all video files in the directory
video_files = [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.mp4')]

# Choose a random video file from the list
random_file = random.choice(video_files)

# Create a window to play the video in
player = pyglet.media.Player()
window = pyglet.window.Window()

# Load the chosen video file into a media source
source = pyglet.media.load(random_file)

# Queue the media source for playback
player.queue(source)

# Set the video player's dimensions to match the window
player.video_player.width = window.width
player.video_player.height = window.height

# Play the video
player.play()

# Start the event loop to display the window and play the video
pyglet.app.run()
