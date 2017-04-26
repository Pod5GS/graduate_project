#!/bin/bash
cd sceneparsing
export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libopencv_highgui.so.2.4:/usr/lib/x86_64-linux-gnu/libopencv_imgproc.so.2.4:/usr/lib/x86_64-linux-gnu/libopencv_core.so.2.4:/usr/lib/x86_64-linux-gnu/libstdc++.so.6:/usr/lib/x86_64-linux-gnu/libfreetype.so.6
export LD_LIBRARY_PATH=/usr/lib/x86_64-linux-gnu/
matlab -nodesktop -nosplash -r "imgName='$1';demoSegmentation;exit"
