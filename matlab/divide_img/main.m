%イメージをスライディングウィンドウで分割

% slidingwindow('sh_20081102T071400_wm8_fp_l.jpg' ,'sh_20081102T071400_wm8_fp_l');

% 以下安全領域判定
% カレントフォルダ内の *.jpg ファイル一覧をテーブル形式で取得

path = 'imgsh_20081102T071400_wm8_fp_l_1.jpg'
test = imread(path);
path_ = 'sh_20081102T071400_wm8_fp_l.jpg';
test_ = imread(path_);
size(test_)
size(test)
fileList = struct2table(dir('divided_img/*.png'));
img_num = size(fileList,1)
% テーブル内の、更新日時が最新の画像の行番号を取得
[~, idx] = max(fileList.datenum);
% 対象画像を読み込み
I = imread(fullfile(fileList.folder{idx},fileList.name{idx}));
load_loc = 'divided_img\'
for i = 1:img_num
    fileList.name{i};
    I = imread(fullfile(fileList.folder{i},fileList.name{i}));
    add_label(load_loc,fileList.name{i});
end