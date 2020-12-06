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

%テンプレートマッチングは回転に弱いらしい（最初に回転させてテンプレートを用意したりするらしい）