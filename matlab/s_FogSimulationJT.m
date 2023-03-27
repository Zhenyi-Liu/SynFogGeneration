%% JT simulation

% Fog free images
inputImage = fullfile(fogsimRootPath, 'data/clear.png');
img = imread(inputImage);

% Estimate ambient light level using dark channel
airlight = estimateA(inputImage);
A = repmat(airlight,1,3);

% medium attenuation coeffcient (extinction = scattering + absorption)
beta = 0.1;

% Load depth map
depth_path = fullfile(fogsimRootPath, 'data/Image_Depth0001.exr');
depth = exrread(depth_path);
depth = depth(:,:,1);

I0 = double(img) / 255.0;
I1 = zeros([size(depth,1), size(depth,2), 3], "single");
transmission = zeros([size(depth,1), size(depth,2)], "single");

for c = 1:3
    transmission = exp(-beta .* depth);
    I1(:, :, c) = I0(:, :, c) .* transmission + A(c) .* (1 - transmission);
end

output_path = fullfile(fogsimRootPath, 'local/foggy_0_1.png');

imwrite(uint8(I1 * 255), output_path);