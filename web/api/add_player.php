<?php
require '../database/db.php';

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    echo json_encode(['error' => 'POST method required']);
    exit;
}

$input = json_decode(file_get_contents('php://input'), true);
$name = trim($input['name'] ?? '');

if ($name === '') {
    http_response_code(400);
    echo json_encode(['error' => 'Player name is required']);
    exit;
}

try {
    $stmt = $pdo->prepare("INSERT INTO leaderboard (name) VALUES (:name)");
    $stmt->execute([':name' => $name]);

    echo json_encode(['success' => true, 'id' => $pdo->lastInsertId()]);

} catch (PDOException $e) {
    if ($e->errorInfo[1] == 1062) { // Duplicate entry

        //if the player exists, return existing id
        $stmt = $pdo->prepare("SELECT id FROM leaderboard WHERE name = :name");
        $stmt->execute([':name' => $name]);
        $player = $stmt->fetch(PDO::FETCH_ASSOC);
        if ($player) {
            echo json_encode(['success' => true, 'id' => $player['id']]);
        } else {
            http_response_code(500);
            echo json_encode(['error' => 'Failed to retrieve player ID']);
        }
    } else {
        http_response_code(500);
        echo json_encode(['error' => 'Server error']);
    }
}