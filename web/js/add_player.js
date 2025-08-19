document
  .getElementById("addPlayerModal")
  .addEventListener("shown.bs.modal", () => {
    document.getElementById("playerName").focus();
  });

document
  .getElementById("addPlayerForm")
  .addEventListener("submit", async function (e) {
    e.preventDefault();

    const name = document.getElementById("playerName").value.trim();
    const errorDiv = document.getElementById("formError");

    // Validation
    if (!name) {
      errorDiv.textContent = "Player name is required.";
      return;
    }

    try {
      const response = await fetch(
        "http://localhost/leaderboard/api/add_player.php",
        {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ name }),
        }
      );

      const result = await response.json();

      if (result.success) {
        const modal = bootstrap.Modal.getInstance(
          document.getElementById("addPlayerModal")
        );
        modal.hide();
        e.target.reset();
        errorDiv.textContent = "";
      } else {
        errorDiv.textContent = result.error || "Something went wrong.";
      }
    } catch (err) {
      errorDiv.textContent = "Failed to add player. Server error.";
      console.error(err);
    }
  });
