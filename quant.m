function NewSignal = quant(signal, bits)
%Quant   Quantizes signal
%   Detailed explanation goes here
%step_size = (max(signal) - min(signal))/power(2,bits);
%steps = power(2,bits);
%upper_limit = (1 - step_size/2);
%lower_limit = -(1 - step_size/2);

%for idx = 1:numel(signal)
 %   element = signal(idx)
  %  element * step_size
    
%end

levels = power(2, bits);
step_size = (max(signal) - min(signal)) / levels;
lower_limit = -(1 - step_size/2);
L = length(signal);
NewSignal = zeros(1,L);
for i = 1:L
    index = round((signal(i) - lower_limit)/step_size);
    if index >= levels
        index = levels - 1;
    end
    xq = min(signal) + index*step_size + step_size/2;
    if xq < lower_limit
        xq = lower_limit;
     end
    NewSignal(i) = xq;
end


