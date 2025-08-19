<?php
require '../database/db.php';

$id = isset($_GET['id']) ? (int) $_GET['id'] : null;
$limit = isset($_GET['limit']) ? (int) $_GET['limit'] : 10;

// Sanity check for limit
$limit = max(1, min($limit, 100));

if ($id) {
    // If an id is provided, override limit to 1 and get the player's current rank
    $sql = "
      SELECT *
      FROM (
          SELECT 
              id, 
              name, 
              matches, 
              wins, 
              losses, 
              CASE 
                  WHEN losses = 0 AND wins > 0 THEN wins
                  WHEN losses = 0 AND wins = 0 THEN 0
                  ELSE ROUND(wins / losses, 2)
              END AS ratio,
              RANK() OVER (ORDER BY matches DESC, wins DESC) AS rank
          FROM leaderboard
      ) AS ranked
      WHERE id = :id
      LIMIT 1
    ";
    $stmt = $pdo->prepare($sql);
    $stmt->bindValue(':id', $id, PDO::PARAM_INT);

} else {
    // Default leaderboard query
    $sql = "
      SELECT 
          id, 
          name, 
          matches, 
          wins, 
          losses, 
          CASE 
              WHEN losses = 0 AND wins > 0 THEN wins
              WHEN losses = 0 AND wins = 0 THEN 0
              ELSE ROUND(wins / losses, 2)
          END AS ratio
      FROM leaderboard
      ORDER BY matches DESC, wins DESC
      LIMIT :limit
    ";
    $stmt = $pdo->prepare($sql);
    $stmt->bindValue(':limit', $limit, PDO::PARAM_INT);
}

$stmt->execute();
$results = $stmt->fetchAll();

header('Content-Type: application/json');
echo json_encode($results);
