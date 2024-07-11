-- a procedure to update user's average score
-- set custom delimeter
DELIMITER //

-- calculate avg score for a user and update it
CREATE PROCEDURE ComputeAverageScoreForUser (IN u_id INT)
BEGIN
  UPDATE users
     SET average_score = (SELECT AVG(score) FROM corrections WHERE user_id = u_id)
   WHERE id = u_id;
END //

-- reset the delimeter
DELIMITER ;
