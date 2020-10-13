filename ='dvSave-2020_09_22_19_12_40.mat';
s = load(filename);
writerObj = VideoWriter(['luna', '.mp4'],'MPEG-4');
writerObj.FrameRate = 100; % How many frames per second.
open(writerObj);
sample = s.aedat.data.frame.samples;
class(size(sample));
endtime = length(sample)
for i = 1:endtime % run through data in milliseconds steps
    figure(1)
    text(10,10,[num2str(i) ' ms  '],'Color','g')
    hold off
    image(sample(:,:,i));
    %imshow(image);
    hold on;
    frame = getframe(gcf)
    writeVideo(writerObj, frame);
end

close(writerObj);
size(sample(:,:,1));
image(sample(:,:,50));