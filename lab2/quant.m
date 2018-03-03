function NewSignal = quant(signal, bits)
%Quant   Quantizes signal
%   Detailed explanation goes here

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
    elem_quant = min(signal) + index*step_size + step_size/2;
    if elem_quant < lower_limit
        elem_quant = lower_limit;
     end
    NewSignal(i) = elem_quant;
end


