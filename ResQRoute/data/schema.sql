-- 1. Citizens
CREATE TABLE citizens (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    phone VARCHAR(15),
    location_lat DOUBLE,
    location_lon DOUBLE,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 2. Vehicles
CREATE TABLE vehicles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    vehicle_id VARCHAR(50) NOT NULL,
    vehicle_type VARCHAR(50) NOT NULL,      -- 'Ambulance', 'Fire', 'Police'
    status VARCHAR(50) DEFAULT 'Available',  -- 'Available','En route','On duty'
    location_lat DOUBLE,
    location_lon DOUBLE
);

-- 3. Drivers
CREATE TABLE drivers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    vehicle_id INT,
    FOREIGN KEY (vehicle_id) REFERENCES vehicles(id)
);

-- 4. Emergencies
CREATE TABLE emergencies (
    id INT AUTO_INCREMENT PRIMARY KEY,
    citizen_id INT,
    emergency_type VARCHAR(50),              -- 'Medical','Fire','Crime'
    requested_vehicle VARCHAR(50),           -- 'Ambulance','Fire','Police'
    location_lat DOUBLE,
    location_lon DOUBLE,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(50) DEFAULT 'Pending',    -- 'Pending','Assigned','In Progress'
    FOREIGN KEY (citizen_id) REFERENCES citizens(id)
);

-- 5. Tasks (assignments)
CREATE TABLE tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    emergency_id INT,
    driver_id INT,
    assigned_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(50) DEFAULT 'Assigned',  -- 'Assigned','In Progress','Completed'
    FOREIGN KEY (emergency_id) REFERENCES emergencies(id),
    FOREIGN KEY (driver_id) REFERENCES drivers(id)
);

-- 6. Signals Configuration
CREATE TABLE signals (
    id INT AUTO_INCREMENT PRIMARY KEY,
    signal_code VARCHAR(50) NOT NULL,        -- e.g. 'SG101'
    location_lat DOUBLE,
    location_lon DOUBLE,
    current_state VARCHAR(10) DEFAULT 'RED', -- 'RED','GREEN','YELLOW'
    green_duration INT DEFAULT 60,            -- seconds when green
    yellow_duration INT DEFAULT 5,            -- seconds when yellow
    red_duration INT DEFAULT 55,              -- seconds when red
    last_override TIMESTAMP
);

-- 7. Signal Override Logs
CREATE TABLE signal_logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    signal_id INT,
    override_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    new_state VARCHAR(10),                   -- 'RED','GREEN','YELLOW'
    overridden_by VARCHAR(100),              -- e.g. 'ControlRoomUser123'
    FOREIGN KEY (signal_id) REFERENCES signals(id)
);
