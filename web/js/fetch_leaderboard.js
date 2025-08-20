leaderboardLimit = 5; // default
let lastData = [];
let lastLimit = leaderboardLimit;

async function fetchLeaderboardData() {
  try {
    const response = await fetch(
      // SVP Code Here
      `http://localhost/leaderboard-svp/web/api/get_leaderboard.php?limit=${leaderboardLimit}`
      // End SVP Code
    );
    if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);

    const data = await response.json();

    // Only update if data or limit changed
    if (
      JSON.stringify(data) !== JSON.stringify(lastData) ||
      leaderboardLimit !== lastLimit
    ) {
      updateLeaderboardTable(data);
      lastData = data;
      lastLimit = leaderboardLimit;
    }
  } catch (error) {
    console.error("Failed to fetch leaderboard:", error);
  }
}

setInterval(fetchLeaderboardData, 1000);