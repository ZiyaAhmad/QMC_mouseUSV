function jet_speed = jet_speed(glottal_area, airflow_or_pressure, f_or_p_flag) 

if(f_or_p_flag == 'p')
    pressure = airflow_or_pressure;
    tracheal_area = 0.95e-6; %m^2
    tracheal_diameter = 2 * sqrt(tracheal_area/pi);
    glottal_diameter = 2 * sqrt(glottal_area/pi);

    beta = glottal_diameter/tracheal_diameter;
    
    room_pressure = 101.325; %normal air pressure in Pa.

    air_density = 1.225; % kg/m3
    
    %calculated based on assumed no obstruction 
    jet_speed = sqrt(2*(max(pressure - room_pressure,0.000001))/(air_density*(1 - beta^4)));
    
elseif (f_or_p_flag == 'f')
    airflow = airflow_or_pressure;
    %
    jet_speed = airflow./glottal_area;
end
