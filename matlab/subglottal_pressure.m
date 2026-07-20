function subglottal_pressure = subglottal_pressure(respiratory_muscle_activity)

pressure_max = 2e3;
room_pressure = 101.325; %normal air pressure in Pa.
pressure_min = room_pressure;

subglottal_pressure = pressure_min+respiratory_muscle_activity*(pressure_max-pressure_min);

end