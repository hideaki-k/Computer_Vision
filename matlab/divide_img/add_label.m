function add_label(load_loc,img)

inputfileName = [load_loc,img];
%img_bgr = imread(inputfileName);

img_ = imread(inputfileName);
img_ = im2gray(img_);

% img_ = imresize(img_,[512,512]);
% img = rgb2gray(img_bgr);
% img = imresize(img,[512,512]);
%imshow(img)
height = size(img_,1);
width =size(img_,2);
mu = mean2(img);
img = double(img);
sigma = var(img(:));
%sigma = std2(img);

img_suihei = zeros(height,width);
img_heitan = zeros(height,width);
F = 16;

for h = F/2:1:height-(F/2)
    for w = F/2:1:width-(F/2)
%         h-(F/2),h+(F/2);
        roi = img_(h-(F/2)+1:h+(F/2), w-(F/2)+1:w+(F/2));
%         imshow(roi)
        mu_ = mean2(roi);
        roi = double(roi);
        sigma_ = var(roi(:));
        %sigma_ = std2(roi);
        roi_mu = (mu_-mu)/sqrt(sigma);
        roi_s = sqrt(sigma_)/sqrt(sigma);
        img_suihei(h,w) = abs(roi_mu);
        img_heitan(h,w) = roi_s; % 平坦度

        size(roi);
    end
    
end

img_suihei_binary = zeros(height,width,3);
img_heitan_binary = zeros(height,width,3);

c = 0.5
Vthm = mean2(img_suihei) %　水平度（輝度平均）
Vths = c*mean2(img_heitan) %　平坦度（分散）0.2953

for h = F/2:1:height-(F/2)
    for w = F/2:1:width-(F/2)
        heitan_roi = img_heitan(h-(F/2)+1:h+(F/2), w-(F/2)+1:w+(F/2));
        suihei_roi = img_suihei(h-(F/2)+1:h+(F/2), w-(F/2)+1:w+(F/2));
%         img_heitan(h,w)
        if img_heitan(h,w) <= Vths
            img_heitan_binary(h,w,:) = 255;
        end
        if abs(img_suihei(h,w)) < Vthm
            img_suihei_binary(h,w,:) = 255;
        end
    end
end

img_bgr = zeros(height,width,3);
img_bgr(:,:,:) =  0 ;

sliderBW = ((img_suihei_binary==255) & (img_heitan_binary==255));
BW = sliderBW;

size(BW)

img_bgr(repmat(~BW,[1 1 1])) = 255;
% newmap = jet;
% disp('fin')
% subplot(1,3,1)
% imshow(img_suihei_binary,'Colormap',newmap)
% title('suihei Image')
% subplot(1,3,2)
% imshow(img_heitan_binary,'Colormap',newmap)
% title('heitan Image')
% subplot(1,3,3)
% imshow(img_)
% title('img')
save_loc = 'C:\Users\aki\Documents\GitHub\Computer_Vision\matlab\divide_img\label_img\';
fileName = [save_loc, img]; 
imwrite(img_bgr,fileName);
end