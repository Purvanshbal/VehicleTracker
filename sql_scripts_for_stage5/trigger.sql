CREATE TRIGGER ApplyTax
    BEFORE INSERT ON Vehicle
        FOR EACH ROW
    BEGIN
        SET @price= (SELECT avg(Price) FROM Vehicle WHERE Brand= new.Brand GROUP BY Brand);
        IF @price > 80000 THEN
            SET new.Average_maintenance_cost = 1.2 * new.Average_maintenance_cost;
        END IF;
    END;