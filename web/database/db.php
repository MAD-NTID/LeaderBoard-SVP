<?php
$host     = "localhost";  
$dbname   = "leaderboard";
$username = "root";       
$password = "";           
$debug    = true;         

try {
    $pdo = new PDO(
        "mysql:host=$host;dbname=$dbname;charset=utf8mb4",
        $username,
        $password
    );
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

} catch (PDOException $e) {
    if ($debug) {
        echo json_encode([
            "success" => false,
            "error"   => $e->getMessage()  // full error for debugging
        ]);
    } else {
        echo json_encode([
            "success" => false,
            "error"   => "Database connection failed."
        ]);
    }
    exit;
}
