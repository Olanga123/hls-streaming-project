Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import subprocess
... import os
... 
... # Set input/output
... input_file = "abb.mp4"
... output_folder = "hls"
... output_playlist = os.path.join(output_folder, "480p.m3u8")
... 
... # Create output directory if not exists
... os.makedirs(output_folder, exist_ok=True)
... 
... # FFmpeg command
... ffmpeg_cmd = [
...     "ffmpeg",
...     "-i", input_file,
...     "-c:v", "libx264",
...     "-preset", "veryfast",
...     "-b:v", "1000k",
...     "-minrate", "1000k",
...     "-maxrate", "1000k",
...     "-bufsize", "2000k",
...     "-c:a", "aac",
...     "-b:a", "128k",
...     "-hls_time", "8",
...     "-hls_list_size", "0",
...     "-hls_segment_filename", os.path.join(output_folder, "480p_%03d.ts"),
...     "-f", "hls",
...     output_playlist
... ]
... 
... # Run the command
... try:
...     subprocess.run(ffmpeg_cmd, check=True)
...     print("✅ HLS conversion completed.")
... except subprocess.CalledProcessError as e:
