


function slidingwindow(img,imgName)

img = imread(img);
size(img)


height = size(img,1);
width =size(img,2);
imgsize = size(img);
F = 480;
count = 0
imgName
%saveloc = 'C:\Users\aki\Documents\GitHub\Computer_Vision\matlab\divide_img\save_loc';
save_loc = 'C:\Users\aki\Documents\GitHub\Computer_Vision\matlab\divide_img\divided_img';
for h = F/2:100:height-(F/2)
    for w = F/2:100:width-(F/2)
        count = count + 1;
        roi = img(h-(F/2)+1:h+(F/2), w-(F/2)+1:w+(F/2),:);
        fileName = [save_loc, '\img', imgName,'_',int2str(count), '.jpg']; 
        imwrite(roi, fileName) 
    end
end

end