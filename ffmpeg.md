# ffmpeg

- https://ffmpegbyexample.com/

## Video

- [`ffmpeg`](https://ffmpeg.org//documentation.html) 
- [The FFMPEG guy](https://www.youtube.com/@theFFMPEGguy/videos)

**Video resize / compression**
```
ffmpeg -i input.avi -s 720x480 -c:a copy output.mkv

ffmpeg -i input.avi -filter:v scale=720:-1 -c:a copy output.mkv
```

**Video Speedup**
https://trac.ffmpeg.org/wiki/How%20to%20speed%20up%20/%20slow%20down%20a%20video
```
ffmpeg -i input.mkv -filter:v "minterpolate='mi_mode=mci:mc_mode=aobmc:vsbmc=1:fps=120'" output.mkv
```

**Make Preview:**
Adjust `$N` and `$F` by dividing `N/F` to approximate the length of the video
```
Source: https://trac.ffmpeg.org/wiki/Create%20a%20thumbnail%20image%20every%20X%20seconds%20of%20the%20video#thumbnailvideofilter
Pick one of the most representative frames in sequences of $N consecutive frames:
ffmpeg -i input.flv -vf thumbnail=n=$N thumb%04d.png

Source: https://trac.ffmpeg.org/wiki/Slideshow#Sequential
Make Slideshow
ffmpeg -framerate $F -i img%03d.png output.mp4
```

## Audio

Copy audio stream without re-encoding
Source: https://stackoverflow.com/a/27413824
```
ffmpeg -i input-video.avi -vn -acodec copy output-audio.aac
```

Extract audio with re-encoding
Source: 
```
ffmpeg -i sample.avi -q:a 0 -map a sample.mp3
```