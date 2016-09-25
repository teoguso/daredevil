addpath ~/daredevil/multi-rtl/examples/utils/

out = zeros(2 * maxtrans + 1, 2 * maxshift + 1);

for iter=1:100,
  system('./mutlirtl_rx_to_cfile_2chan.py');
  ch0=read_complex_binary('ch0.cfile');
  ch1=read_complex_binary('ch1.cfile');
  
  
  c=3e8;
  f0 = 88.8e6;
  maxrange = 100e3;
  maxvel = 500/3.6;
  maxdoppler = (c+maxvel)/c*f0 - f0;

  maxdelay = maxrange / c;

  fs = 200e3;

  len=min([length(ch0), length(ch1)]);
  ch0=ch0(1:len);
  ch1=ch1(1:len);

  maxshift = round(maxdelay * fs);
  maxtrans = round(maxdoppler / (fs / len));

  CH0=fft(ch0);
  CH1=fft(ch1);

  for i=-maxtrans:maxtrans,

    CORR = CH0 .* conj(shift(CH1, i));
    corr = ifft(CORR);

    out(i + maxtrans + 1, :) = [corr(end-maxshift : end), corr(1:maxshift)];
    image(abs(out)/10);
    pause(0.001);
  end
end
