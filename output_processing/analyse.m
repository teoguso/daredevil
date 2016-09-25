# a checkout of this repo: https://github.com/ptrkrysik/multi-rtl
addpath ../../multi-rtl/examples/utils/

ch0=read_complex_binary('../data/ch0.cfile');
ch1=read_complex_binary('../data/ch1.cfile');


c=3e8;
f0 = 88.8e6;
maxrange = 100e3;
maxvel = 500/3.6;
maxdoppler = (c+maxvel)/c*f0 - f0
len = length(ch0)

maxdelay = maxrange / c;

fs = 200e3

maxshift = round(maxdelay * fs);
maxtrans = round(maxdoppler / (fs / len))

out = zeros(2 * maxtrans + 1, 2 * maxshift + 1);
CH0=fft(ch0);
CH1=fft(ch1);

for i=-maxtrans:maxtrans,

CORR = CH0 .* conj(shift(CH1, i));
corr = ifft(CORR);

out(i + maxtrans + 1, :) = [corr(end-maxshift : end), corr(1:maxshift)];
end
image(abs(out)/100);
pause(10)
