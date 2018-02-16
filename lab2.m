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
%{
plot(t(1:s1*5+1), x1(1:s1*5+1), 'b-',t(1:s1*5+1), x1(1:s1*5+1), 'rx');
hold;
plot(t(1:s1*5+1), x2(1:s1*5+1), 'b-',t(1:s1*5+1), x2(1:s1*5+1), 'rx');
figure;
hist(x1, 100);
figure;
hist(x2, 100);
%}

f=fs/N*n;

%{
plot(f, abs(fft(x1)));
%axis([7950 8050 0 1000]); 
figure;
plot(f, abs(fft(x2)));
%axis([7950 8050 0 1000]); 

%logaritmisk skala (dB)
plot(f, db(abs(fft(x1))));
figure;
plot(f, db(abs(fft(x2))));
%}

