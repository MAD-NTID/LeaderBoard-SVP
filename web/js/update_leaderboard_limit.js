let leaderboardLimit = 5;

document.querySelectorAll(".dropdown-item").forEach((item) => {
  item.addEventListener("click", (e) => {
    e.preventDefault();
    leaderboardLimit = parseInt(item.dataset.limit);
    document.getElementById("limitDisplay").textContent = leaderboardLimit;
    fetchLeaderboardData(); // immediate fetch
  });
});