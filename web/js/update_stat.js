async function updateStat(playerId, stat) {
  try {
    const response = await fetch(
      "http://localhost/leaderboard/api/update_stat.php",
      {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ id: playerId, field: stat }),
      }
    );

    const result = await response.json();
    if (!result.success) {
      console.error("Failed to update:", result.error || "Unknown error");
    }
  } catch (err) {
    console.error("Error calling update_stat.php:", err);
  }
}