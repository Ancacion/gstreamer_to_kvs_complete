import cv2
import os
import gstreamer_config

def gstreamer_pipline():
    pipeline = gstreamer_config.enviroment + ' && gst-launch-1.0 v4l2src device=/dev/video0 ! decodebin ! tee name=t t. ! queue ! x264enc bframes=0 key-int-max=45 bitrate=1024 ! video/x-h264,stream-format=avc,alignment=au,profile=baseline ! kvssink stream-name="' + gstreamer_config.kvs_stream_name + '" storage-size=512 access-key="' + gstreamer_config.kvs_access_key + '" secret-key="' + gstreamer_config.kvs_secret_key + '" aws-region="' + gstreamer_config.kvs_region_service + '" t.! queue ! x264enc bframes=0 speed-preset=veryfast bitrate=1024 byte-stream=TRUE tune=zerolatency ! video/x-h264,stream-format=byte-stream,alignment=au,profile=baseline ! appsink sync=TRUE emit-signals=TRUE name=appsink-video t. ! queue ! videorate ! jpegenc quality=400 ! multifilesink location=stream_image.jpg'

    return(pipeline)

if __name__=='__main__':

    os.system(gstreamer_pipline())
    
    




