function updateLeaderboardTable(data) {
  const tbody = document.getElementById("leaderboard-body");
  tbody.innerHTML = ""; // Clear table

  data.forEach((player, index) => {
    const row = document.createElement("tr");
    row.classList.add("fade-in-row");
    row.style.animationDelay = `${index * 0.05}s`; // Staggered animation
    row.style.opacity = 0; // Start invisible

    row.innerHTML = `
        <td>${String(index + 1).padStart(2, "0")}</td>
        <td>${player.name}</td>
        <td>${player.matches}</td>
        <td>
            ${player.wins}
        </td>
        <td>
            ${player.losses}
        </td>
        <td>${player.ratio}</td>
        `;
    tbody.appendChild(row);
  });
}