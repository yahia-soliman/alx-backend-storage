-- Add user correction into the database
-- set custom delimeter
DELIMITER //

-- adds new correction for a student
CREATE PROCEDURE AddBonus (
         IN user_id INT,
         IN project_name VARCHAR(255),
         IN score INT
       )
BEGIN
  DECLARE project_id INT;

  -- get the project id
  set project_id = (SELECT id FROM projects WHERE name = project_name);

  -- create the project if it does not exists
  IF IF(project_id, 0, 1) THEN
    INSERT INTO projects (name)
    VALUES               (project_name);
    SET project_id = LAST_INSERT_ID();
  END IF;

  -- create the correction row
  INSERT INTO corrections (user_id, project_id, score)
  VALUES                  (user_id, project_id, score);

END //

-- reset the delimeter
DELIMITER ;
