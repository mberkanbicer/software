function [ ambiguity ] = lfm_train( time_delay, doppler_frequency, pulse_width, bandwidth, pulse_repetition_interval, number_of_pulses )
%% Calculate the ambiguity function for an LFM pulse train.
%     :param time_delay: The time delay for the ambiguity function (seconds)
%     :param doppler_frequency: The Doppler frequency for the ambiguity function (Hz)
%     :param pulse_width: The waveform pulse width (seconds)
%     :param bandwidth: The waveform band width (Hz)
%     :param pulse_repetition_interval: The time between successive pulses (seconds)
%     :param number_of_pulses: The total number of pulses (unitless)
%     :return: The ambiguity function for an LFM pulse train (unitless)
%
%     Created by: Lee A. Harrison
%     On: 4/26/2019
%
% Copyright (C) 2019 Artech House (artech@artechhouse.com)
% This file is part of Introduction to Radar Using Python and MATLAB
% and can not be copied and/or distributed without the express permission of Artech House.

ambiguity = 0;

for q = -(number_of_pulses - 1):(number_of_pulses - 1)
    a1 = sqrt(lfm_pulse(time_delay - q * pulse_repetition_interval, doppler_frequency, pulse_width, bandwidth));    
    ambiguity = ambiguity + a1 .* abs(sin(pi * doppler_frequency * (number_of_pulses - abs(q)) * pulse_repetition_interval) ...
        ./ sin(pi * doppler_frequency * pulse_repetition_interval));    
end

ambiguity = abs(ambiguity / number_of_pulses) .^ 2;