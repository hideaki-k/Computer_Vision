I = imread('sansyou.jpg');
blockSize = [200 200];
blockproc(I, blockSize, @cropAndSaveBlock);


function cropAndSaveBlock(bs)
save_loc = pwd;
fileName = [save_loc, '/img', int2str(bs.location(1)),'_',int2str(bs.location(2)),'.jpg'];
imwrite(bs.data, fileName);
end