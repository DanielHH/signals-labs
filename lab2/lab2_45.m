T=2.5;              % Tidsutbredning
fs=4e4;             % Samplingsfrekvens
N=T*fs;             % Antal sampel
n=0:N-1;            % Vektor med sampelindex
t=1/fs*n;           % Vektor med sampeltidpunkter
f1=8000;            % signalens frekvens
x1=sin(2*pi*f1*t);  % Vektor med alla sampel
f2=8017;
x2=sin(2*pi*f2*t);

s1 = fs/f1;
s2 = fs/f2;

f=fs/N*n;


for i = 1:8
    y=downsample(x1,i);
    f1=downsample(f,i);
    subplot(2,4,i);
    plot(f1/i, db(abs(fft(y))));
    title("n = " + i);
end

for i = 1:8
    y=downsample(x1,i);
    f1=downsample(f,i);
    subplot(2,4,i);
    
    plot(f1(1:lengt, db(abs(fft(y))));
    title("n = " + i);
end
