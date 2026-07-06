%% impinggement length as a function of CT activity (0 to 1)
function impingement_length = impingement_length(CT_activity, TA_activity)

length_max = 1.5e-3; %150% maximum measured

length_min = 0.1e-3; %50% minimum measured

impingement_length = length_min+(CT_activity-0.24*TA_activity)*(length_max-length_min);

end