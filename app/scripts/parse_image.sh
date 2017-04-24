#!/bin/bash
cd ../sceneparsing
matlab -nodesktop -nosplash -r "imgName='$1';demoSegmentation;exit"