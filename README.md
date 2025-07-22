# HLS Streaming with FFmpeg and Python

This project demonstrates how to convert an MP4 video into HLS (HTTP Live Streaming) format using FFmpeg, automate the process using Python, and host the stream locally using Python's HTTP server. Ngrok is used to expose the local stream to the internet.

## Features
- Converts any MP4 file into HLS-compliant format (.m3u8 + .ts segments)
- Automates conversion via Python script
- Local streaming using Python HTTP server
- Public access via Ngrok tunnel

## Requirements
- Python 3.x
- FFmpeg
- Ngrok (for public URL)

## How to Use

### 1. Convert MP4 to HLS using Python script

Make sure `abb.mp4` is in the project directory. Then run:

```bash
python convert_to_hls.py
