ref = rgb2gray(imread('sansyou.jpg'));
template = rgb2gray(imread('template_45.jpg'));
montage({ref,template})
c = normxcorr2(template,ref);
surf(c)
shading flat

% [ypeak,xpeak] = find(c==max(c(:)));
% yoffSet = ypeak-size(template,1);
% xoffSet = xpeak-size(template,2);
% imshow(ref)
% drawrectangle(gca,'Position',[xoffSet,yoffSet,size(template,2),size(template,1)], ...
%     'FaceAlpha',0);

%�e���v���[�g�}�b�`���O�͉�]�Ɏア�炵���i�ŏ��ɉ�]�����ăe���v���[�g��p�ӂ����肷��炵���j