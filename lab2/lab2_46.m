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

plot(f, db(abs(fft(x2))));
figure;

for i = 2:2:8
    y=quant(x2,i);
    subplot(3,4,i/2);
    plot(f, db(abs(fft(y))));
    title("n = " + i);
    z = x2 - y;
    subplot(3,4,i/2+4);
    plot(f, db(abs(fft(z))));
    title("quant error for n= " + i);
    subplot(3,4,i/2+8)
    hist(z,100);
    title("hist for n = " + i);
end

