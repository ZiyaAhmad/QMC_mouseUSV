%% glottal area as a function of CT and TA activity (0 to 1)
function glottal_area = glottal_area(PCAIA_activity, TA_activity)

area_cart_max = 0.375e-6; % m^2 from CT scan measurment

area_memb_max = 0.7e-6; % m^2 from CT scan measurment

area_cart = area_cart_max * (1-PCAIA_activity);
area_memb = area_memb_max * (1- TA_activity);

glottal_area = area_cart + area_memb;
end