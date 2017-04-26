% This script demos how to use the pre-trained models to
% obtain the predicted segmentations
addpath(genpath('visualizationCode'));


% path to caffe (compile matcaffe first, or you could use python wrapper instead)
addpath '/home/andywei/caffe/matlab' 

% select the pre-trained model. Use 'FCN' for 
% the Fully Convolutional Network or 'Dilated' for DilatedNet
% You can download the FCN model at 
% http://sceneparsing.csail.mit.edu/model/FCN_iter_160000.caffemodel
% and the DilatedNet model at
% http://sceneparsing.csail.mit.edu/model/DilatedNet_iter_120000.caffemodel
model_type = 'FCN'; %Dilated'
if (strcmp(model_type, 'FCN'))
	model_definition = 'models/deploy_FCN.prototxt';
	model_weights = 'models/FCN_iter_160000.caffemodel';
elseif (strcmp(model_type, 'Dilated')) 
	model_definition = 'models/deploy_DilatedNet.prototxt';
	model_weights = 'DilatedNet_iter_120000.caffemodel';
end
disp(model_definition)

% initialize the network
net = caffe.Net(model_definition, model_weights, 'test');

% path to image(.jpg)
pathImg = fullfile('data');

% load class names
load('objectName150.mat');

% load pre-defined colors 
load('color150.mat');

% read image
fileImg = fullfile(pathImg, imgName);

im = imread(fileImg);
  	
% resize image to fit model description
im_inp = double(imresize(im, [384,384]));

% change RGB to BGR
im_inp = im_inp(:,:,end:-1:1);

% substract mean and transpose
im_inp = cat(3, im_inp(:,:,1)-109.5388, im_inp(:,:,2)-118.6897, im_inp(:,:,3)-124.6901);
im_inp = permute(im_inp, [2,1,3]);

% obtain predicted image and resize to original size
imPred = net.forward({im_inp});
[~, imPred] = max(imPred{1},[],3);
imPred = uint8(imPred')-1;
imPred = imresize(imPred, [size(im,1), size(im,2)], 'nearest');
 
% color encoding
rgbPred = colorEncode(imPred, colors);
 
% colormaps
colormap = colorMap(imPred, objectNames);
    
imwrite(colormap,'../app/static/result/colormap.png');
imwrite(rgbPred,'../app/static/result/prediction.png');
