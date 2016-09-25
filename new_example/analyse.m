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

maxshift = maxdelay * fs;
maxtrans = maxdoppler / (fs / len);

%CH0=fft(ch0);
%CH1=fft(ch1);
