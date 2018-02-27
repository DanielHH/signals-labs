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
%M=500;
%w=[zeros(1,floor((N-M)/2)),rectwin(M)',zeros(1,ceil((N-M)/2))];
%maxY = max(db(abs(fft(w))));
%plot(f, db(abs(fft(w))));

figure;
xlim([3000 5000]);
x=sin(2*pi*3999*(1+5e-7*cos(2*pi*100*t)).*t)+sin(2*pi*4099*t)+1e-3*sin(2*pi*4400*t);
plot(f, db(abs(fft(x))));
xlim([3000,5000]);


M1=500;

subplot(3,6,1);
w1=[zeros(1,floor((N-M1)/2)),rectwin(M1)',zeros(1,ceil((N-M1)/2))];
x=sin(2*pi*3999*(1+5e-7*cos(2*pi*100*t)).*t)+sin(2*pi*4099*t)+1e-3*sin(2*pi*4400*t);
plot(f, db(abs(fft(x.*w1))));
xlim([3000,5000]);

subplot(3,6,2);
w2=[zeros(1,floor((N-M1)/2)),hamming(M1)',zeros(1,ceil((N-M1)/2))];
x=sin(2*pi*3999*(1+5e-7*cos(2*pi*100*t)).*t)+sin(2*pi*4099*t)+1e-3*sin(2*pi*4400*t);
plot(f, db(abs(fft(x.*w2))));
xlim([3000,5000]);

subplot(3,6,3);
w3=[zeros(1,floor((N-M1)/2)),nuttallwin(M1)',zeros(1,ceil((N-M1)/2))];
x=sin(2*pi*3999*(1+5e-7*cos(2*pi*100*t)).*t)+sin(2*pi*4099*t)+1e-3*sin(2*pi*4400*t);
plot(f, db(abs(fft(x.*w3))));
xlim([3000,5000]);

M2=1000;

subplot(3,6,4);
w4=[zeros(1,floor((N-M2)/2)),rectwin(M2)',zeros(1,ceil((N-M2)/2))];
x=sin(2*pi*3999*(1+5e-7*cos(2*pi*100*t)).*t)+sin(2*pi*4099*t)+1e-3*sin(2*pi*4400*t);
plot(f, db(abs(fft(x.*w4))));
xlim([3000,5000]);

subplot(3,6,5);
w5=[zeros(1,floor((N-M2)/2)),hamming(M2)',zeros(1,ceil((N-M2)/2))];
x=sin(2*pi*3999*(1+5e-7*cos(2*pi*100*t)).*t)+sin(2*pi*4099*t)+1e-3*sin(2*pi*4400*t);
plot(f, db(abs(fft(x.*w5))));
xlim([3000,5000]);

subplot(3,6,6);
w6=[zeros(1,floor((N-M2)/2)),nuttallwin(M2)',zeros(1,ceil((N-M2)/2))];
x=sin(2*pi*3999*(1+5e-7*cos(2*pi*100*t)).*t)+sin(2*pi*4099*t)+1e-3*sin(2*pi*4400*t);
plot(f, db(abs(fft(x.*w6))));
xlim([3000,5000]);

M3=2000;

subplot(3,6,7);
w7=[zeros(1,floor((N-M3)/2)),rectwin(M3)',zeros(1,ceil((N-M3)/2))];
x=sin(2*pi*3999*(1+5e-7*cos(2*pi*100*t)).*t)+sin(2*pi*4099*t)+1e-3*sin(2*pi*4400*t);
plot(f, db(abs(fft(x.*w7))));
xlim([3000,5000]);

subplot(3,6,8);
w8=[zeros(1,floor((N-M3)/2)),hamming(M3)',zeros(1,ceil((N-M3)/2))];
x=sin(2*pi*3999*(1+5e-7*cos(2*pi*100*t)).*t)+sin(2*pi*4099*t)+1e-3*sin(2*pi*4400*t);
plot(f, db(abs(fft(x.*w8))));
xlim([3000,5000]);

subplot(3,6,9);
w9=[zeros(1,floor((N-M3)/2)),nuttallwin(M3)',zeros(1,ceil((N-M3)/2))];
x=sin(2*pi*3999*(1+5e-7*cos(2*pi*100*t)).*t)+sin(2*pi*4099*t)+1e-3*sin(2*pi*4400*t);
plot(f, db(abs(fft(x.*w9))));
xlim([3000,5000]);



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


%{
M=2000;
fq=0:fs/M:fs*(1-1/M);

x=sin(2*pi*3999*(1+5e-7*cos(2*pi*100*t)).*t)+sin(2*pi*4099*t)+1e-3*sin(2*pi*4400*t);

lzer = zeros(1,floor((N-M)/2));
win = nuttallwin(M)';
xfiltered=x(length(lzer):length(lzer)+M-1);

plot(fq, db(abs(fft(xfiltered.*win))));
xlim([3000,5000]);
%}
%%%%%%%%%%%%%%%%


%%% 1 %%%
x=sin(2*pi*3999*(1+5e-7*cos(2*pi*100*t)).*t)+sin(2*pi*4099*t)+1e-3*sin(2*pi*4400*t);

%%% 2 %%%
M1=500;
fq1=0:fs/M1:fs*(1-1/M1);

lzer1 = zeros(1,floor((N-M1)/2));
xfilt1=x(length(lzer):length(lzer)+M1-1);

subplot(3,6,10);
w10 = rectwin(M1)';
plot(fq1, db(abs(fft(xfilt1.*w10))));
xlim([3000,5000]);

subplot(3,6,11);
w11 = hamming(M1)';
plot(fq1, db(abs(fft(xfilt1.*w11))));
xlim([3000,5000]);

subplot(3,6,12);
w12 = nuttallwin(M1)';
plot(fq1, db(abs(fft(xfilt1.*w12))));
xlim([3000,5000]);

%%%%%

M2=1000;
fq2=0:fs/M2:fs*(1-1/M2);

lzer2 = zeros(1,floor((N-M2)/2));
xfilt2=x(length(lzer):length(lzer)+M2-1);

subplot(3,6,13);
w13 = rectwin(M2)';
plot(fq2, db(abs(fft(xfilt2.*w13))));
xlim([3000,5000]);

subplot(3,6,14);
w14 = hamming(M2)';
plot(fq2, db(abs(fft(xfilt2.*w14))));
xlim([3000,5000]);

subplot(3, 6, 15);
w15 = nuttallwin(M2)';
plot(fq2, db(abs(fft(xfilt2.*w15))));
xlim([3000,5000]);

%%%%%

M3=2000;
fq3=0:fs/M3:fs*(1-1/M3);

lzer3 = zeros(1,floor((N-M3)/2));
xfilt3=x(length(lzer):length(lzer)+M3-1);

subplot(3,6,16);
w16 = rectwin(M3)';
plot(fq3, db(abs(fft(xfilt3.*w16))));
xlim([3000,5000]);

subplot(3,6,17);
w17 = hamming(M3)';
plot(fq3, db(abs(fft(xfilt3.*w17))));
xlim([3000,5000]);

subplot(3, 6, 18);
w18 = nuttallwin(M3)';
plot(fq3, db(abs(fft(xfilt3.*w18))));
xlim([3000,5000]);

%{
figure;
w2=[zeros(1,floor((N-M1)/2)),hamming(M1)',zeros(1,ceil((N-M1)/2))];
x=sin(2*pi*3999*(1+5e-7*cos(2*pi*100*t)).*t)+sin(2*pi*4099*t)+1e-3*sin(2*pi*4400*t);
plot(f, db(abs(fft(x.*w2))));
xlim([3000,5000]);

figure;
w3=[zeros(1,floor((N-M1)/2)),nuttallwin(M1)',zeros(1,ceil((N-M1)/2))];
x=sin(2*pi*3999*(1+5e-7*cos(2*pi*100*t)).*t)+sin(2*pi*4099*t)+1e-3*sin(2*pi*4400*t);
plot(f, db(abs(fft(x.*w3))));
xlim([3000,5000]);

M2=1000;

figure;
w4=[zeros(1,floor((N-M2)/2)),rectwin(M2)',zeros(1,ceil((N-M2)/2))];
x=sin(2*pi*3999*(1+5e-7*cos(2*pi*100*t)).*t)+sin(2*pi*4099*t)+1e-3*sin(2*pi*4400*t);
plot(f, db(abs(fft(x.*w4))));
xlim([3000,5000]);

figure;
w5=[zeros(1,floor((N-M2)/2)),hamming(M2)',zeros(1,ceil((N-M2)/2))];
x=sin(2*pi*3999*(1+5e-7*cos(2*pi*100*t)).*t)+sin(2*pi*4099*t)+1e-3*sin(2*pi*4400*t);
plot(f, db(abs(fft(x.*w5))));
xlim([3000,5000]);

figure;
w6=[zeros(1,floor((N-M2)/2)),nuttallwin(M2)',zeros(1,ceil((N-M2)/2))];
x=sin(2*pi*3999*(1+5e-7*cos(2*pi*100*t)).*t)+sin(2*pi*4099*t)+1e-3*sin(2*pi*4400*t);
plot(f, db(abs(fft(x.*w6))));
xlim([3000,5000]);

M3=2000;

figure;
w7=[zeros(1,floor((N-M3)/2)),rectwin(M3)',zeros(1,ceil((N-M3)/2))];
x=sin(2*pi*3999*(1+5e-7*cos(2*pi*100*t)).*t)+sin(2*pi*4099*t)+1e-3*sin(2*pi*4400*t);
plot(f, db(abs(fft(x.*w7))));
xlim([3000,5000]);

figure;
w8=[zeros(1,floor((N-M3)/2)),hamming(M3)',zeros(1,ceil((N-M3)/2))];
x=sin(2*pi*3999*(1+5e-7*cos(2*pi*100*t)).*t)+sin(2*pi*4099*t)+1e-3*sin(2*pi*4400*t);
plot(f, db(abs(fft(x.*w8))));
xlim([3000,5000]);

figure;
w9=[zeros(1,floor((N-M3)/2)),nuttallwin(M3)',zeros(1,ceil((N-M3)/2))];
x=sin(2*pi*3999*(1+5e-7*cos(2*pi*100*t)).*t)+sin(2*pi*4099*t)+1e-3*sin(2*pi*4400*t);
plot(f, db(abs(fft(x.*w9))));
xlim([3000,5000]);
%}


