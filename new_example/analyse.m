addpath ~/daredevil/multi-rtl/examples/utils/
ch0=read_complex_binary('ch0.cfile');
ch1=read_complex_binary('ch1.cfile');


c=3e8;
f0 = 88.8e6;
maxrange = 100e3;
maxvel = 500/3.6;
maxdoppler = (c+maxvel)/c*f0 - f0;

maxdelay = maxrange / c;

fs = 200e3;
len = min([length(ch0), length(ch1)]);

maxshift = round(maxdelay * fs);
maxtrans = round(maxdoppler / (fs / len));

CH0=fft(ch0);
CH1=fft(ch1);

out = zeros(2 * maxtrans + 1, 2 * maxshift + 1);

for i=-maxtrans:maxtrans,
  ch1s = CH1;
  if (i<0)
    ch0s = [CH0(-i+1:end).'; zeros(-i, 1)];
  else
    ch0s = CH0.';
  end

  if (i>0)
    ch1s = [CH1(i+1:end).'; zeros(i, 1)];
  else
    ch1s = CH1.';
  end

  CORR = ch0s .* conj(ch1s);
  corr = ifft(CORR);

  out(i + maxtrans + 1, :) = [corr(end-maxshift : end)', corr(1:maxshift)'];
  imagesc(abs(out));
  pause(0.001);
end
