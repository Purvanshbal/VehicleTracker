DELIMITER //
CREATE PROCEDURE GetBrandRating()
    BEGIN
        DECLARE b VARCHAR(255);
        DECLARE avprice REAL;
        DECLARE dc INT;
        DECLARE ac INT;
        DECLARE avcost REAL;
        DECLARE rate VARCHAR(1);
        DECLARE done int default 0;
        DECLARE cur CURSOR FOR Select Brand, avg(Price) as AveragePrice, avg(Average_maintenance_cost) as AverageCost From Vehicle NATURAL JOIN Compatible_With Group By Brand;
        DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;
        
        DROP TABLE IF EXISTS FinalTable;
        
        CREATE TABLE FinalTable(
            Brand_Name Varchar(255),
            Average_Price REAL,
            Average_brand_maintenance_cost REAL,
            Number_dc_compatible INT,
            Number_ac_compatible INT,
            Rating Varchar(1)
        );

        OPEN cur;
        
        REPEAT
            FETCH NEXT FROM cur INTO b, avprice, avcost;
            IF avprice >= 80000 OR avcost >= 900 THEN 
                SET rate = 'A';
            END IF;
            
            IF (avprice < 80000 AND avprice >= 60000) OR (avcost < 900 AND avcost >= 700) THEN   
                SET rate = 'B';
            END IF;
            
            IF (avprice < 60000 AND avprice >= 30000) OR (avcost < 700 AND avcost >= 500) THEN   
                SET rate = 'C';
            END IF;
           
            IF (avprice < 60000) OR (avcost < 500) THEN   
                SET rate = 'D';
            END IF;
            
            SELECT count(*) FROM Vehicle NATURAL JOIN Compatible_With WHERE Brand = b AND Charger_Type LIKE '%DC%' GROUP BY Brand  INTO dc;
            SELECT count(*) FROM Vehicle NATURAL JOIN Compatible_With WHERE Brand = b AND Charger_Type LIKE '%AC%' GROUP BY Brand INTO ac;
            INSERT INTO FinalTable VALUES(b, avprice, avcost, dc, ac, rate);
        UNTIL done
        END REPEAT;
        
        CLOSE cur;
        
        SELECT * From FinalTable ORDER BY Rating;

    END
    //
    DELIMITER ;