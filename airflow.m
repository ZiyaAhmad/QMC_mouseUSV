function airflow = airflow(pressure,glottal_area)

room_pressure = 101.325; %normal air pressure in Pa.

air_density = 1.225; % kg/m3

tracheal_area = 0.95e-6; % m^2 from CT scan measurment

tracheal_diameter = 2 * sqrt(tracheal_area/pi);
glottal_diameter = 2 * sqrt(glottal_area/pi);

beta = glottal_diameter/tracheal_diameter; %ratio between diameters

%calculated based on assumed no obstruction. A bit off but we need
%approximation to get Reynolds number
% Note that we assume the glottal pressure to be higher than room pressure,
% if not we assume the pressure to be just slightly higher. That is to say,
% for subglottal pressure lower than room pressure, this functino does not
% make sense.
jet_speed = sqrt(2*(max(pressure - room_pressure,0.000001))./(air_density*(1 - beta.^4)));

kinematic_viscosity_air = 1.5111e-5; %assuming room temp, 20 degrees Celsius

Re = jet_speed*tracheal_diameter/kinematic_viscosity_air; %Reynolds Number (in pipe)

% discharge coefficient (Y. A. Çengel, J. M. Cimbala, Fluid Mechanics, 3rd Ed. New York: McGraw-Hill; 2014)
% online at
% https://www.academia.edu/17118844/Fluid_Mechanics_Fundamentals_and_Applications,
% see page 396, orifice meter
Cd = 0.5959 + 0.0312 * beta.^2.1 - 0.18 * beta.^8 + 91.71*beta.^2.5./(Re.^0.75);

airflow = glottal_area .* Cd .* jet_speed;

end