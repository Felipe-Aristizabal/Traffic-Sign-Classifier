CREATE DATABASE IF NOT EXISTS classifier;
USE classifier;

CREATE TABLE IF NOT EXISTS signals(signal_id VARCHAR(10) PRIMARY KEY,signal_name VARCHAR(15) NOT NULL,
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP);

CREATE TABLE IF NOT EXISTS register_classification(register_id INT PRIMARY KEY AUTO_INCREMENT, signal_id VARCHAR(10) NOT NULL,
 created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, correct_predict TINYINT(0) NOT NULL,
 FOREIGN KEY(signal_id) REFERENCES signals(signal_id));

SELECT * FROM classifier.register_classification;
SELECT * FROM classifier.signals;

INSERT INTO classifier.signals VALUES ('1KfqyZXON3','Speed',default,default);
INSERT INTO classifier.signals VALUES ('5dOFzZcPq0','Stop',default,default);
INSERT INTO classifier.signals VALUES ('LuvxpGCPes','Traffic light',default,default);

INSERT INTO register_classification VALUES(default,'LuvxpGCPes',default, 1);

# DROP TABLE signals;
# DROP TABLE register_classification;
# DROP DATABASE classifier;