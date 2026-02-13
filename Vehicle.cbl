       IDENTIFICATION DIVISION.
       PROGRAM-ID. VehicleSystem.
       AUTHOR. Developer.
       DATE-WRITTEN. 2024.
       
       ENVIRONMENT DIVISION.
       CONFIGURATION SECTION.
       SOURCE-COMPUTER. IBM-PC.
       OBJECT-COMPUTER. IBM-PC.
       
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 VEHICLE-BASE.
          05 VEHICLE-ID        PIC 9(5).
          05 VEHICLE-BRAND     PIC X(20).
          05 VEHICLE-MODEL     PIC X(20).
          05 VEHICLE-YEAR      PIC 9(4).
          05 VEHICLE-COLOR     PIC X(15).
          05 VEHICLE-PRICE     PIC 9(8)V99.
       
       01 CAR-DETAILS.
          05 CAR-BASE.
             10 CAR-ID         PIC 9(5).
             10 CAR-BRAND      PIC X(20).
             10 CAR-MODEL      PIC X(20).
             10 CAR-YEAR       PIC 9(4).
          05 CAR-DOORS         PIC 9(1).
          05 CAR-FUEL-TYPE     PIC X(10).
          05 CAR-TRANSMISSION  PIC X(10).
          05 CAR-MILEAGE       PIC 9(6).
       
       01 TRUCK-DETAILS.
          05 TRUCK-BASE.
             10 TRUCK-ID       PIC 9(5).
             10 TRUCK-BRAND    PIC X(20).
             10 TRUCK-MODEL    PIC X(20).
             10 TRUCK-YEAR     PIC 9(4).
          05 TRUCK-CAPACITY    PIC 9(5).
          05 TRUCK-AXLES       PIC 9(1).
          05 TRUCK-CARGO-TYPE  PIC X(15).
          05 TRUCK-WEIGHT      PIC 9(6).
       
       01 MOTORCYCLE-DETAILS.
          05 BIKE-BASE.
             10 BIKE-ID        PIC 9(5).
             10 BIKE-BRAND     PIC X(20).
             10 BIKE-MODEL     PIC X(20).
             10 BIKE-YEAR      PIC 9(4).
          05 BIKE-ENGINE-CC    PIC 9(4).
          05 BIKE-TYPE         PIC X(15).
       
       01 WS-COUNTER          PIC 9(2) VALUE 0.
       01 WS-TOTAL-VEHICLES   PIC 9(3) VALUE 0.
       
       PROCEDURE DIVISION.
       MAIN-PROCEDURE.
           PERFORM INITIALIZE-VEHICLE.
           PERFORM INITIALIZE-CAR.
           PERFORM INITIALIZE-TRUCK.
           PERFORM INITIALIZE-MOTORCYCLE.
           PERFORM DISPLAY-ALL-VEHICLES.
           STOP RUN.
       
       INITIALIZE-VEHICLE.
           MOVE 10001 TO VEHICLE-ID.
           MOVE "Toyota" TO VEHICLE-BRAND.
           MOVE "Camry" TO VEHICLE-MODEL.
           MOVE 2024 TO VEHICLE-YEAR.
           MOVE "Silver" TO VEHICLE-COLOR.
           MOVE 35000.00 TO VEHICLE-PRICE.
       
       INITIALIZE-CAR.
           MOVE 10002 TO CAR-ID.
           MOVE "Honda" TO CAR-BRAND.
           MOVE "Civic" TO CAR-MODEL.
           MOVE 2023 TO CAR-YEAR.
           MOVE 4 TO CAR-DOORS.
           MOVE "Petrol" TO CAR-FUEL-TYPE.
           MOVE "Automatic" TO CAR-TRANSMISSION.
           MOVE 15000 TO CAR-MILEAGE.
       
       INITIALIZE-TRUCK.
           MOVE 10003 TO TRUCK-ID.
           MOVE "Ford" TO TRUCK-BRAND.
           MOVE "F-150" TO TRUCK-MODEL.
           MOVE 2024 TO TRUCK-YEAR.
           MOVE 5000 TO TRUCK-CAPACITY.
           MOVE 2 TO TRUCK-AXLES.
           MOVE "General" TO TRUCK-CARGO-TYPE.
           MOVE 8500 TO TRUCK-WEIGHT.
       
       INITIALIZE-MOTORCYCLE.
           MOVE 10004 TO BIKE-ID.
           MOVE "Yamaha" TO BIKE-BRAND.
           MOVE "R15" TO BIKE-MODEL.
           MOVE 2023 TO BIKE-YEAR.
           MOVE 155 TO BIKE-ENGINE-CC.
           MOVE "Sport" TO BIKE-TYPE.
       
       DISPLAY-ALL-VEHICLES.
           DISPLAY "=== VEHICLE INVENTORY ===".
           DISPLAY " ".
           DISPLAY "Base Vehicle:".
           DISPLAY "ID: " VEHICLE-ID.
           DISPLAY "Brand: " VEHICLE-BRAND.
           DISPLAY "Model: " VEHICLE-MODEL.
           DISPLAY "Year: " VEHICLE-YEAR.
           DISPLAY "Color: " VEHICLE-COLOR.
           DISPLAY "Price: $" VEHICLE-PRICE.
           DISPLAY " ".
           DISPLAY "Car Details:".
           DISPLAY "ID: " CAR-ID.
           DISPLAY "Brand: " CAR-BRAND " " CAR-MODEL.
           DISPLAY "Doors: " CAR-DOORS.
           DISPLAY "Fuel: " CAR-FUEL-TYPE.
           DISPLAY "Transmission: " CAR-TRANSMISSION.
           DISPLAY " ".
           DISPLAY "Truck Details:".
           DISPLAY "ID: " TRUCK-ID.
           DISPLAY "Brand: " TRUCK-BRAND " " TRUCK-MODEL.
           DISPLAY "Capacity: " TRUCK-CAPACITY " lbs".
           DISPLAY "Axles: " TRUCK-AXLES.
           DISPLAY " ".
           DISPLAY "Motorcycle Details:".
           DISPLAY "ID: " BIKE-ID.
           DISPLAY "Brand: " BIKE-BRAND " " BIKE-MODEL.
           DISPLAY "Engine: " BIKE-ENGINE-CC " CC".
           DISPLAY "Type: " BIKE-TYPE.
