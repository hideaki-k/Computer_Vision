function cmap = camvidColorMap()
% Define the colormap used by CamVid dataset.

cmap = [
    0 0 255 % NotSafe
    255 0 0 % Safe
    ];

% Normalize between [0 1].
cmap = cmap ./ 255;
end