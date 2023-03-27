function A_mean = estimateA(fname)
%% Estimate mean atomospheric light from input images

% fname = './0324/test.png';
img = imread(fname);
I = im2double(img);
dark = DarkChannel(I, 15);
A = AtmLight(I, dark);
A_mean = mean(A);
disp(A_mean);


    function dark = DarkChannel(im, sz)
        rgb = im;
        dc = min(rgb, [], 3);
        kernel = strel('rectangle', [sz sz]);
        dark = imerode(dc, kernel);
    end

    function A = AtmLight(im, dark)
        [h, w, ~] = size(im);
        imsz = h * w;
        numpx = max(floor(imsz/1000), 1);
        darkvec = dark(:);
        imvec = reshape(im, imsz, 3);

        [~, indices] = sort(darkvec, 'descend');
        indices = indices(1:numpx);

        atmsum = sum(imvec(indices, :), 1);
        A = atmsum / numpx;
    end

end