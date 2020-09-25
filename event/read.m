filename ='dvSave-2020_09_22_18_29_15.mat';
s = load(filename);
X = s.aedat.data.polarity.x
Y = s.aedat.data.polarity.y
T = s.aedat.data.polarity.timeStamp
plot3(T,X,Y,'.','MarkerSize',0.1)