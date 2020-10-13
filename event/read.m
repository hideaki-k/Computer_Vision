filename ='dvSave-2020_09_22_19_12_40.mat';
s = load(filename);

sample = s.aedat.data.frame.samples;
size(sample)
size(sample(:,:,1))
image(sample(:,:,50))

polarity_x = s.aedat.data.polarity.x;
size(polarity_x)

disp('=====================================')
polarity_x = s.aedat.data.polarity.x(1:1000000);
polarity_x = cast(polarity_x,'uint64')

polarity_y = s.aedat.data.polarity.y(1:1000000);
polarity_y = cast(polarity_y,'uint64')

T = cast(s.aedat.data.polarity.timeStamp(1:1000000),'uint64')
pol = s.aedat.data.polarity.polarity(1:1000000);
pol = cast(pol,'uint64')

polarity_x = rot90(polarity_x,-1);
polarity_y = rot90(polarity_y,-1);
pol = rot90(pol,-1);
T = rot90(T,-1) - 2560549996;



events = horzcat(polarity_x, polarity_y, pol, T);

save('myFile.mat','events')

disp(' ============')



%save('myFile.mat','events','-v7.3','-nocompression')
% size(polarity_x)
% disp(polarity_x)


% polarity_y = s.aedat.data.polarity.y;
% plot(polarity_x,polarity_y)
% X = s.aedat.data.polarity.x
% Y = s.aedat.data.polarity.y
% T = s.aedat.data.polarity.timeStamp
% plot3(T,X,Y,'.','MarkerSize',0.1)